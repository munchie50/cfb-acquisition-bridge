#!/usr/bin/env python3
from pathlib import Path
import hashlib
p=Path("scripts/cfb_qa_s2_k1_source_context_companion_v1_2026_09_28.py");s=p.read_text()
must=[
'R=R[(R.season.astype(int)==2026)&(R.start_date<cutoff)].copy()',
'pd.Timestamp(tm).normalize()',
'"primitive_ancestry_blob":"37c05aba201d3c2935b5d2b646437552949766fd"',
'"s2_predictions_produced":False',
'"target_outcomes_joined":False',
'"market_joined":False',
'mechanical_primitive_complete',
'derived_primitive_complete',
'mechanical_history_complete',
'derived_history_complete',
'start_ytg_sum',
'start_drive_n',
'context_valid__',
]
for x in must:
 assert x in s,x
assert 'R=R[R.season.astype(int)==2026].copy()' not in s
# Recovered v1.172 primitive formulas/aliases that must remain literal in the companion.
for x in [
'(one(P.rush)|one(P["pass"])|one(P.pass_attempt))&~one(P.punt)',
'rr=sr&one(P.rush)',
'pr=sr&(one(P["pass"])|one(P.pass_attempt))',
'one(P.interception_thrown_stat)|one(P.interception_stat)',
'drop_duplicates(["game_id","pos_team","drive_id"])',
]:
 assert x in s,x
# Frozen S2 map is exactly 10 directional mappings / five reciprocal pairs.
a=s.index('MAP={');b=s.index('\ndef baseline',a);m=s[a:b]
assert m.count('":"')==10,m
print("S2_K1_SOURCE_CONTEXT_STATIC_PASS",hashlib.sha256(p.read_bytes()).hexdigest())
