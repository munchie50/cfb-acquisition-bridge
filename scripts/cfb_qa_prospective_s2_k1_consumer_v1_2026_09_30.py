#!/usr/bin/env python3
"""Prospective QA-only S2_K1 consumer. Requires accepted same-cutoff inputs; no outcomes."""
import sys,json,hashlib
from pathlib import Path
import pandas as pd, numpy as np

s0p, basep, ctxp, fitdir, outdir = map(Path,sys.argv[1:6])
cutoff=pd.Timestamp(sys.argv[6]); outdir.mkdir(parents=True,exist_ok=True)
assert cutoff.tz is not None
S=pd.read_csv(s0p,dtype={"game_id":str})
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

