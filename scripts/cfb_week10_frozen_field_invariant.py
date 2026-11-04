"""Independent exact-original Week10 display/identity invariant; not betting acceptance."""
import argparse
import html
import json
from pathlib import Path

from cfb_neutral_publication_gate import blob, unique
from cfb_week7_first_frozen_projection_gate import archive, FIRST_SHA, CUTOFF, fair

LINEAGE_SHA = '47736c0fd9ff49545db7e46b508805658a1c7a92'


def original(lineage, first):
    if blob(lineage) != LINEAGE_SHA:
        raise ValueError('unqualified Week10 original lineage')
    targets, predictions, exclusions = archive(
        first, FIRST_SHA, 'challenger_b_2026_', '_v1_206', (622, 526, 96), CUTOFF)
    rows = json.loads(lineage, object_pairs_hook=unique)['rows']
    if len(rows) != 63 or len({r['game_id'] for r in rows}) != 63:
        raise ValueError('Week10 original census mismatch')
    modeled = 0
    for row in rows:
        gid = row['game_id']
        target = targets.get(gid)
        if (target is None or any(target[k] != row[k] for k in ('away_team', 'home_team'))
                or target['start_date'] != row['first_frozen_start']):
            raise ValueError('Week10 original target identity/start mismatch')
        if (gid in predictions) == (gid in exclusions):
            raise ValueError('Week10 original prediction/exclusion partition mismatch')
        predicted = gid in predictions
        modeled += predicted
        expected = fair(predictions[gid]) if predicted else 'FIRST_FROZEN EXCLUDED — ' + exclusions[gid]['reasons']
        if row['display'] != expected or row['first_frozen_status'] != ('PREDICTION' if predicted else 'EXCLUDED'):
            raise ValueError('Week10 original display/status changed')
        values = {k: predictions[gid][k] for k in ('pred_margin', 'pred_total', 'pred_win')} if predicted else None
        if (row['original_numeric_strings'] != values
                or row['first_frozen_exclusion'] != (None if predicted else exclusions[gid]['reasons'])):
            raise ValueError('Week10 original numeric/exclusion strings changed')
    if modeled != 55:
        raise ValueError('Week10 original prediction count changed')
    return rows


def audit(sheet, lineage, first):
    rows = original(lineage, first)
    expected = {r['away_team'] + ' @ ' + r['home_team']: r['display'] for r in rows}
    found = {}
    for line in sheet.splitlines():
        if not line.startswith('|'):
            continue
        cells = [x.strip() for x in line.strip('|').split('|')]
        if len(cells) != 9 or cells[1] not in expected:
            continue
        if cells[1] in found:
            raise ValueError('duplicate Week10 frozen display identity')
        found[cells[1]] = html.unescape(cells[2])
    if found != expected:
        raise ValueError('complete Week10 original frozen display mismatch')
    declaration = ('**Frozen-model boundary:** Original accepted FIRST_FROZEN cutoff ' + CUTOFF
                   + '; 55 predictions and 8 exclusions; no REFRESH substitution.')
    if sheet.splitlines().count(declaration) != 1:
        raise ValueError('Week10 original cutoff/count declaration required')
    return {'verdict': 'PASS_WEEK10_ORIGINAL_FROZEN_FIELDS_ONLY', 'games': 63,
            'predictions': 55, 'exclusions': 8, 'numeric_fields': 165,
            'scope': 'original fields only, not market/review/publication/betting acceptance'}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('sheet', 'lineage', 'first'):
        p.add_argument('--' + key, required=True, type=Path)
    a = p.parse_args()
    print(json.dumps(audit(a.sheet.read_text(), a.lineage.read_text(), a.first), indent=2))
