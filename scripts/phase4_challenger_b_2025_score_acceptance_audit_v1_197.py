#!/usr/bin/env python3
# Independent audit of v1.196 outcome scoring. Does not consume v1.196 scored rows as authority.
import sys,json,hashlib
from pathlib import Path
import pandas as pd, numpy as np
frozen,raw,scored,out=map(Path,sys.argv[1:5]); out.mkdir(parents=True,exist_ok=True)
P=pd.read_csv(frozen/"challenger_b_2025_fair_predictions_v1_188.csv",dtype={"game_id":str})
E=pd.read_csv(frozen/"challenger_b_2025_exclusions_v1_188.csv",dtype={"game_id":str})
T=pd.read_csv(frozen/"challenger_b_2025_target_ledger_v1_188.csv",dtype={"game_id":str})
Q=pd.read_csv(scored/"challenger_b_2025_scored_predictions_v1_196.csv",dtype={"game_id":str})
S=json.load(open(scored/"summary_v1_196.json"))
M=json.load(open(scored/"manifest_v1_196.json"))
R=pd.read_parquet(raw); R["game_id"]=R.game_id.astype(str); R=R[R.game_id.isin(set(T.game_id))].copy()
assert len(T)==934 and len(P)==793 and len(E)==141
assert not set(P.game_id)&set(E.game_id) and set(P.game_id)|set(E.game_id)==set(T.game_id)
assert len(R)==934 and R.game_id.nunique()==934 and set(R.game_id)==set(T.game_id)
assert not R[["home_points","away_points"]].isna().any().any()
O=R[["game_id","home_points","away_points"]].copy()
O["actual_margin"]=O.home_points.astype(float)-O.away_points.astype(float)
O["actual_total"]=O.home_points.astype(float)+O.away_points.astype(float)
assert not (O.actual_margin==0).any()
O["actual_home_win"]=(O.actual_margin>0).astype(float)
A=P.merge(O[["game_id","actual_margin","actual_total","actual_home_win"]],on="game_id",validate="one_to_one")
assert set(A.game_id)==set(Q.game_id) and len(Q)==793
# Frozen prediction values must survive scoring byte-for-value after CSV parse.
for c in ["pred_margin","pred_total","pred_win"]:
    z=Q.set_index("game_id").loc[P.game_id,c].to_numpy(float)
    d=np.abs(z-P[c].to_numpy(float))\n    assert np.allclose(z,P[c].to_numpy(float),rtol=0,atol=1e-12), (c,float(d.max()))
for c in ["actual_margin","actual_total","actual_home_win"]:
    z=Q.set_index("game_id").loc[A.game_id,c].to_numpy(float)
    assert np.array_equal(z,A[c].to_numpy(float))

def gauss(y,p):
 e=p-y; return {"n":int(len(y)),"mae":float(np.mean(np.abs(e))),"rmse":float(np.sqrt(np.mean(e*e))),"bias":float(np.mean(e))}
def win(y,p):
 q=np.clip(p,1e-15,1-1e-15); return {"n":int(len(y)),"brier":float(np.mean((p-y)**2)),"logloss":float(-np.mean(y*np.log(q)+(1-y)*np.log(1-q)))}
metrics={"margin":gauss(A.actual_margin.to_numpy(float),A.pred_margin.to_numpy(float)),
"total":gauss(A.actual_total.to_numpy(float),A.pred_total.to_numpy(float)),
"win":win(A.actual_home_win.to_numpy(float),A.pred_win.to_numpy(float))}
for k in metrics:
 for m,v in metrics[k].items():
  if isinstance(v,float): assert np.isclose(v,S["metrics"][k][m],rtol=0,atol=1e-15)
  else: assert v==S["metrics"][k][m]
for fn,h in M.items():
 assert hashlib.sha256((scored/fn).read_bytes()).hexdigest()==h["sha256"]
report={"status":"PASS","target_games":934,"scored_predictions":793,"frozen_exclusions":141,
"target_key_exact":True,"outcomes_complete":True,"prediction_values_numerically_unchanged_at_1e_12":True,
"metrics_independently_recomputed":True,"scoring_artifact_hashes_reproduced":True,"metrics":metrics,
"market_joined":False,"refit_performed":False,"recalibration_performed":False,"redesign_performed":False}
(out/"acceptance_v1_197.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
print(json.dumps(report,indent=2))
