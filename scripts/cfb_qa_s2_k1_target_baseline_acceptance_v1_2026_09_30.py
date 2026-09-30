#!/usr/bin/env python3
"""Independent acceptance audit for a prospective S2_K1 target-baseline candidate."""
import sys,json,hashlib
from pathlib import Path
import pandas as pd, numpy as np

targetp, mechp, derp, canddir, outdir = map(Path,sys.argv[1:6])
cutoff=pd.Timestamp(sys.argv[6]); outdir.mkdir(parents=True,exist_ok=True)
assert cutoff.tz is not None

candp=canddir/"target_baselines.csv"; manp=canddir/"manifest.json"
assert candp.is_file() and manp.is_file()
T=pd.read_csv(targetp,dtype={"game_id":str})
M=pd.read_csv(mechp,dtype={"game_id":str})
D=pd.read_csv(derp,dtype={"game_id":str})
C=pd.read_csv(candp,dtype={"game_id":str})
CM=json.loads(manp.read_text())
for z in (T,M,D):
    for c in ("target_kickoff","start_date"):
        if c in z: z[c]=pd.to_datetime(z[c],utc=True)

FEATURES=["points_for_per_game","points_against_per_game","offensive_scrimmage_plays_per_game","defensive_scrimmage_plays_per_game","offensive_yards_per_play","defensive_yards_per_play","rush_play_rate","pass_play_rate","rush_yards_per_play","pass_yards_per_play","interception_rate","rest_days","offensive_explosive_play_rate","defensive_explosive_play_rate","offensive_success_rate","defensive_success_rate_allowed","average_starting_yards_to_goal"]
COMP={
"points_for_per_game":("M","game_points_for","GAME"),"points_against_per_game":("M","game_points_against","GAME"),
"offensive_scrimmage_plays_per_game":("M","off_plays","GAME"),"defensive_scrimmage_plays_per_game":("M","def_plays","GAME"),
"offensive_yards_per_play":("M","off_yards","off_plays"),"defensive_yards_per_play":("M","def_yards","def_plays"),
"rush_play_rate":("M","rush_plays","off_plays"),"pass_play_rate":("M","pass_plays","off_plays"),
"rush_yards_per_play":("M","rush_yards","rush_plays"),"pass_yards_per_play":("M","pass_yards","pass_plays"),
"interception_rate":("M","interceptions","pass_attempts"),"offensive_explosive_play_rate":("D","off_exp","off_scr"),
"defensive_explosive_play_rate":("D","def_exp","def_scr"),"offensive_success_rate":("D","off_succ","off_succ_q"),
"defensive_success_rate_allowed":("D","def_succ","def_succ_q"),"average_starting_yards_to_goal":("D","start_ytg_sum","start_drive_n")}

# Candidate metadata is checked, never used to compute expected values.
assert CM["status"]=="EXECUTED_NOT_ACCEPTED"
assert CM["s2_predictions_produced"] is False and CM["target_outcomes_joined"] is False and CM["market_joined"] is False
assert pd.Timestamp(CM["cutoff_utc"])==cutoff
assert CM["features"]==FEATURES
assert hashlib.sha256(candp.read_bytes()).hexdigest()==CM["hashes"]["target_baselines.csv"]

reqT={"game_id","team","target_kickoff","qualified_prior_games","snapshot_type","snapshot_cutoff_utc"}
assert reqT.issubset(T.columns) and not T.duplicated(["game_id","team"]).any()
assert set(T.snapshot_type)=={"REFRESH_SNAPSHOT"}
assert set(pd.to_datetime(T.snapshot_cutoff_utc,utc=True))=={cutoff}
assert (T.target_kickoff>cutoff).all()
assert set(M.season.astype(int))=={2026} and set(D.season.astype(int))=={2026}
assert not M.duplicated(["season","game_id","team"]).any()
assert not D.duplicated(["season","game_id","team"]).any()

# Frozen baseline population is UTC-calendar-day strict-prior, not merely timestamp-prior.
day=cutoff.normalize()
assert (M.start_date<cutoff).all() and (D.start_date<cutoff).all()
mc=M.mechanical_primitive_complete.map(lambda x:str(x).strip().lower() in {"true","1"})
dc=D.derived_primitive_complete.map(lambda x:str(x).strip().lower() in {"true","1"})

def expected_baseline(f):
    if f=="rest_days":
        ident=M[["season","game_id","team","start_date"]].copy()
        assert not ident.duplicated(["season","team","start_date"],keep=False).any()
        ident=ident.sort_values(["season","team","start_date","game_id"])
        ident["rest_days"]=ident.groupby(["season","team"]).start_date.diff().dt.total_seconds()/86400
        z=ident[(ident.start_date<day)&ident.rest_days.notna()]
        if z.empty:return np.nan
        v=float(z.rest_days.mean())
        return v if np.isfinite(v) else np.nan
    typ,num,den=COMP[f]
    src=M if typ=="M" else D; complete=mc if typ=="M" else dc
    z=src[(src.start_date<day)&complete]
    if z.empty:return np.nan
    n=float(z[num].sum()); d=float(len(z)) if den=="GAME" else float(z[den].sum())
    return np.nan if (not np.isfinite(n) or not np.isfinite(d) or d<=0) else n/d

E={f:expected_baseline(f) for f in FEATURES}
missing=[f for f,v in E.items() if not np.isfinite(v)]
assert not missing, f"independent baseline unavailable: {missing}"

idcols=["game_id","team"]
assert not C.duplicated(idcols).any()
assert len(C)==len(T)
assert set(map(tuple,C[idcols].astype(str).to_numpy()))==set(map(tuple,T[idcols].astype(str).to_numpy()))
assert set(pd.to_datetime(C.snapshot_cutoff_utc,utc=True))=={cutoff}
assert set(C.snapshot_type)=={"S2_K1_TARGET_BASELINE"}
for f in FEATURES:
    bc="baseline__"+f; ac="available__"+f
    assert bc in C and ac in C
    assert C[ac].map(lambda x:str(x).strip().lower() in {"true","1"}).all()
    vals=C[bc].to_numpy(float)
    assert np.isfinite(vals).all()
    assert np.allclose(vals,E[f],rtol=0,atol=1e-12), f"baseline mismatch: {f}"

# The acceptance path consumes no target outcome, market, wager/execution or fit/optimization surface.
for df,label in ((T,"target"),(C,"candidate")):
    bad=("winner","spread","moneyline","over_under","odds","wager","bet_","execution","actual_","postgame")
    forbidden=[c for c in df.columns if any(x in c.lower() for x in bad)]
    assert not forbidden, f"{label} forbidden fields: {forbidden}"

report={
 "status":"PASS_S2_K1_TARGET_BASELINE_ACCEPTANCE",
 "cutoff_utc":cutoff.isoformat(),
 "rows":len(C),
 "features":len(FEATURES),
 "candidate_hash_reproduced":True,
 "identities_reconciled":True,
 "baselines_independently_recomputed":True,
 "utc_day_strict_prior":True,
 "rest_days_same_team_same_season":True,
 "target_rows_used_as_population_baseline":False,
 "target_outcomes_opened":False,
 "market_joined":False,
 "wager_or_execution_joined":False,
 "protected_2025_test_opened":False,
 "fit_or_optimization_performed":False,
 "candidate_target_baselines_sha256":hashlib.sha256(candp.read_bytes()).hexdigest(),
}
(outdir/"target_baseline_acceptance.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
print(json.dumps(report,indent=2,sort_keys=True))
