#!/usr/bin/env python3
# QA-only S2_K1 source-context companion. Does not produce S2 predictions.
import sys,json,hashlib
from pathlib import Path
import pandas as pd, numpy as np, pyreadr

schedp,raw_schedp,pbpp,outp=map(Path,sys.argv[1:5]); cutoff=pd.Timestamp(sys.argv[5]); outp.mkdir(parents=True,exist_ok=True)
S=pd.read_csv(schedp,dtype={"game_id":str}); S["start_date"]=pd.to_datetime(S.start_date,utc=True)
R=pd.read_parquet(raw_schedp); R["game_id"]=R.game_id.astype(str).str.replace(r"\.0$","",regex=True); R["start_date"]=pd.to_datetime(R.start_date,utc=True)
P=next(iter(pyreadr.read_r(pbpp).values())); P["game_id"]=P.game_id.astype(str).str.replace(r"\.0$","",regex=True)
P["pos_team"]=P.pos_team.replace({"Savannah St":"Savannah State","St. Francis (PA)":"Saint Francis"}); P["def_pos_team"]=P.def_pos_team.replace({"Savannah St":"Savannah State","St. Francis (PA)":"Saint Francis"})
if (S.start_date<=cutoff).any(): raise SystemExit("target not future")
bad=("spread","moneyline","over_under","odds","bet","market","postgame")
if any(any(x in c.lower() for x in bad) for c in S.columns): raise SystemExit("forbidden target field")
one=lambda s:s.fillna(0).eq(1)
def side_state(team,t):
    h=R[(R.start_date<cutoff)&(R.start_date<t)&((R.home_team==team)|(R.away_team==team))].sort_values("start_date")
    ids=h.game_id.tolist()
    if not ids:return {"qualified_prior_games":0},None
    if h.home_points.isna().any() or h.away_points.isna().any():return None,"prior_points_missing"
    pp=P[P.game_id.isin(ids)].copy()
    if set(pp.game_id.unique())!=set(ids):return None,"prior_pbp_missing"
    sr=(one(pp.rush)|one(pp["pass"])|one(pp.pass_attempt))&~one(pp.punt); off=pp.pos_team.eq(team); de=pp.def_pos_team.eq(team); rr=sr&one(pp.rush); pr=sr&(one(pp["pass"])|one(pp.pass_attempt)); yg=pp.yards_gained.fillna(0)
    vals={"qualified_prior_games":len(ids)}
    ptsf=np.where(h.home_team==team,h.home_points,h.away_points).astype(float); ptsa=np.where(h.home_team==team,h.away_points,h.home_points).astype(float)
    offplays=int((sr&off).sum());defplays=int((sr&de).sum());rushplays=int((rr&off).sum());passplays=int((pr&off).sum());passatt=int((one(pp.pass_attempt)&off).sum());ints=int(((one(pp.interception_thrown_stat)|one(pp.interception_stat))&off).sum())
    offyards=float((yg*(sr&off)).sum());defyards=float((yg*(sr&de)).sum());rushyards=float((yg*(rr&off)).sum());passyards=float((yg*(pr&off)).sum())
    scr=sr&pp.yards_gained.notna();sq=scr&pp["down"].notna()&pp.distance.notna()&pp.distance.gt(0)&pp["down"].isin([1,2,3,4]);succ=sq&(((pp["down"]==1)&(pp.yards_gained>=.5*pp.distance))|((pp["down"]==2)&(pp.yards_gained>=.7*pp.distance))|(pp["down"].isin([3,4])&(pp.yards_gained>=pp.distance)))
    os=int((scr&off).sum());ds=int((scr&de).sum());oe=int((scr&off&(pp.yards_gained>=20)).sum());de_=int((scr&de&(pp.yards_gained>=20)).sum());oq=int((sq&off).sum());dq=int((sq&de).sum());osu=int((succ&off).sum());dsu=int((succ&de).sum())
    drive=pp[pp.pos_team.eq(team)&pp.drive_id.notna()&pp.yards_to_goal.notna()][["game_id","drive_id","yards_to_goal"]].copy();drive["ord"]=np.arange(len(drive));drive=drive.sort_values(["game_id","drive_id","ord"]).drop_duplicates(["game_id","drive_id"])
    nums=[ptsf.sum(),ptsa.sum(),offplays,defplays,offyards,defyards,rushplays,passplays,rushyards,passyards,ints,oe,de_,osu,dsu,float(drive.yards_to_goal.sum())]
    dens=[len(ids),len(ids),len(ids),len(ids),offplays,defplays,offplays,offplays,rushplays,passplays,passatt,os,ds,oq,dq,len(drive)]
    names=["points_for_per_game","points_against_per_game","offensive_scrimmage_plays_per_game","defensive_scrimmage_plays_per_game","offensive_yards_per_play","defensive_yards_per_play","rush_play_rate","pass_play_rate","rush_yards_per_play","pass_yards_per_play","interception_rate","offensive_explosive_play_rate","defensive_explosive_play_rate","offensive_success_rate","defensive_success_rate_allowed","average_starting_yards_to_goal"]
    if any(d<=0 for d in dens):return None,"required_feature_na"
    vals.update({n:float(a/b) for n,a,b in zip(names,nums,dens)});vals["rest_days"]=(t-h.start_date.max()).total_seconds()/86400
    vals.update({f"_num_{n}":float(a) for n,a in zip(names,nums)});vals.update({f"_den_{n}":float(b) for n,b in zip(names,dens)})
    return vals,None

rows=[]
for g in S.sort_values(["start_date","game_id"]).itertuples():
  for side,team in (("home",g.home_team),("away",g.away_team)):
    prior=R[(R.start_date<cutoff)&(R.start_date<g.start_date)&((R.home_team==team)|(R.away_team==team))].sort_values("start_date")
    for src in prior.itertuples():
      opp=src.away_team if src.home_team==team else src.home_team if src.away_team==team else None
      if opp is None: raise SystemExit("source participant identity")
      st,err=side_state(opp,src.start_date)
      rec={"target_game_id":g.game_id,"target_side":side,"target_team":team,"target_kickoff":g.start_date.isoformat(),"target_qualified_prior_games":len(prior),"source_game_id":src.game_id,"source_kickoff":src.start_date.isoformat(),"source_opponent":opp,"strict_source_before_target":bool(src.start_date<g.start_date),"own_target_excluded":src.game_id!=g.game_id,"context_available":err is None,"context_reason":err or ""}
      if st:rec.update(st)
      rows.append(rec)
C=pd.DataFrame(rows)
if len(C) and (not C.strict_source_before_target.all() or not C.own_target_excluded.all()):raise SystemExit("chronology")
if len(C) and C.duplicated(["target_game_id","target_side","source_game_id"]).any():raise SystemExit("duplicate context")
C["snapshot_type"]="S2_K1_SOURCE_CONTEXT";C["snapshot_cutoff_utc"]=cutoff.isoformat()
op=outp/"s2_k1_source_context_companion.csv";C.to_csv(op,index=False)
m={"status":"EXECUTED_NOT_ACCEPTED","s2_predictions_produced":False,"target_outcomes_joined":False,"market_joined":False,"rows":len(C),"context_available":int(C.context_available.sum()) if len(C) else 0,"hashes":{op.name:hashlib.sha256(op.read_bytes()).hexdigest()}}
(outp/"manifest.json").write_text(json.dumps(m,indent=2,sort_keys=True)+"\n");print(json.dumps(m,indent=2))
