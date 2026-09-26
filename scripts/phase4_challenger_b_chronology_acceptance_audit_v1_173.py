#!/usr/bin/env python3
import sys,json
from pathlib import Path
import pandas as pd
d=Path(sys.argv[1]); out=Path(sys.argv[2]); out.mkdir(parents=True,exist_ok=True)
m=pd.read_csv(d/"challenger_b_mechanical_primitives_v1_172.csv",dtype={"game_id":str})
f=pd.read_csv(d/"challenger_b_mechanical_features_v1_172.csv",dtype={"game_id":str})
m["start_date"]=pd.to_datetime(m.start_date,utc=True)
assert len(m)==15402 and m.game_id.nunique()==7701
assert not m.duplicated(["season","game_id","team"]).any()
assert not m.duplicated(["season","team","start_date"]).any()
checks=[]; source_pairs=0
for (season,team),z in m.sort_values(["season","team","start_date"]).groupby(["season","team"],sort=False):
    z=z.reset_index(drop=True)
    for i,row in z.iterrows():
        prior=z.iloc[:i]
        if len(prior):
            assert (prior.start_date < row.start_date).all()
            assert not (prior.game_id == row.game_id).any()
            source_pairs += len(prior)
        checks.append((season,team,row.game_id,i,len(prior)))
c=pd.DataFrame(checks,columns=["season","team","target_game_id","chronological_index","strict_prior_source_games"])
assert len(c)==15402
assert (c.chronological_index==c.strict_prior_source_games).all()
assert not (m.season==2025).any() and not (f.season==2025).any()
c.to_csv(out/"strict_chronology_target_exclusion_audit_v1_173.csv",index=False)
manifest={"status":"PASS","target_team_sides":len(c),"target_games":int(m.game_id.nunique()),"source_target_pairs_checked":source_pairs,"equal_kickoff_team_season_rows":0,"non_strict_source_pairs":0,"target_game_in_source_set":0,"2025_accessed":False,"fit_or_score":False}
(out/"manifest_v1_173.json").write_text(json.dumps(manifest,indent=2))
print(json.dumps(manifest,indent=2))
