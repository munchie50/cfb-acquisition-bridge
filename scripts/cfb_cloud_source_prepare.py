"""QA-only resumable public source collection; never issue decisions or publish.

An explicitly approved, hash-pinned manifest declares URLs and game identities.
HTTP success and cached bytes remain UNREVIEWED, never a football/price PASS.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import fcntl
import hashlib
import ipaddress
import json
from pathlib import Path
import socket
import time
import urllib.parse
import urllib.request

SCHEMA = 'CFB_CLOUD_SOURCE_INPUT_V1'
LIMIT = 4 * 1024 * 1024


def utc():
    return datetime.now(timezone.utc).isoformat()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def timestamp(value):
    d = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if d.tzinfo is None:
        raise ValueError('timezone-aware source clock required')
    return d


def url_host(url, hosts):
    p = urllib.parse.urlsplit(url)
    if (p.scheme != 'https' or not p.hostname or p.username or p.password
            or p.port not in (None, 443) or p.fragment):
        raise ValueError('plain public HTTPS URL required')
    host = p.hostname.lower()
    if host not in hosts or host == 'localhost' or '.' not in host:
        raise ValueError('host absent from explicit approved host set')
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return host
    raise ValueError('literal network addresses are not supported')


def public_address(host):
    addresses = socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM)
    if not addresses or any(not ipaddress.ip_address(a[4][0]).is_global for a in addresses):
        raise ValueError('source does not resolve exclusively to public addresses')


def validate(raw, expected):
    if digest(raw) != expected:
        raise ValueError('input SHA-256 mismatch')
    r = json.loads(raw)
    if r.get('schema') != SCHEMA or not r.get('authority_ref'):
        raise ValueError('explicit manifest schema and authority_ref required')
    games = r['game_ids']
    hosts = r['allowed_hosts']
    sources = r['sources']
    if (not games or len(games) != len(set(games))
            or any(not isinstance(g, str) or not g for g in games)):
        raise ValueError('unique explicit game identity population required')
    if not hosts or len(hosts) != len(set(hosts)):
        raise ValueError('explicit unique host set required')
    if not 1 <= len(sources) <= 64:
        raise ValueError('source count outside bounded 1..64 scope')
    ids, urls, covered = set(), set(), set()
    for s in sources:
        if not isinstance(s.get('id'), str) or not s['id'] or s['id'] in ids:
            raise ValueError('duplicate/empty source identity')
        if s.get('kind') not in ('market_board', 'football_material'):
            raise ValueError('explicit source kind required')
        url_host(s['url'], hosts)
        if s['url'] in urls:
            raise ValueError('duplicate URL: declare one source with all affected game_ids')
        linked = s['game_ids']
        if not linked or len(linked) != len(set(linked)) or not set(linked) <= set(games):
            raise ValueError('source links missing, duplicated or outside declared population')
        ids.add(s['id']); urls.add(s['url']); covered.update(linked)
    if covered != set(games):
        raise ValueError('declared game population lacks source links')
    return r


class Redirects(urllib.request.HTTPRedirectHandler):
    def __init__(self, hosts):
        self.hosts = hosts

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        public_address(url_host(newurl, self.hosts))
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def download(url, hosts):
    public_address(url_host(url, hosts))
    request = urllib.request.Request(url, headers={'User-Agent': 'CFB-QA-Source-Preparation/1.0'})
    with urllib.request.build_opener(Redirects(hosts)).open(request, timeout=20) as response:
        url_host(response.url, hosts)
        raw = response.read(LIMIT + 1)
        if not raw or len(raw) > LIMIT:
            raise ValueError('empty or oversized response')
        return raw, {'http_status': response.status, 'final_url': response.url,
                     'content_type': response.headers.get('Content-Type')}


def atomic_json(path, value):
    tmp = path.with_suffix('.tmp')
    tmp.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')
    tmp.replace(path)


def reusable(row, source, output, now, max_age):
    try:
        if row['status'] not in ('FETCHED_UNREVIEWED', 'REUSED_UNREVIEWED') or row['url'] != source['url']:
            return False
        age = (timestamp(now) - timestamp(row['response_recovered_by_utc'])).total_seconds()
        # The original acquisition clock survives every resume. No sliding TTL.
        if not 0 <= age <= max_age:
            return False
        name = row['artifact']
        if name != digest(source['url'].encode()) + '.source':
            return False
        data = (output / name).read_bytes()
        return 0 < len(data) <= LIMIT and len(data) == row['bytes'] and digest(data) == row['sha256']
    except (KeyError, OSError, ValueError, TypeError):
        return False


def prepare(manifest, expected, output, workers=4, max_age=900, fetch=download, clock=utc):
    if not 1 <= workers <= 4 or not 0 <= max_age <= 3600:
        raise ValueError('workers1..4 and cache age0..3600 seconds required')
    specification = validate(manifest, expected)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    # A nonblocking lock prevents two jobs from mutating the same checkpoint.
    with (output / '.prepare.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        return collect(specification, expected, output, workers, max_age, fetch, clock)


def collect(spec, expected, output, workers, max_age, fetch, clock):
    path = output / 'manifest.json'
    previous = json.loads(path.read_text()) if path.exists() else {}
    if previous and previous.get('input_sha256') != expected:
        raise ValueError('output belongs to a different approved input; use a new directory')
    prior = {r['id']: r for r in previous.get('sources', [])}
    started, monotonic = clock(), time.monotonic()
    rows = {}
    state = {'schema': 'CFB_CLOUD_SOURCE_PREPARATION_V1', 'input_sha256': expected,
             'authority_ref': spec['authority_ref'], 'started_at_utc': started,
             'status': 'PREPARATION_INCOMPLETE', 'game_ids': spec['game_ids'],
             'scope': 'UNREVIEWED_SOURCE_COLLECTION_ONLY_NOT_DECISIONS_OR_MONITOR_COMPLETION',
             'workers': workers, 'max_cache_age_seconds': max_age,
             'canonical_mutation': False, 'sources': []}

    def checkpoint():
        state['sources'] = [rows[s['id']] for s in spec['sources'] if s['id'] in rows]
        state['checkpoint_at_utc'] = clock()
        atomic_json(path, state)

    def obtain(s):
        item = {**s, 'attempt_started_at_utc': clock()}
        try:
            raw, metadata = fetch(s['url'], spec['allowed_hosts'])
            if not raw or len(raw) > LIMIT:
                raise ValueError('empty or oversized response')
            url_host(metadata['final_url'], spec['allowed_hosts'])
            if metadata['http_status'] != 200:
                raise ValueError('HTTP success requires status200')
            name = digest(s['url'].encode()) + '.source'
            temporary = output / (name + '.tmp')
            temporary.write_bytes(raw)
            temporary.replace(output / name)
            item.update(metadata, status='FETCHED_UNREVIEWED', artifact=name,
                        bytes=len(raw), sha256=digest(raw), response_recovered_by_utc=clock())
        except Exception as exc:
            # Source failures are recorded, never silently converted into PASS.
            item.update(status='UNAVAILABLE_NOT_A_PASS', error_type=type(exc).__name__,
                        response_recovered_by_utc=clock())
        return item

    pending = []
    for source in spec['sources']:
        row = prior.get(source['id'], {})
        if max_age and reusable(row, source, output, started, max_age):
            rows[source['id']] = {**row, 'status': 'REUSED_UNREVIEWED'}
        else:
            pending.append(source)
    checkpoint()
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(obtain, s) for s in pending]
        for future in as_completed(futures):
            row = future.result()
            rows[row['id']] = row
            checkpoint()
    usable = [r for r in rows.values() if r['status'] != 'UNAVAILABLE_NOT_A_PASS']
    covered = {g for r in usable for g in r['game_ids']}
    state.update(status=('COLLECTION_COMPLETE_UNREVIEWED' if len(usable) == len(spec['sources'])
                         else 'PREPARATION_INCOMPLETE'),
                 completed_at_utc=clock(), elapsed_seconds=round(time.monotonic()-monotonic, 6),
                 fetched_sources=sum(r['status'] == 'FETCHED_UNREVIEWED' for r in rows.values()),
                 reused_sources=sum(r['status'] == 'REUSED_UNREVIEWED' for r in rows.values()),
                 failed_sources=len(rows)-len(usable),
                 games_without_fetched_link=sorted(set(spec['game_ids'])-covered),
                 football_analysis='NOT_PERFORMED', source_semantic_freshness='NOT_CERTIFIED')
    checkpoint()
    return state


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', type=Path, required=True)
    p.add_argument('--expected-sha256', required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--workers', type=int, default=4)
    p.add_argument('--max-cache-age-seconds', type=int, default=900)
    args = p.parse_args()
    result = prepare(args.input.read_bytes(), args.expected_sha256, args.output,
                     args.workers, args.max_cache_age_seconds)
    print(json.dumps({k:v for k,v in result.items() if k != 'sources'}, indent=2))
    raise SystemExit(0 if result['status'] == 'COLLECTION_COMPLETE_UNREVIEWED' else 2)
