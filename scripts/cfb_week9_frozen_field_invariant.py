"""Independent exact-original Week9 display/identity invariant; not betting acceptance."""
import argparse
import html
import json
from pathlib import Path
import cfb_neutral_publication_gate as gate
from cfb_week7_first_frozen_projection_gate import archive, FIRST_SHA, CUTOFF, fair
from cfb_cbs_full_board_normalizer import WEEK9_LINEAGE_SHA


def original(lineage, first):
    if gate.blob(lineage) != WEEK9_LINEAGE_SHA:
        raise ValueError('unqualified Week9 lineage')
    targets, predictions, exclusions = archive(first, FIRST_SHA, 'challenger_b_2026_', '_v1_206', (622, 526, 96), CUTOFF)
    rows = json.loads(lineage, object_pairs_hook=gate.unique)['rows']
    if len(rows) != 56 or len({r['game_id'] for r in rows}) != 56:
        raise ValueError('Week9 lineage census mismatch')
    for row in rows:
        gid = row['game_id']
        t = targets.get(gid)
        if t is None or any(t[k] != row[k] for k in ('away_team', 'home_team')) or t['start_date'] != row['first_frozen_start']:
            raise ValueError('Week9 original target identity/start mismatch')
        modeled = gid in predictions
        expected = fair(predictions[gid]) if modeled else 'FIRST_FROZEN EXCLUDED — ' + exclusions[gid]['reasons']
        if row['display'] != expected or row['first_frozen_status'] != ('PREDICTION' if modeled else 'EXCLUDED'):
            raise ValueError('Week9 original display/status changed')
        values = {k: predictions[gid][k] for k in ('pred_margin', 'pred_total', 'pred_win')} if modeled else None
        if row['original_numeric_strings'] != values or row['first_frozen_exclusion'] != (None if modeled else exclusions[gid]['reasons']):
            raise ValueError('Week9 original numeric/exclusion strings changed')
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
            raise ValueError('duplicate Week9 frozen display identity')
        found[cells[1]] = html.unescape(cells[2])
    if found != expected:
        raise ValueError('complete Week9 original frozen display mismatch')
    declaration = '**Frozen-model boundary:** Original accepted FIRST_FROZEN cutoff ' + CUTOFF + '; 45 predictions and 11 exclusions; no REFRESH substitution.'
    if sheet.splitlines().count(declaration) != 1:
        raise ValueError('Week9 original cutoff/count declaration required')
    return {'verdict': 'PASS_WEEK9_ORIGINAL_FROZEN_FIELDS_ONLY', 'games': 56,
            'predictions': 45, 'exclusions': 11, 'numeric_fields': 135,
            'scope': 'original fields only, not market/review/publication/betting acceptance'}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('sheet', 'lineage', 'first'):
        p.add_argument('--' + key, required=True, type=Path)
    a = p.parse_args()
    print(json.dumps(audit(a.sheet.read_text(), a.lineage.read_text(), a.first), indent=2))
