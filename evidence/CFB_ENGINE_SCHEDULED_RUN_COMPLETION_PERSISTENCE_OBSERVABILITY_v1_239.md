# CFB Engine — Scheduled Run Completion, Persistence, and Observability Contract v1.239

Status: **ACTIVE OPERATIONAL CONTROL**
Date: 2026-09-27
Parents: v1.229, v1.231, v1.233, v1.235, v1.237, v1.238

## Purpose
Make scheduled CFB work recoverable, auditable, and impossible to confuse with mere scheduler invocation. A scheduler firing is not evidence that the requested engine workflow succeeded.

## Recovery doorway
Every scheduled or recovery run must begin at the newest file matching `CFB_ENGINE_CURRENT_RECOVERY_INDEX_v*.md` on the repository default branch. Select the highest current non-superseded index only after inspecting repository state; read that index and follow its required active-control lineage.

Hard-coded version anchors in task prompts are diagnostic hints only. They never override a newer accepted recovery index.

Older ChatGPT Library/handoff material may support historical recovery but must not replace repository authority when superseded.

If the current recovery index or a required active dependency cannot be recovered and independently read back, fail closed. Never substitute retired production-v1 or reconstruct missing authority from memory.

## Terminal result states
Every scheduled run must end in exactly one engine-workflow state:
- **RUN_PASS** — all required work for that run completed and all required durable outputs were persisted and independently read back.
- **RUN_INCOMPLETE** — recovery succeeded but one or more required downstream prerequisites/outputs could not be completed safely.
- **RUN_FAIL** — authoritative recovery/readback failed or another hard control prevented safe execution.

Scheduler/platform status is separate. A scheduler invocation marked completed/successful does not imply RUN_PASS.

## Durable run receipt
Every scheduled CFB run must persist a small append-only receipt under `evidence/run_receipts/` when repository write access is available. Filename:
`CFB_RUN_RECEIPT_<YYYY-MM-DD>_<HHMMSS>CT_<RUN_TYPE>.md`.

Receipt must contain:
- run type and scheduled/actual timestamp CT where available;
- repository tip observed at recovery start;
- recovery index selected and readback result;
- Beta Champion identity/maturity recovered;
- active controls recovered;
- required upstream inputs and whether each was available;
- production ledger and sandbox ledger recovery state when applicable;
- required deliverables for that run;
- persisted artifact paths/commit SHAs where applicable;
- independent readback result for each required artifact;
- terminal state RUN_PASS/RUN_INCOMPLETE/RUN_FAIL;
- exact blockers/gaps for any non-PASS state;
- next safe action.

If repository write access itself is unavailable, the run must report RUN_FAIL or RUN_INCOMPLETE as appropriate and explicitly identify receipt persistence failure; it may not claim RUN_PASS.

## Completion gate
A run may claim RUN_PASS only after:
1. authoritative recovery succeeded;
2. required workflow steps completed;
3. every required durable artifact was persisted;
4. persisted artifacts were independently rediscovered/read back;
5. the run receipt was persisted and read back.

For Sunday QA specifically, RUN_PASS additionally requires the dated/versioned Weekly Beta Learning Review required by v1.233, including the prominent Champion-vs-Challenger section required by v1.235 and v1.237/v1.238 learning/exposure sections where applicable.

No Weekly Beta Learning Review + readback = no Sunday-QA RUN_PASS.

## Persistence versus delivery
Persistence and user delivery are separate dimensions. The receipt must distinguish:
- ENGINE_WORKFLOW_STATE;
- ARTIFACT_PERSISTENCE_STATE;
- USER_DELIVERY_STATE.

A delivery failure does not erase a valid persisted review. A persisted review does not prove user delivery.

## Failure behavior
Do not silently fall back, silently omit a required artifact, or convert a partial run into PASS. Preserve the last accepted Champion. Identify the narrowest exact failure and the next safe recovery action.

## Scientific boundaries
This control changes recovery/completion/observability plumbing only. It does not modify Champion coefficients, features, predictions, calibration, promotion criteria, market semantics, wager authority, or screenshot boundaries.
