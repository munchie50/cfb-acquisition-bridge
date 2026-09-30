#!/usr/bin/env python3
from pathlib import Path
p=Path("scripts/cfb_qa_s2_k1_target_baseline_companion_v1_2026_09_30.py").read_text()
required=[
 "TARGET_BASELINE_BLOCKED_REST_DAYS_HISTORY_SURFACE_REQUIRED",
 "cutoff.normalize()",
 "mechanical_primitive_complete",
 "derived_primitive_complete",
 "s2_predictions_produced",
 "target_outcomes_joined",
 "market_joined",
]
for t in required: assert t in p, f"missing target-baseline invariant: {t}"
# Never permit target rows to become the rest-days population baseline.
assert 'return np.nan' in p[p.index('if f=="rest_days"'):p.index('typ,num,den=COMP[f]')]
print("PASS_S2_K1_TARGET_BASELINE_STATIC_GATE")
