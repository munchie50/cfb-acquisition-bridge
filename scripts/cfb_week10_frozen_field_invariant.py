"""Independent exact-original Week10/11 display/identity invariant; not betting acceptance."""
import argparse
import html
import json
from pathlib import Path

from cfb_neutral_publication_gate import blob, profile_config, unique
from cfb_week7_first_frozen_projection_gate import archive, FIRST_SHA, CUTOFF, fair

LINEAGE_SHA = '47736c0fd9ff49545db7e46b508805658a1c7a92'


def original(lineage, first, profile='WEEK10'):
    if profile not in ('WEEK10', 'WEEK11'):
        raise ValueError('unsupported original field audit profile')
    cfg = profile_config(profile)
    if blob(lineage) != cfg['lineage']:
        raise ValueError(f'unqualified {profile} original lineage')
    targets, predictions, exclusions = archive(
        first, FIRST_SHA, 'challenger_b_2026_', '_v1_206', (622, 526, 96), CUTOFF)
    rows = json.loads(lineage, object_pairs_hook=unique)['rows']
    if len(rows) != cfg['count'] or len({r['game_id'] for r in rows}) != cfg['count']:
        raise ValueError(f'{profile} original census mismatch')
    modeled = 0
    for row in rows:
        gid = row['game_id']
        target = targets.get(gid)
        if (target is None or any(target[k] != row[k] for k in ('away_team', 'home_team'))
                or target['start_date'] != row['first_frozen_start']):
            raise ValueError(f'{profile} original target identity/start mismatch')
        if (gid in predictions) == (gid in exclusions):
            raise ValueError(f'{profile} original prediction/exclusion partition mismatch')
        predicted = gid in predictions
        modeled += predicted
        expected = fair(predictions[gid]) if predicted else 'FIRST_FROZEN EXCLUDED — ' + exclusions[gid]['reasons']
        if row['display'] != expected or row['first_frozen_status'] != ('PREDICTION' if predicted else 'EXCLUDED'):
            raise ValueError(f'{profile} original display/status changed')
        values = {k: predictions[gid][k] for k in ('pred_margin', 'pred_total', 'pred_win')} if predicted else None
        if (row['original_numeric_strings'] != values
                or row['first_frozen_exclusion'] != (None if predicted else exclusions[gid]['reasons'])):
            raise ValueError(f'{profile} original numeric/exclusion strings changed')
    if modeled != cfg['predictions']:
        raise ValueError(f'{profile} original prediction count changed')
    return rows


def audit(sheet, lineage, first, profile='WEEK10'):
    rows = original(lineage, first, profile)
    cfg = profile_config(profile)
    expected = {r['away_team'] + ' @ ' + r['home_team']: r['display'] for r in rows}
    found = {}
    for line in sheet.splitlines():
        if not line.startswith('|'):
            continue
        cells = [x.strip() for x in line.strip('|').split('|')]
        if len(cells) != 9 or cells[1] not in expected:
            continue
        if cells[1] in found:
            raise ValueError(f'duplicate {profile} frozen display identity')
        found[cells[1]] = html.unescape(cells[2])
    if found != expected:
        raise ValueError(f'complete {profile} original frozen display mismatch')
    declaration = ('**Frozen-model boundary:** Original accepted FIRST_FROZEN cutoff ' + CUTOFF
                   + f"; {cfg['predictions']} predictions and {cfg['exclusions']} exclusions; no REFRESH substitution.")
    if sheet.splitlines().count(declaration) != 1:
        raise ValueError(f'{profile} original cutoff/count declaration required')
    return {'verdict': f'PASS_{profile}_ORIGINAL_FROZEN_FIELDS_ONLY', 'games': cfg['count'],
            'predictions': cfg['predictions'], 'exclusions': cfg['exclusions'],
            'numeric_fields': 3 * cfg['predictions'],
            'scope': 'original fields only, not market/review/publication/betting acceptance'}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('sheet', 'lineage', 'first'):
        p.add_argument('--' + key, required=True, type=Path)
    p.add_argument('--profile', choices=('WEEK10', 'WEEK11'), default='WEEK10')
    a = p.parse_args()
    print(json.dumps(audit(a.sheet.read_text(), a.lineage.read_text(), a.first, a.profile), indent=2))
