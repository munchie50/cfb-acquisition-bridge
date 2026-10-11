"""Bounded Week 7 accepted S0 coverage diagnostic; never operational acceptance."""
import csv
import hashlib
import io
import json
import re
import zipfile
from datetime import datetime
from zoneinfo import ZoneInfo

ALIASES = {
    'Middle Tenn.': 'Middle Tennessee', 'FIU': 'Florida International',
    'Jacksonville St.': 'Jacksonville State', 'Kennesaw St.': 'Kennesaw State',
    'Missouri St.': 'Missouri State', 'W. Kentucky': 'Western Kentucky',
    'Ga. Southern': 'Georgia Southern', 'Colorado St.': 'Colorado State',
    'Texas St.': 'Texas State', 'App. St.': 'App State', 'C. Carolina': 'Coastal Carolina',
    'Miss. State': 'Mississippi State', 'Georgia St.': 'Georgia State',
    'FAU': 'Florida Atlantic', 'Michigan St.': 'Michigan State',
    'Ball St.': 'Ball State', 'Charleston So.': 'Charleston Southern',
    'UMass': 'Massachusetts', 'W. Michigan': 'Western Michigan',
    'C. Michigan': 'Central Michigan', 'N. Illinois': 'Northern Illinois',
    'Arizona St.': 'Arizona State', 'E. Michigan': 'Eastern Michigan',
    'Miami-OH': 'Miami (OH)', 'Washington St.': 'Washington State',
    'Miami (Fla.)': 'Miami', 'Kent St.': 'Kent State',
    'N. Dakota St.': 'North Dakota State', 'Arkansas St.': 'Arkansas State',
    'So. Miss': 'Southern Miss', 'UL-Monroe': 'UL Monroe',
    'San Jose St.': 'San José State', 'UTEP': 'UTEP',
    'Sacramento St.': 'Sacramento State', 'Fresno St.': 'Fresno State',
    'San Diego St.': 'San Diego State', 'Hawaii': "Hawai'i",
}

def sheet_rows(sheet):
    rows = []
    for line in sheet.splitlines():
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) != 9 or not re.fullmatch(r'(Tue|Wed|Thu|Fri|Sat) Oct (13|14|15|16|17) \d{1,2}:\d{2} [AP]M CT', cells[0]):
            continue
        away, home = cells[1].split(' @ ')
        pair = (ALIASES.get(away, away), ALIASES.get(home, home))
        clock = datetime.strptime(cells[0][:-3] + ' 2026', '%a %b %d %I:%M %p %Y').replace(tzinfo=ZoneInfo('America/Chicago'))
        rows.append((pair, clock))
    if len(rows) != 62 or len({p for p, _ in rows}) != 62:
        raise ValueError('exactly 62 unique display identities required')
    return rows

def coverage(targets, predictions, exclusions, rows):
    ids = [r['game_id'] for r in targets]
    if len(ids) != len(set(ids)):
        raise ValueError('duplicate target IDs')
    by_pair = {}
    for r in targets:
        by_pair.setdefault((r['away_team'], r['home_team']), []).append(r)
    sets = []
    for group in (predictions, exclusions):
        values = [r['game_id'] for r in group]
        if len(values) != len(set(values)):
            raise ValueError('duplicate prediction/exclusion IDs')
        sets.append(set(values))
    pred, excl = sets
    if pred & excl or pred | excl != set(ids):
        raise ValueError('prediction/exclusion partition mismatch')
    found = []
    for pair, clock in rows:
        candidates = by_pair.get(pair, [])
        if len(candidates) != 1:
            raise ValueError('missing or ambiguous exact directed team-pair identity: ' + str(pair))
        r = candidates[0]
        archived = datetime.fromisoformat(r['start_date'])
        if not ('2026-10-13' <= archived.date().isoformat() <= '2026-10-18'):
            raise ValueError('matched target outside bounded Week 7 dates')
        found.append({'game_id': r['game_id'], 'away_team': pair[0], 'home_team': pair[1],
                      'archive_start': r['start_date'], 'current_display_start': clock.isoformat(),
                      'start_matches': archived == clock,
                      'accepted_s0_coverage': 'PREDICTION' if r['game_id'] in pred else 'EXPLICIT_EXCLUSION'})
    return {'status': 'ANCESTRY_COVERAGE_ONLY_NOT_OPERATIONAL_ACCEPTANCE',
            'display_count': len(found),
            's0_predictions': sum(r['accepted_s0_coverage'] == 'PREDICTION' for r in found),
            's0_exclusions': sum(r['accepted_s0_coverage'] == 'EXPLICIT_EXCLUSION' for r in found),
            'archive_start_mismatches': sum(not r['start_matches'] for r in found),
            'rows': found}

def audit(zip_path, pointer, sheet):
    raw = zip_path.read_bytes()
    if pointer.get('status') != 'ACCEPTED_PREDICTION_SOURCE_STATE':
        raise ValueError('accepted source pointer required')
    if hashlib.sha256(raw).hexdigest() != pointer['candidate_artifact_zip_sha256']:
        raise ValueError('accepted ZIP identity mismatch')
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        def table(name):
            return list(csv.DictReader(io.StringIO(z.read('s0/challenger_b_2026_refresh_' + name + '_v1_246.csv').decode())))
        targets, predictions, exclusions = [table(n) for n in ('target_ledger', 'fair_predictions', 'exclusions')]
        manifest = json.loads(z.read('s0/manifest_v1_246.json'))
        if manifest['cutoff_utc'] != pointer['accepted_cutoff_utc'] or manifest['snapshot_type'] != 'REFRESH_SNAPSHOT':
            raise ValueError('accepted cutoff/type mismatch')
        for name, digest in manifest['hashes'].items():
            if hashlib.sha256(z.read('s0/' + name)).hexdigest() != digest:
                raise ValueError('manifest output hash mismatch')
        by_id = {r['game_id']: r for r in targets}
        for r in predictions + exclusions:
            if r['game_id'] not in by_id or any(r[k] != by_id[r['game_id']][k] for k in ('away_team','home_team')):
                raise ValueError('prediction/exclusion directed identity mismatch')
            if r['snapshot_cutoff_utc'] != pointer['accepted_cutoff_utc']:
                raise ValueError('row cutoff mismatch')
        result = coverage(targets, predictions, exclusions, sheet_rows(sheet))
        result['archive_manifest'] = manifest
        result['zip_sha256'] = hashlib.sha256(raw).hexdigest()
        return result

if __name__ == '__main__':
    import sys
    from pathlib import Path
    result = audit(Path(sys.argv[1]), json.loads(Path(sys.argv[2]).read_text()), Path(sys.argv[3]).read_text())
    print(json.dumps(result, indent=2))
