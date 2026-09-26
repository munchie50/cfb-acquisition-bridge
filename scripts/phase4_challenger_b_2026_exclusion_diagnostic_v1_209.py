#!/usr/bin/env python3
# v1.209: descriptive diagnosis of v1.206 exclusions; never changes predictions.
import sys,json
from pathlib import Path
import pandas as pd
art,raw,out=map(Path,sys.argv[1:4]); out.mkdir(parents=True,exist_ok=True)
L=pd.read_csv(art/"challenger_b_2026_feature_eligibility_ledger_v1_206.csv",dtype={"game_id":str})
M=json.load(open(art/"manifest_v1_206.json")); cutoff=pd.Timestamp(M["cutoff_utc"])
R=pd.read_parquet(raw); R["game_id"]=R.game_id.astype(str).str.replace(r"\.0$","",regex=True); R["start_date"]=pd.to_datetime(R.start_date,utc=True)
bad=L[(~L.eligible.astype(bool))&(L.reason=="prior_points_missing")].copy()
rows=[]
for x in bad.itertuples():
    prior=R[(R.start_date<cutoff)&(R.start_date<pd.Timestamp(x.target_kickoff))&((R.home_team==x.team)|(R.away_team==x.team))].sort_values("start_date")
    miss=prior[prior.home_points.isna()|prior.away_points.isna()]
    for g in miss.itertuples():
        rows.append({"target_game_id":x.game_id,"side":x.side,"team":x.team,"target_kickoff":x.target_kickoff,"prior_game_id":g.game_id,"prior_kickoff":g.start_date.isoformat(),"prior_home":g.home_team,"prior_away":g.away_team,"completed":getattr(g,"completed",None),"home_points":g.home_points,"away_points":g.away_points})
D=pd.DataFrame(rows).drop_duplicates()
D.to_csv(out/"prior_points_missing_trace_v1_209.csv",index=False)
report={"status":"DESCRIPTIVE_ONLY","affected_team_sides":len(bad),"unique_affected_targets":bad.game_id.nunique(),"missing_prior_rows":len(D),"unique_missing_prior_games":D.prior_game_id.nunique() if len(D) else 0,"completed_true":int(D.completed.fillna(False).astype(bool).sum()) if len(D) else 0,"completed_false_or_missing":int((~D.completed.fillna(False).astype(bool)).sum()) if len(D) else 0,"cutoff_utc":M["cutoff_utc"],"predictions_changed":False}
(out/"diagnostic_v1_209.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n"); print(json.dumps(report,indent=2))
