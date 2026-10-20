"""Authenticate original Week8 fields independently of market/publication acceptance."""
import argparse,json,html
from pathlib import Path
import cfb_neutral_publication_gate as gate
from cfb_week7_first_frozen_projection_gate import archive,FIRST_SHA,CUTOFF,fair
from cfb_cbs_full_board_normalizer import WEEK8_LINEAGE_SHA

def original(lineage,first):
    if gate.blob(lineage)!=WEEK8_LINEAGE_SHA:raise ValueError('unqualified Week8 lineage')
    targets,predictions,exclusions=archive(first,FIRST_SHA,'challenger_b_2026_','_v1_206',(622,526,96),CUTOFF)
    rows=json.loads(lineage,object_pairs_hook=gate.unique)['rows']
    if len(rows)!=56 or len({r['game_id'] for r in rows})!=56:raise ValueError('Week8 lineage census mismatch')
    for row in rows:
        gid=row['game_id'];t=targets.get(gid)
        if t is None or any(t[k]!=row[k] for k in ('away_team','home_team')) or t['start_date']!=row['first_frozen_start']:
            raise ValueError('original target identity/start mismatch')
        expected=fair(predictions[gid]) if gid in predictions else 'FIRST_FROZEN EXCLUDED — '+exclusions[gid]['reasons']
        state='PREDICTION' if gid in predictions else 'EXCLUDED'
        if row['display']!=expected or row['first_frozen_status']!=state or row['first_frozen_exclusion']!=(None if gid in predictions else exclusions[gid]['reasons']):
            raise ValueError('original numeric/exclusion projection mismatch')
    return rows


def audit(sheet,lineage,first):
    rows=original(lineage,first);expected={r['away_team']+' @ '+r['home_team']:r['display'] for r in rows};found={}
    for line in sheet.splitlines():
        if not line.startswith('|'):continue
        cells=[c.strip() for c in line.strip('|').split('|')]
        if len(cells)!=9 or cells[1] not in expected:continue
        if cells[1] in found:raise ValueError('duplicate frozen display identity')
        found[cells[1]]=html.unescape(cells[2])
    if found!=expected:raise ValueError('complete original frozen fields/identity union mismatch')
    declaration='**Frozen-model boundary:** Original accepted FIRST_FROZEN cutoff '+CUTOFF+'; 49 predictions and 7 exclusions; no REFRESH substitution.'
    if sheet.splitlines().count(declaration)!=1:raise ValueError('original cutoff/count declaration required')
    return {'verdict':'PASS_WEEK8_ORIGINAL_FROZEN_FIELDS_ONLY','games':56,'predictions':49,'exclusions':7,'numeric_fields':147,'scope':'original fields only; not market/decision/publication/betting acceptance'}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('sheet','lineage','first'):p.add_argument('--'+key,required=True,type=Path)
    a=p.parse_args();print(json.dumps(audit(a.sheet.read_text(),a.lineage.read_text(),a.first),indent=2))
