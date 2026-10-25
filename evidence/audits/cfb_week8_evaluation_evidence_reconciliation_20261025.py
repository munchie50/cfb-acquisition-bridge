"""Bounded retained-evidence reconciliation; no outcomes or live decisions."""
import copy
import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

PREFIX = 'evidence/operational/'
BATCH = PREFIX + 'CFB_WEEK8_FULL_BATCH_QUALIFICATION_20261023T040417Z.json'
PARTIAL = PREFIX + 'CFB_WEEK8_RECOVERY_MULTI_MARKET_REVIEW_20261022T224648Z_R2.json'
LATE = PREFIX + 'CFB_WEEK8_LATE_MORNING_RECONSIDERATION_20261023T160305Z.md'
SAT = PREFIX + 'CFB_WEEK8_SATURDAY_DISPOSITIONS_20261023T033025Z.md'
SEVEN = PREFIX + 'CFB_WEEK8_SEVEN_FINAL_DISPOSITIONS_20261023T112439Z.md'
BRANCHES = {'FAVORITE_SPREAD', 'UNDERDOG_SPREAD', 'AWAY_MONEYLINE',
            'HOME_MONEYLINE', 'OVER', 'UNDER'}


def indexed(rows):
    result = {r['game_id']: r for r in rows}
    if len(result) != len(rows):
        raise ValueError('duplicate game identity')
    return result


def reconcile(fixture, sources):
    census = indexed(fixture['lineage']['rows'])
    decisions = indexed(fixture['decision']['rows'])
    if set(census) != set(decisions) or len(census) != 56:
        raise ValueError('incomplete original census/decision union')
    if fixture['decision']['as_of_utc'] != '2026-10-24T18:10:00Z':
        raise ValueError('unqualified snapshot boundary')
    target = {gid for gid, r in census.items()
              if r['first_frozen_status'] == 'PREDICTION'
              and decisions[gid]['state'] == 'PASS'}
    if len(target) != 40:
        raise ValueError('unexpected target population')
    records = {gid: [] for gid in target}

    def add(gid, path, location, record_clock):
        if gid in target:
            records[gid].append({'path': path, 'blob': sources[path]['sha'],
                                 'location': location, 'record_clock_utc': record_clock,
                                 'scope': 'SAVED_ANALYTICAL_PASS_NOT_CURRENT_SOURCE_CERTIFICATION'})

    partial = indexed(json.loads(sources[PARTIAL]['content'])['games'])
    if set(partial) != set(census):
        raise ValueError('partial source does not account for original census')
    for gid in target:
        if partial[gid]['original_model'] != census[gid]['display']:
            raise ValueError('original model identity mismatch')
        if set(partial[gid]['market_dispositions']) != BRANCHES:
            raise ValueError('missing original market branches')

    batch = json.loads(sources[BATCH]['content'])
    for gid, r in indexed(batch['games']).items():
        if gid not in census or r['original_model'] != census[gid]['display']:
            raise ValueError('batch original identity mismatch')
        if set(r['market_dispositions']) != BRANCHES:
            raise ValueError('missing batch market branches')
        if r['state'] == 'PASS':
            add(gid, BATCH, 'games.game_id=' + gid, batch['recorded_at_utc'])

    pairs = {r['away_team'] + ' @ ' + r['home_team']: gid for gid, r in census.items()}
    for match in re.finditer(r'^### (.+?) — (PASS|CONDITIONAL|EXCLUSION)\n(.*?)(?=^### |^## |\Z)',
                             sources[LATE]['content'], re.M | re.S):
        pair, state, section = match.groups()
        if pair not in pairs:
            raise ValueError('unknown ordered pair')
        if state == 'PASS':
            for label in ('Both spread selections:', 'Both moneyline selections:', 'Over and under:'):
                if label not in section:
                    raise ValueError('missing paired market judgment')
            add(pairs[pair], LATE, 'heading=' + pair, '2026-10-23T16:14:17Z')

    for match in re.finditer(r'^## (\d+) (.+?) — current PASS.*?\n(.*?)(?=^## |\Z)',
                             sources[SAT]['content'], re.M | re.S):
        gid, pair, section = match.groups()
        if gid not in census:
            raise ValueError('unknown focused identity')
        for label in ('Favorite spread:', 'Underdog spread:', 'Away ML:', 'Home ML:', 'Over:', 'Under:'):
            if label not in section:
                raise ValueError('missing focused market judgment')
        add(gid, SAT, 'heading game_id=' + gid, '2026-10-23T03:30:50Z')

    for match in re.finditer(r'^### (\d+) (.+?)\n(.*?)(?=^### |^## |\Z)',
                             sources[SEVEN]['content'], re.M | re.S):
        gid, pair, section = match.groups()
        if gid not in census or pairs.get(pair) != gid:
            raise ValueError('focused ordered pair mismatch')
        if 'State: PASS.' in section:
            for label in BRANCHES:
                if '- ' + label + ':' not in section:
                    raise ValueError('missing final market judgment')
            add(gid, SEVEN, 'heading game_id=' + gid, '2026-10-23T11:31:21Z')

    rows = []
    for gid in sorted(target):
        row = {'game_id': gid, 'game': census[gid]['away_team'] + ' @ ' + census[gid]['home_team'],
               'canonical_state': decisions[gid]['state'],
               'canonical_reason': decisions[gid]['reason'],
               'classification': 'ANALYTICAL_PASS_RECORD_RECOVERED' if records[gid]
                                 else 'PARTIAL_REVIEW_IN_RECOVERED_LINEAGE',
               'analytical_pass_evidence': records[gid],
               'partial_review_source': {'path': PARTIAL, 'blob': sources[PARTIAL]['sha'],
                                         'status': partial[gid]['review_status']}}
        rows.append(row)
    return {'scope': 'HISTORICAL_EVIDENCE_RECOVERY_NOT_NEW_RECOMMENDATIONS',
            'source_commit': 'c3eca98aa43f72b4da1f5d7906fa72a10aa30379',
            'canonical_boundary_utc': fixture['decision']['as_of_utc'],
            'population': 40, 'counts': dict(Counter(r['classification'] for r in rows)),
            'limitations': ['Saved analytical PASS is not current material/source clearance.',
                            'Incomplete means incomplete in the recovered lineage; no exhaustive absence claim.',
                            'No historical recommendation, outcome, financial edge, execution or model change.'],
            'rows': rows}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repository-root', type=Path, default=Path('.'))
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    commit = 'c3eca98aa43f72b4da1f5d7906fa72a10aa30379'

    def saved(path):
        return subprocess.run(['git', 'show', commit + ':' + path], cwd=args.repository_root,
                              check=True, capture_output=True).stdout.decode('utf-8')

    decision_text = saved(PREFIX + 'CFB_DECISION_WAIT_LEDGER.md')
    packets = re.findall(r'^```cfb-week8-decision-v1\s*\n(.*?)^```', decision_text, re.M | re.S)
    if not packets:
        raise ValueError('missing original decision packet')
    fixture = {'lineage': json.loads(saved('evidence/scheduler_qa/CFB_WEEK8_ORIGINAL_ANCESTRY_RECOVERY_20261020.json')),
               'decision': json.loads(packets[-1])}
    sources = {}
    for path in (BATCH, PARTIAL, LATE, SAT, SEVEN):
        content = saved(path)
        raw = content.encode('utf-8')
        digest = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
        sources[path] = {'content': content, 'sha': digest}
    before = copy.deepcopy(fixture)
    result = reconcile(fixture, sources)
    assert fixture == before
    assert result['counts'] == {'ANALYTICAL_PASS_RECORD_RECOVERED': 38,
                               'PARTIAL_REVIEW_IN_RECOVERED_LINEAGE': 2}
    assert {r['game_id'] for r in result['rows'] if not r['analytical_pass_evidence']} == {'401869845', '401862807'}
    # Semantic faults must fail before producing a report.
    for kind in ('duplicate', 'missing_identity', 'wrong_model', 'missing_market', 'wrong_pair'):
        f, s = copy.deepcopy(fixture), copy.deepcopy(sources)
        if kind == 'duplicate': f['decision']['rows'].append(f['decision']['rows'][0])
        elif kind == 'missing_identity': f['decision']['rows'].pop()
        elif kind in ('wrong_model', 'missing_market'):
            b = json.loads(s[BATCH]['content'])
            if kind == 'wrong_model': b['games'][0]['original_model'] = 'Wrong game'
            else: b['games'][0]['market_dispositions'].pop('OVER')
            s[BATCH]['content'] = json.dumps(b)
        else: s[LATE]['content'] = s[LATE]['content'].replace('Duke @ Virginia — PASS', 'Texas @ Virginia — PASS', 1)
        try: reconcile(f, s)
        except ValueError: pass
        else: raise AssertionError('accepted mutation: ' + kind)
    result['recorded_at_utc'] = datetime.now(timezone.utc).isoformat()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'counts': result['counts'], 'semantic_rejections': 5,
                      'incomplete': [r['game'] for r in result['rows'] if not r['analytical_pass_evidence']]}, indent=2))
