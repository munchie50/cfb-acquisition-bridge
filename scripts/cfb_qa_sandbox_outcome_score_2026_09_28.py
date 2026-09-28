#!/usr/bin/env python3
# QA Sandbox: score immutable Run #13 candidate predictions against accepted v1.179 historical targets.
import sys,json,hashlib
from pathlib import Path
import pandas as pd, numpy as np

pred,dataset,out=map(Path,sys.argv[1:4]); out.mkdir(parents=True,exist_ok=True)
P=pd.read_csv(pred,dtype={"game_id":str})
D=pd.read_csv(dataset,dtype={"game_id":str})
if hashlib.sha256(pred.read_bytes()).hexdigest()!="ed858f1bd72decd93d02aec4de507c3217470b8d01294c2cf677a2d79ed78ee3": raise SystemExit("prediction identity mismatch")
if hashlib.sha256(dataset.read_bytes()).hexdigest()!="f8c479c83abf5dac3be6dcb4bba3d6a0996ae2623297a9a3514465824b7c4af8": raise SystemExit("dataset identity mismatch")
needp={"season","game_id","candidate_id","pred_margin","pred_total","pred_win"}
needd={"season","game_id","target_home_margin","target_total_points","target_home_win"}
if not needp.issubset(P) or not needd.issubset(D): raise SystemExit("required columns missing")
if len(P)!=55834 or len(D)!=6246: raise SystemExit("frozen cardinality mismatch")
if P.duplicated(["season","game_id","candidate_id"]).any() or D.duplicated(["season","game_id"]).any(): raise SystemExit("duplicate identity")
if (P.season==2025).any() or (D.season==2025).any(): raise SystemExit("2025 exposure")
if not set(P.season.astype(int)).issubset(set(range(2016,2025))) or not set(D.season.astype(int)).issubset(set(range(2016,2025))): raise SystemExit("season boundary")
Q=P.merge(D[list(needd)],on=["season","game_id"],how="left",validate="many_to_one")
targets=["target_home_margin","target_total_points","target_home_win"]
if Q[targets].isna().any().any(): raise SystemExit("outcome join incomplete")
if not np.isfinite(Q[["pred_margin","pred_total","pred_win"]+targets].to_numpy(float)).all(): raise SystemExit("nonfinite score input")
if ((Q.pred_win<0)|(Q.pred_win>1)).any(): raise SystemExit("invalid win probability")

def gauss(y,p):
 e=p-y
 return {"n":int(len(y)),"mae":float(np.mean(np.abs(e))),"rmse":float(np.sqrt(np.mean(e*e))),"bias":float(np.mean(e))}
def win(y,p):
 q=np.clip(p,1e-15,1-1e-15)
 direction=((p>=0.5)==(y>=0.5)).astype(float)
 return {"n":int(len(y)),"brier":float(np.mean((p-y)**2)),"logloss":float(-np.mean(y*np.log(q)+(1-y)*np.log(1-q))),"winner_direction_accuracy":float(np.mean(direction))}

def metrics(g):
 return {"margin":gauss(g.target_home_margin.to_numpy(float),g.pred_margin.to_numpy(float)),
 "total":gauss(g.target_total_points.to_numpy(float),g.pred_total.to_numpy(float)),
 "win":win(g.target_home_win.to_numpy(float),g.pred_win.to_numpy(float))}

summary={}
season_rows=[]
for cid,g in Q.groupby("candidate_id",sort=True):
 summary[cid]=metrics(g)
 for season,sg in g.groupby("season",sort=True):
  mm=metrics(sg)
  for target,vals in mm.items(): season_rows.append({"candidate_id":cid,"season":int(season),"target":target,**vals})

# Large-disagreement slices are defined outcome-blind relative to S0 before inspecting target values.
base=P[P.candidate_id=="S0"][["season","game_id","pred_margin","pred_total","pred_win"]].rename(columns={"pred_margin":"s0_margin","pred_total":"s0_total","pred_win":"s0_win"})
R=Q.merge(base,on=["season","game_id"],how="left",validate="many_to_one")
R["margin_disagreement"]=abs(R.pred_margin-R.s0_margin)
R["total_disagreement"]=abs(R.pred_total-R.s0_total)
R["win_disagreement"]=abs(R.pred_win-R.s0_win)
# Fixed transparent thresholds; descriptive QA only, not selection metrics.
slice_rows=[]
for cid,g in R[R.candidate_id!="S0"].groupby("candidate_id",sort=True):
 for name,col,thr in [("margin_abs_vs_s0_ge_7","margin_disagreement",7.0),("total_abs_vs_s0_ge_7","total_disagreement",7.0),("win_abs_vs_s0_ge_0.10","win_disagreement",0.10)]:
  z=g[g[col]>=thr]
  if len(z):
   mm=metrics(z)
   for target,vals in mm.items(): slice_rows.append({"candidate_id":cid,"slice":name,"target":target,**vals})

Q.to_csv(out/"scored_predictions.csv",index=False)
pd.DataFrame(season_rows).to_csv(out/"metrics_by_season.csv",index=False)
pd.DataFrame(slice_rows).to_csv(out/"large_disagreement_slices.csv",index=False)
(out/"summary.json").write_text(json.dumps({"status":"EXECUTED_NOT_ACCEPTED","prediction_rows":len(Q),"candidate_metrics":summary,"2025_accessed":False,"market_joined":False,"predictions_modified":False,"refit_performed":False},indent=2,sort_keys=True)+"\n")
manifest={}
for p in sorted(out.iterdir()):
 if p.name=="manifest.json": continue
 manifest[p.name]={"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"bytes":p.stat().st_size}
(out/"manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n")
print(json.dumps({"rows":len(Q),"candidate_metrics":summary},indent=2,sort_keys=True))
