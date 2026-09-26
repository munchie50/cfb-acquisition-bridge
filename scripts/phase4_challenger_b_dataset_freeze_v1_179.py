#!/usr/bin/env python3
import sys,json,hashlib
from pathlib import Path
import pandas as pd, numpy as np
feat,sched,out=map(Path,sys.argv[1:4]); out.mkdir(parents=True,exist_ok=True)
K=["season","game_id","team"]
m=pd.read_csv(feat/"challenger_b_mechanical_features_v1_172.csv",dtype={"game_id":str})
d=pd.read_csv(feat/"challenger_b_derived_features_v1_172.csv",dtype={"game_id":str})
l=pd.read_csv(feat/"challenger_b_feature_eligibility_ledger_v1_172.csv",dtype={"game_id":str})
ss=[pd.read_csv(sched/f"challenger_b_historical_schedule_{y}_v1_166.csv",dtype={"game_id":str}) for y in range(2016,2025)]
s=pd.concat(ss,ignore_index=True); s["start_date"]=pd.to_datetime(s.start_date,utc=True)
if len(s)!=7701 or s.game_id.nunique()!=7701 or s.duplicated(["season","game_id"]).any(): raise SystemExit("schedule population invariant")
if (s.season==2025).any(): raise SystemExit("2025 schedule exposure")
if len(l)!=15402 or l.game_id.nunique()!=7701 or l[K].duplicated().any(): raise SystemExit("eligibility ledger invariant")
if l.loc[~l.own_pbp_game_present.astype(bool),"game_id"].nunique()!=45: raise SystemExit("45-game PBP ledger mismatch")
if l.loc[l.newly_admitted_v1_158.astype(bool),"game_id"].nunique()!=1342: raise SystemExit("1342-game admission mismatch")
if m[K].duplicated().any() or d[K].duplicated().any(): raise SystemExit("duplicate feature key")
features=["points_for_per_game","points_against_per_game","offensive_scrimmage_plays_per_game","defensive_scrimmage_plays_per_game","offensive_yards_per_play","defensive_yards_per_play","rush_play_rate","pass_play_rate","rush_yards_per_play","pass_yards_per_play","interception_rate","rest_days","offensive_explosive_play_rate","defensive_explosive_play_rate","offensive_success_rate","defensive_success_rate_allowed","average_starting_yards_to_goal"]
x=m.merge(d[K+[c for c in features if c in d.columns]+["derived_history_complete"]],on=K,validate="one_to_one").merge(l[K+["population_class","competition_class","mechanical_history_complete","derived_history_complete","qualified_prior_games","own_pbp_game_present","newly_admitted_v1_158"]],on=K,validate="one_to_one",suffixes=("","_ledger"))
rows=[]; ledger=[]
for _,g in s.sort_values(["season","start_date","game_id"]).iterrows():
 h=x[(x.season==g.season)&(x.game_id==g.game_id)&(x.team==g.home_team)]
 a=x[(x.season==g.season)&(x.game_id==g.game_id)&(x.team==g.away_team)]
 reasons=[]
 if len(h)!=1: reasons.append("home_feature_identity")
 if len(a)!=1: reasons.append("away_feature_identity")
 if pd.isna(g.home_points) or pd.isna(g.away_points): reasons.append("target_missing")
 if pd.isna(g.neutral_site): reasons.append("venue_missing")
 for side,z in [("home",h),("away",a)]:
  if len(z)==1:
   if int(z.iloc[0].qualified_prior_games)==0: reasons.append(side+"_opening_no_prior")
   if not bool(z.iloc[0].mechanical_history_complete): reasons.append(side+"_mechanical_history_incomplete")
   if not bool(z.iloc[0].derived_history_complete_ledger): reasons.append(side+"_derived_history_incomplete")
   if z[features].isna().any(axis=None): reasons.append(side+"_required_feature_na")
 base={"season":int(g.season),"game_id":g.game_id,"start_date":g.start_date.isoformat(),"home_team":g.home_team,"away_team":g.away_team,"population_class":g.population_class,"competition_class":g.competition_class}
 if reasons:
  base["reasons"]="|".join(sorted(set(reasons))); ledger.append(base); continue
 rec=base|{"venue_state":"NEUTRAL" if bool(g.neutral_site) else "HOME","target_home_margin":float(g.home_points)-float(g.away_points),"target_total_points":float(g.home_points)+float(g.away_points),"target_home_win":int(float(g.home_points)>float(g.away_points))}
 for f in features: rec["home_"+f]=h.iloc[0][f]; rec["away_"+f]=a.iloc[0][f]
 rows.append(rec)
o=pd.DataFrame(rows); e=pd.DataFrame(ledger)
pred=[p+f for f in features for p in ("home_","away_")]
if len(pred)!=34 or o[pred].isna().any(axis=None): raise SystemExit("predictor invariant")
if o.duplicated(["season","game_id"]).any() or (o.season==2025).any(): raise SystemExit("output identity/2025 invariant")
bad=("spread","moneyline","market","odds","favorite","underdog","closing","consensus","clv")
if any(any(w in c.lower() for w in bad) for c in pred): raise SystemExit("market-like predictor")
if len(o)+len(e)!=7701: raise SystemExit("population accounting")
classes=s.groupby(["population_class","competition_class"]).size().rename("target_games").reset_index()
actual=pd.concat([o.assign(disposition="ELIGIBLE"),e.assign(disposition="EXCLUDED")]).groupby(["population_class","competition_class","disposition"]).size().rename("games").reset_index()
o.to_csv(out/"challenger_b_dataset_v1_179.csv",index=False); e.to_csv(out/"challenger_b_exclusion_ledger_v1_179.csv",index=False); classes.to_csv(out/"challenger_b_population_contract_v1_179.csv",index=False); actual.to_csv(out/"challenger_b_population_disposition_v1_179.csv",index=False)
config={"version":"v1.179","authority":["v1.124","v1.151","v1.173","v1.178"],"source_feature_artifact_id":10895523493,"source_feature_digest":"sha256:702930b2ba905c9f917acbc627d12342e8190cfb44a4c8afd1aee49fbf59e239","features_team_level":features,"numeric_predictors":pred,"categorical_predictor":"venue_state","targets":["target_home_margin","target_total_points","target_home_win"],"partitions":{"TRAIN":[2016,2017,2018,2019,2020,2021,2022],"SPENT_CORROBORATIVE":[2023,2024],"TEST_PROTECTED":[2025]},"lambda_grid":[0,0.0001,0.001,0.01,0.1,1,10,100]}
(out/"challenger_b_config_v1_179.json").write_text(json.dumps(config,indent=2,sort_keys=True)+"\n")
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
manifest={"status":"DATASET_FREEZE_EXECUTED_NOT_ACCEPTED","target_population_games":7701,"eligible_rows":len(o),"excluded_games":len(e),"rows_by_season":{str(k):int(v) for k,v in o.groupby("season").size().items()},"exclusions_by_season":{str(k):int(v) for k,v in e.groupby("season").size().items()},"source_pbp_missing_games":45,"newly_admitted_games":1342,"predictor_count_numeric":34,"2025_accessed":False,"fit_or_score":False,"sha256":{}}
for p in sorted(out.iterdir()): manifest["sha256"][p.name]=sha(p)
(out/"manifest_v1_179.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n")
print(json.dumps(manifest,indent=2,sort_keys=True))
