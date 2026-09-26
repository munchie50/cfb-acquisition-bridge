#!/usr/bin/env python3
# v1.167 corrected schedule-first mechanical feature producer.
import sys,json
from pathlib import Path
import pandas as pd, pyreadr, numpy as np
hist=Path(sys.argv[1]); raw=Path(sys.argv[2]); out=Path(sys.argv[3]); out.mkdir(parents=True,exist_ok=True)
parts=[]; source_avail={}
def one(s): return s.fillna(0).eq(1)
for y in range(2016,2025):
 s=pd.read_csv(hist/f"challenger_b_historical_schedule_{y}_v1_166.csv",dtype={"game_id":str})
 s["start_date"]=pd.to_datetime(s.start_date,utc=True)
 p=next(iter(pyreadr.read_r(raw/f"pbp_{y}.rds").values())); p["game_id"]=p.game_id.astype(str).str.replace(r"\.0$","",regex=True)
 p=p[p.game_id.isin(set(s.game_id))].copy()
 source_avail[y]=set(p.game_id)
 sr=(one(p.rush)|one(p["pass"])|one(p.pass_attempt)) & ~one(p.punt)
 rr=sr&one(p.rush); pr=sr&(one(p["pass"])|one(p.pass_attempt)); ints=one(p.interception_thrown_stat)|one(p.interception_stat)
 yg=p.yards_gained.fillna(0)
 rows=[]
 for_game=p.assign(sr=sr.astype(int),rr=rr.astype(int),pr=pr.astype(int),yg_sr=yg*sr,yg_rr=yg*rr,yg_pr=yg*pr,pa=one(p.pass_attempt).astype(int),ints=ints.astype(int))
 off=for_game.groupby(["game_id","pos_team"],dropna=True).agg(off_plays=("sr","sum"),off_yards=("yg_sr","sum"),rush_plays=("rr","sum"),pass_plays=("pr","sum"),rush_yards=("yg_rr","sum"),pass_yards=("yg_pr","sum"),pass_attempts=("pa","sum"),interceptions=("ints","sum")).reset_index().rename(columns={"pos_team":"team"})
 de=for_game.groupby(["game_id","def_pos_team"],dropna=True).agg(def_plays=("sr","sum"),def_yards=("yg_sr","sum")).reset_index().rename(columns={"def_pos_team":"team"})
 prim=off.merge(de,on=["game_id","team"],how="outer").fillna(0)
 # explicit schedule target sides; own primitives may be absent but target row never disappears
 h=s.assign(team=s.home_team,venue=np.where(s.neutral_site,"NEUTRAL","HOME"),game_points_for=s.home_points,game_points_against=s.away_points)
 a=s.assign(team=s.away_team,venue=np.where(s.neutral_site,"NEUTRAL","AWAY"),game_points_for=s.away_points,game_points_against=s.home_points)
 t=pd.concat([h,a],ignore_index=True)
 t=t.merge(prim,on=["game_id","team"],how="left",validate="one_to_one")
 t["own_pbp_present"]=t.game_id.isin(source_avail[y])
 for c in ["off_plays","off_yards","rush_plays","pass_plays","rush_yards","pass_yards","pass_attempts","interceptions","def_plays","def_yards"]: t[c]=t[c].fillna(0)
 parts.append(t)
g=pd.concat(parts,ignore_index=True).sort_values(["season","team","start_date","game_id"])
features=[]
for (y,team),z in g.groupby(["season","team"],sort=False):
 z=z.sort_values(["start_date","game_id"]).copy()
 # v1.162 proved no equal kickoff ambiguity per team; strict earlier chronology.
 def lagcs(c): return z[c].cumsum().shift(1,fill_value=0)
 prior=np.arange(len(z)); safe=lambda n,d: n.where(d.ne(0),np.nan)/d.where(d.ne(0),np.nan)
 f=pd.DataFrame({"season":z.season,"game_id":z.game_id,"team":team,"start_date":z.start_date,"home_away_neutral":z.venue,"qualified_prior_games":prior,
 "points_for_per_game":safe(lagcs("game_points_for"),pd.Series(prior,index=z.index)),
 "points_against_per_game":safe(lagcs("game_points_against"),pd.Series(prior,index=z.index)),
 "offensive_scrimmage_plays_per_game":safe(lagcs("off_plays"),pd.Series(prior,index=z.index)),
 "defensive_scrimmage_plays_per_game":safe(lagcs("def_plays"),pd.Series(prior,index=z.index)),
 "offensive_yards_per_play":safe(lagcs("off_yards"),lagcs("off_plays")),"defensive_yards_per_play":safe(lagcs("def_yards"),lagcs("def_plays")),
 "rush_play_rate":safe(lagcs("rush_plays"),lagcs("off_plays")),"pass_play_rate":safe(lagcs("pass_plays"),lagcs("off_plays")),
 "rush_yards_per_play":safe(lagcs("rush_yards"),lagcs("rush_plays")),"pass_yards_per_play":safe(lagcs("pass_yards"),lagcs("pass_plays")),
 "interception_rate":safe(lagcs("interceptions"),lagcs("pass_attempts")),
 "rest_days":z.start_date.diff().dt.total_seconds()/86400,"own_pbp_present":z.own_pbp_present})
 features.append(f)
feat=pd.concat(features,ignore_index=True)
assert len(feat)==15402 and feat[["season","game_id","team"]].duplicated().sum()==0 and not (feat.season==2025).any()
g.to_csv(out/"challenger_b_mechanical_primitives_v1_167.csv",index=False); feat.to_csv(out/"challenger_b_mechanical_features_v1_167.csv",index=False)
m={"status":"DIAGNOSTIC_PASS","target_team_sides":len(feat),"target_games":feat.game_id.nunique(),"own_pbp_missing_team_sides":int((~feat.own_pbp_present).sum()),"2025_accessed":False,"fit_or_score":False}
(out/"manifest_v1_167.json").write_text(json.dumps(m,indent=2)+"\n"); print(json.dumps(m,indent=2))
