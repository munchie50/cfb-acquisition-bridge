#!/usr/bin/env python3
# v1.204: source/cutoff preflight only. No model prediction.
import sys,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
import pandas as pd, pyreadr

schedp,pbpp,outp=map(Path,sys.argv[1:4]); outp.mkdir(parents=True,exist_ok=True)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
cutoff=datetime.now(timezone.utc)
R=pd.read_parquet(schedp); R["game_id"]=R.game_id.astype(str).str.replace(r"\.0$","",regex=True)
R["start_date"]=pd.to_datetime(R.start_date,utc=True)
R=R[R.season.astype(int)==2026].copy()
assert len(R)>0 and R.game_id.notna().all() and not R.game_id.duplicated().any() and R.start_date.notna().all()
P=next(iter(pyreadr.read_r(pbpp).values())); P["game_id"]=P.game_id.astype(str).str.replace(r"\.0$","",regex=True)
# Frozen 2025 accepted membership + 2026 v1.203 additions.
BASE2017=["Air Force","Akron","Alabama","Appalachian State","Arizona","Arizona State","Arkansas","Arkansas State","Army","Auburn","BYU","Ball State","Baylor","Boise State","Boston College","Bowling Green","Buffalo","California","Central Michigan","Charlotte","Cincinnati","Clemson","Coastal Carolina","Colorado","Colorado State","Duke","East Carolina","Eastern Michigan","FIU","Florida","Florida Atlantic","Florida State","Fresno State","Georgia","Georgia Southern","Georgia State","Georgia Tech","Hawaii","Houston","Idaho","Illinois","Indiana","Iowa","Iowa State","Kansas","Kansas State","Kent State","Kentucky","LSU","Louisiana","Louisiana Tech","Louisville","Marshall","Maryland","Memphis","Miami (FL)","Miami (OH)","Michigan","Michigan State","Middle Tennessee","Minnesota","Mississippi State","Missouri","NC State","Navy","Nebraska","Nevada","New Mexico","New Mexico State","North Carolina","North Texas","Northern Illinois","Northwestern","Notre Dame","Ohio","Ohio State","Oklahoma","Oklahoma State","Old Dominion","Ole Miss","Oregon","Oregon State","Penn State","Pittsburgh","Purdue","Rice","Rutgers","SMU","San Diego State","San Jose State","South Alabama","South Carolina","South Florida","Southern Miss","Stanford","Syracuse","TCU","Temple","Tennessee","Texas","Texas A&M","Texas State","Texas Tech","Toledo","Troy","Tulane","Tulsa","UAB","UCF","UCLA","UConn","UL Monroe","UMass","UNLV","USC","UTEP","UTSA","Utah","Utah State","Vanderbilt","Virginia","Virginia Tech","Wake Forest","Washington","Washington State","West Virginia","Western Kentucky","Western Michigan","Wisconsin","Wyoming"]
cur=set(BASE2017)
for add,rem in [({"Liberty"},{"Idaho"}),({"James Madison"},set()),({"Jacksonville State","Sam Houston"},set()),({"Kennesaw State"},set()),({"Delaware","Missouri State"},set()),({"North Dakota State","Sacramento State"},set())]: cur=(cur|add)-rem
assert len(cur)==138
aliases={"Hawai'i":"Hawaii","App State":"Appalachian State","San José State":"San Jose State","Massachusetts":"UMass","Florida International":"FIU","Miami":"Miami (FL)"}
canon=lambda x: aliases.get(str(x),str(x))
R["home_canonical"]=R.home_team.map(canon); R["away_canonical"]=R.away_team.map(canon)
R["home_fbs"]=R.home_canonical.isin(cur); R["away_fbs"]=R.away_canonical.isin(cur)
Q=R[R.home_fbs|R.away_fbs].copy()
Q["population_class"]=Q.apply(lambda r:"FBS_VS_FBS" if r.home_fbs and r.away_fbs else "FBS_VS_NONFBS",axis=1)
future=Q[Q.start_date>pd.Timestamp(cutoff)].copy()
spent=Q[Q.start_date<=pd.Timestamp(cutoff)].copy()
# PBP may lag live schedule; record rather than invent completeness.
pbp_ids=set(P.game_id.dropna().unique())
spent_completed=spent[spent.completed.fillna(False).astype(bool)] if "completed" in spent else spent.iloc[0:0]
missing_pbp=sorted(set(spent_completed.game_id)-pbp_ids)
keep=["season","game_id","start_date","home_team","away_team","neutral_site","population_class"]
F=future[keep].sort_values(["start_date","game_id"]).copy()
bad=("point","score","winner","spread","moneyline","over_under","odds","bet","post_win","postgame","market")
assert not [c for c in F if any(t in c.lower() for t in bad)]
F.to_csv(outp/"challenger_b_2026_future_target_projection_v1_204.csv",index=False)
report={"status":"PASS_SOURCE_PREFLIGHT","cutoff_utc":cutoff.isoformat(),"schedule_sha256":sha(schedp),"pbp_sha256":sha(pbpp),"raw_schedule_rows_2026":len(R),"qualified_relevant_fbs_rows":len(Q),"spent_at_cutoff":len(spent),"future_at_cutoff":len(F),"future_fbs_vs_fbs":int((future.population_class=="FBS_VS_FBS").sum()),"future_fbs_vs_nonfbs":int((future.population_class=="FBS_VS_NONFBS").sum()),"completed_spent_games":len(spent_completed),"completed_spent_missing_pbp":len(missing_pbp),"missing_pbp_game_ids":missing_pbp,"membership_count":138,"model_prediction_performed":False,"market_joined":False,"target_outcomes_projected":False}
(outp/"preflight_v1_204.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
print(json.dumps(report,indent=2))
