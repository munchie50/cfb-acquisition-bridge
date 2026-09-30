#!/usr/bin/env python3
"""Static regression gate for independent S2_K1 target-baseline acceptance."""
from pathlib import Path
p=Path("scripts/cfb_qa_s2_k1_target_baseline_acceptance_v1_2026_09_30.py").read_text()
required=[
 'PASS_S2_K1_TARGET_BASELINE_ACCEPTANCE',
 'CM["status"]=="EXECUTED_NOT_ACCEPTED"',
 'cutoff.normalize()',
 'src.start_date<day',
 'ident.start_date<day',
 'groupby(["season","team"]).start_date.diff().dt.total_seconds()/86400',
 'not ident.duplicated(["season","team","start_date"],keep=False).any()',
 'np.allclose(vals,E[f],rtol=0,atol=1e-12)',
 '"target_rows_used_as_population_baseline":False',
 '"target_outcomes_opened":False',
 '"market_joined":False',
 '"wager_or_execution_joined":False',
 '"protected_2025_test_opened":False',
 '"fit_or_optimization_performed":False',
]
for t in required: assert t in p, f"missing acceptance invariant: {t}"
# Independent recomputation must not import or invoke the candidate producer.
assert "cfb_qa_s2_k1_target_baseline_companion" not in p
assert "subprocess" not in p
# Candidate values may only be compared after E is independently reconstructed.
assert p.index("E={f:expected_baseline(f)") < p.index("vals=C[bc].to_numpy(float)")
print("PASS_S2_K1_TARGET_BASELINE_ACCEPTANCE_STATIC_GATE")
