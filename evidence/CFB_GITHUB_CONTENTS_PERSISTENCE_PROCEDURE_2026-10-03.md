# CFB Engine — GitHub Contents Persistence Procedure — 2026-10-03

Status: ACTIVE OPERATIONAL PERSISTENCE PROCEDURE
Scope: GitHub persistence mechanics only; no scientific, Champion, prediction, market, decision, execution, or outcome semantics change.

## Purpose
Repair the repeated Market Monitor persistence failure by binding governed repository writes to the connected GitHub Contents operations that have been directly demonstrated.

## Required write primitives
1. New append-only receipt/evidence file: use create_file on the intended branch, then independently fetch_file and verify path/content.
2. Existing canonical surface: fetch_file immediately before mutation, retain its current blob SHA, construct the complete new file content by appending the governed delta without rewriting historical entries, call update_file with that exact fetched SHA, then independently fetch_file and verify the expected append and resulting blob SHA.
3. Writes to the same path are strictly serial. Never issue parallel update/delete operations for one path.
4. A stale-SHA conflict or failed readback is a persistence failure. Re-fetch current state and reconcile; never overwrite competing changes or silently retry from stale content.
5. create_file is prohibited for an existing canonical surface; update_file is prohibited for a new receipt path.
6. RUN_STARTED and terminal receipts are distinct new append-only files unless an active receipt contract explicitly requires a single file. RUN_STARTED never proves completion.

## Completion interaction
v1.239/v1.242 remain governing completion/evidence controls. RUN_PASS still requires applicable canonical surface persistence/readback, Hot Sheet persistence/readback, and terminal receipt persistence/readback. This procedure only specifies the safe connector mechanics used to satisfy those controls.

## Direct demonstration
2026-10-03 diagnostic:
- create_file -> independent fetch_file readback: PASS
- fetch_file current blob SHA -> update_file -> independent fetch_file readback: PASS
- diagnostic path: evidence/run_receipts/CFB_GITHUB_WRITE_PATH_DIAGNOSTIC_2026-10-03.md
- governed engine-state mutation during diagnostic: NONE

## Failure correction
Prior statements that the connected repository was generally unable to write are superseded. The demonstrated failure class is incorrect/unsupported persistence invocation, not repository-wide write denial.

Scientific effect: NONE.
Champion effect: NONE.
