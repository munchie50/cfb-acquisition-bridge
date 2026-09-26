#!/usr/bin/env python3
# v1.165 corrected PBP coverage audit. v1.163 class counters used the wrong literal.
import json,sys
from pathlib import Path
import pandas as pd, pyreadr
pop=Path(sys.argv[1]); raw=Path(sys.argv[2]); out=Path(sys.argv[3]); out.mkdir(parents=True,exist_ok=True)
allrows=[]; summaries=[]
for y in range(2016,2025):
 s=pd.read_csv(pop/f"challenger_b_schedule_{y}_v1_157.csv",dtype={"game_id":str})
 if not set(s.population_class.dropna().unique()) <= {"FBS_VS_FBS","FBS_VS_NONFBS"}:
  raise SystemExit(f"unexpected population class {y}: {sorted(s.population_class.dropna().unique())}")
 p=next(iter(pyreadr.read_r(raw/f"pbp_{y}.rds").values()))
 gid=next(c for c in ["game_id","id_game"] if c in p.columns)
 ids=set(p[gid].dropna().astype(str).str.replace(r"\.0$","",regex=True))
 s["pbp_present"]=s.game_id.astype(str).isin(ids); miss=s[~s.pbp_present].copy()
 miss["reason"]="NO_GAME_ID_IN_CFBFASTR_PBP"; allrows.append(miss)
 summaries.append({"season":y,"target_games":len(s),"pbp_present":int(s.pbp_present.sum()),"pbp_missing":len(miss),
  "missing_fbs_vs_fbs":int((miss.population_class=="FBS_VS_FBS").sum()),
  "missing_fbs_vs_nonfbs":int((miss.population_class=="FBS_VS_NONFBS").sum()),
  "missing_regular":int((miss.competition_class=="REGULAR").sum()),
  "missing_postseason":int((miss.competition_class=="POSTSEASON").sum())})
m=pd.concat(allrows,ignore_index=True)
m.to_csv(out/"missing_pbp_ledger_v1_165.csv",index=False)
tot={"FBS_VS_FBS":int((m.population_class=="FBS_VS_FBS").sum()),"FBS_VS_NONFBS":int((m.population_class=="FBS_VS_NONFBS").sum()),
     "REGULAR":int((m.competition_class=="REGULAR").sum()),"POSTSEASON":int((m.competition_class=="POSTSEASON").sum())}
manifest={"status":"BOUNDED_COVERAGE","by_season":summaries,"missing_total":len(m),"missing_by_class":tot,
 "pbp_present_total":sum(x["pbp_present"] for x in summaries),"target_total":sum(x["target_games"] for x in summaries),
 "2025_accessed":False,"fit_or_score":False}
(out/"manifest_v1_165.json").write_text(json.dumps(manifest,indent=2)+"\n"); print(json.dumps(manifest,indent=2))
