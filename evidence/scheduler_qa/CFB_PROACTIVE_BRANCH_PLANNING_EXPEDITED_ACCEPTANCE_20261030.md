# Proactive branch planning — expedited acceptance contract — 2026-10-30
Status: QA TEST CONTRACT / NOT PRODUCTION. Parent: CFB_V6_PROACTIVE_BRANCH_PLANNING_CANDIDATE_20261030.md.

## Predeclared gates
G1. Historical blind replay, 3 distinct cases: successful natural run, NO_UPDATE before receipt, and STARTED/terminal canonical write failure. For each, use only information known at branch selection time; record anticipated success, partial/failure branches, discriminating evidence, safe next action, and stop/rollback. Reveal actual outcome afterward. PASS requires all 3 cases correctly avoid false PASS, duplicate unsafe retry and fabricated root cause, with a concrete next action.
G2. Baseline comparison against v5 for those same cases: identify a meaningful earlier or clearer next action in at least 2 of 3; no loss of v5 safety and no new production task. If no demonstrable gain, REVISE or RETIRE, not promotion by enthusiasm.
G3. At least one ordinary ongoing work unit using the branches before outcome is known, then expected-vs-actual reconciliation; may use current natural task evidence when available. Do not require multiple weeks.
G4. Friction budget: concise branches embedded in existing work record, no redundant checklists, no material execution delay, no unsupported automatic retries or production mutation.

## Decision cadence
At the first existing QA review after G1/G2 are completed, issue PROMOTE_RECOMMENDATION, REVISE_WITH_SPECIFIC_FAILED_GATE, or RETIRE. If G3 awaits a genuine natural trigger, mark READY_PENDING_NATURAL_PROOF with exact trigger, not generic HOLD. After G3, decide in same review cycle; if gate fails, change only affected control and replay that case plus one adjacent regression. No arbitrary observation period. Explicit user authorization and independent production readback required before v5 minor acceptance.

## Version/rollback
If accepted, allocate next available v5 minor control ID in v5 registry, reference exact source and evidence commits, effective time, rollback condition. Keep v6 test candidate and original v5 baseline intact. Do not silently promote.
