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


## 2026-10-09 Health terminal-failure containment integration

Observed evidence: recovered indexed October 8 21:42:36Z Dual Engine Health response reports RUN_INCOMPLETE and two rejected CFB health-receipt writes. It describes a non-authoritative fallback, but its exact file identity and the original tool trace/error/payload are not recovered. This is reported runtime evidence, not new durable closure or narrower rejection-cause proof.

For the CFB portion of Dual Engine Health, explicitly apply this procedure's permitted persistence primitives, atomic provenance, allowed rejection handling and terminal-persistence-unavailable response envelope, with the October 5 two-phase terminal closure contract. An incomplete or rejected health-receipt write must preserve the unresolved audit coverage boundary. Never advance that boundary from last_run_time or another task's PASS.

The Health invocation must not disable/change schedules or create/dispatch replacement tasks because its own repository/tool work failed. Its existing separately governed Market Monitor enabled-state recovery remains permitted only when all existing ownership/cadence/scope/conflict checks pass, followed by independent four-task readback and truthful recovery reporting. A blocked recovery receipt means reported recovery with durable evidence unavailable; configuration readback and receipt persistence are separate proof classes.

If terminal persistence is unavailable, report RUN_INCOMPLETE/RUN_FAIL as earned, TERMINAL_PERSISTENCE_UNAVAILABLE and the permitted content-free diagnostic envelope. Missing exact fields must be explicitly UNAVAILABLE, never reconstructed from later successful writes. A fallback file/chat response is not a GitHub terminal receipt, not authoritative operational completion and not RUN_PASS. Do not use another destination or operation to evade a write restriction. Preserve all historical failures.

Integration status: installed operational containment; natural Health success/failure demonstration remains pending. This does not identify or repair the opaque connector rejection and does not change scientific/model/Champion authority or task cadence.

## October 9 accepted-write / prior-version readback reconciliation

Two immediate post-update fetches in user-directed QA failed the expected-content check. For the recovery-index update, the accepted write returned commit 67976b33dabdcf31f4c60bd7f2ca198411d7b15d and blob 256c1e698d21c9aecbbbbb1715c56b20eeb04e12 while the immediate main fetch returned the exact prior blob 1c4ea311ad20e29d351fe2d1c74bdbe86fd4adbb. Subsequent independent exact-commit and main reads matched the planned content/blob. No write was repeated. The other accepted QA append subsequently read back exactly; its first response was not retained, so its initial blob is not claimed.

This establishes a prior-version post-write read, not its caching/replication cause and not the earlier rejected-write cause. A write response alone still never establishes completed readback.

If a permitted update returns a commit/content identity but immediate readback mismatches:
1. Retain the accepted-write response, proposed content/blob digest and observed readback blob. Stop downstream completion claims. Do not repeat the write merely because the read mismatched.
2. Use bounded read-only reconciliation: independently fetch the affected file at the returned immutable commit, then independently fetch the same path on the intended current branch. Compare exact expected content/blob, and inspect commit ancestry/current branch if needed. No fallback destination, alternate mutation primitive or restricted-action bypass is authorized.
3. If both exact-commit and current-branch evidence match, record initial mismatch plus successful independent reconciliation. Only then continue the original completion/closure checks.
4. If a read is blocked, the commit/file is absent, or the branch still differs after this bounded reconciliation, keep the affected work RUN_INCOMPLETE with the last proved stage. Classify a genuine competing change separately and reconcile from fresh current bytes under the existing serialized SHA rule; never overwrite it or pretend the originally planned readback passed.
5. An opaque/rejected write without a proved accepted commit continues to follow the existing rejection rules. This guard grants no additional write retry. Natural producer use remains DEMONSTRATION_PENDING; the observed manual exact-commit/current-branch recovery is bounded proof only.

This read-only reconciliation strengthens existing independent readback. No schedule, scientific, Champion or semantic authority change.

## October11 recovery-index pre-write validation and rejected-checkpoint containment

Trigger: any mutation of the tagged current recovery navigation. The reader validates EVERY active tagged checkpoint, not only the last. A new valid tail cannot repair an earlier active malformed record or duplicated/reversed checkpoint clock. Never assume append-only construction proves conformance.

Before writing the complete proposed index:
1. Recover the exact current blob and entire active history; assemble the full proposal against those bytes.
2. Apply unchanged scripts/cfb_recovery_navigation_reader.py to that complete proposal with actual timezone-aware current UTC. Verify accepted fields, evidence/-only paths, unique pointers, strictly increasing active checkpoint clocks, no future clock, and no uncheckpointed tail. Independently reconcile each applicable current source/view pointer; navigation output itself is not source readback.
3. Inspect the actual validator result before issuing update_file. A failing proposal must not reach repository mutation. When computation is unavailable, perform the equivalent complete validation and state what remains unverified; do not claim an executable ran or use post-write CI as prospective proof.
4. Preserve prior valid records and all failed-run evidence. An old malformed active record is not permission to relax reader validation. Reclassifying historical fence status requires specific user/accepted governance direction; do not silently erase, rewrite JSON, invent chronology or self-authorize quarantine.
5. Under the user's narrowly directed October11 repair only, two QA-authored19:02:07Z malformed opening fences are now cfb-frontier-json-rejected. Complete original JSON, all other prior bytes, original Git blobs/commits and incomplete receipts remain intact. Rejected records are historical evidence, not active navigation or accepted claims. Any such authorized reclassification must be followed by a fresh valid final checkpoint and independently executed full reader/source/display checks.
6. After accepted write, independently fetch exact expected content/blob and use existing immutable-commit/current-branch reconciliation if needed. Preserve actual original failures; a subsequent repair never upgrades an earlier RUN_INCOMPLETE.

Demonstrated current repair: complete local proposal validated before update,20navigation assertions preserve invalid-active-history, duplicate/reversed-clock, rejected-tail and no-active-recovery rejection. Strict reader unchanged. Full independent GitHub/current pointer reconciliation remains separately required before closure. Future producer pre-write use remains DEMONSTRATION_PENDING; no broad scheduler/rejection class closure.
Scientific/Champion/model/task schedule effect NONE.


## October17 complete recovery-consumer preflight

Before appending a new cfb-frontier-json checkpoint, recover the previous complete checkpoint and all current consumer requirements. A new checkpoint replaces navigation as a whole; unchanged money/weekly/source references are not inherited automatically. Reconcile required references explicitly, preserving exact hashes and active role uniqueness; do not guess a missing reference from filenames.

Run `python scripts/cfb_recovery_consumer_preflight.py --index <complete-proposed-index> --repository-root <recovered-repository>` at the actual clock BEFORE the index write. It verifies every declared pointer against recovered bytes, the currently qualified money/weekly-source consumers and current sheet/decision binding. Any omission, stale hash, missing/ambiguous current role or source-binding error blocks the navigation write; repair the proposal, never weaken the guard. This bounded preflight uses current qualified Week7/October11-review dependencies; separately qualify a changed weekly consumer rather than carrying this boundary into a different week by assumption.

After fresh-SHA update/readback, repeat the preflight on independent readback bytes and require the existing full Hot Sheet workflow result before claiming integrated validation. If runtime/recovered dependencies are unavailable, report incomplete verification. Preflight is navigation integration only: not market freshness, model acceptance, earned recommendations, current operational readiness or RUN_PASS. Existing two-phase closure requirements and historical failure preservation remain unchanged.


## October19 CT exact large-file transfer verification

Manual recovery QA caught a shell-output transport truncation while moving the large recovery index into a Contents update. The intermediate malformed commit is preserved; complete original bytes plus validated append were restored and independently matched to expected Git blob2bca8206d06285bb8b30c49465fb8663c3b7b435. Never use a truncated tool-output string as file content. Recover complete content through structured blob retrieval or bounded exact chunks; compare expected full character/byte length and Git blob hash before write and independently after readback. Equality against the same truncated proposal is insufficient. Reject truncation banners/elision markers introduced by transport. Complete local validation does not establish that the connector received those local bytes. Existing stale-SHA, serialized writes and no-repeat-after-accepted-write rules remain unchanged.

## October23 authority and observed-clock declarations

Apply the existing exact-identity/readback rule to hashes and clocks written INSIDE an audit, preflight or receipt, as well as to the identity of that file. A correct file blob does not validate its internal declarations.

Before persisting those declarations, bind each authority path to the exact recovered commit/ref and independently returned Git blob SHA. Compare the value to the proposed text. Label SHA-256 and Git blob SHA separately. An unavailable exact binding remains UNVERIFIED; a mismatch must be reported explicitly and cannot establish accepted authority or advance an audit coverage watermark. Do not copy an earlier receipt's authority hashes without checking its stated ref. The existing full navigation preflight remains the navigation check; it does not verify arbitrary prose inside referenced audits.

Acquire any field called actual/current/as-of run clock from the runtime at the point the work occurs. Preserve an earlier source or canonical input boundary under its own label. Do not choose a future round-minute clock for preflight, publication, terminal recording or a historical check, and do not present a run-start clock as terminal-record creation time. In historical reconciliation, compare a claimed observed clock with the immutable commit that first saved it. A later claimed clock makes that original timing proof inconsistent; retain the discrepancy rather than using a later replay to validate it retrospectively. If independently observed clock evidence is unavailable, say CLOCK_UNVERIFIED and retain the last proven stage.

October22 Health's two mismatched authority hashes and October23 Evening's preflight observed-clock claim are preserved historical evidence errors. Exact correction/disposition belongs in the linked October23 reconciliation, not a rewritten original receipt. Content-level rejection of those declarations is demonstrated against immutable history; natural producer compliance remains DEMONSTRATION_PENDING at the next applicable existing invocation. This clarification adds no new task, schedule, software gate, model or betting prerequisite. Existing persistence retries, closure rules and permission boundaries continue to apply.

## October23 repeated transfer and incomplete handoff correction

The scheduled morning Monitor again persisted a truncated large market file, repaired it, then declared RUN_PASS without advancing recovery navigation. Independent current consumer preflight and existing CI still failed. Preserve that run's original receipts as reported status; later manual repair does not prove its original integration succeeded.

Use the bounded transfer mode of the existing scripts/cfb_planned_append_metadata.py when moving complete local proposals through tool text. First obtain its manifest with --transfer-file FILE --expected-transport-sha EXPECTED_GIT_BLOB; then request each zero-based --chunk-index exactly once. The default and maximum chunk size is12000Unicode characters. Each response binds the same complete source hash, total bytes/characters/count and its own chunk identity. Changed/truncated source fails before emission. These successful responses are transport evidence only.

At the receiving tool-orchestration boundary, parse every chunk as JSON, check exact consecutive indices/count and chunk identities, concatenate content in order, and independently recompute the COMPLETE outgoing argument's UTF-8 byte count and Git blob. Compare against the planned manifest before calling create_file/update_file. A length check alone is insufficient. Never manually reconstruct content from an abbreviated tool view. Missing, duplicated, reordered or changed pieces block the write. Preserve full-content SHA-guarded serialized Contents writes and independent complete readback; transport chunks are not separate semantic repository writes. No transport operation authorizes a rejected action or bypasses permission restrictions.

After all market/decision/scorecard/Hot Sheet changes, update the complete recovery frontier to the exact current canonical blobs and sole selected current sheet, retaining all unchanged consumer references and historical records. Validate the complete proposal before its write, independently read back all saved bytes, then run the existing complete consumer preflight on actual saved files. Require the existing selected-publication CI integration result before claiming integrated success. Perform these existing checks BEFORE terminal RUN_PASS, even if no new index was initially planned. A saved sheet alone cannot close an incomplete handoff. If a required check fails or is unavailable, report RUN_INCOMPLETE with the exact next action; retain successful research/publication as bounded progress.

This is a correction to the existing producer finish path, not a new betting gate, task, cadence, review quota or model. The Monitor prompt explicitly consumes it; full natural compliance remains pending at the next existing invocation. Bounded authentic replay and manual end-to-end proof belong in this repair's audit/closure.
