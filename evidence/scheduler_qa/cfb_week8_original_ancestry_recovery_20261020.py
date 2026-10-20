"""Read-only recovery of already accepted Week8 original lineage, no publication."""
import json,re,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'scripts'))
from cfb_week7_first_frozen_projection_gate import archive,FIRST_SHA,CUTOFF,fair
from cfb_week7_accepted_s0_ancestry_audit import ALIASES
from cfb_cbs_full_board_normalizer import cells
from cfb_hot_sheet_current_decision_binding_gate import blob

def recover(first,board):
    targets,predictions,exclusions=archive(first,FIRST_SHA,'challenger_b_2026_','_v1_206',(622,526,96),CUTOFF)
    aliases={**ALIASES,'New Mexico St.':'New Mexico State','Boise St.':'Boise State','Utah St.':'Utah State','Iowa St.':'Iowa State'}
    names=[]
    for line in board.splitlines():
        if not line.startswith('|'):continue
        c=cells(line)
        n=re.findall(r'(?<!!)\[([^\]]+)\]\(https://www\.cbssports\.com/college-football/teams/[^)]+\)',c[0])
        if n:names.append(aliases.get(n[-1],n[-1]))
    assert len(names)==112
    pairs=list(zip(names[::2],names[1::2]));assert len(set(pairs))==56
    rows=[]
    for away,home in pairs:
        match=[r for r in targets.values() if (r['away_team'],r['home_team'])==(away,home)]
        assert len(match)==1,(away,home)
        r=match[0];gid=r['game_id'];assert '2026-10-20'<=r['start_date'][:10]<='2026-10-25'
        rows.append({'game_id':gid,'away_team':away,'home_team':home,'first_frozen_start':r['start_date'],
            'first_frozen_status':'PREDICTION' if gid in predictions else 'EXCLUDED',
            'display':fair(predictions[gid]) if gid in predictions else 'FIRST_FROZEN EXCLUDED — '+exclusions[gid]['reasons'],
            'first_frozen_exclusion':None if gid in predictions else exclusions[gid]['reasons']})
    assert len({r['game_id'] for r in rows})==56
    assert sum(r['first_frozen_status']=='PREDICTION' for r in rows)==49
    return {'status':'RECOVERED_ACCEPTED_ORIGINAL_LINEAGE_ONLY_NOT_PUBLICATION_ACCEPTANCE',
      'original_artifact_id':10897612260,'original_zip_sha256':FIRST_SHA,'original_cutoff_utc':CUTOFF,
      'board_blob':blob(board),'board_role':'RETAINED_IDENTITY_CENSUS_ONLY_NOT_FRESH_MARKET',
      'targets':56,'predictions':49,'exclusions':7,'numeric_fields':147,
      'source_of_numbers':'ORIGINAL_ACCEPTED_BYTES_NO_RECOMPUTATION_OR_REFRESH_SUBSTITUTION',
      'remaining':'Week8 publication profile/bootstrap and actual kickoff/decision/source qualification; Tuesday refresh is separate.',
      'rows':rows}
if __name__=='__main__':
    result=recover(Path(sys.argv[1]),Path(sys.argv[2]).read_text())
    Path(sys.argv[3]).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
