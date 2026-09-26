#!/usr/bin/env python3
# v1.196: outcome-only scoring of the already-frozen v1.188 2025 predictions.
import sys,json,hashlib
from pathlib import Path
import pandas as pd, numpy as np

art,raw,out=map(Path,sys.argv[1:4]); out.mkdir(parents=True,exist_ok=True)
P=pd.read_csv(art/"challenger_b_2025_fair_predictions_v1_188.csv",dtype={"game_id":str})
E=pd.read_csv(art/"challenger_b_2025_exclusions_v1_188.csv",dtype={"game_id":str})
T=pd.read_csv(art/"challenger_b_2025_target_ledger_v1_188.csv",dtype={"game_id":str})
if len(P)!=793 or len(E)!=141 or len(T)!=934: raise SystemExit("frozen artifact accounting")
if set(P.game_id)&set(E.game_id) or set(P.game_id)|set(E.game_id)!=set(T.game_id): raise SystemExit("frozen disposition identity")
R=pd.read_parquet(raw); R["game_id"]=R.game_id.astype(str)
# Exact target-key restriction before any outcome projection.
R=R[R.game_id.isin(set(T.game_id))].copy()
if R.game_id.duplicated().any() or set(R.game_id)!=set(T.game_id): raise SystemExit("outcome source target-key identity")
need=["game_id","home_points","away_points"]
if not set(need).issubset(R.columns): raise SystemExit("outcome fields missing")
O=R[need].copy()
if O[["home_points","away_points"]].isna().any().any(): raise SystemExit("target outcomes incomplete")
O["actual_margin"]=O.home_points.astype(float)-O.away_points.astype(float)
O["actual_total"]=O.home_points.astype(float)+O.away_points.astype(float)
O["actual_home_win"]=(O.actual_margin>0).astype(float)
# Ties cannot be silently coerced into a binary win target.
if (O.actual_margin==0).any(): raise SystemExit("tie outcome requires explicit handling")
Q=P.merge(O[["game_id","actual_margin","actual_total","actual_home_win"]],on="game_id",how="left",validate="one_to_one")
if Q[["actual_margin","actual_total","actual_home_win"]].isna().any().any(): raise SystemExit("prediction outcome join incomplete")

def gauss(y,p):
    e=p-y
    return {"n":int(len(y)),"mae":float(np.mean(np.abs(e))),"rmse":float(np.sqrt(np.mean(e*e))),"bias":float(np.mean(e))}
def win(y,p):
    q=np.clip(p,1e-15,1-1e-15)
    return {"n":int(len(y)),"brier":float(np.mean((p-y)**2)),"logloss":float(-np.mean(y*np.log(q)+(1-y)*np.log(1-q)))}

metrics={
 "margin":gauss(Q.actual_margin.to_numpy(float),Q.pred_margin.to_numpy(float)),
 "total":gauss(Q.actual_total.to_numpy(float),Q.pred_total.to_numpy(float)),
 "win":win(Q.actual_home_win.to_numpy(float),Q.pred_win.to_numpy(float))
}
# Predetermined descriptive slices only; no optimization or model changes.
slices=[]
for dim in ["venue_state","population_class","competition_class"]:
    if dim not in Q.columns:
        Q=Q.merge(T[["game_id",dim]],on="game_id",how="left",validate="one_to_one")
    for key,g in Q.groupby(dim,dropna=False):
        slices += [
          {"target":"margin","dimension":dim,"slice":str(key),**gauss(g.actual_margin.to_numpy(float),g.pred_margin.to_numpy(float))},
          {"target":"total","dimension":dim,"slice":str(key),**gauss(g.actual_total.to_numpy(float),g.pred_total.to_numpy(float))},
          {"target":"win","dimension":dim,"slice":str(key),**win(g.actual_home_win.to_numpy(float),g.pred_win.to_numpy(float))}
        ]
Q.to_csv(out/"challenger_b_2025_scored_predictions_v1_196.csv",index=False)
pd.DataFrame(slices).to_csv(out/"challenger_b_2025_evaluation_slices_v1_196.csv",index=False)
summary={"status":"EXECUTED_NOT_ACCEPTED","frozen_predictions":793,"frozen_exclusions":141,"target_games":934,"metrics":metrics,
"prediction_values_modified":False,"market_joined":False,"refit_performed":False,"recalibration_performed":False,"redesign_performed":False}
(out/"summary_v1_196.json").write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n")
manifest={}
for p in sorted(out.iterdir()):
    if p.name.startswith("manifest"): continue
    manifest[p.name]={"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"bytes":p.stat().st_size}
(out/"manifest_v1_196.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n")
print(json.dumps(summary,indent=2))
