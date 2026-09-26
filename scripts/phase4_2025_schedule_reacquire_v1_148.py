#!/usr/bin/env python3
import hashlib, json, sys
from pathlib import Path
import pandas as pd

src=Path(sys.argv[1]); out=Path(sys.argv[2]); out.mkdir(parents=True,exist_ok=True)
raw=src.read_bytes(); raw_sha=hashlib.sha256(raw).hexdigest()
df=pd.read_parquet(src)
cols=set(df.columns)
req={"game_id","season","start_date","home_team","away_team","neutral_site"}
missing=sorted(req-cols)
if missing: raise SystemExit("missing required columns: "+",".join(missing))
x=df[df["season"].astype(str)=="2025"].copy()
# Fresh-source diagnostic population only; not asserted equivalent to historical CBS-membership scope.
season_type=x["season_type"].astype(str).str.lower() if "season_type" in x else pd.Series("",index=x.index)
completed=x["completed"].fillna(False).astype(bool) if "completed" in x else pd.Series(True,index=x.index)
hd=x["home_division"].astype(str).str.lower() if "home_division" in x else pd.Series("",index=x.index)
ad=x["away_division"].astype(str).str.lower() if "away_division" in x else pd.Series("",index=x.index)
candidate=x[(season_type=="regular") & completed & (hd=="fbs") & (ad=="fbs")].copy()
keep=["season","game_id","start_date","home_team","away_team","neutral_site"]
for c in ["season_type","week","status","home_division","away_division"]:
    if c in candidate: keep.append(c)
p=candidate[keep].copy()
# Explicitly forbid outcomes/market/postgame result fields from projection.
forbidden_tokens=("point","score","winner","spread","moneyline","over_under","odds","bet")
bad=[c for c in p.columns if any(t in c.lower() for t in forbidden_tokens)]
if bad: raise SystemExit("forbidden projection columns: "+",".join(bad))
if p["game_id"].isna().any() or p["game_id"].duplicated().any(): raise SystemExit("bad game_id")
if p["start_date"].isna().any(): raise SystemExit("missing start_date")
if p["home_team"].isna().any() or p["away_team"].isna().any(): raise SystemExit("missing team")
p=p.sort_values(["start_date","game_id"])
proj=out/"phase4_2025_outcome_blind_schedule_projection_v1_148.csv"
p.to_csv(proj,index=False)
proj_sha=hashlib.sha256(proj.read_bytes()).hexdigest()
meta={
 "status":"PASS" if len(p)==762 else "RECONCILIATION_REQUIRED",
 "source_repo":"sportsdataverse/cfbfastR-cfb-data",
 "source_path":"cfb/cfb_schedules/parquet/cfb_schedules_2025.parquet",
 "raw_sha256":raw_sha,
 "raw_rows_2025":int(len(x)),
 "fresh_diagnostic_population_rule":"season_type=regular AND completed AND home_division=fbs AND away_division=fbs",
 "fresh_candidate_rows":int(len(p)),
 "fresh_candidate_unique_game_ids":int(p.game_id.nunique()),
 "historical_authority_unique_admitted_ids":762,
 "count_delta_vs_historical":int(len(p)-762),
 "projection_columns":list(p.columns),
 "projection_sha256":proj_sha,
 "outcomes_scored":False,
 "model_fit_or_score_performed":False,
 "warning":"Fresh provider-division filter is diagnostic and is not declared equivalent to historical CBS membership authority."
}
(out/"manifest.json").write_text(json.dumps(meta,indent=2)+"\n")
print(json.dumps(meta,indent=2))
