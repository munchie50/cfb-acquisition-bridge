# CFB Scheduler Canary v2 — prospective demonstration armed

Status: SCHEDULE_READ_BACK / DEMONSTRATION_PENDING.
Date: 2026-10-06 America/Chicago.
Production routine v5 remains active; Routine v6 remains candidate/test.
Scientific effect: NONE. Champion effect: NONE.

## Trigger and authority
User instructed continuation of scheduler testing using Test Routine after explicitly directing removal of sign-in dependence. Recovered v1.245 doorway, Routine v6 back-half candidate, scheduled-control defect, and GitHub contents persistence procedure. Prior original Stage 1 stays RESULT_UNOBSERVED; no historical result reconstructed.
Existing canary 6ac4e807aaac8191b3255fae8ab82577 updated in place. This is an authorized changed diagnostic (scheduled read plus isolated diagnostic persistence), not a rerun represented as the original read-only result.

## Expected producer and outputs
One-time exact schedule: DTSTART;TZID=America/Chicago:20261006T082700.
Enabled schedule independently read back. Tool update timestamp 2026-10-06T12:51:43.820837Z.
Prior launch 2026-10-06T12:25:56.916711Z. New schedule respects tool's once-per-hour limit.
Only connected GitHub tools; browser and sign-in fallback forbidden.
Expected: one unique invocation identifier with a STARTED file and a separate RESULT file under evidence/scheduler_qa/, each created append-only and independently read back by producer.
Fixed diagnostic read target: evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md; known blob SHA a5268b1d0259a257c3c44c05fbeb61928b103983. Re-fetch if current bytes differ; do not infer authority from this fixed probe.

## Independent reconciliation after trigger
Enumerate evidence/scheduler_qa/ directly, then fetch the invocation's STARTED and RESULT files separately through the connected GitHub API.
Check invocation id, canary task id, actual start/completion timestamps, target path and returned SHA, terminal marker and producer readback declaration.
Compare target SHA with independently fetched target bytes. Result bytes are diagnostic evidence, not a production RUN_PASS receipt.
No launch/no artifacts = trigger/early-execution observation gap. STARTED without RESULT = incomplete post-start execution. RESULT with failed target read = explicit connected-read failure. Persisted/read-back PASS with matching identities = narrow scheduled diagnostic success.
A missing marker alone does not identify a root cause. Missing terminal after 08:42 CT is a bounded investigation trigger, not proof that execution failed or a reason to blindly redispatch.
Original Stage 1 remains unverified regardless of this result.

## WAIT sweep and protection
Before trigger, directly enumerated scheduler_qa: only prior Stage 1 observation gate and no-browser correction records; no v2 execution evidence exists.
Independent task topology readback proves four enabled recurring production tasks. Every production prompt, schedule, and enabled flag equals the pre-mutation snapshot. Temporary canary is enabled one-time only, not a fifth recurring producer.
Market Monitor retains enabled 07:00/13:00 CT Sunday-Saturday exact cadence and sole primary Hot Sheet ownership. Health and other downstream consumers unchanged.
No operational surfaces changed. No market/model work or production rerun dispatched.
Next: genuine 08:27 CT trigger and independent artifact reconciliation. Production defect closure still requires representative natural Market Monitor terminal/canonical/Hot Sheet evidence; toy canary success cannot close it.
