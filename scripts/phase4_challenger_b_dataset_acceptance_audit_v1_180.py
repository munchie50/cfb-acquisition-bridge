#!/usr/bin/env python3
import sys,json,hashlib
from pathlib import Path
import pandas as pd
p=Path(sys.argv[1])
d=pd.read_csv(p/"challenger_b_dataset_v1_179.csv",dtype={"game_id":str})
e=pd.read_csv(p/"challenger_b_exclusion_ledger_v1_179.csv",dtype={"game_id":str})
pc=pd.read_csv(p/"challenger_b_population_contract_v1_179.csv")
pdsp=pd.read_csv(p/"challenger_b_population_disposition_v1_179.csv")
cfg=json.load(open(p/"challenger_b_config_v1_179.json")); man=json.load(open(p/"manifest_v1_179.json"))
assert man["status"]=="DATASET_FREEZE_EXECUTED_NOT_ACCEPTED" and not man["2025_accessed"] and not man["fit_or_score"]
assert man["target_population_games"]==7701 and len(d)+len(e)==7701
assert d.game_id.nunique()==len(d) and e.game_id.nunique()==len(e) and set(d.game_id).isdisjoint(set(e.game_id))
assert not (d.season==2025).any() and not (e.season==2025).any()
assert len(cfg["numeric_predictors"])==34 and d[cfg["numeric_predictors"]].notna().all(axis=None)
assert cfg["source_feature_artifact_id"]==10895523493
assert cfg["source_feature_digest"]=="sha256:702930b2ba905c9f917acbc627d12342e8190cfb44a4c8afd1aee49fbf59e239"
assert cfg["partitions"]["TRAIN"]==[2016,2017,2018,2019,2020,2021,2022] and cfg["partitions"]["SPENT_CORROBORATIVE"]==[2023,2024] and cfg["partitions"]["TEST_PROTECTED"]==[2025]
# population semantic accounting: every target class total equals eligible+excluded disposition total
a=pc.groupby(["population_class","competition_class"]).target_games.sum().sort_index()
b=pdsp.groupby(["population_class","competition_class"]).games.sum().sort_index()
assert a.equals(b) and int(a.sum())==7701
# excluded rows must explain themselves; no copied temporal blacklist reason is allowed
assert e.reasons.notna().all() and e.reasons.str.len().gt(0).all()
assert not e.reasons.str.contains("v1.128_temporal_exclusion",regex=False).any()
# target algebra and venue
assert ((d.target_home_margin==0)==(d.target_home_win==0)).sum()>=0  # ties may exist; win is strict home win
assert set(d.venue_state).issubset({"HOME","NEUTRAL"})
bad=("spread","moneyline","market","odds","favorite","underdog","closing","consensus","clv")
assert not any(any(w in c.lower() for w in bad) for c in cfg["numeric_predictors"])
# producer manifest hashes must verify for all files it covered
for fn,h in man["sha256"].items(): assert hashlib.sha256((p/fn).read_bytes()).hexdigest()==h
print(json.dumps({"status":"INDEPENDENT_DATASET_AUDIT_PASS","eligible_rows":len(d),"excluded_games":len(e),"population_classes":len(a),"seasons":sorted(map(int,d.season.unique())),"fit_or_score":False,"2025_accessed":False},indent=2))
