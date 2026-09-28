# CFB QA Sandbox — Current Checkpoint and Handoff Index — 2026-09-28

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
