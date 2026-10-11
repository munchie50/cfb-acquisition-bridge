"""Week7 original frozen-field invariant, independent of full cycle acceptance."""
import argparse,json,re
from pathlib import Path
from cfb_hot_sheet_current_decision_binding_gate import blob
from cfb_week7_accepted_s0_ancestry_audit import ALIASES
from cfb_week7_first_frozen_projection_gate import archive,fair,FIRST_SHA,CUTOFF

LINEAGE_SHA='d80e26c398de48e7a386ad9a627fe44f4111ac45'

def audit(sheet,first,lineage):
    if blob(lineage)!=LINEAGE_SHA:raise ValueError('unqualified Week7 identity census')
    census=json.loads(lineage);cr=census['rows']
    if len(cr)!=62 or len({r['game_id'] for r in cr})!=62:raise ValueError('census ID mismatch')
    t,p,e=archive(first,FIRST_SHA,'challenger_b_2026_','_v1_206',(622,526,96),CUTOFF)
    pairs={}
    for r in cr:
        gid=r['game_id']
        if gid not in t or any(r[k]!=t[gid][k] for k in ('away_team','home_team')):raise ValueError('census/archive identity mismatch')
        key=(r['away_team'],r['home_team'])
        if key in pairs:raise ValueError('ambiguous directed matchup; game-ID display required')
        predicted=gid in p
        if r['first_frozen_status']!=('PREDICTION' if predicted else 'EXCLUDED'):raise ValueError('census status mismatch')
        value=fair(p[gid]) if predicted else 'FIRST_FROZEN EXCLUDED — '+e[gid]['reasons']+'; Oct6 REFRESH '+r['oct6_refresh_status']+' (not substituted)'
        if value!=r['display']:raise ValueError('accepted display census mismatch')
        pairs[key]=(gid,value,predicted)
    boundaries=re.findall(r'^\*\*Frozen-model boundary:\*\* (.+)$',sheet,re.M)
    if len(boundaries)!=1 or 'FIRST_FROZEN' not in boundaries[0] or CUTOFF not in boundaries[0]:
        raise ValueError('original frozen cutoff/lineage declaration required')
    seen=set();matched=excluded=0;section=None
    for line in sheet.splitlines():
        if line.startswith('## '):section=line[3:].strip()
        if not line.startswith('| '):continue
        cells=[c.strip() for c in line.strip('|').split('|')]
        if not cells or not re.match(r'^(Tue|Wed|Thu|Fri|Sat|UNRESOLVED)\b',cells[0]):continue
        if section=='FULL WEEKLY SLATE' and len(cells)==2 and cells[0]=='UNRESOLVED KICKOFF' and cells[1].isdigit():continue
        if len(cells)==4:continue # watchlist view; not the governed nine-column population
        if len(cells)!=9:raise ValueError('unsupported governed row schema')
        parts=cells[1].split(' @ ')
        if len(parts)!=2:raise ValueError('ordered matchup required')
        key=tuple(ALIASES.get(n,n) for n in parts)
        if key not in pairs:raise ValueError('unqualified/unknown Week7 matchup')
        gid,value,predicted=pairs[key]
        if gid in seen:raise ValueError('duplicate governed identity')
        if cells[2]!=value:raise ValueError('original frozen value/exclusion/refresh-substitution mismatch')
        seen.add(gid);matched+=predicted;excluded+=not predicted
    if seen!={r['game_id'] for r in cr} or (matched,excluded)!=(51,11):
        raise ValueError('governed original prediction/exclusion union mismatch')
    return {'verdict':'PASS_ORIGINAL_FROZEN_FIELDS_ONLY','games':62,'predictions':matched,'exclusions':excluded,
            'numeric_fields':153,'favorite_directions':51,'archive_sha256':FIRST_SHA,
            'lineage_census_blob':LINEAGE_SHA,'sheet_blob':blob(sheet),
            'scope':'original frozen fields/exclusions only; publication cycle, market/decision/cutoff/current-source truth NOT accepted'}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for n in ('sheet','first','lineage'):p.add_argument('--'+n,required=True,type=Path)
    a=p.parse_args();print(json.dumps(audit(a.sheet.read_text(),a.first,a.lineage.read_text()),indent=2))
