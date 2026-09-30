#!/usr/bin/env python3
"""Static gate for generic weekly REFRESH_SNAPSHOT acceptance audit."""
from pathlib import Path
p=Path("scripts/cfb_qa_weekly_refresh_acceptance.py").read_text()
required=[
 'PASS_WEEKLY_REFRESH_ACCEPTANCE',
 'snapshot_type":"REFRESH_SNAPSHOT',
 'predictions_independently_recomputed',
 'artifact_hashes_reproduced',
 'target_outcomes_opened":False',
 'market_joined":False',
 'fit_or_optimization_performed":False',
 'challenger_b_2026_refresh_fair_predictions_v1_246.csv',
 'manifest_v1_246.json',
 'np.allclose',
 'schedule_sha256',
 'pbp_sha256',
]
for token in required: assert token in p, f"missing weekly acceptance invariant: {token}"
for forbidden in ["622","526","10897612260","10897001956"]:
    assert forbidden not in p, f"FIRST_FROZEN hard-code leaked into generic audit: {forbidden}"
print("PASS_WEEKLY_REFRESH_ACCEPTANCE_STATIC_GATE")
