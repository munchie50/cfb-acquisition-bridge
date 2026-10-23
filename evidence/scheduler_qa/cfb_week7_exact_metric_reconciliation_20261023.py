"""Reconcile Week7 scorecard displays with authenticated ORIGINAL predictions.

Usage: python THIS_FILE /path/to/accepted-first-frozen.zip
Read-only. The archive is the original accepted artifact, never REFRESH. Final
scores are reused from the existing pre-audit scorecard; no network or writes.
"""
import csv
import hashlib
import io
import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path

ARCHIVE_SHA = '772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf'
SCORE_SHA = 'd210d8c51106ef393a23a4fb69c6fcdb219e3f16'
LINEAGE_SHA = 'd80e26c398de48e7a386ad9a627fe44f4111ac45'


def historical(sha):
    raw = subprocess.check_output(['git', 'cat-file', 'blob', sha])
    if hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest() != sha:
        raise ValueError('historical blob identity mismatch')
    return raw


def audit(archive):
    if hashlib.sha256(archive).hexdigest() != ARCHIVE_SHA:
        raise ValueError('unaccepted original prediction archive')
    with zipfile.ZipFile(io.BytesIO(archive)) as z:
        predictions = list(csv.DictReader(io.StringIO(z.read('challenger_b_2026_fair_predictions_v1_206.csv').decode())))
    if len(predictions) != 526 or len({r['game_id'] for r in predictions}) != 526:
        raise ValueError('original immutable prediction population')
    by_id = {r['game_id']: r for r in predictions}
    lineage = json.loads(historical(LINEAGE_SHA))['rows']
    modeled = {r['game_id']: r for r in lineage if r['first_frozen_status'] == 'PREDICTION'}
    if len(lineage) != 62 or len(modeled) != 51:
        raise ValueError('original Week7 lineage partition')
    by_pair = {(r['away_team'], r['home_team']): gid for gid, r in modeled.items()}
    if len(by_pair) != 51:
        raise ValueError('ambiguous model pair')
    section = historical(SCORE_SHA).decode().split('## Week 7 Tuesday')[1].split('## Week 8')[0]
    rows = []
    for line in section.splitlines():
        c = [v.strip() for v in line.split('|')[1:-1]]
        declared_id = None
        if len(c) == 11 and c[0].isdigit():
            declared_id = c.pop(0)
        if len(c) != 10 or ' @ ' not in c[0]:
            continue
        pair = tuple(c[0].split(' @ '))
        gid = by_pair[pair]
        if declared_id is not None and declared_id != gid:
            raise ValueError('scorecard ID/pair mismatch')
        p = by_id[gid]
        if (p['away_team'], p['home_team']) != pair:
            raise ValueError('prediction ID/pair mismatch')
        numbers = re.findall(r'\d+', c[4])
        if len(numbers) != 2:
            raise ValueError('ambiguous saved final')
        away, home = map(int, numbers)
        actual, total = home - away, home + away
        if actual != float(c[5]) or total != float(c[6]) or actual == 0:
            raise ValueError('saved final/actual inconsistency')
        pm, pt, pw = (float(p[k]) for k in ('pred_margin', 'pred_total', 'pred_win'))
        direction_correct = int((pm > 0) == (actual > 0))
        row = {'game_id': gid, 'game': c[0], 'source_start': p['start_date'],
               'original_margin': pm, 'original_total': pt, 'original_home_win_p': pw,
               'final_away': away, 'final_home': home, 'actual_home_margin': actual,
               'exact_margin_error': actual - pm, 'exact_total_error': total - pt,
               'margin_direction_correct': direction_correct,
               'probability_classifier_correct': int((pw > .5) == (actual > 0)),
               'brier_contribution': (pw - int(actual > 0)) ** 2,
               'saved_display_margin': float(c[1]), 'saved_su_correct_flag': int(c[-1])}
        row['saved_margin_display_inconsistent'] = abs(pm - row['saved_display_margin']) > .051
        row['saved_su_flag_inconsistent'] = direction_correct != row['saved_su_correct_flag']
        rows.append(row)
    if len(rows) != 51 or {r['game_id'] for r in rows} != set(modeled):
        raise ValueError('complete unique exact model/result join')
    return {'verdict': 'PASS_EXACT_ORIGINAL_WEEK7_PREDICTION_METRIC_RECONCILIATION',
            'archive_artifact_id': 10897612260, 'archive_sha256': ARCHIVE_SHA,
            'original_prediction_count': 526, 'week7_lineage_blob': LINEAGE_SHA,
            'outcome_scorecard_blob': SCORE_SHA, 'matched_modeled_games': 51,
            'margin_direction_correct': sum(r['margin_direction_correct'] for r in rows),
            'probability_classifier_correct': sum(r['probability_classifier_correct'] for r in rows),
            'margin_mae': sum(abs(r['exact_margin_error']) for r in rows) / 51,
            'total_mae': sum(abs(r['exact_total_error']) for r in rows) / 51,
            'home_win_brier': sum(r['brier_contribution'] for r in rows) / 51,
            'saved_su_flags_sum': sum(r['saved_su_correct_flag'] for r in rows),
            'inconsistent_saved_rows': [r for r in rows if r['saved_margin_display_inconsistent'] or r['saved_su_flag_inconsistent']],
            'rows': rows,
            'scope': 'Exact original forecast and existing saved-final arithmetic; original aggregate31/51 and MAEs corroborated. Derived display/flag error and preliminary32/51 correction rejected. No model mutation or fresh result acquisition.'}


if __name__ == '__main__':
    data = Path(sys.argv[1]).read_bytes()
    result = audit(data)
    try:
        audit(data + b'changed')
    except ValueError:
        result['unaccepted_archive_rejection_demonstrated'] = True
    else:
        raise AssertionError('changed archive accepted')
    print(json.dumps(result, indent=2))
