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


## 2026-10-03 canonical-update hardening
Observed evidence:
- 07:19 CT: full canonical existing-file updates succeeded using immediate fetch -> exact blob SHA -> update -> readback.
- 13:00 CT: two attempts to append a larger externally researched market delta to CFB_MARKET_MONITOR_STATE were rejected by the connected write-safety layer.
- 21:55 CT diagnostic: the same canonical file accepted and independently read back a minimal operational-only SHA-guarded append.

Classification: connector write-safety/content-envelope rejection, not repository-wide write denial, branch failure, persistent permission failure, or broken existing-file update primitive. The exact proprietary safety trigger is not exposed, so do not claim a narrower cause without evidence.

Required hardening for scheduled runs:
1. Keep each canonical mutation to the smallest governed delta required for that surface. Do not resend/rewrite unrelated historical prose beyond the complete file content mechanically required by update_file.
2. Separate market observations, decision transitions, Hot Sheet rendering, settlement, and diagnostics into their own serialized surface writes; never combine them into one oversized semantic mutation.
3. If a canonical update is rejected, immediately re-fetch the same path and verify whether any competing change occurred.
4. If SHA is unchanged, retry once with a reduced/minimal delta that preserves the same governed facts and provenance without optional explanatory prose. This is a persistence-envelope retry, not permission to omit required data, alter semantics, or backfill.
5. If the reduced retry also fails, terminate RUN_INCOMPLETE with the rejected surface named. Do not proceed as though downstream surfaces incorporated the missing state.
6. Never split one logical market observation in a way that loses timestamp/source/book/availability/executability/provenance. Required observation fields remain atomic.
7. Never retry after a deadline by reconstructing prospective state from outcomes. Historical incomplete cycles stay incomplete.
8. A diagnostic probe may establish write-path health but cannot upgrade a historical RUN_INCOMPLETE to RUN_PASS.

Scientific effect: NONE. Champion effect: NONE.

## 2026-10-09 test-routing planned-append metadata capture

Purpose: preserve content-free evidence for future permitted canonical append attempts. This does not resolve the October 8 rejection cause, reconstruct a missing historical payload, authorize a rejected action, or certify a production run.

1. Before each permitted append attempt, retain its run identity, attempt number, operation and target path, and the immediately fetched baseline blob SHA. Where a computation runtime is available, compute the proposed complete-content and appended-delta SHA-256 digests, proposed Git blob SHA, UTF-8 byte lengths, Unicode character counts, and whether all prior bytes are preserved.
2. The read-only helper scripts/cfb_planned_append_metadata.py computes those values from local baseline and proposal files. Supply --prior, --proposed, --expected-prior-sha and a comma-separated --inventory. It rejects stale baselines, rewritten history, invalid UTF-8, and empty, duplicate or unsupported inventory names. It never invokes a repository write.
3. Governed field inventory is caller-declared: game_identity, observation_timestamp, source, book, line, price, availability, executability, provenance, champion_snapshot, decision_state. Include only applicable names. Inventory presence is not semantic validation of their values or completeness.
4. If computation is unavailable, explicitly record HASH_UNAVAILABLE or SIZE_UNAVAILABLE with the reason; never invent metadata. A helper result is PROPOSED_ONLY_NOT_WRITE_SUCCESS and is not proof that the connector received or accepted those exact bytes.
5. When allowed, preserve the metadata with the run receipt. After rejection, record the observed failure classification and permitted non-sensitive explanation, then immediately re-fetch the target and retain the observed blob SHA. Bind each allowed reduced attempt to its own metadata; do not conflate attempts.
6. Do not archive raw rejected content, secrets, or restricted tool traces through this procedure. Do not encode, relocate or split content to evade a restriction. Existing rejection handling, atomic governed observation fields, deadlines and terminal closure requirements remain governing.
7. Successful append completion still requires independent canonical readback matching the proposal and the separately verified terminal closure. Metadata alone cannot upgrade RUN_INCOMPLETE.
8. Test-routing verification: the helper passed 11 synthetic metadata and fail-closed assertions, including independent Git blob hashing, delta hashing, UTF-8 byte/character distinction, no raw content in output, proposal-only status, stale SHA, historical rewrite, duplicate/unknown inventory and invalid UTF-8 rejection. A zero-length delta is metadata only and does not establish a mutation.

Integration: Market Monitor already names this persistence procedure as an authority. No recurring task prompt, schedule or enabled state is changed. Runtime use and receipt capture in a natural scheduled production attempt remain unverified.

Scientific effect: NONE. Champion effect: NONE. Production rejection root cause: OPEN.

## 2026-10-09 scheduled-run failure containment and task lifecycle guard

Scope: error containment for existing engine schedules. User-authorized topology remains the four recurring production tasks with their existing cadences; the temporary diagnostic canary and retired duplicates remain disabled.

A repository/tool rejection or an incomplete engine cycle stops the affected operational mutation and triggers truthful terminal reporting under the closure contract. It does not grant the scheduled engine invocation authority to disable itself or another recurring task, alter prompts/cadences, create a replacement task, or initiate another run.

Within scheduled Market Monitor and Evening Availability invocations:
1. Keep automation-management mutations out of the engine work path. Scheduling/lifecycle changes require an explicit user-directed scheduling or QA instruction; failure alone is not that instruction.
2. Preserve the failure. Attempt a permitted terminal candidate naming completed work, unresolved surfaces, observed blocker and next safe action; independently read it back before a separate closure. If receipt persistence is unavailable, report TERMINAL_PERSISTENCE_UNAVAILABLE with the permitted observed explanation, never manufacture repository closure.
3. Continue to respect write restrictions and allowed retry limits. Keeping a schedule enabled does not authorize bypassing restrictions, repeating rejected actions, completing downstream work from missing state, or claiming success.
4. During user-directed QA, inspect topology independently. Reconcile any drift against current user instructions before correction; never undo an explicit user pause.
5. Installation/readback is not a natural execution demonstration. This guard remains NATURAL_DEMONSTRATION_PENDING until later applicable scheduled invocations preserve topology and produce honest terminal evidence.

Observed motivating cases: recovered October 8 Evening Availability response says it disabled its recurring task after write rejection; that task was restored. October 9 morning Market Monitor is observed disabled after a STARTED-only cycle. The latter disabling actor/reason is not established by the available metadata; do not assert an identical cause without a trace.

Scientific effect: NONE. Champion effect: NONE. Existing schedule cadence and protected evidence boundaries unchanged.

## 2026-10-09 terminal-persistence unavailable response envelope

Trigger: a permitted terminal receipt cannot be persisted/read back. Keep the affected operational run incomplete and preserve task lifecycle under the guard above.

When permitted, the final run response must carry a small content-free diagnostic envelope: run identity, reported terminal status, last proven stage, failed target path/operation and actual tool name, allowed observed rejection classification/code, baseline/refetched SHA, each attempted proposal/delta digest and byte/character length when computed, attempt count, and terminal_persistence=UNAVAILABLE. Reuse already computed values; if absent, explicitly say HASH_UNAVAILABLE, SIZE_UNAVAILABLE, ERROR_DETAIL_UNAVAILABLE or TOOL_NAME_UNAVAILABLE. Distinguish intended proposal metadata from proof of connector receipt.

A chat response is reported runtime evidence, not durable repository closure or RUN_PASS. It does not authorize exposing restricted error details, raw attempted bodies or secrets, nor retrying via another destination to bypass a rejection. The envelope improves permitted observability even when a durable terminal cannot be written.

Motivation: recovered October 9 07:04 response reports two market-update and two terminal-receipt rejections but lacks exact operation names/errors/proposal metadata. Do not reconstruct them from later successful manual writes.

Status: RESPONSE_REQUIREMENT_INSTALLED; natural failure-response demonstration pending. This does not fix the opaque write restriction.

## 2026-10-09 pre-write benchmark envelope validation

For permitted new pregame retrieval-only public benchmark observations, scripts/cfb_benchmark_observation_envelope.py provides a deterministic typed formatter before the first write attempt. It does not invoke a write or qualify source truth. Use --input JSON, --as-of timezone-aware timestamp and --run-id. When this runtime is unavailable, do not claim its validation ran.

The narrow envelope preserves source/game identity, observed and source-scheduled kickoff timestamps, source URL/book label/provenance, retrieval-only time semantics, unknown offer update time, unverified execution status and atomic side-specific spread/total/moneyline quote availability. Missing prices remain null; genuinely not-yet-available selections have null values and explicit availability. Preserve asymmetric side-specific numbers; never create a consensus by coercion.

Duplicate JSON keys/identities, unknown or missing fields, copied outcome/raw-body fields, control characters, malformed timestamps/URLs/numbers and a false verified-execution claim fail closed. It never accepts bookmaker-update timing or post-kickoff captures under this retrieval-only pregame schema; use the separately governed appropriate observation path for other valid classes rather than relabelling them.

Source qualification, exact frozen game mapping, actual kickoff conflicts, current availability, practical execution and betting decisions remain separate gates. Do not discard known facts or observations to satisfy this schema. Canonical append still requires immediate fetch, preserved prior bytes, exact SHA, planned-attempt metadata and independent readback. This helper is not authority to reinterpret/replay restricted rejected content or bypass a write rejection.

Demonstration: thirty boundary/rejection/CLI checks and deterministic replay of five genuinely retained October 9 07:34 observations passed. Input/output retained only under evidence/scheduler_qa/; no new market/decision observation, canonical mutation or scheduled test was made by this replay. Actual production failure cause and natural producer integration remain OPEN.
