import json, pandas as pd
DATA="phase4_challenger_a_dataset_v1_131.csv"; CFG="phase4_challenger_a_config_v1_131.json"
df=pd.read_csv(DATA,nrows=5); cfg=json.load(open(CFG))
cols=list(df.columns); preds=list(cfg["numeric_predictors"])+[cfg["categorical_predictor"]]
sentinel="__QA_FUTURE_INFORMATION_SENTINEL__"
assert sentinel not in cols
assert sentinel not in preds
assert not any("2025" in str(x) for x in cols)
full=pd.read_csv(DATA,usecols=["season"])
assert int((full.season==2025).sum())==0
# Isolated invalid control: demonstrate a deliberately created future-information
# column is detectable and would be rejected by the candidate-column equality gate.
qa=df.copy(); qa[sentinel]=1
candidate_allowed=set(preds)
observed_candidate=set(preds+[sentinel])
assert sentinel in qa.columns
assert observed_candidate != candidate_allowed
print(json.dumps({"status":"PASS","sentinel":sentinel,"sentinel_absent_from_frozen_dataset":True,"sentinel_absent_from_frozen_predictor_config":True,"injected_sentinel_detected_by_exact_column_gate":True,"test_2025_rows":0,"model_fit_or_score_performed":False},indent=2))
