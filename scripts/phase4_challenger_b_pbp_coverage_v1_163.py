#!/usr/bin/env python3
import json,sys
from pathlib import Path
import pandas as pd
import pyreadr
pop=Path(sys.argv[1]); raw=Path(sys.argv[2]); out=Path(sys.argv[3]); out.mkdir(parents=True,exist_ok=True)
allrows=[]; summaries=[]
for y in range(2016,2025):
 s=pd.read_csv(pop/f"challenger_b_schedule_{y}_v1_157.csv",dtype={"game_id":str})
 obj=pyreadr.read_r(raw/f"pbp_{y}.rds")
 p=next(iter(obj.values()))
 gid=next(c for c in ["game_id","id_game"] if c in p.columns)
 ids=set(p[gid].dropna().astype(str).str.replace(r"\.0$","",regex=True))
 s["pbp_present"]=s.game_id.astype(str).isin(ids)
 miss=s[~s.pbp_present].copy()
 miss["reason"]="NO_GAME_ID_IN_CFBFASTR_PBP"
 allrows.append(miss)
 summaries.append({"season":y,"target_games":len(s),"pbp_present":int(s.pbp_present.sum()),"pbp_missing":int((~s.pbp_present).sum()),
  "missing_fbs_nonfbs":int(((~s.pbp_present)&(s.population_class=="FBS_NONFBS")).sum()),
  "missing_postseason":int(((~s.pbp_present)&(s.competition_class=="POSTSEASON")).sum())})
m=pd.concat(allrows,ignore_index=True)
m.to_csv(out/"missing_pbp_ledger_v1_163.csv",index=False)
json.dump({"status":"DIAGNOSTIC","by_season":summaries,"missing_total":len(m),"2025_accessed":False,
 "fit_or_score":False},open(out/"manifest.json","w"),indent=2)
print(json.dumps({"by_season":summaries,"missing_total":len(m)},indent=2))
