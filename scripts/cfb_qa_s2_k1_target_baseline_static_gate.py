#!/usr/bin/env python3
from pathlib import Path
p=Path("scripts/cfb_qa_s2_k1_target_baseline_companion_v1_2026_09_30.py").read_text()
required=[
 "TARGET_BASELINE_UNAVAILABLE",
 "cutoff.normalize()",
 "mechanical_primitive_complete",
 "derived_primitive_complete",
 'groupby(["season","team"]).start_date.diff().dt.total_seconds()/86400',
 'ident.start_date<t',
 'ident.rest_days.notna()',
 'not ident.duplicated(["season","team","start_date"],keep=False).any()',
 "s2_predictions_produced",
 "target_outcomes_joined",
 "market_joined",
]
for t in required: assert t in p, f"missing target-baseline invariant: {t}"
rest=p[p.index('if f=="rest_days"'):p.index('typ,num,den=COMP[f]')]
assert "T[" not in rest, "future target rows leaked into rest-days population baseline"
assert "M[[" in rest, "rest-days ancestry must derive from accepted primitive schedule identities"
print("PASS_S2_K1_TARGET_BASELINE_STATIC_GATE")
