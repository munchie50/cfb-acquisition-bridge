#!/usr/bin/env python3
# v1.214 exact census of frozen v1.206 exclusion/side reasons.
import sys,json
from pathlib import Path
import pandas as pd
art,out=map(Path,sys.argv[1:3]); out.mkdir(parents=True,exist_ok=True)
L=pd.read_csv(art/"challenger_b_2026_feature_eligibility_ledger_v1_206.csv",dtype={"game_id":str})
E=pd.read_csv(art/"challenger_b_2026_exclusions_v1_206.csv",dtype={"game_id":str})
B=L[~L.eligible.astype(bool)].copy()
side=B.groupby("reason").agg(team_sides=("game_id","size"),unique_targets=("game_id","nunique")).reset_index().sort_values(["unique_targets","team_sides","reason"],ascending=[False,False,True])
side.to_csv(out/"side_reason_census_v1_214.csv",index=False)
# exact exclusion strings as frozen by producer
tmp=B.groupby("game_id")["reason"].apply(lambda z:"+".join(sorted(set(z.astype(str))))).reset_index(name="reason_combination")
assert set(tmp.game_id)==set(E.game_id)
exc=tmp.groupby("reason_combination").size().reset_index(name="targets").sort_values(["targets","reason_combination"],ascending=[False,True])
exc.to_csv(out/"target_exclusion_reason_census_v1_214.csv",index=False)
report={"status":"DESCRIPTIVE_ONLY","excluded_targets":len(E),"ineligible_team_sides":len(B),"side_reasons":side.to_dict("records"),"target_exclusion_reasons":exc.to_dict("records"),"predictions_changed":False}
(out/"diagnostic_v1_214.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n"); print(json.dumps(report,indent=2))
