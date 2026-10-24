#!/usr/bin/env python3
"""Prospective QA-only S2_K1 consumer. Requires accepted same-cutoff inputs; no outcomes."""
import sys,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
import pandas as pd, numpy as np

def opponent_residuals(no, rawo, bo):
    """Frozen k=1 residual: zero-history uses its finite baseline and contributes 0."""
    no, rawo, bo = (np.asarray(v, dtype=float) for v in (no, rawo, bo))
    if (no.ndim != 1 or rawo.shape != no.shape or bo.shape != no.shape or
            not np.isfinite(no).all() or (no < 0).any() or (no % 1 != 0).any() or
            not np.isfinite(bo).all()):
        raise ValueError("CONTEXT_NONFINITE_OR_INVALID_HISTORY")
    positive = no > 0
    if not np.isfinite(rawo[positive]).all():
        raise ValueError("CONTEXT_NONFINITE_POSITIVE_HISTORY")
    resid = np.zeros(len(no), dtype=float)
    resid[positive] = (no[positive] / (no[positive] + 1.0) * rawo[positive] +
                       1 / (no[positive] + 1.0) * bo[positive]) - bo[positive]
    return resid

FEATURES=["points_for_per_game","points_against_per_game","offensive_scrimmage_plays_per_game","defensive_scrimmage_plays_per_game","offensive_yards_per_play","defensive_yards_per_play","rush_play_rate","pass_play_rate","rush_yards_per_play","pass_yards_per_play","interception_rate","rest_days","offensive_explosive_play_rate","defensive_explosive_play_rate","offensive_success_rate","defensive_success_rate_allowed","average_starting_yards_to_goal"]
MAP={"points_for_per_game":"points_against_per_game","points_against_per_game":"points_for_per_game","offensive_scrimmage_plays_per_game":"defensive_scrimmage_plays_per_game","defensive_scrimmage_plays_per_game":"offensive_scrimmage_plays_per_game","offensive_yards_per_play":"defensive_yards_per_play","defensive_yards_per_play":"offensive_yards_per_play","offensive_explosive_play_rate":"defensive_explosive_play_rate","defensive_explosive_play_rate":"offensive_explosive_play_rate","offensive_success_rate":"defensive_success_rate_allowed","defensive_success_rate_allowed":"offensive_success_rate"}
MAPPED=set(MAP); S1ONLY=set(FEATURES)-MAPPED
assert len(MAPPED)==10 and len(S1ONLY)==7

# Only explicit allowlisted projections reach the transform. Same-cutoff input
# acceptance remains a separately proved prerequisite; this is not acceptance.
from cfb_qa_s2_k1_input_gate import load_inputs
targetsidep, targetledgerp, basep, ctxp, fitdir, outdir = map(Path,sys.argv[1:7])
cutoff=pd.Timestamp(sys.argv[7])
if len(sys.argv) not in (9,11) or sys.argv[8] not in ('--readiness-only','--execute-prospective') or (len(sys.argv)==11 and sys.argv[9]!='--projection-acceptance-ref'):
    raise SystemExit('EXPLICIT_MODE_REQUIRED_USE_READINESS_ONLY_OR_EXECUTE_PROSPECTIVE')
assert cutoff.tz is not None
frames,input_audit=load_inputs(targetsidep,targetledgerp,basep,ctxp,cutoff)
S,G,B,C=(frames[k] for k in ('side','target','baseline','context'))
projection_context=None
if len(sys.argv)==11:
    from cfb_qa_s2_k1_projection import apply_accepted_projection
    acceptance_ref=json.loads(Path(sys.argv[10]).read_text())
    frames,projection_context=apply_accepted_projection(targetledgerp.parent.parent,acceptance_ref,datetime.now(timezone.utc).isoformat())
    S,G,B,C=(frames[k] for k in ('side','target','baseline','context'))
s0_eligible=set(frames['predicted'].game_id)
# Readiness uses the true observed clock; original source cutoff is never retimed.
freeze_recorded_at_utc=datetime.now(timezone.utc).isoformat()
future=(pd.to_datetime(G.game_id.map(projection_context['qualified_kickoffs_utc']),utc=True) if projection_context else pd.to_datetime(G.start_date,utc=True))>pd.Timestamp(freeze_recorded_at_utc)
if '--readiness-only' in sys.argv[8:]:
    print(json.dumps({**input_audit,'observed_at_utc':freeze_recorded_at_utc,
        'future_at_saved_kickoff':int(future.sum()),'elapsed_at_saved_kickoff':int((~future).sum()),
        'kickoff_truth':'ACCEPTED_SOURCE_ONLY_NOT_CURRENT_REQUALIFICATION',
        'freeze_ready':False,'active_targets':len(G),'active_context_rows':len(C),'projection':projection_context,'next_proof':'independent future-only projection/freeze qualification; synthetic numerical equivalence is separately tested'},indent=2))
    raise SystemExit(0)
if '--execute-prospective' not in sys.argv[8:]:
    raise SystemExit('EXPLICIT_PROSPECTIVE_EXECUTION_REQUIRED_USE_READINESS_ONLY')
if not future.all():
    raise SystemExit('ELAPSED_TARGETS_PROHIBITED_REQUIRE_QUALIFIED_FUTURE_ONLY_BOUNDARY')
outdir.mkdir(parents=True,exist_ok=False)
# This consumer accepts only already-accepted boundary files supplied by the caller.
# It does not open raw schedule/PBP, outcomes, market, decision or execution surfaces.
for df,label,idcols in ((S,"s0",["game_id","team"]),(B,"baseline",["game_id","team"])):
    assert not df.duplicated(idcols).any(), f"{label} duplicate identity"
    assert set(pd.to_datetime(df.snapshot_cutoff_utc,utc=True))=={cutoff}
assert set(S.snapshot_type)=={"REFRESH_SNAPSHOT"}
assert set(B.snapshot_type)=={"S2_K1_TARGET_BASELINE"}
assert set(pd.to_datetime(C.snapshot_cutoff_utc,utc=True))=={cutoff}
assert set(C.snapshot_type)=={"S2_K1_SOURCE_CONTEXT"}
assert set(map(tuple,S[["game_id","team"]].astype(str).to_numpy()))==set(map(tuple,B[["game_id","team"]].astype(str).to_numpy()))

bad=("winner","spread","moneyline","over_under","odds","wager","bet_","execution","actual_","postgame")
for df,label in ((S,"s0_side"),(G,"s0_target"),(B,"baseline"),(C,"context")):
    forbidden=[c for c in df.columns if any(x in c.lower() for x in bad)]
    assert not forbidden, f"{label} forbidden fields: {forbidden}"

J=S.merge(B,on=["game_id","team"],suffixes=("","__b"),validate="one_to_one")
assert (pd.to_datetime(J.target_kickoff,utc=True)>cutoff).all()
rows=[]; exclusions=[]
for r in J.itertuples(index=False):
    n=int(r.qualified_prior_games)
    if r.game_id not in s0_eligible:
        exclusions.append({"game_id":r.game_id,"team":r.team,"reason":"S0_INELIGIBLE"});continue
    if n<=0:
        exclusions.append({"game_id":r.game_id,"team":r.team,"reason":"NO_QUALIFIED_PRIOR_GAMES"});continue
    rec={"game_id":r.game_id,"team":r.team,"target_kickoff":r.target_kickoff,"qualified_prior_games":n}
    badreason=None
    for f in FEATURES:
        raw=getattr(r,f); b=getattr(r,"baseline__"+f)
        if not np.isfinite(raw) or not np.isfinite(b):
            badreason="S1_INPUT_UNAVAILABLE:"+f;break
        s1=n/(n+1.0)*float(raw)+1/(n+1.0)*float(b)
        if f in MAPPED:
            z=C[(C.target_game_id==str(r.game_id))&(C.target_team==r.team)]
            vc="context_valid__"+f; pair=MAP[f]
            if vc not in z or ("raw__"+pair) not in z or ("baseline__"+pair) not in z:
                badreason="CONTEXT_SCHEMA_UNAVAILABLE:"+f;break
            z=z[z[vc].map(lambda x:str(x).strip().lower() in {"true","1"})]
            if z.empty:
                badreason="CONTEXT_UNAVAILABLE:"+f;break
            # Frozen k=1 opponent S1 residual: n_o/(n_o+1)*raw + 1/(n_o+1)*B - B
            no=z.opponent_qualified_prior_games.to_numpy(float)
            rawo=z["raw__"+pair].to_numpy(float); bo=z["baseline__"+pair].to_numpy(float)
            try:
                resid=opponent_residuals(no, rawo, bo)
            except ValueError:
                badreason="CONTEXT_NONFINITE:"+f;break
            # Frozen historical generator subtracts the paired residual exactly once.
            s2=s1-float(resid.mean())
        else:
            s2=s1
        rec[f]=s2
    if badreason: exclusions.append({"game_id":r.game_id,"team":r.team,"reason":badreason})
    else: rows.append(rec)

X=pd.DataFrame(rows); E=pd.DataFrame(exclusions,columns=["game_id","team","reason"])
# Both target sides must survive before game-level prediction.
validgames=set()
if len(X):
    counts=X.groupby("game_id").team.nunique()
    validgames=set(counts[counts==2].index.astype(str))
X=X[X.game_id.astype(str).isin(validgames)].copy() if len(X) else X

coefp=fitdir/"selected_coefficients.csv"; scalep=fitdir/"train_scaling.csv"
assert hashlib.sha256(coefp.read_bytes()).hexdigest()=="bf15ce41180bfb4e250d311df279e98c13b65432756ae07f7a30264cbae0e221"
assert hashlib.sha256(scalep.read_bytes()).hexdigest()=="68fb5193ccb8828ac8d34dfe820101181c2bde078a04a6d5afd4c08bcf0cab45"
coef=pd.read_csv(coefp); scale=pd.read_csv(scalep)
assert len(FEATURES)==17 and len(scale)==34
assert set(coef.groupby("target")["lambda"].first().to_dict().items())=={("margin",0.1),("total",0.1),("win",0.01)}

# Compose the accepted v1.246 boundary instead of extending either artifact.
assert "side" in S.columns and set(S.side).issubset({"home","away"})
assert not S.duplicated(["game_id","side"]).any()
assert set(S.game_id.astype(str))==set(G.game_id.astype(str))
role=S[["game_id","side","team"]].merge(G[["game_id","home_team","away_team","neutral_site"]],on="game_id",validate="many_to_one")
assert ((role.side=="home")==(role.team==role.home_team)).all()
assert ((role.side=="away")==(role.team==role.away_team)).all()
venue=G[["game_id","home_team","away_team","neutral_site"]].copy()
def neutral_state(x):
    if isinstance(x,(bool,np.bool_)): return bool(x)
    z=str(x).strip().lower()
    if z in {"true","t","1","yes","y"}: return True
    if z in {"false","f","0","no","n"}: return False
    raise SystemExit("unrecognized neutral_site value")
venue["venue_state"]=np.where(venue.neutral_site.map(neutral_state),"NEUTRAL","HOME")


assert not G.duplicated(["game_id"]).any()
assert set(pd.to_datetime(G.snapshot_cutoff_utc,utc=True))=={cutoff}
assert set(G.snapshot_type)=={"REFRESH_SNAPSHOT"}
assert {"game_id","home_team","away_team","neutral_site","start_date"}.issubset(G.columns)
assert set(S.game_id.astype(str))==set(G.game_id.astype(str))
assert (S.groupby("game_id").side.nunique()==2).all()
assert (role.loc[role.side=="home","team"].to_numpy()==role.loc[role.side=="home","home_team"].to_numpy()).all()
assert (role.loc[role.side=="away","team"].to_numpy()==role.loc[role.side=="away","away_team"].to_numpy()).all()

# Mirror the accepted v1.246 prediction assembly exactly.
pred=[p+f for f in FEATURES for p in ("home_","away_")]
assert len(pred)==34 and len(scale)==34 and set(scale.feature)==set(pred)
scalei=scale.set_index("feature")
coef_expected={"margin":0.1,"total":0.1,"win":0.01}
predrows=[]; game_exclusions=[]
for gid in sorted(validgames):
    z=X[X.game_id.astype(str)==gid]
    if len(z)!=2 or set(z.team)!=set(role.loc[role.game_id.astype(str)==gid,["home_team","away_team"]].iloc[0]):
        game_exclusions.append({"game_id":gid,"reason":"ROLE_OR_SIDE_IDENTITY"}); continue
    gr=G[G.game_id.astype(str)==gid].iloc[0]
    home=z[z.team==gr.home_team].iloc[0]; away=z[z.team==gr.away_team].iloc[0]
    vals={}
    for f in FEATURES:
        vals["home_"+f]=float(home[f]); vals["away_"+f]=float(away[f])
    arr=np.array([vals[f] for f in pred],dtype=float)
    zz=(arr-scalei.loc[pred,"mean"].to_numpy(float))/scalei.loc[pred,"sd"].to_numpy(float)
    vstate=venue.loc[venue.game_id.astype(str)==gid,"venue_state"].iloc[0]
    zz=np.r_[zz,1.0 if vstate=="NEUTRAL" else 0.0]
    names=["intercept"]+pred+["venue_neutral"]
    q={}
    for kind,lam in coef_expected.items():
        c=coef[(coef.target==kind)&(coef["lambda"]==lam)].set_index("term")
        assert set(c.index)==set(names), f"coefficient identity {kind}"
        w=c.loc[names,"coefficient"].to_numpy(float)
        value=float(np.r_[1.0,zz]@w)
        if kind=="win": value=float(1/(1+np.exp(-np.clip(value,-40,40))))
        q[kind]=value
    depth=min(int(home.qualified_prior_games),int(away.qualified_prior_games))
    depth_slice="DEPTH_1_2" if depth<=2 else ("DEPTH_3_4" if depth<=4 else "DEPTH_5_PLUS")
    predrows.append({"season":int(gr.season) if "season" in G.columns else 2026,"game_id":gid,"start_date":gr.start_date,
        "home_team":gr.home_team,"away_team":gr.away_team,"venue_state":vstate,
        "snapshot_type":"REFRESH_SNAPSHOT","snapshot_cutoff_utc":cutoff.isoformat(),
        "candidate_id":"S2_K1","k":1,"home_qualified_prior_games":int(home.qualified_prior_games),
        "away_qualified_prior_games":int(away.qualified_prior_games),"history_depth_slice":depth_slice,
        "pred_margin":q["margin"],"pred_total":q["total"],"pred_win":q["win"]})

P=pd.DataFrame(predrows)
if len(P):
    assert not P.game_id.duplicated().any()
    assert np.isfinite(P[["pred_margin","pred_total","pred_win"]].to_numpy(float)).all()
    assert P.pred_win.between(0,1).all()
GE=pd.DataFrame(game_exclusions,columns=["game_id","reason"])
side_excluded=set(E.game_id.astype(str)) if len(E) else set()
predicted=set(P.game_id.astype(str)) if len(P) else set()
game_failed=set(GE.game_id.astype(str)) if len(GE) else set()
assert predicted.isdisjoint(side_excluded|game_failed)
assert predicted|side_excluded|game_failed==set(G.game_id.astype(str))

config={"candidate_id":"S2_K1","k":1,"features":FEATURES,"mapping":MAP,
        "context_sign":"SUBTRACT_MEAN_PAIRED_RESIDUAL","lambdas":coef_expected,
        "coefficient_sha256":"bf15ce41180bfb4e250d311df279e98c13b65432756ae07f7a30264cbae0e221",
        "scaling_sha256":"68fb5193ccb8828ac8d34dfe820101181c2bde078a04a6d5afd4c08bcf0cab45"}
config_sha256=hashlib.sha256(json.dumps(config,sort_keys=True,separators=(',',':')).encode()).hexdigest()
if len(P):
    original=frames['predicted'].set_index('game_id')
    for name in ('pred_margin','pred_total','pred_win'):
        P['s0_'+name]=P.game_id.map(original[name])
    for kind,digest in input_audit['input_sha256'].items():P[kind+'_input_sha256']=digest
    P['freeze_recorded_at_utc']=freeze_recorded_at_utc
    P['frozen_config_sha256']=config_sha256
    P['consumer_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    consumer_bytes=Path(__file__).read_bytes()
    P['consumer_git_blob']=hashlib.sha1(b'blob '+str(len(consumer_bytes)).encode()+b'\0'+consumer_bytes).hexdigest()
    P['input_gate_sha256']=input_audit['input_gate_sha256']
    for kind,digest in input_audit['raw_source_sha256'].items():P['raw_'+kind+'_sha256']=digest
if len(P) and projection_context:
    P['qualified_kickoff_utc']=P.game_id.map(projection_context['qualified_kickoffs_utc'])
    P['projection_sha256']=projection_context['projection_sha256']
    for kind,digest in projection_context['projected_input_sha256'].items():P[kind+'_projected_sha256']=digest
prediction_completed_at_utc=datetime.now(timezone.utc).isoformat()
if projection_context:
    assert all(pd.Timestamp(k)>pd.Timestamp(prediction_completed_at_utc) for k in projection_context['qualified_kickoffs_utc'].values())
P.to_csv(outdir/"s2_k1_predictions.csv",index=False)
E.to_csv(outdir/"s2_k1_side_exclusions.csv",index=False)
GE.to_csv(outdir/"s2_k1_game_exclusions.csv",index=False)
manifest={
 "status":"EXECUTED_NOT_ACCEPTED","candidate_id":"S2_K1","k":1,"snapshot_type":"REFRESH_SNAPSHOT",
 "snapshot_cutoff_utc":cutoff.isoformat(),"freeze_recorded_at_utc":freeze_recorded_at_utc,"prediction_rows":len(P),"side_exclusion_rows":len(E),"game_exclusion_rows":len(GE),
 "target_outcomes_opened":False,"market_joined":False,"wager_or_execution_joined":False,
 "protected_2025_test_opened":False,"fit_or_optimization_performed":False,
 "coefficient_sha256":"bf15ce41180bfb4e250d311df279e98c13b65432756ae07f7a30264cbae0e221",
 "scaling_sha256":"68fb5193ccb8828ac8d34dfe820101181c2bde078a04a6d5afd4c08bcf0cab45",
 "input_sha256":input_audit["input_sha256"],
 "projection":projection_context,"prediction_completed_at_utc":prediction_completed_at_utc,
 "input_acceptance_records":input_audit["acceptance_records"],
 "raw_source_sha256":input_audit["raw_source_sha256"],
 "input_gate_sha256":input_audit["input_gate_sha256"],
 "frozen_config":config,"frozen_config_sha256":config_sha256,
 "consumer_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 "consumer_git_blob":hashlib.sha1(b"blob "+str(len(Path(__file__).read_bytes())).encode()+b"\0"+Path(__file__).read_bytes()).hexdigest(),
 "hashes":{}
}
for p in sorted(outdir.iterdir()):
    if p.is_file(): manifest["hashes"][p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
(outdir/"manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n")
print(json.dumps(manifest,indent=2))
