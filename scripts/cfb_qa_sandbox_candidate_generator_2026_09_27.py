#!/usr/bin/env python3
"""CFB QA Sandbox S1/S2 candidate generator.
Outcome-blind construction only. Frozen 2026-09-27 semantics.
"""
import argparse, hashlib, json, os, re
from pathlib import Path
import numpy as np
import pandas as pd

KGRID=(1,2,4,8)
FEATURES=[
"points_for_per_game","points_against_per_game",
"offensive_scrimmage_plays_per_game","defensive_scrimmage_plays_per_game",
"offensive_yards_per_play","defensive_yards_per_play",
"rush_play_rate","pass_play_rate","rush_yards_per_play","pass_yards_per_play",
"interception_rate","rest_days","offensive_explosive_play_rate",
"defensive_explosive_play_rate","offensive_success_rate",
"defensive_success_rate_allowed","average_starting_yards_to_goal"]
MAP={
"points_for_per_game":"points_against_per_game",
"points_against_per_game":"points_for_per_game",
"offensive_scrimmage_plays_per_game":"defensive_scrimmage_plays_per_game",
"defensive_scrimmage_plays_per_game":"offensive_scrimmage_plays_per_game",
"offensive_yards_per_play":"defensive_yards_per_play",
"defensive_yards_per_play":"offensive_yards_per_play",
"offensive_explosive_play_rate":"defensive_explosive_play_rate",
"defensive_explosive_play_rate":"offensive_explosive_play_rate",
"offensive_success_rate":"defensive_success_rate_allowed",
"defensive_success_rate_allowed":"offensive_success_rate"}
FORBID=re.compile(r"(target|actual|final_|market|spread|odds|moneyline|wager|stake|closing|close_|outcome)",re.I)

def sha(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--dataset",required=True)
    ap.add_argument("--mechanical-primitives",required=True)
    ap.add_argument("--derived-primitives",required=True)
    ap.add_argument("--mechanical-features",required=True)
    ap.add_argument("--derived-features",required=True)
    ap.add_argument("--scaling",required=True)
    ap.add_argument("--coefficients",required=True)
    ap.add_argument("--out",required=True)
    a=ap.parse_args(); out=Path(a.out); out.mkdir(parents=True,exist_ok=True)

    ds=pd.read_csv(a.dataset,dtype={"game_id":str})
    if (ds.season==2025).any(): raise SystemExit("2025 TEST exposure")
    # Outcome columns may exist in the accepted dataset, but are stripped before candidate construction.
    safe_cols=[c for c in ds.columns if not FORBID.search(c)]
    work=ds[safe_cols].copy()
    if any(FORBID.search(c) for c in work.columns): raise SystemExit("forbidden candidate input")

    mf=pd.read_csv(a.mechanical_features,dtype={"game_id":str})
    df=pd.read_csv(a.derived_features,dtype={"game_id":str})
    mp=pd.read_csv(a.mechanical_primitives,dtype={"game_id":str})
    dp=pd.read_csv(a.derived_primitives,dtype={"game_id":str})
    for z in (mf,df,mp,dp):
        if (z.season==2025).any(): raise SystemExit("2025 substrate exposure")
        z["start_date"]=pd.to_datetime(z["start_date"],utc=True)

    # Feature-side table keyed to each team pregame state.
    side=mf[["season","game_id","team","start_date","qualified_prior_games"]+[x for x in FEATURES if x in mf]].merge(
        df[["season","game_id","team"]+[x for x in FEATURES if x in df]],
        on=["season","game_id","team"],how="inner",validate="one_to_one")
    if side[FEATURES].isna().any().any():
        # opening/incomplete sides are permitted in substrate but never in accepted candidate population.
        pass

    # Accepted eligible game-side rows.
    homes=work[["season","game_id","start_date","home_team"]].rename(columns={"home_team":"team"})
    aways=work[["season","game_id","start_date","away_team"]].rename(columns={"away_team":"team"})
    need=pd.concat([homes,aways],ignore_index=True)[["season","game_id","team"]]
    elig=need.merge(side,on=["season","game_id","team"],how="left",validate="one_to_one")
    if elig[FEATURES+["qualified_prior_games"]].isna().any().any(): raise SystemExit("eligible side missing feature/history")

    # Frozen pooled-component population baselines: season-local and strict-cutoff-local.
    side=side.sort_values("start_date")
    COMPONENTS={
      "points_for_per_game":("M","game_points_for","GAME"),
      "points_against_per_game":("M","game_points_against","GAME"),
      "offensive_scrimmage_plays_per_game":("M","off_plays","GAME"),
      "defensive_scrimmage_plays_per_game":("M","def_plays","GAME"),
      "offensive_yards_per_play":("M","off_yards","off_plays"),
      "defensive_yards_per_play":("M","def_yards","def_plays"),
      "rush_play_rate":("M","rush_plays","off_plays"),
      "pass_play_rate":("M","pass_plays","off_plays"),
      "rush_yards_per_play":("M","rush_yards","rush_plays"),
      "pass_yards_per_play":("M","pass_yards","pass_plays"),
      "interception_rate":("M","interceptions","pass_attempts"),
      "offensive_explosive_play_rate":("D","off_exp","off_scr"),
      "defensive_explosive_play_rate":("D","def_exp","def_scr"),
      "offensive_success_rate":("D","off_succ","off_succ_q"),
      "defensive_success_rate_allowed":("D","def_succ","def_succ_q"),
      "average_starting_yards_to_goal":("D","start_ytg_sum","start_drive_n")}
    def baseline(feature,t,season):
        if feature=="rest_days":
            cutoff=pd.Timestamp(t).normalize()
            z=side[(side.season==season)&(side.start_date<cutoff)&side.rest_days.notna()]
            if z.empty: raise RuntimeError("unreproducible rest-days baseline")
            return float(z.rest_days.mean())
        typ,num,den=COMPONENTS[feature]
        src=mp if typ=="M" else dp
        complete="mechanical_primitive_complete" if typ=="M" else "derived_primitive_complete"
        cutoff=pd.Timestamp(t).normalize()
        z=src[(src.season==season)&(src.start_date<cutoff)&src[complete].astype(bool)].copy()
        if z.empty: raise RuntimeError("unreproducible component baseline")
        n=float(z[num].sum())
        d=float(len(z)) if den=="GAME" else float(z[den].sum())
        if not np.isfinite(d) or d<=0: raise RuntimeError("zero/unavailable pooled denominator")
        return n/d

    # S1 states for any side on demand.
    cache={}
    def s1(row,feature,k):
        key=(row.season,row.game_id,row.team,feature,k)
        if key in cache:return cache[key]
        b=baseline(feature,row.start_date,row.season); n=float(row.qualified_prior_games)
        v=n/(n+k)*float(row[feature])+k/(n+k)*b
        cache[key]=v; return v

    # Build game/opponent lookup and source histories from accepted primitive identities.
    ident=mp[["season","game_id","team","start_date","home_team","away_team"]].copy()
    ident["opponent"]=np.where(ident.team==ident.home_team,ident.away_team,
                      np.where(ident.team==ident.away_team,ident.home_team,None))
    if ident.opponent.isna().any(): raise SystemExit("opponent identity failure")
    side_idx=side.set_index(["season","game_id","team"],drop=False)

    def s2(row,feature,k):
        base=s1(row,feature,k)
        if feature not in MAP:return base
        prior=ident[(ident.season==row.season)&(ident.team==row.team)&(ident.start_date<row.start_date)].sort_values("start_date")
        if len(prior)!=int(row.qualified_prior_games): raise RuntimeError("source chronology/count mismatch")
        residuals=[]
        pair=MAP[feature]
        for g in prior.itertuples():
            key=(g.season,g.game_id,g.opponent)
            if key not in side_idx.index: raise RuntimeError("missing opponent pregame state")
            opp=side_idx.loc[key]
            if not opp.start_date < row.start_date: raise RuntimeError("future context")
            # Opponent context is S1 at the source game's pregame state; no S2 recursion.
            try:
                ob=baseline(pair,opp.start_date,opp.season)
                ov=s1(opp,pair,k)
            except RuntimeError as e:
                # Only absence of a completion-safe population pool is an expected
                # source-context omission. Other baseline defects fail closed.
                if str(e) in ("unreproducible component baseline","unreproducible rest-days baseline"):
                    continue
                raise
            residuals.append(ov-ob)
        if not residuals:
            raise RuntimeError("no valid completion-safe S2 context")
        return base-float(np.mean(residuals))

    scale=pd.read_csv(a.scaling).set_index("feature")
    coef=pd.read_csv(a.coefficients)
    EXPECTED34=set(["home_"+x for x in FEATURES]+["away_"+x for x in FEATURES])
    if set(scale.index)!=EXPECTED34: raise SystemExit("scaling feature mismatch")
    rows=[]
    work["start_date"]=pd.to_datetime(work.start_date,utc=True)
    for game in work.itertuples():
        hs=side_idx.loc[(game.season,game.game_id,game.home_team)]
        as_=side_idx.loc[(game.season,game.game_id,game.away_team)]
        candidates=[("S0",None,None)]
        for k in KGRID:
            candidates += [(f"S1_K{k}","S1",k),(f"S2_K{k}","S2",k)]
        for cid,kind,k in candidates:
            hv={}; av={}
            unavailable=False
            try:
                for f in FEATURES:
                    if cid=="S0": hv[f]=float(hs[f]); av[f]=float(as_[f])
                    elif kind=="S1": hv[f]=s1(hs,f,k); av[f]=s1(as_,f,k)
                    else: hv[f]=s2(hs,f,k); av[f]=s2(as_,f,k)
            except RuntimeError as e:
                if kind=="S2" and str(e)=="no valid completion-safe S2 context":
                    unavailable=True
                else:
                    raise
            if unavailable:
                continue
            vec={}
            for f in FEATURES:
                vec["home_"+f]=hv[f]; vec["away_"+f]=av[f]
            # scaling/coefficients use 34 home_/away_ names.
            def pred34(target):
                w=coef[coef.target==target].set_index("term").coefficient
                z=float(w["intercept"])
                for name,val in vec.items():
                    z+=((val-float(scale.loc[name,"mean"]))/float(scale.loc[name,"sd"]))*float(w[name])
                z+=(1.0 if game.venue_state=="NEUTRAL" else 0.0)*float(w["venue_neutral"])
                return 1/(1+np.exp(-np.clip(z,-40,40))) if target=="win" else z
            rows.append({"season":int(game.season),"game_id":str(game.game_id),
                "start_date":game.start_date.isoformat(),"home_team":game.home_team,
                "away_team":game.away_team,"venue_state":game.venue_state,
                "candidate_id":cid,"k":k,"pred_margin":pred34("margin"),
                "pred_total":pred34("total"),"pred_win":pred34("win")})
    pred=pd.DataFrame(rows)
    if any(FORBID.search(c) for c in pred.columns): raise SystemExit("forbidden prediction column")
    expected=56170
    expected_s0=len(work)
    expected_s1=len(work)*4
    expected_s2=(len(work)-11)*4
    if pred.duplicated(["season","game_id","candidate_id"]).any():
        raise SystemExit("duplicate candidate prediction rows")
    vals=pred[["pred_margin","pred_total","pred_win"]].to_numpy(dtype=float)
    if not np.isfinite(vals).all():
        raise SystemExit("non-finite candidate prediction")
    if not pred["pred_win"].between(0.0,1.0,inclusive="both").all():
        raise SystemExit("candidate win probability outside [0,1]")
    expected_k={"S0":None,"S1_K1":1,"S1_K2":2,"S1_K4":4,"S1_K8":8,
      "S2_K1":1,"S2_K2":2,"S2_K4":4,"S2_K8":8}
    for cid,kexp in expected_k.items():
        z=pred[pred.candidate_id.eq(cid)]
        if z.empty:
            raise SystemExit(f"missing candidate id {cid}")
        if kexp is None:
            if z.k.notna().any(): raise SystemExit("S0 k must be null")
        elif not z.k.eq(kexp).all():
            raise SystemExit(f"candidate k mismatch {cid}")
    counts=pred.candidate_id.str.extract(r'^(S[012])')[0].value_counts().to_dict()
    if len(pred)!=expected: raise SystemExit("candidate row count mismatch")
    if counts.get("S0",0)!=expected_s0 or counts.get("S1",0)!=expected_s1 or counts.get("S2",0)!=expected_s2:
        raise SystemExit("candidate family cardinality mismatch")
    expected_s2_omissions={
      (2017,"400935254"),(2018,"401022521"),(2018,"401022524"),(2019,"401112443"),
      (2020,"401246425"),(2022,"401403946"),(2022,"401403976"),(2022,"401405073"),
      (2022,"401413257"),(2022,"401415219"),(2022,"401426543")}
    s2_games=set(map(tuple,pred[pred.candidate_id.str.startswith("S2")][["season","game_id"]].drop_duplicates().to_numpy()))
    all_games=set((int(r.season),str(r.game_id)) for r in work[["season","game_id"]].drop_duplicates().itertuples(index=False))
    actual_s2_omissions=all_games-s2_games
    if actual_s2_omissions!=expected_s2_omissions:
        raise SystemExit("S2 omitted-game identity mismatch")
    p=out/"sandbox_candidate_predictions.csv"; pred.to_csv(p,index=False)
    config={"k_grid":list(KGRID),"features":FEATURES,"s2_mapping":MAP,
      "population_cutoff":"UTC_DATE_MIDNIGHT_STRICT_PRIOR",
      "s2_fail_closed":True,"expected_prediction_rows":56170}
    config_sha256=hashlib.sha256(json.dumps(config,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    manifest={"status":"PREDICTIONS_FROZEN_NOT_SCORED","games":len(work),"prediction_rows":len(pred),
      "candidate_ids":sorted(pred.candidate_id.unique()),"seasons":sorted(map(int,pred.season.unique())),
      "2025_accessed":False,"outcomes_joined":False,"generator_sha256":sha(__file__),
      "config_sha256":config_sha256,"config":config,
      "input_sha256":{"dataset":sha(a.dataset),"mechanical_primitives":sha(a.mechanical_primitives),
        "derived_primitives":sha(a.derived_primitives),"mechanical_features":sha(a.mechanical_features),
        "derived_features":sha(a.derived_features),"scaling":sha(a.scaling),"coefficients":sha(a.coefficients)},
      "prediction_sha256":sha(p)}
    (out/"manifest.json").write_text(json.dumps(manifest,indent=2))
    print(json.dumps(manifest,indent=2))
if __name__=="__main__": main()
