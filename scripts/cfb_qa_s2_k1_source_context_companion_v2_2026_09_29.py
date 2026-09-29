#!/usr/bin/env python3
# QA-only S2_K1 source-context companion v2. Corrected recovered v1.172 primitive semantics; no S2 predictions.
import sys,json,hashlib
from pathlib import Path
import pandas as pd, numpy as np, pyreadr
schedp,rawp,pbpp,outp=map(Path,sys.argv[1:5]); cutoff=pd.Timestamp(sys.argv[5]); outp.mkdir(parents=True,exist_ok=True)
S=pd.read_csv(schedp,dtype={"game_id":str});S["start_date"]=pd.to_datetime(S.start_date,utc=True)
R=pd.read_parquet(rawp);R["game_id"]=R.game_id.astype(str).str.replace(r"\.0$","",regex=True);R["start_date"]=pd.to_datetime(R.start_date,utc=True);R=R[(R.season.astype(int)==2026)&(R.start_date<cutoff)].copy()
P=next(iter(pyreadr.read_r(pbpp).values()));P["game_id"]=P.game_id.astype(str).str.replace(r"\.0$","",regex=True);P["pos_team"]=P.pos_team.replace({"Savannah St":"Savannah State","St. Francis (PA)":"Saint Francis"});P["def_pos_team"]=P.def_pos_team.replace({"Savannah St":"Savannah State","St. Francis (PA)":"Saint Francis"})
if (S.start_date<=cutoff).any():raise SystemExit("target not future")
one=lambda x:x.fillna(0).eq(1);pids=set(P.game_id.unique())
sr=(one(P.rush)|one(P["pass"])|one(P.pass_attempt))&~one(P.punt);rr=sr&one(P.rush);pr=sr&(one(P["pass"])|one(P.pass_attempt));ints=one(P.interception_thrown_stat)|one(P.interception_stat);yg=P.yards_gained.fillna(0)
q=P.assign(sr=sr.astype(int),rr=rr.astype(int),pr=pr.astype(int),yg_sr=yg*sr,yg_rr=yg*rr,yg_pr=yg*pr,pa=one(P.pass_attempt).astype(int),ints=ints.astype(int))
off=q.groupby(["game_id","pos_team"],dropna=True).agg(off_plays=("sr","sum"),off_yards=("yg_sr","sum"),rush_plays=("rr","sum"),pass_plays=("pr","sum"),rush_yards=("yg_rr","sum"),pass_yards=("yg_pr","sum"),pass_attempts=("pa","sum"),interceptions=("ints","sum")).reset_index().rename(columns={"pos_team":"team"})
de=q.groupby(["game_id","def_pos_team"],dropna=True).agg(def_plays=("sr","sum"),def_yards=("yg_sr","sum")).reset_index().rename(columns={"def_pos_team":"team"});mp=off.merge(de,on=["game_id","team"],how="outer")
scr=sr&P.yards_gained.notna();sq=scr&P["down"].notna()&P.distance.notna()&P.distance.gt(0)&P["down"].isin([1,2,3,4]);succ=sq&(((P["down"]==1)&(P.yards_gained>=.5*P.distance))|((P["down"]==2)&(P.yards_gained>=.7*P.distance))|(P["down"].isin([3,4])&(P.yards_gained>=P.distance)))
dq=q.assign(scr=scr.astype(int),exp=(scr&(P.yards_gained>=20)).astype(int),succq=sq.astype(int),succ=succ.astype(int))
do=dq.groupby(["game_id","pos_team"],dropna=True).agg(off_scr=("scr","sum"),off_exp=("exp","sum"),off_succ_q=("succq","sum"),off_succ=("succ","sum")).reset_index().rename(columns={"pos_team":"team"})
dd=dq.groupby(["game_id","def_pos_team"],dropna=True).agg(def_scr=("scr","sum"),def_exp=("exp","sum"),def_succ_q=("succq","sum"),def_succ=("succ","sum")).reset_index().rename(columns={"def_pos_team":"team"});dp=do.merge(dd,on=["game_id","team"],how="outer")
for c in ["off_scr","off_exp","off_succ_q","off_succ","def_scr","def_exp","def_succ_q","def_succ"]:
 if c in dp:dp[c]=dp[c].fillna(0)
drive=P[P.pos_team.notna()&P.drive_id.notna()&P.yards_to_goal.notna()][["game_id","pos_team","drive_id","yards_to_goal"]].copy();drive["ord"]=np.arange(len(drive));drive=drive.sort_values(["game_id","pos_team","drive_id","ord"]).drop_duplicates(["game_id","pos_team","drive_id"])
fd=drive.groupby(["game_id","pos_team"]).yards_to_goal.agg(["sum","count"]).reset_index().rename(columns={"pos_team":"team","sum":"start_ytg_sum","count":"start_drive_n"});dp=dp.merge(fd,on=["game_id","team"],how="left");dp["start_ytg_sum"]=dp.start_ytg_sum.fillna(0);dp["start_drive_n"]=dp.start_drive_n.fillna(0)
h=R.assign(team=R.home_team,game_points_for=R.home_points,game_points_against=R.away_points);a=R.assign(team=R.away_team,game_points_for=R.away_points,game_points_against=R.home_points);t=pd.concat([h,a],ignore_index=True);t["pbp_game_present"]=t.game_id.isin(pids)
mm=t.merge(mp,on=["game_id","team"],how="left",validate="one_to_one");dm=t.merge(dp,on=["game_id","team"],how="left",validate="one_to_one")
mr=["off_plays","off_yards","rush_plays","pass_plays","rush_yards","pass_yards","pass_attempts","interceptions","def_plays","def_yards"];dr=["off_scr","off_exp","off_succ_q","off_succ","def_scr","def_exp","def_succ_q","def_succ","start_ytg_sum","start_drive_n"]
mm["mechanical_primitive_complete"]=mm[mr].notna().all(axis=1);dm["derived_primitive_complete"]=dm[dr].notna().all(axis=1)
key=["season","game_id","team"]; 
if mm[key].duplicated().any() or dm[key].duplicated().any() or mm.duplicated(["season","team","start_date"]).any():raise SystemExit("primitive identity/chronology")
def safe(n,d):return n.where(d.ne(0),np.nan)/d.where(d.ne(0),np.nan)
mech=[];der=[]
for _,z in mm.sort_values(["team","start_date"]).groupby("team",sort=False):
 z=z.sort_values("start_date").copy();prior=np.arange(len(z));den=pd.Series(prior,index=z.index);cs=lambda c:z[c].fillna(0).cumsum().shift(1,fill_value=0);ok=((~z.pbp_game_present)|(~z.mechanical_primitive_complete)).astype(int).cumsum().shift(1,fill_value=0).eq(0)
 f=pd.DataFrame({"season":z.season,"game_id":z.game_id,"team":z.team,"start_date":z.start_date,"qualified_prior_games":prior,"mechanical_history_complete":ok,"points_for_per_game":safe(z.game_points_for.cumsum().shift(1,fill_value=0),den),"points_against_per_game":safe(z.game_points_against.cumsum().shift(1,fill_value=0),den),"offensive_scrimmage_plays_per_game":safe(cs("off_plays"),den),"defensive_scrimmage_plays_per_game":safe(cs("def_plays"),den),"offensive_yards_per_play":safe(cs("off_yards"),cs("off_plays")),"defensive_yards_per_play":safe(cs("def_yards"),cs("def_plays")),"rush_play_rate":safe(cs("rush_plays"),cs("off_plays")),"pass_play_rate":safe(cs("pass_plays"),cs("off_plays")),"rush_yards_per_play":safe(cs("rush_yards"),cs("rush_plays")),"pass_yards_per_play":safe(cs("pass_yards"),cs("pass_plays")),"interception_rate":safe(cs("interceptions"),cs("pass_attempts")),"rest_days":z.start_date.diff().dt.total_seconds()/86400})
 for c in ["offensive_scrimmage_plays_per_game","defensive_scrimmage_plays_per_game","offensive_yards_per_play","defensive_yards_per_play","rush_play_rate","pass_play_rate","rush_yards_per_play","pass_yards_per_play","interception_rate"]:f.loc[~ok,c]=np.nan
 mech.append(f)
for _,z in dm.sort_values(["team","start_date"]).groupby("team",sort=False):
 z=z.sort_values("start_date").copy();prior=np.arange(len(z));cs=lambda c:z[c].fillna(0).cumsum().shift(1,fill_value=0);ok=((~z.pbp_game_present)|(~z.derived_primitive_complete)).astype(int).cumsum().shift(1,fill_value=0).eq(0)
 f=pd.DataFrame({"season":z.season,"game_id":z.game_id,"team":z.team,"start_date":z.start_date,"qualified_prior_games":prior,"derived_history_complete":ok,"offensive_explosive_play_rate":safe(cs("off_exp"),cs("off_scr")),"defensive_explosive_play_rate":safe(cs("def_exp"),cs("def_scr")),"offensive_success_rate":safe(cs("off_succ"),cs("off_succ_q")),"defensive_success_rate_allowed":safe(cs("def_succ"),cs("def_succ_q")),"average_starting_yards_to_goal":safe(cs("start_ytg_sum"),cs("start_drive_n"))})
 for c in ["offensive_explosive_play_rate","defensive_explosive_play_rate","offensive_success_rate","defensive_success_rate_allowed","average_starting_yards_to_goal"]:f.loc[~ok,c]=np.nan
 der.append(f)
mf=pd.concat(mech,ignore_index=True);df=pd.concat(der,ignore_index=True);side=mf.merge(df,on=key+["start_date","qualified_prior_games"],validate="one_to_one")
COMP={"points_for_per_game":("M","game_points_for","GAME"),"points_against_per_game":("M","game_points_against","GAME"),"offensive_scrimmage_plays_per_game":("M","off_plays","GAME"),"defensive_scrimmage_plays_per_game":("M","def_plays","GAME"),"offensive_yards_per_play":("M","off_yards","off_plays"),"defensive_yards_per_play":("M","def_yards","def_plays"),"rush_play_rate":("M","rush_plays","off_plays"),"pass_play_rate":("M","pass_plays","off_plays"),"rush_yards_per_play":("M","rush_yards","rush_plays"),"pass_yards_per_play":("M","pass_yards","pass_plays"),"interception_rate":("M","interceptions","pass_attempts"),"offensive_explosive_play_rate":("D","off_exp","off_scr"),"defensive_explosive_play_rate":("D","def_exp","def_scr"),"offensive_success_rate":("D","off_succ","off_succ_q"),"defensive_success_rate_allowed":("D","def_succ","def_succ_q"),"average_starting_yards_to_goal":("D","start_ytg_sum","start_drive_n")}
MAP={"points_for_per_game":"points_against_per_game","points_against_per_game":"points_for_per_game","offensive_scrimmage_plays_per_game":"defensive_scrimmage_plays_per_game","defensive_scrimmage_plays_per_game":"offensive_scrimmage_plays_per_game","offensive_yards_per_play":"defensive_yards_per_play","defensive_yards_per_play":"offensive_yards_per_play","offensive_explosive_play_rate":"defensive_explosive_play_rate","defensive_explosive_play_rate":"offensive_explosive_play_rate","offensive_success_rate":"defensive_success_rate_allowed","defensive_success_rate_allowed":"offensive_success_rate"}
def baseline(f,tm):
 cut=pd.Timestamp(tm).normalize()
 if f=="rest_days":
  z=side[(side.start_date<cut)&side.rest_days.notna()];return np.nan if z.empty else float(z.rest_days.mean())
 typ,num,den=COMP[f];src=mm if typ=="M" else dm;flag="mechanical_primitive_complete" if typ=="M" else "derived_primitive_complete";z=src[(src.start_date<cut)&src[flag]]
 if z.empty:return np.nan
 n=float(z[num].sum());d=float(len(z)) if den=="GAME" else float(z[den].sum());return np.nan if (not np.isfinite(n)) or (not np.isfinite(d)) or d<=0 else n/d
idx=side.set_index(["game_id","team"],drop=False);rows=[]
for g in S.sort_values(["start_date","game_id"]).itertuples():
 for role,team in (("home",g.home_team),("away",g.away_team)):
  prior=mm[(mm.team==team)&(mm.start_date<g.start_date)&(mm.start_date<cutoff)].sort_values("start_date")
  for src in prior.itertuples():
   opp=src.away_team if team==src.home_team else src.home_team
   k=(src.game_id,opp)
   if k not in idx.index:raise SystemExit("missing opponent state")
   o=idx.loc[k]
   rec={"target_game_id":g.game_id,"target_side":role,"target_team":team,"target_kickoff":g.start_date.isoformat(),"source_game_id":src.game_id,"source_kickoff":src.start_date.isoformat(),"source_opponent":opp,"opponent_qualified_prior_games":int(o.qualified_prior_games),"mechanical_history_complete":bool(o.mechanical_history_complete),"derived_history_complete":bool(o.derived_history_complete)}
   for f,pair in MAP.items():
    b=baseline(pair,o.start_date);raw=o[pair];rec["baseline__"+pair]=b;rec["raw__"+pair]=raw;rec["context_valid__"+f]=bool(np.isfinite(b) and (int(o.qualified_prior_games)==0 or ((bool(o.mechanical_history_complete) and bool(o.derived_history_complete)) and np.isfinite(raw))))
   rows.append(rec)
C=pd.DataFrame(rows);C["snapshot_type"]="S2_K1_SOURCE_CONTEXT";C["snapshot_cutoff_utc"]=cutoff.isoformat()
for name,d in [("mechanical_primitives",mm),("derived_primitives",dm),("source_context",C)]:
 op=outp/(name+".csv");d.to_csv(op,index=False)
manifest={"status":"EXECUTED_NOT_ACCEPTED","s2_predictions_produced":False,"target_outcomes_joined":False,"market_joined":False,"primitive_ancestry_blob":"37c05aba201d3c2935b5d2b646437552949766fd","rows":{"mechanical":len(mm),"derived":len(dm),"context":len(C)},"hashes":{}}
for p in sorted(outp.glob("*.csv")):manifest["hashes"][p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
(outp/"manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n");print(json.dumps(manifest,indent=2))
