#!/usr/bin/env python3
from pathlib import Path
import hashlib
p=Path("scripts/cfb_qa_s2_k1_source_context_companion_v2_2026_09_29.py");s=p.read_text()
must=[
'T=pd.read_csv(targetsidep',
'if T.duplicated(["game_id","team"]).any():raise SystemExit("target-side identity")',
'len(prior)!=int(expected)',
'raise SystemExit("target/source history count mismatch")',
'pd.Timestamp(o.start_date)!=pd.Timestamp(src.start_date)',
'raise SystemExit("opponent/source kickoff identity")',
'raise SystemExit("opponent qualified-prior identity")',
'(not np.isfinite(n)) or (not np.isfinite(d))',
'f.loc[~ok,c]=np.nan',
'"accepted_target_side_crosscheck":True',
'"s2_predictions_produced":False',
'"target_outcomes_joined":False',
'"market_joined":False',
]
for x in must: assert x in s,x
assert s.count('f.loc[~ok,c]=np.nan')==2
assert 'R=R[(R.season.astype(int)==2026)&(R.start_date<cutoff)].copy()' in s
assert 'R=R[R.season.astype(int)==2026].copy()' not in s
print("S2_K1_SOURCE_CONTEXT_V2_STATIC_PASS",hashlib.sha256(p.read_bytes()).hexdigest())
