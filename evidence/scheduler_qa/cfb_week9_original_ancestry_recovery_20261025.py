"""Recover accepted original Week9 date-cohort bytes; not current-slate acceptance.

No network, model execution, source timing qualification or operational writes.
"""
import argparse
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))
from cfb_week7_first_frozen_projection_gate import archive, FIRST_SHA, CUTOFF, fair


def recover(first):
    targets, predictions, exclusions = archive(
        first, FIRST_SHA, 'challenger_b_2026_', '_v1_206', (622, 526, 96), CUTOFF)
    cohort = [r for r in targets.values()
              if r['population_class'] == 'FBS_VS_FBS'
              and '2026-10-27' <= r['start_date'][:10] < '2026-11-02']
    ids = {r['game_id'] for r in cohort}
    if len(cohort) != 56 or len(ids) != 56:
        raise ValueError('original Week9 date-cohort identity/count mismatch')
    rows = []
    for target in sorted(cohort, key=lambda r: (r['start_date'], r['game_id'])):
        gid = target['game_id']
        if (gid in predictions) == (gid in exclusions):
            raise ValueError('prediction/exclusion partition mismatch')
        original = predictions.get(gid, exclusions.get(gid))
        if any(original[k] != target[k] for k in ('away_team', 'home_team', 'population_class')):
            raise ValueError('original ordered identity mismatch')
        values = {k: predictions[gid][k] for k in ('pred_margin', 'pred_total', 'pred_win')} if gid in predictions else None
        if values is not None and (not all(math.isfinite(float(v)) for v in values.values())
                                   or not 0 <= float(values['pred_win']) <= 1):
            raise ValueError('invalid original numeric field')
        rows.append({
            'game_id': gid, 'away_team': target['away_team'], 'home_team': target['home_team'],
            'first_frozen_start': target['start_date'],
            'first_frozen_status': 'PREDICTION' if values is not None else 'EXCLUDED',
            'original_numeric_strings': values,
            'display': fair(predictions[gid]) if values is not None else 'FIRST_FROZEN EXCLUDED — ' + exclusions[gid]['reasons'],
            'first_frozen_exclusion': None if values is not None else exclusions[gid]['reasons'],
            'current_qualified_kickoff_utc': None,
        })
    modeled = sum(r['first_frozen_status'] == 'PREDICTION' for r in rows)
    if modeled != 45 or len(rows) - modeled != 11:
        raise ValueError('original Week9 prediction/exclusion counts differ')
    return {
        'status': 'RECOVERED_ACCEPTED_ORIGINAL_DATE_COHORT_ONLY_NOT_CURRENT_SLATE_OR_PUBLICATION_ACCEPTANCE',
        'original_artifact_id': 10897612260, 'original_zip_sha256': FIRST_SHA,
        'original_cutoff_utc': CUTOFF,
        'cohort_rule': 'FBS_VS_FBS; original target UTC dates 2026-10-27 inclusive through 2026-11-02 exclusive',
        'targets': 56, 'predictions': 45, 'exclusions': 11, 'numeric_fields': 135,
        'source_of_numbers': 'EXACT_ORIGINAL_ACCEPTED_STRINGS_NO_RECOMPUTATION_OR_REFRESH_SUBSTITUTION',
        'current_cbs_slate_reconciled': False, 'qualified_current_kickoffs': 0,
        'publication_profile_accepted': False,
        'remaining': 'Independent complete current CBS Week9 identity census/source/kickoff qualification, explicit publication-profile qualification and genuinely earned decisions; Tuesday refresh remains separate.',
        'rows': rows,
    }


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--first', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    if a.first.resolve() == a.output.resolve():
        p.error('output must not overwrite the accepted archive')
    result = recover(a.first)
    a.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'rows'}, indent=2))
