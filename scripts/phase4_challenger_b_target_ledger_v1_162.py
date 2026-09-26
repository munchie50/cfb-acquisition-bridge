#!/usr/bin/env python3
import json,sys
from pathlib import Path
import pandas as pd
root=Path(sys.argv[1]); out=Path(sys.argv[2]); out.mkdir(parents=True,exist_ok=True)
rows=[]
for y in range(2016,2025):
 p=root/f"challenger_b_schedule_{y}_v1_157.csv"
 d=pd.read_csv(p,dtype={"game_id":str})
 for _,r in d.iterrows():
  for side in ("home","away"):
   rows.append({"season":y,"game_id":str(r.game_id),"team":r[f"{side}_team"],"start_date":r.start_date,
    "venue":"NEUTRAL" if bool(r.neutral_site) else side.upper(),
    "population_class":r.population_class,"competition_class":r.competition_class})
x=pd.DataFrame(rows)
assert not x.duplicated(["season","game_id","team"]).any()
x["start_ts"]=pd.to_datetime(x.start_date,utc=True,errors="coerce")
assert x.start_ts.notna().all()
# Equal-kickoff games for same team are ambiguous for strict prior availability and must be ledgered.
ties=x[x.duplicated(["season","team","start_ts"],keep=False)].sort_values(["season","team","start_ts","game_id"])
x.drop(columns=["start_ts"]).to_csv(out/"challenger_b_target_team_sides_v1_162.csv",index=False)
ties.drop(columns=["start_ts"]).to_csv(out/"challenger_b_equal_kickoff_ambiguity_v1_162.csv",index=False)
summary={"target_games":int(x.game_id.nunique()),"target_team_sides":len(x),
 "equal_kickoff_ambiguous_team_sides":len(ties),"equal_kickoff_ambiguous_games":int(ties.game_id.nunique()),
 "status":"PASS" if len(ties)==0 else "AMBIGUITY_REQUIRES_FAIL_CLOSED_LEDGER",
 "model_fit_or_score_performed":False,"2025_accessed":False}
(out/"manifest.json").write_text(json.dumps(summary,indent=2)+"\n"); print(json.dumps(summary,indent=2))
