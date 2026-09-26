#!/usr/bin/env python3
# v1.164: independently prove target-ledger/population structural invariants.
import json,sys
from pathlib import Path
import pandas as pd
p=Path(sys.argv[1]); out=Path(sys.argv[2]); out.mkdir(parents=True,exist_ok=True)
exp={2016:873,2017:874,2018:884,2019:888,2020:570,2021:887,2022:896,2023:910,2024:919}
rows=[]; checks=[]
for y,n in exp.items():
 d=pd.read_csv(p/f"challenger_b_schedule_{y}_v1_157.csv",dtype={"game_id":str})
 c={"season":y,"rows":len(d),"expected":n,"unique_ids":d.game_id.nunique(),
    "null_team":int(d[["home_team","away_team"]].isna().any(axis=1).sum()),
    "self_game":int((d.home_team==d.away_team).sum()),
    "classes":sorted(d.population_class.dropna().unique().tolist())}
 c["pass"]=c["rows"]==n and c["unique_ids"]==n and c["null_team"]==0 and c["self_game"]==0
 checks.append(c); rows.extend(d.game_id.tolist())
global_unique=len(set(rows))==len(rows)
status=all(x["pass"] for x in checks) and global_unique
m={"status":"PASS" if status else "FAIL","checks":checks,"global_game_ids_unique":global_unique,
   "games":len(rows),"expected_games":sum(exp.values()),"2025_accessed":False,"fit_or_score":False}
(out/"population_invariant_manifest_v1_164.json").write_text(json.dumps(m,indent=2)+"\n")
print(json.dumps(m,indent=2))
if not status: raise SystemExit(4)
