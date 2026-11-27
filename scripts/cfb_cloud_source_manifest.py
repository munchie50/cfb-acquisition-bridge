"""Build a QA collection plan from exact accepted snapshot references.

Source associations are explicit. Full-board links never count as football
material coverage; neither role certifies research, prices or freshness.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urlsplit
from cfb_cloud_source_prepare import SCHEMA, atomic_json, digest, url_host, validate
from cfb_recovery_navigation_reader import read, unique

ACTIVE = {'CURRENT_PRICE_COMPARATIVE_PASS_REASSESSMENT',
          'NEW_PROSPECTIVE_PASS_RECONSIDERATION', 'RETAINED_UNEXPIRED_CONDITIONAL_REASSESSED'}
HISTORY = {'ORIGINAL_EXCLUSION_NO_RECOMMENDATION', 'ELAPSED_HISTORY_PRESERVED_NO_NEW_DECISION',
           'EXPIRED_UNPUBLISHED_NO_REOPEN', 'EXPIRED_CONDITIONAL_HISTORY_ONLY'}


def blob(text):
    b = text.encode('utf-8')
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()


def identities(rows):
    ids = [r['game_id'] for r in rows]
    if not ids or len(ids) != len(set(ids)):
        raise ValueError('empty or duplicate game population')
    return set(ids)


def build(index, expected_index, authority_commit, loader, paths, market_url, as_of,
          extra=None, expected_extra=None, approved_association_commits=()):
    if not re.fullmatch('[0-9a-f]{40}', authority_commit) or blob(index) != expected_index:
        raise ValueError('exact authority commit and index blob required')
    frontier = read(index, as_of)['frontier']
    pointers = {p['path']: p for p in frontier['pointers']}
    bindings = {}

    def bound(path, expected=None):
        if path not in pointers:
            raise ValueError('input missing from accepted frontier: '+path)
        raw = loader(path)
        sha = blob(raw)
        if sha != pointers[path]['blob'] or (expected and sha != expected):
            raise ValueError('stale input or review binding: '+path)
        bindings[path] = sha
        return json.loads(raw, object_pairs_hook=unique)

    lineage, research, review = [bound(paths[k]) for k in ('lineage', 'research', 'revalidation')]
    if not pointers[paths['revalidation']]['purpose'].startswith('CURRENT_COMPLETE_'):
        raise ValueError('revalidation is not the explicit current complete review role')
    if not re.fullmatch(r'CFB_WEEK\d+_REMAINING_WINDOW_REVALIDATION_V1', review['schema']):
        raise ValueError('unqualified revalidation schema')
    if research.get('schema') != 'CFB_COMPLETE_MULTI_MARKET_REVIEW_V1':
        raise ValueError('unqualified material inventory schema')
    population = identities(lineage['rows'])
    if population != identities(research['games']) or population != identities(review['cases']):
        raise ValueError('lineage, research and current review populations differ')
    if (len(population) != lineage['targets'] or len(population) != review['source_coverage']['governed_games']
            or len(population) != review['source_coverage']['matched_games']
            or review['source_coverage']['missing_game_ids']):
        raise ValueError('incomplete declared source population')
    statuses = {r['game_id']: r['first_frozen_status'] for r in lineage['rows']}
    if any(v not in ('PREDICTION', 'EXCLUDED') for v in statuses.values()):
        raise ValueError('unknown original population status')
    if (sum(v == 'PREDICTION' for v in statuses.values()) != lineage['predictions']
            or sum(v == 'EXCLUDED' for v in statuses.values()) != lineage['exclusions']):
        raise ValueError('original prediction/exclusion counts differ')
    if any(r['classification'] not in ACTIVE | HISTORY for r in review['cases']):
        raise ValueError('new review classification requires qualification')
    selected = {r['game_id'] for r in review['cases'] if r['classification'] in ACTIVE}
    if any(r['temporal_status'] != 'FUTURE_AT_CAPTURE' or statuses[r['game_id']] != 'PREDICTION'
           for r in review['cases'] if r['game_id'] in selected):
        raise ValueError('active source scope includes elapsed or excluded identity')
    # This is a saved review boundary, never a claim of fresh current timing.
    from cfb_cloud_source_prepare import timestamp
    if timestamp(review['as_of_utc']) > timestamp(as_of):
        raise ValueError('future review boundary')
    urls = {r['current_offer'].get('source_url') for r in review['cases'] if r.get('current_offer')}
    if urls != {market_url}:
        raise ValueError('market URL absent from saved actual source observations')
    source = review['source']
    if (source['path'] not in pointers or pointers[source['path']]['blob'] != source['blob']
            or blob(loader(source['path'])) != source['blob']):
        raise ValueError('market capture exact binding unavailable')
    bindings[source['path']] = source['blob']

    catalog = {s['id']: s for s in research['sources']}
    if len(catalog) != len(research['sources']):
        raise ValueError('duplicate source catalog identity')
    planned = {}

    def add(url, kind, games, provenance):
        host = urlsplit(url).hostname
        url_host(url, [host])
        if not set(games) <= population or not games:
            raise ValueError('unknown or absent explicit source game association')
        old = planned.get(url)
        if old and old['kind'] != kind:
            raise ValueError('same URL cannot silently switch source roles')
        if not old:
            old = planned[url] = {'id': digest(url.encode())[:24], 'url': url, 'kind': kind,
                                  'game_ids': [], 'provenance': []}
        old['game_ids'] = sorted(set(old['game_ids']) | set(games))
        old['provenance'].append(provenance)

    add(market_url, 'market_board', sorted(population),
        {'path': source['path'], 'blob': source['blob'], 'reference_clock': source['recovered_by'],
         'qualification': 'SAVED_FULL_BOARD_LINK_NOT_NEW_QUOTE_OR_FOOTBALL_COVERAGE'})
    for game in research['games']:
        # Validate references even on excluded/history rows, but don't fetch them.
        for sid in game['source_ids']:
            if sid not in catalog: raise ValueError('unresolved explicit source ID')
        if game['game_id'] not in selected:
            continue
        for sid in game['source_ids']:
            s = catalog[sid]
            add(s['url'], 'football_material', [game['game_id']],
                {'path': paths['research'], 'blob': bindings[paths['research']], 'source_id': sid,
                 'reference_clock': s.get('response_recovered_by'),
                 'qualification': s.get('qualification', 'UNQUALIFIED_RETAINED_REFERENCE')})

    for game in review['cases']:
        if game['game_id'] not in selected or not game.get('review_ref'):
            continue
        ref = game['review_ref']
        immutable = bound(ref['path'], ref['blob'])
        if immutable['game_id'] != game['game_id']:
            raise ValueError('immutable review game differs')
        for s in immutable['material_sources']:
            add(s['url'], 'football_material', [game['game_id']],
                {'path': ref['path'], 'blob': ref['blob'], 'reference_clock': s.get('retrieved_at'),
                 'qualification': 'EXPLICIT_IMMUTABLE_REVIEW_MATERIAL_REFERENCE'})

    # New global source lists lack per-game IDs. Never guess links from URL slugs.
    additions = {s['url']: s for s in review.get('new_material_sources', [])}
    links = {}
    if extra is not None:
        if digest(extra) != expected_extra:
            raise ValueError('supplemental association SHA-256 mismatch')
        supplement = json.loads(extra, object_pairs_hook=unique)
        if (supplement['schema'] != 'CFB_QA_EXPLICIT_SOURCE_ASSOCIATIONS_V1'
                or (supplement['authority_commit'] != authority_commit
                    and supplement['authority_commit'] not in approved_association_commits)
                or supplement['revalidation_blob'] != bindings[paths['revalidation']]):
            raise ValueError('supplemental association authority mismatch')
        for item in supplement['links']:
            if item['url'] not in additions or item['url'] in links:
                raise ValueError('unknown or duplicate supplemental source')
            if (not set(item['game_ids']) <= selected or not item['game_ids']
                    or len(item['game_ids']) != len(set(item['game_ids']))):
                raise ValueError('supplement links outside eligible saved population')
            links[item['url']] = item['game_ids']
    unassigned = []
    for url, item in additions.items():
        if 'game_ids' in item:
            games = item['game_ids']
            if not games or len(games)!=len(set(games)) or not set(games)<=selected:
                raise ValueError('explicit material association outside eligible saved population')
        elif url in links:
            games = links[url]
        elif url in planned and planned[url]['kind'] == 'football_material':
            games = planned[url]['game_ids']
        else:
            unassigned.append(url); continue
        add(url, 'football_material', games,
            {'path': paths['revalidation'], 'blob': bindings[paths['revalidation']],
             'reference_clock': item.get('recovered_by_utc'),
             'qualification': item.get('qualification'), 'explicit_qa_association_sha256': expected_extra})
    materials = {g for s in planned.values() if s['kind'] == 'football_material' for g in s['game_ids']}
    report = {'governed_games': len(population), 'saved_active_prediction_games': len(selected),
              'football_required_game_ids': sorted(selected),
              'saved_review_boundary_utc': review['as_of_utc'], 'plan_recorded_at_utc': as_of,
              'market_linked_games': len(population), 'football_linked_active_games': len(materials & selected),
              'active_games_without_football_links': sorted(selected-materials),
              'new_material_urls_without_explicit_game_links': sorted(unassigned),
              'nonactive_or_excluded_game_ids_not_material_collection_targets': sorted(population-selected),
              'source_count': len(planned),
              'source_link_coverage_is_not_football_review_completeness': True}
    report['status'] = ('READY_FOR_UNREVIEWED_COLLECTION_ONLY' if not unassigned and selected <= materials
                        else 'SOURCE_PLAN_INCOMPLETE_NOT_A_PASS')
    plan = {'schema': SCHEMA, 'authority_ref': authority_commit, 'index_blob': expected_index,
            'authority_input_bindings': bindings, 'game_ids': sorted(population),
            'allowed_hosts': sorted({urlsplit(s['url']).hostname for s in planned.values()}),
            'sources': sorted(planned.values(), key=lambda s: s['url']),
            'scope': 'QA_SOURCE_URL_PLAN_FROM_SAVED_AUTHORITY_NOT_FRESH_FACTS_OR_CURRENT_ELIGIBILITY',
            'source_role_coverage': report, 'supplemental_qa_association_sha256': expected_extra}
    raw = (json.dumps(plan, indent=2, sort_keys=True)+'\n').encode()
    validate(raw, digest(raw))  # Existing worker bounds; never silently truncate.
    return plan, report


def snapshot_plan(root, authority_commit, index_path, expected_index, paths, market_url,
                  as_of, extra=None, expected_extra=None, require_current_head=True):
    """Resolve accepted snapshot and unchanged live frontier before any fetch.

    A request worker may use an accepted ancestor snapshot only while the exact
    current frontier and every consumer binding remain unchanged. A producer
    creating a new request must still name the freshly observed main head.
    """
    if not re.fullmatch('[0-9a-f]{40}', authority_commit):raise ValueError('exact main commit required')
    def git(*args):
        return subprocess.check_output(['git','-C',str(root),*args],stderr=subprocess.PIPE).decode()
    current=git('rev-parse','refs/remotes/origin/main').strip()
    if require_current_head and current!=authority_commit:
        raise ValueError('fresh connector-observed main must match fetched origin/main')
    git('merge-base','--is-ancestor',authority_commit,current)
    def loader(commit):
        def load(path):
            if not re.fullmatch(r'evidence/[A-Za-z0-9_./-]+',path) or '..' in Path(path).parts:
                raise ValueError('unsupported authority path')
            return git('show',commit+':'+path)
        return load
    live,anchor=loader(current),loader(authority_commit)
    index=live(index_path)
    if blob(index)!=expected_index or anchor(index_path)!=index:
        raise ValueError('request frontier changed; prepare a new current source plan')
    from cfb_recovery_consumer_preflight import audit
    audit(index,live,as_of)  # Full consumer closure, not selected-source hashes only.
    approved=[]
    if extra is not None:
        if digest(extra)!=expected_extra:raise ValueError('supplemental association SHA-256 mismatch')
        supplement=json.loads(extra,object_pairs_hook=unique)
        parent=supplement['authority_commit']
        if not re.fullmatch('[0-9a-f]{40}',parent):raise ValueError('exact association provenance required')
        git('merge-base','--is-ancestor',parent,authority_commit)
        if blob(loader(parent)(paths['revalidation']))!=supplement['revalidation_blob']:
            raise ValueError('association parent does not contain its declared review')
        approved.append(parent)
    return build(index,expected_index,authority_commit,anchor,paths,market_url,as_of,
                 extra,expected_extra,approved)


if __name__ == '__main__':
    from datetime import datetime, timezone
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, default=Path('.'))
    p.add_argument('--authority-commit', required=True)
    p.add_argument('--index', required=True)
    p.add_argument('--expected-index-blob', required=True)
    for name in ('lineage', 'research', 'revalidation', 'market-url'):
        p.add_argument('--'+name, required=True)
    p.add_argument('--extra-links', type=Path)
    p.add_argument('--expected-extra-sha256')
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    plan, report = snapshot_plan(a.root, a.authority_commit, a.index, a.expected_index_blob,
        {k:getattr(a, k) for k in ('lineage', 'research', 'revalidation')}, a.market_url,
        datetime.now(timezone.utc).isoformat(),
        a.extra_links.read_bytes() if a.extra_links else None, a.expected_extra_sha256)
    a.output.mkdir(parents=True, exist_ok=True)
    atomic_json(a.output/'source-plan.json', plan)
    atomic_json(a.output/'coverage.json', report)
    print(json.dumps({'plan_sha256': digest((a.output/'source-plan.json').read_bytes()), **report}, indent=2))
    raise SystemExit(0 if report['status'] == 'READY_FOR_UNREVIEWED_COLLECTION_ONLY' else 2)
