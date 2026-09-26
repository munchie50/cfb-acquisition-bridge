#!/usr/bin/env python3
# v1.172 corrected full feature substrate: proven PBP aliases + frozen v1.115 derived semantics.
import sys,json
from pathlib import Path
import pandas as pd, pyreadr, numpy as np
hist,raw,old,miss,out=map(Path,sys.argv[1:6]); out.mkdir(parents=True,exist_ok=True)
missing_ids=set(pd.read_csv(miss,dtype={"game_id":str}).game_id)
mech_parts=[]; der_parts=[]
def one(s): return s.fillna(0).eq(1)
for y in range(2016,2025):
 s=pd.read_csv(hist/f"challenger_b_historical_schedule_{y}_v1_166.csv",dtype={"game_id":str})
 s["start_date"]=pd.to_datetime(s.start_date,utc=True)
 p=next(iter(pyreadr.read_r(raw/f"pbp_{y}.rds").values()))
 p["game_id"]=p.game_id.astype(str).str.replace(r"\.0$","",regex=True)
 p=p[p.game_id.isin(set(s.game_id))].copy()\n # v1.171 proved exact raw-PBP aliases for these schedule identities.\n p["pos_team"]=p.pos_team.replace({"Savannah St":"Savannah State","St. Francis (PA)":"Saint Francis"})\n p["def_pos_team"]=p.def_pos_team.replace({"Savannah St":"Savannah State","St. Francis (PA)":"Saint Francis"})
 sr=(one(p.rush)|one(p["pass"])|one(p.pass_attempt)) & ~one(p.punt)
 rr=sr&one(p.rush); pr=sr&(one(p["pass"])|one(p.pass_attempt)); ints=one(p.interception_thrown_stat)|one(p.interception_stat)
 yg=p.yards_gained.fillna(0)
 q=p.assign(sr=sr.astype(int),rr=rr.astype(int),pr=pr.astype(int),yg_sr=yg*sr,yg_rr=yg*rr,yg_pr=yg*pr,pa=one(p.pass_attempt).astype(int),ints=ints.astype(int))
 off=q.groupby(["game_id","pos_team"],dropna=True).agg(off_plays=("sr","sum"),off_yards=("yg_sr","sum"),rush_plays=("rr","sum"),pass_plays=("pr","sum"),rush_yards=("yg_rr","sum"),pass_yards=("yg_pr","sum"),pass_attempts=("pa","sum"),interceptions=("ints","sum")).reset_index().rename(columns={"pos_team":"team"})
 de=q.groupby(["game_id","def_pos_team"],dropna=True).agg(def_plays=("sr","sum"),def_yards=("yg_sr","sum")).reset_index().rename(columns={"def_pos_team":"team"})
 mp=off.merge(de,on=["game_id","team"],how="outer")
 scr=sr & p.yards_gained.notna()
 succq=scr & p["down"].notna() & p.distance.notna() & p.distance.gt(0) & p["down"].isin([1,2,3,4])
 succ=succq & (((p["down"]==1)&(p.yards_gained>=.5*p.distance))|((p["down"]==2)&(p.yards_gained>=.7*p.distance))|(p["down"].isin([3,4])&(p.yards_gained>=p.distance)))
 dq=q.assign(scr=scr.astype(int),exp=(scr&(p.yards_gained>=20)).astype(int),succq=succq.astype(int),succ=succ.astype(int))
 do=dq.groupby(["game_id","pos_team"],dropna=True).agg(off_scr=("scr","sum"),off_exp=("exp","sum"),off_succ_q=("succq","sum"),off_succ=("succ","sum")).reset_index().rename(columns={"pos_team":"team"})
 dd=dq.groupby(["game_id","def_pos_team"],dropna=True).agg(def_scr=("scr","sum"),def_exp=("exp","sum"),def_succ_q=("succq","sum"),def_succ=("succ","sum")).reset_index().rename(columns={"def_pos_team":"team"})
 dp=do.merge(dd,on=["game_id","team"],how="outer")\n # Frozen v1.115 establishes team/game by scrimmage participation, then zero-fills absent aggregate event counts.\n der_counts=["off_scr","off_exp","off_succ_q","off_succ","def_scr","def_exp","def_succ_q","def_succ"]\n for c in der_counts:\n  if c in dp: dp[c]=dp[c].fillna(0)
 drive=p[p.pos_team.notna()&p.drive_id.notna()&p.yards_to_goal.notna()][["game_id","pos_team","drive_id","yards_to_goal"]].copy()
 drive["ord"]=np.arange(len(drive)); drive=drive.sort_values(["game_id","pos_team","drive_id","ord"]).drop_duplicates(["game_id","pos_team","drive_id"])
 fd=drive.groupby(["game_id","pos_team"]).yards_to_goal.agg(["sum","count"]).reset_index().rename(columns={"pos_team":"team","sum":"start_ytg_sum","count":"start_drive_n"})
 dp=dp.merge(fd,on=["game_id","team"],how="left")\n dp["start_ytg_sum"]=dp.start_ytg_sum.fillna(0); dp["start_drive_n"]=dp.start_drive_n.fillna(0)
 h=s.assign(team=s.home_team,venue=np.where(s.neutral_site,"NEUTRAL","HOME"),game_points_for=s.home_points,game_points_against=s.away_points)
 a=s.assign(team=s.away_team,venue=np.where(s.neutral_site,"NEUTRAL","AWAY"),game_points_for=s.away_points,game_points_against=s.home_points)
 t=pd.concat([h,a],ignore_index=True)
 t["pbp_game_present"]=~t.game_id.isin(missing_ids)
 mm=t.merge(mp,on=["game_id","team"],how="left",validate="one_to_one")
 dm=t.merge(dp,on=["game_id","team"],how="left",validate="one_to_one")
 mech_req=["off_plays","off_yards","rush_plays","pass_plays","rush_yards","pass_yards","pass_attempts","interceptions","def_plays","def_yards"]
 der_req=["off_scr","off_exp","off_succ_q","off_succ","def_scr","def_exp","def_succ_q","def_succ","start_ytg_sum","start_drive_n"]
 mm["mechanical_primitive_complete"]=mm[mech_req].notna().all(axis=1)
 dm["derived_primitive_complete"]=dm[der_req].notna().all(axis=1)
 mech_parts.append(mm); der_parts.append(dm)
mraw=pd.concat(mech_parts,ignore_index=True); draw=pd.concat(der_parts,ignore_index=True)
key=["season","game_id","team"]; assert len(mraw)==15402 and len(draw)==15402 and not mraw[key].duplicated().any() and not draw[key].duplicated().any()
assert not (mraw.season==2025).any()
# no same-team equal kickoff ambiguity; strict chronology is therefore explicit and deterministic
assert not mraw.duplicated(["season","team","start_date"]).any()
def safe(n,d): return n.where(d.ne(0),np.nan)/d.where(d.ne(0),np.nan)
mech=[]; der=[]
for (y,team),z in mraw.sort_values(["season","team","start_date"]).groupby(["season","team"],sort=False):
 z=z.sort_values("start_date").copy(); prior=np.arange(len(z)); idx=z.index
 def cs(c): return z[c].fillna(0).cumsum().shift(1,fill_value=0)
 missing_game=(~z.pbp_game_present).astype(int).cumsum().shift(1,fill_value=0)
 missing_primitive=(~z.mechanical_primitive_complete).astype(int).cumsum().shift(1,fill_value=0)
 missing=((~z.pbp_game_present) | (~z.mechanical_primitive_complete)).astype(int).cumsum().shift(1,fill_value=0)
 hist_ok=missing.eq(0); denom=pd.Series(prior,index=idx)
 f=pd.DataFrame({"season":z.season,"game_id":z.game_id,"team":team,"start_date":z.start_date,"home_away_neutral":z.venue,
 "qualified_prior_games":prior,"missing_prior_pbp_games":missing_game.astype(int),"missing_prior_mechanical_primitive_sources":missing_primitive.astype(int),"missing_prior_mechanical_source_games":missing.astype(int),"mechanical_history_complete":hist_ok,
 "points_for_per_game":safe(z.game_points_for.cumsum().shift(1,fill_value=0),denom),
 "points_against_per_game":safe(z.game_points_against.cumsum().shift(1,fill_value=0),denom),
 "offensive_scrimmage_plays_per_game":safe(cs("off_plays"),denom),"defensive_scrimmage_plays_per_game":safe(cs("def_plays"),denom),
 "offensive_yards_per_play":safe(cs("off_yards"),cs("off_plays")),"defensive_yards_per_play":safe(cs("def_yards"),cs("def_plays")),
 "rush_play_rate":safe(cs("rush_plays"),cs("off_plays")),"pass_play_rate":safe(cs("pass_plays"),cs("off_plays")),
 "rush_yards_per_play":safe(cs("rush_yards"),cs("rush_plays")),"pass_yards_per_play":safe(cs("pass_yards"),cs("pass_plays")),
 "interception_rate":safe(cs("interceptions"),cs("pass_attempts")),"rest_days":z.start_date.diff().dt.total_seconds()/86400,
 "own_pbp_game_present":z.pbp_game_present,"own_mechanical_primitive_complete":z.mechanical_primitive_complete})
 pbpcols=["offensive_scrimmage_plays_per_game","defensive_scrimmage_plays_per_game","offensive_yards_per_play","defensive_yards_per_play","rush_play_rate","pass_play_rate","rush_yards_per_play","pass_yards_per_play","interception_rate"]
 f.loc[~hist_ok,pbpcols]=np.nan; mech.append(f)
for (y,team),z in draw.sort_values(["season","team","start_date"]).groupby(["season","team"],sort=False):
 z=z.sort_values("start_date").copy(); prior=np.arange(len(z)); idx=z.index
 def cs(c): return z[c].fillna(0).cumsum().shift(1,fill_value=0)
 missing_game=(~z.pbp_game_present).astype(int).cumsum().shift(1,fill_value=0); missing_primitive=(~z.derived_primitive_complete).astype(int).cumsum().shift(1,fill_value=0); missing=((~z.pbp_game_present) | (~z.derived_primitive_complete)).astype(int).cumsum().shift(1,fill_value=0); hist_ok=missing.eq(0)
 f=pd.DataFrame({"season":z.season,"game_id":z.game_id,"team":team,"start_date":z.start_date,"qualified_prior_games":prior,
 "missing_prior_pbp_games":missing_game.astype(int),"missing_prior_derived_primitive_sources":missing_primitive.astype(int),"missing_prior_derived_source_games":missing.astype(int),"derived_history_complete":hist_ok,
 "offensive_explosive_play_rate":safe(cs("off_exp"),cs("off_scr")),"defensive_explosive_play_rate":safe(cs("def_exp"),cs("def_scr")),
 "offensive_success_rate":safe(cs("off_succ"),cs("off_succ_q")),"defensive_success_rate_allowed":safe(cs("def_succ"),cs("def_succ_q")),
 "average_starting_yards_to_goal":safe(cs("start_ytg_sum"),cs("start_drive_n")),
 "explosive_play_denominator":cs("off_scr"),"success_play_denominator":cs("off_succ_q"),"field_position_drive_denominator":cs("start_drive_n"),
 "own_pbp_game_present":z.pbp_game_present,"own_derived_primitive_complete":z.derived_primitive_complete})
 vals=["offensive_explosive_play_rate","defensive_explosive_play_rate","offensive_success_rate","defensive_success_rate_allowed","average_starting_yards_to_goal","explosive_play_denominator","success_play_denominator","field_position_drive_denominator"]
 f.loc[~hist_ok,vals]=np.nan; der.append(f)
mf=pd.concat(mech,ignore_index=True); df=pd.concat(der,ignore_index=True)
ledger=mraw[key+["start_date","population_class","competition_class"]].merge(mf[key+["qualified_prior_games","missing_prior_mechanical_source_games","mechanical_history_complete","own_pbp_game_present","own_mechanical_primitive_complete"]],on=key).merge(df[key+["missing_prior_derived_source_games","derived_history_complete","own_derived_primitive_complete"]],on=key)
legacy=pd.read_csv(old/"phase4_feature_canary_v1_109.csv",dtype={"game_id":str}); legacy_ids=set(legacy.game_id)
ledger["newly_admitted_v1_158"]=~ledger.game_id.isin(legacy_ids)
assert ledger.game_id.nunique()==7701 and ledger.loc[ledger.newly_admitted_v1_158,"game_id"].nunique()==1342
assert ledger.loc[~ledger.own_pbp_game_present,"game_id"].nunique()==45 and (~ledger.own_pbp_game_present).sum()==90
opening=ledger.qualified_prior_games.eq(0)
by=[]
for (season,pc),z in ledger.groupby(["season","population_class"]):
 by.append({"season":int(season),"population_class":pc,"target_team_sides":len(z),"opening_no_prior_sides":int((z.qualified_prior_games==0).sum()),"mechanical_history_incomplete_sides":int((~z.mechanical_history_complete).sum()),"derived_history_incomplete_sides":int((~z.derived_history_complete).sum()),"own_mechanical_primitive_missing_sides":int((~z.own_mechanical_primitive_complete).sum()),"newly_admitted_sides":int(z.newly_admitted_v1_158.sum())})
manifest={"status":"DIAGNOSTIC_COMPLETE","target_games":7701,"target_team_sides":15402,"newly_admitted_games":1342,
"opening_no_prior_team_sides":int(opening.sum()),"own_pbp_missing_games":int(ledger.loc[~ledger.own_pbp_game_present,"game_id"].nunique()),"own_pbp_missing_team_sides":int((~ledger.own_pbp_game_present).sum()),"team_side_primitive_unmaterialized_with_pbp_present":int((ledger.own_pbp_game_present & ~ledger.own_mechanical_primitive_complete).sum()),
"mechanical_history_incomplete_team_sides":int((~ledger.mechanical_history_complete).sum()),"derived_history_incomplete_team_sides":int((~ledger.derived_history_complete).sum()),
"by_season_population_class":by,"2025_accessed":False,"fit_or_score":False}
mraw.to_csv(out/"challenger_b_mechanical_primitives_v1_172.csv",index=False); mf.to_csv(out/"challenger_b_mechanical_features_v1_172.csv",index=False)
draw.to_csv(out/"challenger_b_derived_primitives_v1_172.csv",index=False); df.to_csv(out/"challenger_b_derived_features_v1_172.csv",index=False)
ledger.to_csv(out/"challenger_b_feature_eligibility_ledger_v1_172.csv",index=False)
(out/"manifest_v1_172.json").write_text(json.dumps(manifest,indent=2))
print(json.dumps(manifest,indent=2))
