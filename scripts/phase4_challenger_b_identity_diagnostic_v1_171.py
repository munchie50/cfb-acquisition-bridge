#!/usr/bin/env python3
import sys,json
from pathlib import Path
import pandas as pd, pyreadr
ids=set("400869356 400869808 400944831 401013102 401014979 401309541 401416568 401532393 401644732 401644737".split())
raw=Path(sys.argv[1]); out=Path(sys.argv[2]); out.mkdir(parents=True,exist_ok=True)
rows=[]
for y in range(2016,2025):
 p=next(iter(pyreadr.read_r(raw/f"pbp_{y}.rds").values()))
 p["game_id"]=p.game_id.astype(str).str.replace(r"\.0$","",regex=True)
 z=p[p.game_id.isin(ids)]
 for gid,g in z.groupby("game_id"):
  rows.append({"season":y,"game_id":gid,
   "pos_team_labels":" | ".join(sorted(set(g.pos_team.dropna().astype(str)))),
   "def_pos_team_labels":" | ".join(sorted(set(g.def_pos_team.dropna().astype(str)))),
   "plays":len(g)})
d=pd.DataFrame(rows).sort_values(["season","game_id"])
assert set(d.game_id)==ids
d.to_csv(out/"pbp_identity_labels_v1_171.csv",index=False)
(out/"manifest_v1_171.json").write_text(json.dumps({"status":"IDENTITY_DIAGNOSTIC","games":len(d),"2025_accessed":False,"fit_or_score":False},indent=2))
print(d.to_string(index=False))
