#!/usr/bin/env python3
"""Independent generic acceptance audit for a weekly v1.246 REFRESH_SNAPSHOT."""
import sys,json,hashlib
from pathlib import Path
import pandas as pd, numpy as np

art, rawdir, fitdir, out = map(Path, sys.argv[1:5])
out.mkdir(parents=True, exist_ok=True)

names={
 "pred":"challenger_b_2026_refresh_fair_predictions_v1_246.csv",
 "exc":"challenger_b_2026_refresh_exclusions_v1_246.csv",
 "chron":"challenger_b_2026_refresh_chronology_audit_v1_246.csv",
 "target":"challenger_b_2026_refresh_target_ledger_v1_246.csv",
 "side":"challenger_b_2026_refresh_feature_eligibility_ledger_v1_246.csv",
 "manifest":"manifest_v1_246.json",
}
for fn in names.values():
    assert (art/fn).is_file(), f"missing complete S0 artifact: {fn}"

P=pd.read_csv(art/names["pred"],dtype={"game_id":str})
E=pd.read_csv(art/names["exc"],dtype={"game_id":str})
A=pd.read_csv(art/names["chron"],dtype={"game_id":str})
T=pd.read_csv(art/names["target"],dtype={"game_id":str})
L=pd.read_csv(art/names["side"],dtype={"game_id":str})
M=json.loads((art/names["manifest"]).read_text())

assert M["status"]=="EXECUTED_NOT_ACCEPTED"
assert M["snapshot_type"]=="REFRESH_SNAPSHOT" and M["parent_lineage"]=="v1.216"
cutoff=pd.Timestamp(M["cutoff_utc"])
assert cutoff.tz is not None
assert len(T)>0 and T.game_id.nunique()==len(T) and not T.game_id.duplicated().any()
assert len(P)+len(E)==len(T)
assert not set(P.game_id)&set(E.game_id)
assert set(P.game_id)|set(E.game_id)==set(T.game_id)
assert len(L)==2*len(T) and not L.duplicated(["game_id","side"]).any() and set(L.game_id)==set(T.game_id)
assert set(T.population_class.unique()).issubset({"FBS_VS_FBS","FBS_VS_NONFBS"})

for df in (P,E,T,L):
    assert (df["snapshot_type"]=="REFRESH_SNAPSHOT").all()
    assert (pd.to_datetime(df["snapshot_cutoff_utc"],utc=True)==cutoff).all()
assert (pd.to_datetime(T.start_date,utc=True)>cutoff).all()

bad=("point","score","winner","spread","moneyline","over_under","odds","bet","market","actual","postgame")
for df,label in ((T,"target"),):
    forbidden=[c for c in df.columns if any(x in c.lower() for x in bad)]
    assert not forbidden, f"{label} forbidden fields: {forbidden}"

if len(A):
    assert A.own_game_excluded.astype(bool).all() and A.strict_chronology.astype(bool).all()
    prior=pd.to_datetime(A.max_prior_kickoff,utc=True)
    target=pd.to_datetime(A.target_kickoff,utc=True)
    assert (prior<target).all() and (prior<cutoff).all()

predcols=["pred_margin","pred_total","pred_win"]
assert set(predcols).issubset(P.columns)
if len(P):
    assert np.isfinite(P[predcols].to_numpy(float)).all() and P.pred_win.between(0,1).all()

coefp=fitdir/"selected_coefficients.csv"; scalep=fitdir/"train_scaling.csv"
assert hashlib.sha256(coefp.read_bytes()).hexdigest()=="bf15ce41180bfb4e250d311df279e98c13b65432756ae07f7a30264cbae0e221"
assert hashlib.sha256(scalep.read_bytes()).hexdigest()=="68fb5193ccb8828ac8d34dfe820101181c2bde078a04a6d5afd4c08bcf0cab45"
coef=pd.read_csv(coefp); scale=pd.read_csv(scalep)
features=scale.feature.tolist()
assert len(features)==34 and len(coef)==108
assert set(coef.groupby("target")["lambda"].first().to_dict().items())=={("margin",0.1),("total",0.1),("win",0.01)}

if len(P):
    Z=(P[features].to_numpy(float)-scale.set_index("feature").loc[features,"mean"].to_numpy(float))/scale.set_index("feature").loc[features,"sd"].to_numpy(float)
    Z=np.c_[Z,(P.venue_state=="NEUTRAL").astype(float).to_numpy()]
    terms=["intercept"]+features+["venue_neutral"]
    for kind,lam in [("margin",0.1),("total",0.1),("win",0.01)]:
        cc=coef[(coef.target==kind)&(coef["lambda"]==lam)].set_index("term")
        assert set(cc.index)==set(terms)
        q=np.c_[np.ones(len(Z)),Z]@cc.loc[terms,"coefficient"].to_numpy(float)
        if kind=="win": q=1/(1+np.exp(-np.clip(q,-40,40)))
        assert np.allclose(q,P["pred_"+kind].to_numpy(float),rtol=0,atol=1e-12)

for fn,h in M["hashes"].items():
    p=art/fn
    assert p.is_file(), f"manifest-listed output missing: {fn}"
    assert hashlib.sha256(p.read_bytes()).hexdigest()==h, f"output hash mismatch: {fn}"

raw_sched=rawdir/"cfb_schedules_2026.parquet"; raw_pbp=rawdir/"pbp_2026.rds"
assert raw_sched.is_file() and raw_pbp.is_file()
source_hashes={
 "schedule_sha256":hashlib.sha256(raw_sched.read_bytes()).hexdigest(),
 "pbp_sha256":hashlib.sha256(raw_pbp.read_bytes()).hexdigest(),
}
report={
 "status":"PASS_WEEKLY_REFRESH_ACCEPTANCE",
 "snapshot_type":"REFRESH_SNAPSHOT",
 "cutoff_utc":M["cutoff_utc"],
 "target_games":len(T),
 "eligible_predictions":len(P),
 "excluded_games":len(E),
 "team_side_ledger_rows":len(L),
 "chronology_rows":len(A),
 "strict_chronology":True,
 "predictions_independently_recomputed":True,
 "artifact_hashes_reproduced":True,
 "target_outcomes_opened":False,
 "market_joined":False,
 "fit_or_optimization_performed":False,
 **source_hashes,
}
(out/"weekly_refresh_acceptance.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
print(json.dumps(report,indent=2,sort_keys=True))
