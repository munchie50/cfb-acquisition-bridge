#!/usr/bin/env python3
"""QA-only prospective S2_K1 target-baseline companion. Produces no predictions."""
import sys,json,hashlib
from pathlib import Path
import pandas as pd, numpy as np

targetsidep, mechp, derp, outp = map(Path,sys.argv[1:5])
cutoff=pd.Timestamp(sys.argv[5]); outp.mkdir(parents=True,exist_ok=True)
T=pd.read_csv(targetsidep,dtype={"game_id":str})
M=pd.read_csv(mechp,dtype={"game_id":str}); D=pd.read_csv(derp,dtype={"game_id":str})
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

reqT={"game_id","team","target_kickoff","qualified_prior_games","snapshot_type","snapshot_cutoff_utc","rest_days"}
assert reqT.issubset(T.columns) and not T.duplicated(["game_id","team"]).any()
assert set(T.snapshot_type)=={"REFRESH_SNAPSHOT"} and set(T.snapshot_cutoff_utc)=={cutoff.isoformat()}
assert (T.target_kickoff>cutoff).all()
assert set(M.season.astype(int))=={2026} and set(D.season.astype(int))=={2026}
assert not M.duplicated(["season","game_id","team"]).any() and not D.duplicated(["season","game_id","team"]).any()
assert (M.start_date<cutoff).all() and (D.start_date<cutoff).all()

def boolflag(s):
    return s.map(lambda x:str(x).strip().lower() in {"true","1"})
mc=boolflag(M.mechanical_primitive_complete); dc=boolflag(D.derived_primitive_complete)
def baseline(f):
    # Frozen historical semantics normalize the target/source kickoff to UTC date midnight.
    t=cutoff.normalize()
    if f=="rest_days":
        # target-side pregame rest_days is itself computed from strict-prior history;
        # population baseline is the mean of valid pregame rest intervals whose state exists before cutoff day.
        z=T[(T.target_kickoff.dt.normalize()==t)&T.rest_days.notna()]
        # T is future target state, so using its rest_days would make the pool target-population dependent.
        # Fail closed here; rest-days baseline requires an accepted pregame feature-history surface.
        return np.nan
    typ,num,den=COMP[f]; src=M if typ=="M" else D; complete=mc if typ=="M" else dc
    z=src[(src.start_date<t)&complete]
    if z.empty:return np.nan
    n=float(z[num].sum()); d=float(len(z)) if den=="GAME" else float(z[den].sum())
    return np.nan if (not np.isfinite(n) or not np.isfinite(d) or d<=0) else n/d

b={f:baseline(f) for f in FEATURES}
rows=[]
for r in T.itertuples():
    rec={"game_id":r.game_id,"team":r.team,"target_kickoff":r.target_kickoff.isoformat(),"qualified_prior_games":int(r.qualified_prior_games),"snapshot_type":"S2_K1_TARGET_BASELINE","snapshot_cutoff_utc":cutoff.isoformat()}
    for f in FEATURES:
        rec["baseline__"+f]=b[f]; rec["available__"+f]=bool(np.isfinite(b[f]))
    rows.append(rec)
O=pd.DataFrame(rows)
# The executable is deliberately blocked until rest_days gets a legitimate strict-prior feature-history source.
if not O["available__rest_days"].all():
    raise SystemExit("TARGET_BASELINE_BLOCKED_REST_DAYS_HISTORY_SURFACE_REQUIRED")
O.to_csv(outp/"target_baselines.csv",index=False)
manifest={"status":"EXECUTED_NOT_ACCEPTED","s2_predictions_produced":False,"target_outcomes_joined":False,"market_joined":False,"cutoff_utc":cutoff.isoformat(),"rows":len(O),"features":FEATURES,"hashes":{"target_baselines.csv":hashlib.sha256((outp/"target_baselines.csv").read_bytes()).hexdigest()}}
(outp/"manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n")
print(json.dumps(manifest,indent=2))
