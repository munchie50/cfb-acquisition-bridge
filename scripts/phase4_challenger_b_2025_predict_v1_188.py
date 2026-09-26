#!/usr/bin/env python3
# v1.188: prospective 2025 feature + fair-prediction producer under frozen v1.187 contract.
import sys,json,hashlib,os
from pathlib import Path
import pandas as pd, numpy as np, pyreadr

schedp, raw_schedp, pbpp, fitp, outp = map(Path,sys.argv[1:6]); outp.mkdir(parents=True,exist_ok=True)
S=pd.read_csv(schedp,dtype={"game_id":str}); S["start_date"]=pd.to_datetime(S.start_date,utc=True)
REQS=["season","game_id","start_date","home_team","away_team","neutral_site","population_class","competition_class"]
if set(S.columns)!=set(REQS) or len(S)!=934 or S.game_id.nunique()!=880 or S.game_id.duplicated().any(): raise SystemExit(f"target schedule identity cols={list(S.columns)} rows={len(S)} unique={S.game_id.nunique()}")
S=S[REQS].copy()
if set(S.population_class.value_counts().to_dict().items())!={("FBS_VS_FBS",808),("FBS_VS_NONFBS",126)}: raise SystemExit("population class mismatch")
if set(S.competition_class.value_counts().to_dict().items())!={("REGULAR",879),("CONFERENCE_CHAMPIONSHIP",9),("POSTSEASON",46)}: raise SystemExit("competition class mismatch")
bad=("point","score","winner","spread","moneyline","over_under","odds","bet","post_win","postgame","market")
if any(any(x in c.lower() for x in bad) for c in S.columns): raise SystemExit("target outcome/market field")

# Quarantine layer: outcome-bearing source is never merged to target rows. Only strict-prior IDs are projected below.
R=pd.read_parquet(raw_schedp); R["game_id"]=R.game_id.astype(str).str.replace(r"\\.0$","",regex=True); R["start_date"]=pd.to_datetime(R.start_date,utc=True)
P=next(iter(pyreadr.read_r(pbpp).values())); P["game_id"]=P.game_id.astype(str).str.replace(r"\\.0$","",regex=True)
P["pos_team"]=P.pos_team.replace({"Savannah St":"Savannah State","St. Francis (PA)":"Saint Francis"})
P["def_pos_team"]=P.def_pos_team.replace({"Savannah St":"Savannah State","St. Francis (PA)":"Saint Francis"})

features=["points_for_per_game","points_against_per_game","offensive_scrimmage_plays_per_game","defensive_scrimmage_plays_per_game","offensive_yards_per_play","defensive_yards_per_play","rush_play_rate","pass_play_rate","rush_yards_per_play","pass_yards_per_play","interception_rate","rest_days","offensive_explosive_play_rate","defensive_explosive_play_rate","offensive_success_rate","defensive_success_rate_allowed","average_starting_yards_to_goal"]
def one(s): return s.fillna(0).eq(1)
def safe(n,d): return np.nan if d==0 else n/d
def side_features(team,target_time,prior_ids):
    # Outcome/PBP projection happens only after strict chronology determines allowed source IDs.
    rs=R[(R.game_id.isin(prior_ids)) & ((R.home_team==team)|(R.away_team==team))].copy()
    if len(rs)!=len(prior_ids): return None,"prior_schedule_identity"
    rs=rs.sort_values("start_date")
    if not (rs.start_date < target_time).all(): return None,"chronology_violation"
    if rs.home_points.isna().any() or rs.away_points.isna().any(): return None,"prior_points_missing"
    ptsf=np.where(rs.home_team==team,rs.home_points,rs.away_points).astype(float); ptsa=np.where(rs.home_team==team,rs.away_points,rs.home_points).astype(float)
    pp=P[P.game_id.isin(prior_ids)].copy()
    if set(pp.game_id.unique()) != set(prior_ids): return None,"prior_pbp_missing"
    sr=(one(pp.rush)|one(pp["pass"])|one(pp.pass_attempt)) & ~one(pp.punt)
    off=pp.pos_team.eq(team); de=pp.def_pos_team.eq(team); rr=sr&one(pp.rush); pr=sr&(one(pp["pass"])|one(pp.pass_attempt)); yg=pp.yards_gained.fillna(0)
    offplays=int((sr&off).sum()); defplays=int((sr&de).sum()); rushplays=int((rr&off).sum()); passplays=int((pr&off).sum())
    passatt=int((one(pp.pass_attempt)&off).sum()); ints=int(((one(pp.interception_thrown_stat)|one(pp.interception_stat))&off).sum())
    offyards=float((yg*(sr&off)).sum()); defyards=float((yg*(sr&de)).sum()); rushyards=float((yg*(rr&off)).sum()); passyards=float((yg*(pr&off)).sum())
    scr=sr & pp.yards_gained.notna(); succq=scr & pp["down"].notna() & pp.distance.notna() & pp.distance.gt(0) & pp["down"].isin([1,2,3,4])
    succ=succq & (((pp["down"]==1)&(pp.yards_gained>=.5*pp.distance))|((pp["down"]==2)&(pp.yards_gained>=.7*pp.distance))|(pp["down"].isin([3,4])&(pp.yards_gained>=pp.distance)))
    offscr=int((scr&off).sum()); defscr=int((scr&de).sum()); offexp=int((scr&off&(pp.yards_gained>=20)).sum()); defexp=int((scr&de&(pp.yards_gained>=20)).sum())
    offsq=int((succq&off).sum()); defsq=int((succq&de).sum()); offsucc=int((succ&off).sum()); defsucc=int((succ&de).sum())
    drive=pp[pp.pos_team.eq(team)&pp.drive_id.notna()&pp.yards_to_goal.notna()][["game_id","drive_id","yards_to_goal"]].copy()
    drive["ord"]=np.arange(len(drive)); drive=drive.sort_values(["game_id","drive_id","ord"]).drop_duplicates(["game_id","drive_id"])
    n=len(prior_ids); last=rs.start_date.max()
    vals=[ptsf.sum()/n,ptsa.sum()/n,offplays/n,defplays/n,safe(offyards,offplays),safe(defyards,defplays),safe(rushplays,offplays),safe(passplays,offplays),safe(rushyards,rushplays),safe(passyards,passplays),safe(ints,passatt),(target_time-last).total_seconds()/86400,safe(offexp,offscr),safe(defexp,defscr),safe(offsucc,offsq),safe(defsucc,defsq),safe(drive.yards_to_goal.sum(),len(drive))]
    if not np.isfinite(vals).all(): return None,"required_feature_na"
    return dict(zip(features,map(float,vals))),None

rows=[]; exclusions=[]; audit=[]
for _,g in S.sort_values(["start_date","game_id"]).iterrows():
    rec={"season":2025,"game_id":g.game_id,"start_date":g.start_date.isoformat(),"home_team":g.home_team,"away_team":g.away_team,"population_class":g.population_class,"competition_class":g.competition_class,"venue_state":"NEUTRAL" if bool(g.neutral_site) else "HOME"}
    reasons=[]; sides={}
    for label,team in [("home",g.home_team),("away",g.away_team)]:
        prior=S[(S.start_date<g.start_date)&((S.home_team==team)|(S.away_team==team))].sort_values("start_date")
        ids=prior.game_id.tolist()
        if not ids: reasons.append(label+"_opening_no_prior"); continue
        if g.game_id in ids: raise SystemExit("own game leaked")
        f,err=side_features(team,g.start_date,ids)
        audit.append({"game_id":g.game_id,"side":label,"team":team,"prior_games":len(ids),"max_prior_kickoff":prior.start_date.max().isoformat(),"target_kickoff":g.start_date.isoformat(),"own_game_excluded":g.game_id not in ids,"strict_chronology":bool((prior.start_date<g.start_date).all())})
        if err: reasons.append(label+"_"+err)
        else: sides[label]=f
    if reasons:
        exclusions.append(rec|{"reasons":"|".join(sorted(set(reasons)))})
    else:
        for f in features:
            rec["home_"+f]=sides["home"][f]; rec["away_"+f]=sides["away"][f]
        rows.append(rec)
X=pd.DataFrame(rows); E=pd.DataFrame(exclusions); A=pd.DataFrame(audit)
pred=[p+f for f in features for p in ("home_","away_")]
if len(pred)!=34 or (len(X) and (X[pred].isna().any(axis=None) or not np.isfinite(X[pred].to_numpy(float)).all())): raise SystemExit("predictor invariant")
if len(X)+len(E)!=934 or set(X.game_id).intersection(set(E.game_id)): raise SystemExit("population accounting")
if len(A) and (not A.own_game_excluded.all() or not A.strict_chronology.all()): raise SystemExit("leakage audit")

coef=pd.read_csv(fitp/"selected_coefficients.csv"); scale=pd.read_csv(fitp/"train_scaling.csv")
if len(scale)!=34 or set(scale.feature)!=set(pred): raise SystemExit("scaling identity")
Z=(X[pred].to_numpy(float)-scale.set_index("feature").loc[pred,"mean"].to_numpy(float))/scale.set_index("feature").loc[pred,"sd"].to_numpy(float)
Z=np.c_[Z,(X.venue_state=="NEUTRAL").astype(float).to_numpy()]
names=["intercept"]+pred+["venue_neutral"]
for kind,lam in [("margin",10),("total",100),("win",10)]:
    c=coef[(coef.target==kind)&(coef["lambda"]==lam)].set_index("term")
    if set(c.index)!=set(names): raise SystemExit("coefficient identity")
    w=c.loc[names,"coefficient"].to_numpy(float); q=np.c_[np.ones(len(Z)),Z]@w
    if kind=="win": q=1/(1+np.exp(-np.clip(q,-40,40)))
    X["pred_"+kind]=q
if len(X) and (not np.isfinite(X[["pred_margin","pred_total","pred_win"]]).all(axis=None) or not X.pred_win.between(0,1).all()): raise SystemExit("prediction invariant")
X.to_csv(outp/"challenger_b_2025_fair_predictions_v1_188.csv",index=False); E.to_csv(outp/"challenger_b_2025_exclusions_v1_188.csv",index=False); A.to_csv(outp/"challenger_b_2025_chronology_audit_v1_188.csv",index=False); S.to_csv(outp/"challenger_b_2025_target_ledger_v1_188.csv",index=False)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
manifest={"status":"EXECUTED_NOT_ACCEPTED","target_games":934,"eligible_predictions":len(X),"excluded_games":len(E),"target_population":{"FBS_VS_FBS":808,"FBS_VS_NONFBS":126,"REGULAR":879,"CONFERENCE_CHAMPIONSHIP":9,"POSTSEASON":46},"predictor_count":34,"fit_or_optimization_performed":False,"market_joined":False,"target_outcomes_joined":False,"source_chronology":"strictly earlier kickoff only","hashes":{}}
for p in sorted(outp.iterdir()): manifest["hashes"][p.name]=sha(p)
(outp/"manifest_v1_188.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n")
print(json.dumps(manifest,indent=2))
