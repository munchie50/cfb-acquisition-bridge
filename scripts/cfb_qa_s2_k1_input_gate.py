"""Read-only S2 input interface checks. Input checks never establish acceptance.

Read only explicit CSV projections; no raw/PBP, outcomes, coefficients or predictions
are constructed here. The caller must independently prove same-cutoff acceptance.
"""
import ast
import csv
import hashlib
from pathlib import Path
import numpy as np
import pandas as pd

PREFIX='challenger_b_2026_refresh_'

def frozen_interface():
    source=Path(__file__).with_name('cfb_qa_prospective_s2_k1_consumer_v1_2026_09_30.py')
    nodes=ast.parse(source.read_text()).body
    values={n.targets[0].id:ast.literal_eval(n.value) for n in nodes
            if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in ('FEATURES','MAP')}
    return values['FEATURES'],values['MAP']


def check(ok,reason):
    if not bool(ok):raise ValueError(reason)


def boolean(series):
    def one(v):
        if isinstance(v,(bool,np.bool_)):return bool(v)
        if str(v).strip().lower() in ('true','1'):return True
        if str(v).strip().lower() in ('false','0'):return False
        raise ValueError('INVALID_BOOLEAN')
    return series.map(one)


def counts(series):
    n=pd.to_numeric(series,errors='raise').to_numpy(float)
    check(np.isfinite(n).all() and (n>=0).all() and (n%1==0).all(),'INVALID_HISTORY_COUNT')
    return n


def times(series):
    t=pd.to_datetime(series,utc=True,errors='raise')
    check(t.notna().all(),'MISSING_CLOCK')
    # Require explicit timezone rather than silently interpreting naive data.
    check(all(pd.Timestamp(v).tzinfo is not None for v in series),'NAIVE_CLOCK')
    return t


def schemas():
    fs,mp=frozen_interface();snap=['snapshot_type','snapshot_cutoff_utc']
    return {
      'side':['game_id','side','team','target_kickoff','qualified_prior_games','eligible','reason']+fs+snap,
      'target':['season','game_id','start_date','home_team','away_team','neutral_site','population_class']+snap,
      'baseline':['game_id','team','target_kickoff','qualified_prior_games']+snap+[p+f for f in fs for p in ('baseline__','available__')],
      'context':['target_game_id','target_side','target_team','target_kickoff','source_game_id','source_kickoff','source_opponent','opponent_qualified_prior_games','mechanical_history_complete','derived_history_complete']+[p+mp[f] if p!='context_valid__' else p+f for f in mp for p in ('baseline__','raw__','context_valid__')]+snap,
      'predicted':['season','game_id','start_date','home_team','away_team','venue_state','pred_margin','pred_total','pred_win']+snap,
      'excluded':['season','game_id','start_date','home_team','away_team','reasons']+snap,
      'chronology':['game_id','side','team','prior_games','max_prior_kickoff','target_kickoff','own_game_excluded','strict_chronology']+snap}


def read_projected(path,columns):
    with Path(path).open(newline='') as handle:header=next(csv.reader(handle))
    check(len(header)==len(set(header)),'DUPLICATE_INPUT_COLUMN')
    # Accepted S0 prediction CSV also contains the frozen raw model features.
    # They remain outside this S0 eligibility/identity projection.
    fs,_=frozen_interface()
    allowed=set(columns)|({'population_class','venue_state'} if 'reasons' in columns else set())
    if 'pred_margin' in columns:allowed|={'population_class'}|{p+f for f in fs for p in ('home_','away_')}
    check(set(columns)<=set(header) and set(header)<=allowed,'INPUT_COLUMN_ALLOWLIST')
    return pd.read_csv(path,usecols=columns,dtype={k:str for k in ('game_id','target_game_id','source_game_id') if k in columns})


def validate_frames(frames,cutoff):
    fs,mp=frozen_interface();S,G,B,C,P,E,A=(frames[k].copy() for k in ('side','target','baseline','context','predicted','excluded','chronology'))
    cutoff=pd.Timestamp(cutoff);check(cutoff.tzinfo is not None,'NAIVE_CUTOFF')
    ids=set(G.game_id)
    for df,kind in ((S,'REFRESH_SNAPSHOT'),(G,'REFRESH_SNAPSHOT'),(B,'S2_K1_TARGET_BASELINE'),(C,'S2_K1_SOURCE_CONTEXT'),(P,'REFRESH_SNAPSHOT'),(E,'REFRESH_SNAPSHOT'),(A,'REFRESH_SNAPSHOT')):
        check((times(df.snapshot_cutoff_utc)==cutoff).all(),'INPUT_CUTOFF_MISMATCH')
        check(set(df.snapshot_type)<= {kind},'INPUT_SNAPSHOT_TYPE')
    check(len(G)>0 and not G.game_id.duplicated().any(),'TARGET_IDENTITY')
    check((G.season==2026).all(),'ONLY_2026_TARGETS_ALLOWED')
    check((G.home_team!=G.away_team).all(),'TARGET_SELF_OPPONENT')
    check((times(G.start_date)>cutoff).all(),'TARGET_NOT_FUTURE_AT_SOURCE_CUTOFF')
    boolean(G.neutral_site)
    check(not S.duplicated(['game_id','side']).any() and not S.duplicated(['game_id','team']).any(),'SIDE_IDENTITY')
    check(set(S.game_id)==ids and set(S.side)=={'home','away'} and len(S)==2*len(G),'SIDE_UNION')
    n=counts(S.qualified_prior_games);eligible=boolean(S.eligible)
    check((~eligible|pd.Series(n>0,index=S.index)).all(),'S0_ELIGIBLE_WITHOUT_HISTORY')
    check(not B.duplicated(['game_id','team']).any(),'BASELINE_IDENTITY')
    check(set(zip(S.game_id,S.team))==set(zip(B.game_id,B.team)),'BASELINE_UNION')
    si=S.set_index(['game_id','team']);bi=B.set_index(['game_id','team']).loc[si.index]
    check(np.array_equal(counts(bi.qualified_prior_games),n),'BASELINE_HISTORY_MISMATCH')
    check((times(bi.target_kickoff).to_numpy()==times(si.target_kickoff).to_numpy()).all(),'BASELINE_KICKOFF_MISMATCH')
    gi=G.set_index('game_id')
    for r in S.itertuples():
        g=gi.loc[r.game_id]
        check(r.team==getattr(g,r.side+'_team') and pd.Timestamp(r.target_kickoff)==pd.Timestamp(g.start_date),'TARGET_ROLE_KICKOFF_MISMATCH')
    for f in fs:
        check(np.array_equal(boolean(B['available__'+f]).to_numpy(),np.isfinite(B['baseline__'+f].to_numpy(float))),'BASELINE_AVAILABILITY_MISMATCH')
    predicted=set(P.game_id);excluded=set(E.game_id)
    check(not P.game_id.duplicated().any() and not E.game_id.duplicated().any(),'S0_DUPLICATE_IDENTITY')
    check(predicted.isdisjoint(excluded) and predicted|excluded==ids,'S0_PREDICTION_EXCLUSION_UNION')
    eligible_ids=set(S.assign(ok=eligible).groupby('game_id').ok.all().loc[lambda x:x].index)
    check(predicted==eligible_ids,'S0_ELIGIBILITY_MISMATCH')
    for df in (P,E):
        check((df.season==2026).all(),'ONLY_2026_TARGETS_ALLOWED')
        for r in df.itertuples():
            g=gi.loc[r.game_id]
            check((r.home_team,r.away_team,pd.Timestamp(r.start_date))==(g.home_team,g.away_team,pd.Timestamp(g.start_date)),'S0_TARGET_BINDING')
    check(np.isfinite(P[['pred_margin','pred_total','pred_win']].to_numpy(float)).all() and P.pred_win.between(0,1).all(),'S0_NONFINITE_PREDICTION')
    check(not C.duplicated(['target_game_id','target_team','source_game_id']).any(),'DUPLICATE_SOURCE_CONTEXT')
    check(set(zip(C.target_game_id,C.target_team))<=set(si.index),'UNKNOWN_CONTEXT_TARGET')
    counts(C.opponent_qualified_prior_games)
    source_at=times(C.source_kickoff);target_at=times(C.target_kickoff)
    check(((source_at<cutoff)&(source_at<target_at)&(C.source_game_id!=C.target_game_id)).all(),'SOURCE_CHRONOLOGY')
    for r in C.itertuples():
        s=si.loc[(r.target_game_id,r.target_team)]
        check(r.target_side==s.side and pd.Timestamp(r.target_kickoff)==pd.Timestamp(s.target_kickoff),'CONTEXT_TARGET_BINDING')
        check(isinstance(r.source_opponent,str) and bool(r.source_opponent.strip()) and r.source_opponent!=r.target_team,'CONTEXT_SELF_OPPONENT')
    actual=C.groupby(['target_game_id','target_team']).size().reindex(si.index,fill_value=0).to_numpy()
    check(np.array_equal(actual,n),'SOURCE_HISTORY_COUNT_MISMATCH')
    mech=boolean(C.mechanical_history_complete);derived=boolean(C.derived_history_complete);zero=C.opponent_qualified_prior_games.eq(0)
    for f,pair in mp.items():
        expected=np.isfinite(C['baseline__'+pair])&(zero|(mech&derived&np.isfinite(C['raw__'+pair])))
        check(np.array_equal(boolean(C['context_valid__'+f]),expected),'CONTEXT_COMPLETION_FLAG_MISMATCH')
    check(not A.duplicated(['game_id','team']).any(),'CHRONOLOGY_IDENTITY')
    positive=si.loc[si.qualified_prior_games>0]
    check(set(zip(A.game_id,A.team))==set(positive.index),'CHRONOLOGY_UNION')
    check(boolean(A.own_game_excluded).all() and boolean(A.strict_chronology).all(),'CHRONOLOGY_FALSE')
    maxes=C.assign(source_clock=source_at).groupby(['target_game_id','target_team']).source_clock.max()
    for r in A.itertuples():
        s=si.loc[(r.game_id,r.team)]
        check(r.side==s.side and r.prior_games==s.qualified_prior_games and pd.Timestamp(r.max_prior_kickoff)==maxes.loc[(r.game_id,r.team)] and pd.Timestamp(r.target_kickoff)==pd.Timestamp(s.target_kickoff),'CHRONOLOGY_BINDING')
    return {'status':'PASS_S2_INPUT_INTERFACE_ONLY_NOT_ACCEPTANCE_OR_FREEZE','targets':len(G),'target_sides':len(S),'source_context_rows':len(C),'s0_eligible_games':len(P),'s0_exclusions':len(E),'chronology_rows':len(A),'cutoff_utc':cutoff.isoformat(),'predictions_generated':False,'outcomes_opened':False}


def accepted_input_binding(paths,cutoff):
    """Admit only the exact separately accepted boundary; later weeks need acceptance."""
    check(pd.Timestamp(cutoff)==pd.Timestamp('2026-10-13T15:13:13.866672+00:00'),'UNQUALIFIED_INPUT_ACCEPTANCE_BOUNDARY')
    expected={
      'side':'e77649e2f3fbd7e50be4c253c05737a652c3fc460087e272635fd27ecaeee356',
      'target':'3fb31ce0413222e0079f9a85330baea50901e50e69fd90f1c9fcbf654bfe21f9',
      'baseline':'4047014eccd739c8caaee7691cbdd4b5cea4951572162b57516bf9f4ca353f5f',
      'context':'7f69d23a3d62766cef7f3c351a2c8b6ea8a562f6fb8ccc6c9f3d75a16606c629',
      'predicted':'c16afc4adcf9daeae571107b4901bd90a7086b23ad03dda829adb4f645ffd27f',
      'excluded':'f772c416b527b6102d4e46817d3e1ffffe966db26ed212e3432ac8a6eb4ac6a0',
      'chronology':'703dc5cbaaa7287587245e85636b20f78e87fb619c01aaaf188153ad0aff1fd3'}
    actual={k:hashlib.sha256(p.read_bytes()).hexdigest() for k,p in paths.items()}
    check(actual==expected,'ACCEPTED_INPUT_BYTES_MISMATCH')
    root=Path(__file__).resolve().parents[1]
    records={
      'evidence/CFB_QA_WEEKLY_REFRESH_ACCEPTANCE_2026-10-16_OCT13.md':'18073bb6953082c9089e210cca1efe867140dcad',
      'evidence/CFB_QA_S2_K1_OCT13_INPUT_ACCEPTANCE_2026-10-23.md':'6db7be770a6e033d140398ab142f9114c677815b'}
    for name,digest in records.items():
        raw=(root/name).read_bytes()
        check(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==digest,'ACCEPTANCE_RECORD_BINDING')
    return actual,records


def load_inputs(targetside,targetledger,baseline,context,cutoff):
    base=Path(targetledger).parent
    paths={'side':Path(targetside),'target':Path(targetledger),'baseline':Path(baseline),'context':Path(context),
           'predicted':base/(PREFIX+'fair_predictions_v1_246.csv'),'excluded':base/(PREFIX+'exclusions_v1_246.csv'),
           'chronology':base/(PREFIX+'chronology_audit_v1_246.csv')}
    hashes,acceptances=accepted_input_binding(paths,cutoff)
    frames={k:read_projected(p,schemas()[k]) for k,p in paths.items()}
    report=validate_frames(frames,cutoff)
    report['input_sha256']=hashes
    report['acceptance_records']=acceptances
    report['raw_source_sha256']={'schedule':'5335a2776ab6425e304bd6c05aeed7ad408ae351f1c8547a1b54e08f34f92176','pbp':'8620a553c03c377638895e97eefc1aa8278a1176ee6615dcc124d8c3e604e0bc'}
    report['raw_source_binding']='INHERITED_EXACT_ACCEPTED_PACKAGE_NOT_REOPENED'
    report['input_gate_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    report['selected_columns']={k:list(df.columns) for k,df in frames.items()}
    return frames,report
