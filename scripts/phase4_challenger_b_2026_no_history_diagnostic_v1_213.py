#!/usr/bin/env python3
# v1.213 descriptive readback of no_prior_history exclusions.
import sys,json
from pathlib import Path
import pandas as pd
art,out=map(Path,sys.argv[1:3]); out.mkdir(parents=True,exist_ok=True)
L=pd.read_csv(art/"challenger_b_2026_feature_eligibility_ledger_v1_206.csv",dtype={"game_id":str})
B=L[(~L.eligible.astype(bool))&(L.reason=="no_prior_history")].copy()
cols=[c for c in ["game_id","side","team","target_kickoff","reason"] if c in B.columns]
B[cols].sort_values(["team","target_kickoff"]).to_csv(out/"no_prior_history_v1_213.csv",index=False)
report={"status":"DESCRIPTIVE_ONLY","affected_team_sides":len(B),"unique_targets":B.game_id.nunique(),"teams":sorted(B.team.unique().tolist()),"team_count":B.team.nunique(),"predictions_changed":False}
(out/"diagnostic_v1_213.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n"); print(json.dumps(report,indent=2))
