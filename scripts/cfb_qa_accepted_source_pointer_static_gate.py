#!/usr/bin/env python3
"""Static governance gate for accepted-source pointer preparation."""
from pathlib import Path
p=Path("scripts/cfb_qa_prepare_accepted_source_pointer.py").read_text()
required=[
 'PASS_WEEKLY_REFRESH_ACCEPTANCE',
 'POINTER_ADVANCE_PREPARED_NOT_PERSISTED',
 'predictions_independently_recomputed',
 'artifact_hashes_reproduced',
 'strict_chronology',
 'target_outcomes_opened',
 'market_joined',
 'fit_or_optimization_performed',
 'new>old',
 'accepted refresh cannot advance pointer on unchanged source state',
 'candidate workflow success alone must never update this pointer',
]
for t in required: assert t in p, f"missing pointer governance invariant: {t}"
for forbidden in ["github","requests","urllib","subprocess","git push","update_file","create_file"]:
    assert forbidden not in p, f"pointer preparer acquired mutation capability: {forbidden}"
print("PASS_ACCEPTED_SOURCE_POINTER_PREPARATION_STATIC_GATE")
