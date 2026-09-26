#!/usr/bin/env python3
# Independent acceptance audit for v1.188 prospective 2025 fair predictions.
import sys,json,hashlib
from pathlib import Path
import pandas as pd, numpy as np
art,sched,fit,out=map(Path,sys.argv[1:5]); out.mkdir(parents=True,exist_ok=True)
P=pd.read_csv(art/"challenger_b_2025_fair_predictions_v1_188.csv",dtype={"game_id":str})
E=pd.read_csv(art/"challenger_b_2025_exclusions_v1_188.csv",dtype={"game_id":str})
A=pd.read_csv(art/"challenger_b_2025_chronology_audit_v1_188.csv",dtype={"game_id":str})
T=pd.read_csv(art/"challenger_b_2025_target_ledger_v1_188.csv",dtype={"game_id":str})
S=pd.read_csv(sched,dtype={"game_id":str})
M=json.load(open(art/"manifest_v1_188.json"))
assert len(S)==934 and len(T)==934 and set(S.game_id)==set(T.game_id)
assert S.game_id.nunique()==934 and T.game_id.nunique()==934
assert len(P)+len(E)==934 and not set(P.game_id)&set(E.game_id) and set(P.game_id)|set(E.game_id)==set(S.game_id)
assert (S.population_class=="FBS_VS_FBS").sum()==808 and (S.population_class=="FBS_VS_NONFBS").sum()==126
assert (S.competition_class=="REGULAR").sum()==879 and (S.competition_class=="CONFERENCE_CHAMPIONSHIP").sum()==9 and (S.competition_class=="POSTSEASON").sum()==46
bad=("point","score","winner","spread","moneyline","over_under","odds","bet","market","actual")
assert not [c for c in T.columns if any(x in c.lower() for x in bad)]
assert A.own_game_excluded.astype(bool).all() and A.strict_chronology.astype(bool).all()
A["max_prior_kickoff"]=pd.to_datetime(A.max_prior_kickoff,utc=True); A["target_kickoff"]=pd.to_datetime(A.target_kickoff,utc=True)
assert (A.max_prior_kickoff < A.target_kickoff).all()
predcols=["pred_margin","pred_total","pred_win"]; assert set(predcols).issubset(P.columns)
assert np.isfinite(P[predcols].to_numpy(float)).all() and P.pred_win.between(0,1).all()
assert not [c for c in P.columns if any(x in c.lower() for x in ("spread","moneyline","over_under","odds","market","actual","target_"))]
coef=pd.read_csv(fit/"selected_coefficients.csv"); scale=pd.read_csv(fit/"train_scaling.csv")
assert len(scale)==34 and len(coef)==98
assert set(coef.groupby("target")["lambda"].first().to_dict().items())=={("margin",10),("total",100),("win",10)}
for fn,h in M["hashes"].items():
    assert hashlib.sha256((art/fn).read_bytes()).hexdigest()==h
report={"status":"PASS","target_games":934,"eligible_predictions":len(P),"excluded_games":len(E),"chronology_rows":len(A),"target_key_exact":True,"own_game_exclusion":True,"strict_chronology":True,"model_identity_terms":len(coef),"scaling_features":len(scale),"artifact_hashes_reproduced":True,"2025_outcomes_opened":False,"2025_outcomes_scored":False}
(out/"acceptance_v1_189.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n"); print(json.dumps(report,indent=2))
