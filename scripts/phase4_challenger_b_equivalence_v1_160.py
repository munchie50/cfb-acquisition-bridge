#!/usr/bin/env python3
# Challenger B producer-equivalence harness v1.160.
# It does not redefine features: it audits accepted artifacts against a fresh
# execution of the frozen v1.109/v1.115 producers on their original schedule.
import hashlib, json, sys
from pathlib import Path
import pandas as pd
import numpy as np

old=Path(sys.argv[1]); fresh=Path(sys.argv[2]); out=Path(sys.argv[3]); out.mkdir(parents=True,exist_ok=True)
files=["phase4_feature_canary_v1_109.csv","phase4_team_game_mechanical_primitives_v1_109.csv",
       "phase4_derived_feature_canary_v1_115.csv","phase4_derived_team_game_primitives_v1_115.csv"]
report={}
ok=True
for fn in files:
    a=pd.read_csv(old/fn); b=pd.read_csv(fresh/fn)
    keys=[c for c in ["season","game_id","team"] if c in a.columns and c in b.columns]
    if not keys: raise SystemExit("no comparison keys "+fn)
    for d in (a,b):
        if "game_id" in d: d["game_id"]=d["game_id"].astype(str)
    ac=set(map(tuple,a[keys].astype(str).to_numpy())); bc=set(map(tuple,b[keys].astype(str).to_numpy()))
    cols=[c for c in a.columns if c in b.columns]
    m=a.merge(b,on=keys,how="outer",suffixes=("_old","_fresh"),indicator=True)
    mism=[]
    for c in cols:
        if c in keys: continue
        x=m[c+"_old"]; y=m[c+"_fresh"]
        if pd.api.types.is_numeric_dtype(x) and pd.api.types.is_numeric_dtype(y):
            neq=~(np.isclose(x,y,rtol=1e-12,atol=1e-12,equal_nan=True))
        else:
            xs=x.fillna("<NA>").astype(str); ys=y.fillna("<NA>").astype(str); neq=xs!=ys
        n=int(neq.sum())
        if n: mism.append({"column":c,"mismatch_rows":n})
    passed=(ac==bc and not mism and (m["_merge"]=="both").all())
    ok &= passed
    report[fn]={"status":"PASS" if passed else "FAIL","old_rows":len(a),"fresh_rows":len(b),
                "key_sets_equal":ac==bc,"column_mismatches":mism}
manifest={"status":"PASS" if ok else "FAIL","files":report,"model_fit_or_score_performed":False,"2025_accessed":False}
(out/"equivalence_manifest_v1_160.json").write_text(json.dumps(manifest,indent=2)+"\n")
print(json.dumps(manifest,indent=2))
if not ok: raise SystemExit(4)
