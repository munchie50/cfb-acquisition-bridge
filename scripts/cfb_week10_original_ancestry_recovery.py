"""Recover exact accepted original fields for the independently joined Week10 IDs.

Read-only archive recovery. No model execution, REFRESH substitution, current
kickoff qualification, decision authoring or operational selection.
"""
import argparse
import json
import math
from pathlib import Path

from cfb_neutral_publication_gate import blob, unique
from cfb_week7_first_frozen_projection_gate import archive, FIRST_SHA, CUTOFF, fair

INVENTORY_PATH = 'evidence/audits/CFB_WEEK10_ACCEPTED_REFRESH_R91_JOIN_20261104.json'
INVENTORY_SHA = '8fd0ba1f85e37b940d9bfe5f13188e2da956b32d'


def recover(first, inventory):
    if blob(inventory) != INVENTORY_SHA:
        raise ValueError('unqualified Week10 inventory binding')
    source = json.loads(inventory, object_pairs_hook=unique)
    if source.get('schema') != 'CFB_WEEK10_ACCEPTED_REFRESH_R91_IDENTITY_JOIN_AUDIT':
        raise ValueError('unqualified Week10 inventory schema')
    census = source['rows']
    ids = {r['game_id'] for r in census}
    if len(census) != 63 or len(ids) != 63:
        raise ValueError('Week10 inventory must contain 63 unique identities')
    targets, predictions, exclusions = archive(
        first, FIRST_SHA, 'challenger_b_2026_', '_v1_206', (622, 526, 96), CUTOFF)
    rows = []
    for identity in census:
        gid = identity['game_id']
        target = targets.get(gid)
        if target is None or any(target[k] != identity[k] for k in ('away_team', 'home_team')):
            raise ValueError('original directed Week10 identity mismatch: ' + gid)
        if (gid in predictions) == (gid in exclusions):
            raise ValueError('original prediction/exclusion partition mismatch')
        original = predictions.get(gid, exclusions.get(gid))
        if any(original[k] != target[k] for k in ('away_team', 'home_team', 'population_class')):
            raise ValueError('original ordered identity mismatch')
        values = ({k: predictions[gid][k] for k in ('pred_margin', 'pred_total', 'pred_win')}
                  if gid in predictions else None)
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
    rows.sort(key=lambda r: (r['first_frozen_start'], r['game_id']))
    modeled = sum(r['first_frozen_status'] == 'PREDICTION' for r in rows)
    if modeled != 55 or len(rows) - modeled != 8:
        raise ValueError('original Week10 prediction/exclusion counts differ')
    return {
        'status': 'RECOVERED_ACCEPTED_ORIGINAL_EXACT_ID_COHORT_ONLY_NOT_CURRENT_PUBLICATION_ACCEPTANCE',
        'original_artifact_id': 10897612260, 'original_zip_sha256': FIRST_SHA,
        'original_cutoff_utc': CUTOFF,
        'cohort_rule': 'Exact 63 directed inventory IDs; not a date-only or FBS_VS_FBS-only filter',
        'inventory_path': INVENTORY_PATH, 'inventory_blob': INVENTORY_SHA,
        'targets': 63, 'predictions': 55, 'exclusions': 8, 'numeric_fields': 165,
        'source_of_numbers': 'EXACT_ORIGINAL_ACCEPTED_STRINGS_NO_RECOMPUTATION_OR_REFRESH_SUBSTITUTION',
        'qualified_current_kickoffs': 0, 'publication_profile_accepted': False,
        'remaining': 'Current kickoff/source qualification, independently earned decisions and explicit publication integration; accepted weekly REFRESH remains separate.',
        'rows': rows,
    }


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--first', type=Path, required=True)
    p.add_argument('--inventory', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    if a.output.resolve() in {a.first.resolve(), a.inventory.resolve()}:
        p.error('output must not overwrite source evidence')
    result = recover(a.first, a.inventory.read_text())
    a.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'rows'}, indent=2))
