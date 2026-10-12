"""Explicit accepted October6 REFRESH field interface; never an operational selector."""
import argparse,json
from datetime import datetime
from pathlib import Path
from cfb_hot_sheet_current_decision_binding_gate import blob
from cfb_week7_first_frozen_projection_gate import archive,fair,REFRESH_SHA
from cfb_week7_frozen_field_invariant import LINEAGE_SHA

POINTER_SHA='6254ab28b90d9fa4a815124ea7ffec2850ddfc30'
ACCEPTANCE_SHA='a4fb4c56addf12335a477034673e167afc28ebb4'
CUTOFF='2026-10-06T15:11:29.838398+00:00'
SCOPE='ACCEPTED_REFRESH_FIELDS_ONLY_NOT_OPERATIONAL_SELECTION'

def prepare(refresh,pointer,acceptance,lineage):
    if (blob(pointer),blob(acceptance),blob(lineage))!=(POINTER_SHA,ACCEPTANCE_SHA,LINEAGE_SHA):
        raise ValueError('unqualified accepted boundary/acceptance/original-census identity')
    state=json.loads(pointer)
    if state['status']!='ACCEPTED_PREDICTION_SOURCE_STATE' or state['candidate_artifact_zip_sha256']!=REFRESH_SHA or state['accepted_cutoff_utc']!=CUTOFF:
        raise ValueError('accepted boundary mismatch')
    t,p,e=archive(refresh,REFRESH_SHA,'s0/challenger_b_2026_refresh_','_v1_246',(498,495,3),CUTOFF)
    original=json.loads(lineage)['rows'];records=[]
    for old in original:
        gid=old['game_id']
        if gid not in t or any(t[gid][k]!=old[k] for k in ('away_team','home_team')):raise ValueError('directed target identity mismatch')
        target=t[gid]
        if target['snapshot_type']!='REFRESH_SNAPSHOT' or target['snapshot_cutoff_utc']!=CUTOFF or datetime.fromisoformat(target['start_date'])<=datetime.fromisoformat(CUTOFF):
            raise ValueError('snapshot type/cutoff/future-target mismatch')
        row=p.get(gid,e.get(gid))
        if row['snapshot_type']!='REFRESH_SNAPSHOT' or row['snapshot_cutoff_utc']!=CUTOFF:raise ValueError('prediction/exclusion cutoff mismatch')
        predicted=gid in p
        field=fair(p[gid]).replace('FIRST_FROZEN:','REFRESH_SNAPSHOT:',1) if predicted else 'REFRESH_SNAPSHOT EXCLUDED — '+e[gid]['reasons']
        records.append({'game_id':gid,'away_team':old['away_team'],'home_team':old['home_team'],
                        'snapshot_type':'REFRESH_SNAPSHOT','snapshot_cutoff_utc':CUTOFF,
                        'snapshot_target_start':target['start_date'],'refresh_status':'PREDICTION' if predicted else 'EXCLUDED',
                        'refresh_field':field,'refresh_exclusion':None if predicted else e[gid]['reasons'],
                        'original_first_frozen_status':old['first_frozen_status'],
                        'original_first_frozen_exclusion':old['first_frozen_exclusion'],
                        'original_first_frozen_field':old['display']})
    if len({r['game_id'] for r in records})!=62 or sum(r['refresh_status']=='PREDICTION' for r in records)!=61:
        raise ValueError('bounded refresh population mismatch')
    return {'schema':'CFB_ACCEPTED_OCT6_REFRESH_FIELD_INTERFACE_V1','source_type':'REFRESH_SNAPSHOT',
            'cutoff_utc':CUTOFF,'artifact_zip_sha256':REFRESH_SHA,'scope':SCOPE,'records':records}

def audit(package,refresh,pointer,acceptance,lineage):
    expected=prepare(refresh,pointer,acceptance,lineage)
    if not isinstance(package,dict) or set(package)!=set(expected):raise ValueError('unsupported package fields')
    for k in expected:
        if k!='records' and package[k]!=expected[k]:raise ValueError('declared source/type/cutoff/scope mismatch')
    if not isinstance(package['records'],list) or len(package['records'])!=62:raise ValueError('record count mismatch')
    actual={r['game_id']:r for r in package['records']}
    wanted={r['game_id']:r for r in expected['records']}
    if len(actual)!=62 or actual!=wanted:raise ValueError('identity/value/original-lineage preservation mismatch')
    promoted=sum(r['original_first_frozen_status']=='EXCLUDED' and r['refresh_status']=='PREDICTION' for r in actual.values())
    return {'verdict':'PASS_ACCEPTED_REFRESH_FIELDS_ONLY','targets':62,'refresh_predictions':61,'refresh_exclusions':1,
            'numeric_fields':183,'original_predictions_unchanged':51,'original_exclusions_unchanged':11,
            'later_eligible_original_exclusions':promoted,'cutoff_utc':CUTOFF,'artifact_zip_sha256':REFRESH_SHA,
            'scope':SCOPE,'limitations':['Historical October6 accepted boundary only; later boundary requires independent qualification.',
                'Archive target clock is snapshot provenance, not current kickoff/cutoff authority.',
                'No current HotSheet selection, original overwrite, market, bet, acceptance/pointer promotion or numerical model rerun.']}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for n in ('refresh','pointer','acceptance','lineage'):p.add_argument('--'+n,required=True,type=Path)
    a=p.parse_args();pointer=a.pointer.read_text();acceptance=a.acceptance.read_text();lineage=a.lineage.read_text()
    diagnostic=prepare(a.refresh,pointer,acceptance,lineage)
    print(json.dumps(audit(diagnostic,a.refresh,pointer,acceptance,lineage),indent=2))
