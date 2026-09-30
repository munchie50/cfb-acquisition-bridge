#!/usr/bin/env python3
"""Prepare, but never persist, the next accepted prediction-source pointer."""
import sys,json,re
from pathlib import Path
from datetime import datetime

accept_path,current_path,out_path=map(Path,sys.argv[1:4])
evidence_id=sys.argv[4]
assert re.fullmatch(r"[A-Za-z0-9_.-]+",evidence_id), "invalid acceptance evidence identity"
assert evidence_id.endswith(".md"), "acceptance evidence must be a persisted markdown record identity"

a=json.loads(accept_path.read_text())
cur=json.loads(current_path.read_text())
assert a["status"]=="PASS_WEEKLY_REFRESH_ACCEPTANCE"
assert a["snapshot_type"]=="REFRESH_SNAPSHOT"
for k in ("predictions_independently_recomputed","artifact_hashes_reproduced","strict_chronology"):
    assert a[k] is True, f"acceptance invariant false: {k}"
for k in ("target_outcomes_opened","market_joined","fit_or_optimization_performed"):
    assert a[k] is False, f"forbidden acceptance state: {k}"
for k in ("schedule_sha256","pbp_sha256"):
    assert re.fullmatch(r"[0-9a-f]{64}",a[k]), f"bad source hash: {k}"

old=datetime.fromisoformat(cur["accepted_cutoff_utc"].replace("Z","+00:00"))
new=datetime.fromisoformat(a["cutoff_utc"].replace("Z","+00:00"))
assert new>old, "accepted pointer must advance strictly forward in time"
assert (a["schedule_sha256"],a["pbp_sha256"]) != (cur["schedule_sha256"],cur["pbp_sha256"]), "accepted refresh cannot advance pointer on unchanged source state"

payload={
 "status":"ACCEPTED_PREDICTION_SOURCE_STATE",
 "accepted_prediction_boundary":evidence_id,
 "accepted_cutoff_utc":a["cutoff_utc"],
 "schedule_sha256":a["schedule_sha256"],
 "pbp_sha256":a["pbp_sha256"],
 "source_state_proof":evidence_id,
 "update_rule":"Advance only after a later weekly prediction boundary is independently accepted and persisted; candidate workflow success alone must never update this pointer."
}
out_path.write_text(json.dumps(payload,indent=2,sort_keys=False)+"\n")
print(json.dumps({"status":"POINTER_ADVANCE_PREPARED_NOT_PERSISTED","from_cutoff":cur["accepted_cutoff_utc"],"to_cutoff":a["cutoff_utc"],"acceptance_evidence":evidence_id},indent=2))
