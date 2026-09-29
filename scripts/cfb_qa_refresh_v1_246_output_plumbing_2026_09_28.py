import pathlib,pandas as pd,numpy as np,hashlib,json,sys
fitp=pathlib.Path(sys.argv[1]); outp=pathlib.Path(sys.argv[2]); outp.mkdir(exist_ok=True)
src=pathlib.Path("scripts/phase4_challenger_b_2026_refresh_predict_v1_246.py").read_text()
a=src.index('pred=[p+f for f in features'); block=src[a:]
features=["points_for_per_game","points_against_per_game","offensive_scrimmage_plays_per_game","defensive_scrimmage_plays_per_game","offensive_yards_per_play","defensive_yards_per_play","rush_play_rate","pass_play_rate","rush_yards_per_play","pass_yards_per_play","interception_rate","rest_days","offensive_explosive_play_rate","defensive_explosive_play_rate","offensive_success_rate","defensive_success_rate_allowed","average_starting_yards_to_goal"]
rows=[]
for i in range(2):
 r={"season":2026,"game_id":f"out{i+1}","start_date":f"2026-10-0{i+1}T17:00:00+00:00","home_team":"Nebraska","away_team":"Purdue","population_class":"FBS_VS_FBS","venue_state":"NEUTRAL" if i else "HOME"}
 for j,f in enumerate(features): r["home_"+f]=float(j+1+i); r["away_"+f]=float(j+2+i)
 rows.append(r)
X=pd.DataFrame(rows)
E=pd.DataFrame([{"season":2026,"game_id":"out3","start_date":"2026-10-03T17:00:00+00:00","home_team":"Army","away_team":"Test NonFBS","population_class":"FBS_VS_NONFBS","venue_state":"HOME","reasons":"away_opening_no_prior"}])
A=pd.DataFrame([{"game_id":"out1","side":"home","team":"Nebraska","prior_games":2,"max_prior_kickoff":"2026-09-20T00:00:00+00:00","target_kickoff":"2026-10-01T17:00:00+00:00","own_game_excluded":True,"strict_chronology":True}])
L=pd.DataFrame([{"game_id":g,"side":s,"team":t,"target_kickoff":"2026-10-01T17:00:00+00:00","qualified_prior_games":2,"eligible":True,"reason":""} for g in ("out1","out2","out3") for s,t in (("home","Nebraska"),("away","Purdue"))])
S=pd.DataFrame([
{"season":2026,"game_id":"out1","start_date":pd.Timestamp("2026-10-01T17:00:00Z"),"home_team":"Nebraska","away_team":"Purdue","neutral_site":False,"population_class":"FBS_VS_FBS"},
{"season":2026,"game_id":"out2","start_date":pd.Timestamp("2026-10-02T17:00:00Z"),"home_team":"Nebraska","away_team":"Purdue","neutral_site":True,"population_class":"FBS_VS_FBS"},
{"season":2026,"game_id":"out3","start_date":pd.Timestamp("2026-10-03T17:00:00Z"),"home_team":"Army","away_team":"Test NonFBS","neutral_site":False,"population_class":"FBS_VS_NONFBS"}])
cutoff=pd.Timestamp("2026-09-28T12:00:00Z")
g={"pd":pd,"np":np,"hashlib":hashlib,"json":json,"features":features,"X":X,"E":E,"A":A,"L":L,"S":S,"cutoff":cutoff,"fitp":fitp,"outp":outp}
exec(compile(block,"v1_246_post_feature_block","exec"),g)
m=json.loads((outp/"manifest_v1_246.json").read_text())
assert (m["target_games"],m["eligible_predictions"],m["excluded_games"])==(3,2,1)
assert m["target_population"]=={"FBS_VS_FBS":2,"FBS_VS_NONFBS":1}
assert m["snapshot_type"]=="REFRESH_SNAPSHOT" and m["parent_lineage"]=="v1.216"
assert not m["fit_or_optimization_performed"] and not m["market_joined"] and not m["target_outcomes_joined"]
files=[p for p in outp.iterdir() if p.name!="manifest_v1_246.json"]
expected={p.name for p in files}
assert set(m["hashes"])==expected
assert len(files) in (5,6)
if len(files)==6:
 substrate=outp/"challenger_b_2026_refresh_team_side_substrate_v1_246.csv"
 ledger=outp/"challenger_b_2026_refresh_feature_eligibility_ledger_v1_246.csv"
 assert substrate.exists() and ledger.exists() and substrate.read_bytes()==ledger.read_bytes()
for p in files:
 assert m["hashes"][p.name]==hashlib.sha256(p.read_bytes()).hexdigest()
 if p.suffix==".csv":
  d=pd.read_csv(p); assert {"snapshot_type","snapshot_cutoff_utc"}.issubset(d.columns); assert set(d.snapshot_type)=={"REFRESH_SNAPSHOT"}
assert (outp/"manifest_v1_246.json").read_bytes().endswith(b"\n")
print("V1_246_OUTPUT_PLUMBING_PASS",3,2,1)
