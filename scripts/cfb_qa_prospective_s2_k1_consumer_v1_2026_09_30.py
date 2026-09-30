#!/usr/bin/env python3
"""Prospective QA-only S2_K1 consumer. Requires accepted same-cutoff inputs; no outcomes."""
import sys,json,hashlib
from pathlib import Path
import pandas as pd, numpy as np

targetsidep, targetledgerp, basep, ctxp, fitdir, outdir = map(Path,sys.argv[1:7])
cutoff=pd.Timestamp(sys.argv[7]); outdir.mkdir(parents=True,exist_ok=True)
assert cutoff.tz is not None
S=pd.read_csv(targetsidep,dtype={"game_id":str})
G=pd.read_csv(targetledgerp,dtype={"game_id":str})
B=pd.read_csv(basep,dtype={"game_id":str})
C=pd.read_csv(ctxp,dtype={"target_game_id":str,"source_game_id":str})

FEATURES=["points_for_per_game","points_against_per_game","offensive_scrimmage_plays_per_game","defensive_scrimmage_plays_per_game","offensive_yards_per_play","defensive_yards_per_play","rush_play_rate","pass_play_rate","rush_yards_per_play","pass_yards_per_play","interception_rate","rest_days","offensive_explosive_play_rate","defensive_explosive_play_rate","offensive_success_rate","defensive_success_rate_allowed","average_starting_yards_to_goal"]
MAP={"points_for_per_game":"points_against_per_game","points_against_per_game":"points_for_per_game","offensive_scrimmage_plays_per_game":"defensive_scrimmage_plays_per_game","defensive_scrimmage_plays_per_game":"offensive_scrimmage_plays_per_game","offensive_yards_per_play":"defensive_yards_per_play","defensive_yards_per_play":"offensive_yards_per_play","offensive_explosive_play_rate":"defensive_explosive_play_rate","defensive_explosive_play_rate":"offensive_explosive_play_rate","offensive_success_rate":"defensive_success_rate_allowed","defensive_success_rate_allowed":"offensive_success_rate"}
MAPPED=set(MAP); S1ONLY=set(FEATURES)-MAPPED
assert len(MAPPED)==10 and len(S1ONLY)==7

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
            if not (np.isfinite(no).all() and np.isfinite(rawo).all() and np.isfinite(bo).all()):
                badreason="CONTEXT_NONFINITE:"+f;break
            resid=(no/(no+1.0)*rawo+1/(no+1.0)*bo)-bo
            # Paired opponent residual is added once under the frozen offense<->defense mapping.
            s2=s1+float(resid.mean())
        else:
            s2=s1
        rec[f]=s2
    if badreason: exclusions.append({"game_id":r.game_id,"team":r.team,"reason":badreason})
    else: rows.append(rec)

X=pd.DataFrame(rows); E=pd.DataFrame(exclusions)
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
GE=pd.DataFrame(game_exclusions)
side_excluded=set(E.game_id.astype(str)) if len(E) else set()
predicted=set(P.game_id.astype(str)) if len(P) else set()
game_failed=set(GE.game_id.astype(str)) if len(GE) else set()
assert predicted.isdisjoint(side_excluded|game_failed)
assert predicted|side_excluded|game_failed==set(G.game_id.astype(str))

P.to_csv(outdir/"s2_k1_predictions.csv",index=False)
E.to_csv(outdir/"s2_k1_side_exclusions.csv",index=False)
GE.to_csv(outdir/"s2_k1_game_exclusions.csv",index=False)
manifest={
 "status":"EXECUTED_NOT_ACCEPTED","candidate_id":"S2_K1","k":1,"snapshot_type":"REFRESH_SNAPSHOT",
 "snapshot_cutoff_utc":cutoff.isoformat(),"prediction_rows":len(P),"side_exclusion_rows":len(E),"game_exclusion_rows":len(GE),
 "target_outcomes_opened":False,"market_joined":False,"wager_or_execution_joined":False,
 "protected_2025_test_opened":False,"fit_or_optimization_performed":False,
 "coefficient_sha256":"bf15ce41180bfb4e250d311df279e98c13b65432756ae07f7a30264cbae0e221",
 "scaling_sha256":"68fb5193ccb8828ac8d34dfe820101181c2bde078a04a6d5afd4c08bcf0cab45",
 "hashes":{}
}
for p in sorted(outdir.iterdir()):
    if p.is_file(): manifest["hashes"][p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
(outdir/"manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n")
print(json.dumps(manifest,indent=2))
