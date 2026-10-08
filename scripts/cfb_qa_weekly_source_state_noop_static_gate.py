#!/usr/bin/env python3
"""Static regression gate for the recurring Tuesday weekly no-op control."""
import json
from pathlib import Path

wf = Path(".github/workflows/cfb_weekly_tuesday_candidate_freeze.yml").read_text()
pointer_path = Path("evidence/operational/CFB_ACCEPTED_PREDICTION_SOURCE_STATE.json")
pointer = json.loads(pointer_path.read_text())

required_pointer = {
    "status",
    "accepted_prediction_boundary",
    "accepted_cutoff_utc",
    "schedule_sha256",
    "pbp_sha256",
    "source_state_proof",
    "update_rule",
}
missing = [k for k in required_pointer if k not in pointer]
assert not missing, f"accepted-source pointer missing fields: {missing}"
assert pointer["status"] == "ACCEPTED_PREDICTION_SOURCE_STATE"
for key in ("schedule_sha256", "pbp_sha256"):
    value = pointer[key]
    assert isinstance(value, str) and len(value) == 64 and all(c in "0123456789abcdef" for c in value), key
assert "independently accepted" in pointer["update_rule"]
assert "candidate workflow success alone must never update this pointer" in pointer["update_rule"]

required_workflow_tokens = [
    "Compare with last independently accepted prediction source state",
    'id: source_gate',
    'evidence/operational/CFB_ACCEPTED_PREDICTION_SOURCE_STATE.json',
    'changed=any(current[k] != accepted[k] for k in current)',
    'candidate_needed=pre["future_at_cutoff"] > 0 and changed',
    "CFB_WEEKLY_TUESDAY_NOOP",
]
for token in required_workflow_tokens:
    assert token in wf, f"missing weekly no-op control token: {token}"

guard = "if: steps.source_gate.outputs.candidate_needed == 'true'"
guarded_steps = [
    "Fetch frozen Champion fit",
    "Run accepted S0 refresh producer",
    "Run accepted v4 source-context producer",
    "Run S2_K1 target-baseline candidate companion",
    "Retain complete candidate boundary",
]
for step in guarded_steps:
    marker = f"- name: {step}"
    start = wf.index(marker)
    next_step = wf.find("\n      - ", start + len(marker))
    block = wf[start:] if next_step == -1 else wf[start:next_step]
    assert guard in block, f"unguarded candidate step: {step}"

upload_marker = "- uses: actions/upload-artifact@v4"
start = wf.index(upload_marker)
block = wf[start:]
assert guard in block.split("with:", 1)[0], "candidate artifact upload is not no-op guarded"

# Fail if workflow starts mutating the accepted pointer itself.
assert "CFB_ACCEPTED_PREDICTION_SOURCE_STATE.json" not in wf.replace(
    'evidence/operational/CFB_ACCEPTED_PREDICTION_SOURCE_STATE.json', ''
), "unexpected accepted-pointer mutation/reference"

print("PASS_WEEKLY_SOURCE_STATE_NOOP_STATIC_GATE")
