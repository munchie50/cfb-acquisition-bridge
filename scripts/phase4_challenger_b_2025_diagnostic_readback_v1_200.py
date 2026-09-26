#!/usr/bin/env python3
# Read-only post-holdout diagnostic readback from already accepted v1.196 artifact.
import sys,json
from pathlib import Path
import pandas as pd
art,out=map(Path,sys.argv[1:3]); out.mkdir(parents=True,exist_ok=True)
D=pd.read_csv(art/"challenger_b_2025_evaluation_slices_v1_196.csv")
required={"target","dimension","slice","n"}
assert required.issubset(D.columns)
assert set(D.dimension)=={"venue_state","population_class","competition_class"}
# No ranking/selection: preserve all prospectively generated slices.
records=D.where(pd.notna(D),None).to_dict("records")
report={"status":"DESCRIPTIVE_ONLY","source":"accepted v1.196 scoring artifact","slice_rows":len(D),"slices":records,
"used_for_tuning":False,"used_for_recalibration":False,"used_for_redesign":False,"used_for_promotion":False}
(out/"challenger_b_2025_diagnostic_readback_v1_200.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
print(D.to_string(index=False))
