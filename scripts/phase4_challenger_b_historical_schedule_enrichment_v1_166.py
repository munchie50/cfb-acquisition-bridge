#!/usr/bin/env python3
# v1.166 historical schedule enrichment: accepted v1.157 target identity + same-lineage historical scores.
import sys,json
from pathlib import Path
import pandas as pd
pop=Path(sys.argv[1]); src=Path(sys.argv[2]); out=Path(sys.argv[3]); out.mkdir(parents=True,exist_ok=True)
summary=[]
for y in range(2016,2025):
 t=pd.read_csv(pop/f"challenger_b_schedule_{y}_v1_157.csv",dtype={"game_id":str})
 s=pd.read_csv(src/f"schedule_{y}.csv",dtype={"game_id":str})
 # normalize known cfbfastR schedule score names
 ren={}
 for dest,cands in {"home_points":["home_points","home_score"],"away_points":["away_points","away_score"]}.items():
  for c in cands:
   if c in s.columns: ren[c]=dest; break
 if "home_points" not in ren.values() or "away_points" not in ren.values(): raise SystemExit(f"{y} score columns unavailable")
 s=s.rename(columns=ren)[["game_id","home_points","away_points"]].drop_duplicates("game_id")
 d=t.merge(s,on="game_id",how="left",validate="one_to_one")
 miss=d[["home_points","away_points"]].isna().any(axis=1)
 summary.append({"season":y,"targets":len(d),"missing_final_score":int(miss.sum())})
 d.to_csv(out/f"challenger_b_historical_schedule_{y}_v1_166.csv",index=False)
m={"status":"PASS" if sum(x["missing_final_score"] for x in summary)==0 else "FAIL_CLOSED_MISSING_OUTCOME",
"by_season":summary,"2025_accessed":False,"fit_or_score":False}
(out/"manifest_v1_166.json").write_text(json.dumps(m,indent=2)+"\n"); print(json.dumps(m,indent=2))
if m["status"]!="PASS": raise SystemExit(4)
