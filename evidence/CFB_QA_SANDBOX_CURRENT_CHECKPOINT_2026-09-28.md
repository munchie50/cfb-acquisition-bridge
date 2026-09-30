# CFB QA Sandbox — Current Checkpoint and Handoff Index — 2026-09-28

Current QA status (2026-09-29): **REAL TARGET-SIDE AND v4 SOURCE-CONTEXT CAPABILITIES ACCEPTED / PROSPECTIVE CADENCE WAIT.** Earlier dated statuses are retained as historical evidence; the final 2026-09-29 reconciliation governs the current frontier.

Status: CURRENT QA SANDBOX HANDOFF ENTRY POINT — HISTORICAL OUTCOME SCORING ACCEPTED / S2_K1 CONTINUED-STUDY DISPOSITION PERSISTED
Scope: QA Sandbox only. Production/Champion authority is unchanged.
Parent recovery doorway: evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md
Operating procedure: Production Routine v5 (evidence/CFB_ENGINE_ROUTINE_V5_PRODUCTION_PROMOTION_v1_103.md) + ACTIVE CORE RULE v1.132 (evidence/CFB_ENGINE_CORE_LEARNING_ENFORCEMENT_RULE_v1_132.md) + ACTIVE CORE RULES v1.133 (evidence/CFB_ENGINE_CORE_EXECUTION_CONTROLS_v1_133.md).

## Purpose
Provide one deterministic recovery point for the opponent-strength/small-sample stabilization QA experiment without reliance on conversation history, GitHub Actions color, or filename order.

## Governing science
- evidence/CFB_QA_SANDBOX_OPPONENT_STRENGTH_STABILIZATION_CONTRACT_2026-09-27.md
- evidence/CFB_QA_SANDBOX_S1_S2_TRANSFORM_SPEC_2026-09-27.md
- evidence/CFB_QA_SANDBOX_POOLED_BASELINE_MAPPING_FREEZE_2026-09-27.md
- evidence/CFB_QA_SANDBOX_COMPLETION_SAFE_POPULATION_CHRONOLOGY_2026-09-27.md
- evidence/CFB_QA_SANDBOX_S0_EQUIVALENCE_PROOF_2026-09-27.md
- evidence/CFB_QA_SANDBOX_REST_DAYS_BASELINE_COVERAGE_RECONCILIATION_2026-09-27.md
- evidence/CFB_QA_SANDBOX_S2_FAIL_CLOSED_CARDINALITY_CORRECTION_2026-09-27.md
- evidence/CFB_QA_SANDBOX_EXECUTION_ATTEMPT_LEDGER_2026-09-28.md

Frozen candidate families: S0; S1_K1/K2/K4/K8; S2_K1/K2/K4/K8.
Expected accepted target games: 6,246.
Frozen acceptance expectation: 55,834 rows = S0 6,246 + S1 24,816 + S2 24,772.
Expected S1 omitted games: 42.
Expected S2 omitted games: 53.
2025 protected TEST: forbidden.
Outcome scoring/join: separately authorized, executed, and independently accepted on 2026-09-28; see evidence/CFB_QA_SANDBOX_OUTCOME_SCORING_ACCEPTANCE_2026-09-28.md.

## Authoritative input identities
- dataset: f8c479c83abf5dac3be6dcb4bba3d6a0996ae2623297a9a3514465824b7c4af8
- mechanical primitives: bc02b5cc41eee5cd6f109ccef625c73258efd6347c5d81a8754be4b3a93f4563
- derived primitives: f5a4fac267109cc4b06ceccfa883f1ffaec0ed789aee6c69b25a783a708b8782
- mechanical features: 57aefddf68afdd996c914e5a98bf0ba31710d2a83cf11b192354e93328872a9b
- derived features: 2d36ab91b5d5660e5a7d713b6b89480b93f4ccc31fa6dc30034f9eeba5d60c58
- scaling: 68fb5193ccb8828ac8d34dfe820101181c2bde078a04a6d5afd4c08bcf0cab45
- coefficients: bf15ce41180bfb4e250d311df279e98c13b65432756ae07f7a30264cbae0e221

## Run #11 / #12 reconciliation
Run #11 (36413551460, head 496d5b0b...) proved the optimized implementation reaches candidate cardinality checks in about 19 minutes, but failed before artifact upload at `candidate row count mismatch`.

Run #12 diagnostic (36417777142, head efef5c23...) used the same exact frozen inputs and a diagnostic-only branch that printed cardinality evidence before preserving the existing fail-closed assertion:
- S0: 6,246
- each S1: 6,204
- each S2: 5,731
- total: 53,986
- S1 omissions: exact frozen 42
- S2 omissions: 515
- shortfall vs frozen expectation: 1,848 rows = 462 excess S2 omissions × four k values.

The performance optimization did not introduce the relevant S2 semantics; comparison to pre-optimization generator versions shows the same S2 construction path.

## Root cause and bounded correction
The S2 inner source-opponent baseline handler still recognized obsolete error strings but not the current `unavailable frozen population baseline` emitted by `baseline()`. The error therefore escaped to the outer candidate-level fail-closed handler, dropping the whole target S2 candidate instead of skipping only the unavailable historical opponent residual and retaining other valid residuals.

This is an implementation defect against the already-frozen S2 completion-safe rule, not a scientific reason to redefine the frozen omission expectation.

Corrected implementation on main:
- commit: 2f8aad0963d6a09ae9b8eb749163f3ff65d3566a
- generator Git blob: 40447984a58dbc530cbe942bc1176f0c5bcbe9b2
- changed only the recognized inner source-baseline exception condition to include `unavailable frozen population baseline`.

No Champion/model/science/chronology/k-grid/mapping/coefficient/scaling/2025/outcome rule changed.

## Current frontier
DONE:
- Outcome-blind candidate freeze accepted and construction phase closed.
- Historical outcome scoring separately authorized.
- Authoritative scoring run 36491252415 SUCCESS on exact frozen predictions and accepted v1.179 outcomes.
- 55,834 scored rows, seasons 2016–2024 only; 2025 not accessed; no market/wager/execution inputs.
- Scoring artifact 11000219253, ZIP SHA-256 9fd59b3e98cdf6644cde707ebc991165caacd03ddd48680bce0f463b880e48a3.
- Independent reproduction accepted; see evidence/CFB_QA_SANDBOX_OUTCOME_SCORING_ACCEPTANCE_2026-09-28.md.
- S2_K1 is the only candidate supported for deeper bounded disposition review. Its common-game margin MAE and proper win metrics improve, with margin improvement in 7 of 9 seasons and stronger results in predeclared large-disagreement slices.
- S2_K1 also has mixed evidence: slight aggregate total-MAE and winner-direction degradation, 2022/2024 margin exceptions, and history-depth stability unavailable because the required field was not frozen. No post-outcome reconstruction is allowed.

ACTIVE:
- Prospective S2_K1 continuation is frozen by evidence/CFB_QA_SANDBOX_PROSPECTIVE_S2_K1_CONTINUATION_CONTRACT_2026-09-28.md.
- BLOCKED implementation gate: generalized S0 refresh producer v1.246 exists, but exact executable equivalence to accepted v1.206 is pending. See evidence/CFB_QA_REFRESH_V1_246_EQUIVALENCE_STATUS_2026-09-28.md. 
- External cadence WAIT remains: do not manufacture a weekly snapshot.

CURRENT CLASSIFICATION:
- S2_K1 may continue in Sandbox study because the historical signal is broad enough to warrant further prospective validation.
- This is NOT scientific acceptance, Challenger promotion, Champion mutation, refit, recalibration, or production authorization.
- The original stability bar is not fully demonstrated because the predeclared history-depth diagnostic is unavailable.
- S0 remains the control and production/Champion authority is unchanged.

NEXT:
1. Preserve S2_K1 exactly as frozen; no post-outcome parameter tuning or k-grid expansion.
2. First execute and independently read back the exact v1.246-vs-v1.206 equivalence gate. Structural review alone is not acceptance.
3. Do not build or execute the live S2_K1 companion on v1.246 until that gate passes.
4. After equivalence acceptance, complete the separate S2_K1 companion and its outcome-blind identity/structural gates.
5. At the next v1.216 weekly cadence, run current source preflight; only a qualified fresh state may create REFRESH_SNAPSHOT artifacts.
6. If refresh is a no-op, create no QA snapshot.
7. Keep 2025 TEST protected unless separately authorized; independently evaluate any future prospective window only under separate scoring authority.

## DO NOT TOUCH
- Champion v1.193 or production coefficients/scaling.
- 2025 protected TEST.
- any new outcome/postgame scoring outside separately authorized bounded evaluation.
- frozen S1/S2 formulas, mapping, k-grid, chronology, or expected omission sets absent new pre-outcome evidence.
- market/wager/execution data as model inputs.
- production promotion.

## Recovery/staleness rule
If this checkpoint names an ACTIVE external run that is already terminal, or its parent recovery doorway is superseded, classify this checkpoint as STALE-NEEDS-RECONCILIATION before following its NEXT instructions. Recover terminal evidence first; do not blindly rerun or mutate.

## Process learning
- Repeated expensive execution failure triggers structural/performance investigation before more resources.
- Row/key availability is weaker than semantic completion-safe availability.
- Diagnostic gates should expose actual cardinality/omission evidence before a generic cardinality assertion when doing so does not weaken fail-closed behavior.
- Identity controls remain mandatory even when their controlled-stop ergonomics are inconvenient.
- A lesson is not closed until persisted, read back, and later demonstrated.


## 2026-09-29 reconciled current frontier — supersedes older ACTIVE/NEXT statuses above
Direct terminal/artifact reconciliation accepted:
- real S0 target-side boundary: CFB_QA_V1_246_REAL_TARGET_SIDE_ACCEPTANCE_2026-09-29.md (run 36636336698, artifact 11064541770; 1,114 sides);
- v4 source-context capability: CFB_QA_S2_K1_SOURCE_CONTEXT_V4_ACCEPTANCE_2026-09-29.md (run 36637810698, artifact 11065575217; 4,355 context rows, 662 rows per primitive surface).
Exact hashes, counts, independent semantic proof and limitations are in those acceptance records. All 1,114 target-side counts, including six zero-history cases, passed. No S2 predictions or 2026 S2 outcomes evaluated.
Current disposition: ACCEPTED QA INPUT CAPABILITIES / S2_K1 STILL STUDY-ONLY / CADENCE WAIT.
v1.246 and source-context infrastructure gates are closed for these retained bytes. Do not blindly rerun earlier pending dependencies. Original historical raw-byte replay limitation remains.
Next: at the next v1.216 weekly cadence, requalify source state and determine refresh/no-op before constructing/producing a prospective S2 consumer. September 29 is within the cycle anchored by September 26 FIRST_FROZEN; no exception is authorized here. Structural QA runs do not constitute an operational prospective refresh.
No-op means no manufactured snapshot. Qualified consumer/freeze must remain exact k=1, use same-cutoff accepted boundaries, whitelist frozen input fields, freeze deterministic history-depth slices, and remain separate from S0. Outcome scoring remains separately gated. Champion unchanged.


## Cadence-wait independent-work sweep — 2026-09-29
Read-only next-cycle plumbing/retention audit: `CFB_QA_CADENCE_WAIT_READINESS_AUDIT_2026-09-29.md`.
Existing workflows are evidence for the September 29 boundary, with pinned inputs and finite artifact retention; they are not an automatic fresh prospective freeze. The S0 retained package excludes prediction-file bytes. Next-cycle prerequisites and retention metadata are recorded in the audit. No new executable, scientific acceptance, or cadence exception is introduced. Current frontier remains CADENCE WAIT.


## Accepted-boundary preservation — 2026-09-29
`CFB_QA_ACCEPTED_BOUNDARY_ARCHIVE_2026-09-29.md` records byte-identical secondary archives of raw artifact 11031055060, S0 artifact 11064541770 and v4 artifact 11065575217. All saved copies passed independent materialization and exact ZIP-byte/hash readback. The finite GitHub-retention gap for these packages is closed; absent S0 prediction-file bytes and original historical replay limitations remain. Scientific frontier stays CADENCE WAIT.


## 2026-09-30 weekly no-op enforcement correction
Cadence-wait routine review found that the installed Tuesday scheduler proved future targets but did not compare fresh source identity with the last independently accepted prediction-source boundary. This could manufacture a candidate boundary on unchanged source bytes, contrary to v1.218/v1.247.

Correction persisted in `CFB_QA_WEEKLY_SOURCE_STATE_NOOP_GATE_CORRECTION_2026-09-30.md`.
The operational pointer `evidence/operational/CFB_ACCEPTED_PREDICTION_SOURCE_STATE.json` is initialized from accepted v1.208/v1.218 source identities and may advance only after a later prediction boundary is independently accepted and persisted. Tuesday now exits as a successful no-op before Champion-fit/S0/context execution when source identities are unchanged or no future targets remain.

Scientific frontier remains CADENCE WAIT. No workflow was dispatched, no prediction generated, no S2 consumer built, no 2025 TEST accessed, and Champion remains unchanged. Real-path demonstration of the installed trigger is pending the next normal Tuesday run.


## 2026-09-30 weekly no-op regression guard
Routine WAIT-sweep follow-through added a dedicated static regression guard for the accepted-source no-op correction. See `CFB_QA_WEEKLY_SOURCE_STATE_NOOP_REGRESSION_GUARD_2026-09-30.md`.

The guard fails if the accepted-source pointer loses required governance/source identities, if Tuesday stops comparing fresh schedule/PBP identities with the accepted pointer, or if Champion-fit/S0/context/package/upload work becomes unconditional. It is wired to changes in the Tuesday workflow, pointer, guard script, and guard workflow.

Static repository readback is verified. Runtime execution is not claimed because the available connector run helper exposes PR-triggered runs only and returned no proof for the push-triggered workflow. Frontier remains CADENCE WAIT; no operational snapshot or scientific evidence was created.


## 2026-09-30 Wednesday fallback cycle binding
Routine chain review found that Wednesday's original 36-hour success test could let a manual/test Tuesday run suppress the normal weekly fallback. The correction is persisted in `CFB_QA_WEDNESDAY_FALLBACK_CYCLE_BINDING_CORRECTION_2026-09-30.md`.

Wednesday now accepts only a successful scheduled Tuesday run from the immediately preceding UTC calendar day as the weekly disposition. Otherwise it dispatches the bounded Tuesday fallback once. A dedicated static regression gate protects that binding and rejects restoration of the broad 36-hour rule.

The same review confirmed Monday readiness and Tuesday reacquisition are intentionally separate: Monday proves readiness; Tuesday must capture the actual immutable candidate cutoff with freshly qualified same-cutoff raw bytes. Frontier remains CADENCE WAIT; runtime demonstration is pending normal schedule.


## 2026-09-30 generic weekly REFRESH_SNAPSHOT acceptance readiness
Routine acceptance-path review found that the existing v1.207 independent acceptance audit is FIRST_FROZEN-specific and cannot accept a normal v1.246 REFRESH_SNAPSHOT. The next weekly candidate therefore lacked a generic independent acceptance executable.

`scripts/cfb_qa_weekly_refresh_acceptance.py` now supplies that bridge without self-acceptance. It requires the complete retained v1.246 S0 package, independently verifies population/chronology/model identity/output hashes, recomputes predictions, and emits exact raw schedule/PBP hashes for a later accepted-source pointer advance.

A static regression gate rejects FIRST_FROZEN fixed counts/artifact IDs in the generic audit. The audit is deliberately not wired to candidate generation; actual weekly bytes must still be independently recovered, audited, accepted, persisted and read back before pointer advancement or S2_K1 consumer execution.

See `CFB_QA_WEEKLY_REFRESH_ACCEPTANCE_READINESS_2026-09-30.md`. Frontier remains CADENCE WAIT.


## 2026-09-30 accepted-source pointer advancement readiness
Post-acceptance dependency review found no bounded transition procedure from a persisted weekly REFRESH_SNAPSHOT acceptance to the canonical accepted prediction-source pointer. `scripts/cfb_qa_prepare_accepted_source_pointer.py` now prepares—but cannot persist—that transition.

The preparer requires a later-cutoff PASS acceptance with independent recomputation/hash/chronology proof, forbidden outcome/market/refit states false, changed schedule/PBP identities, and an explicit persisted acceptance-evidence record. A static gate prevents the preparer from acquiring repository/network mutation capability.

Required order is now explicit: candidate → independent audit → persisted/read-back acceptance → pointer preparation → separate canonical pointer write → direct pointer readback. See `CFB_QA_ACCEPTED_SOURCE_POINTER_ADVANCEMENT_READINESS_2026-09-30.md`.

Current pointer remains unchanged at v1.208/v1.218. Frontier remains CADENCE WAIT.


## 2026-09-30 prospective S2_K1 consumer specification freeze
Routine S2 handoff review confirmed the historical Sandbox generator cannot be reused directly for prospective execution because it is bound to the historical 2016–2024 population/cardinalities. The accepted v4 source-context capability plus accepted weekly S0 boundary are the correct prospective substrate.

`CFB_QA_PROSPECTIVE_S2_K1_CONSUMER_SPEC_2026-09-30.md` now freezes the future consumer interface/mechanics before live execution: exact k=1, frozen ten-feature mapping, seven S1-only features, same-cutoff accepted S0+v4 inputs, explicit field allowlist, no unused winner/rank metadata, fail-closed eligibility, frozen history-depth slices, v1.193 scaling/coefficients, separate S2 artifact, and pre-outcome freeze/readback gate.

A static gate rejects prospective k-grid expansion and loss of the chronology/contamination/output locks. No consumer prediction was generated and actual execution remains gated on the next independently accepted weekly S0 plus same-cutoff accepted v4 context boundary. Frontier remains CADENCE WAIT.
