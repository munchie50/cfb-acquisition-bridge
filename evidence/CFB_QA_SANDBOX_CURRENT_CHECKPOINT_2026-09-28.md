# CFB QA Sandbox — Current Checkpoint and Handoff Index — 2026-09-28

Status: CURRENT QA SANDBOX HANDOFF ENTRY POINT — RUN #12 RECONCILED / CORRECTED GENERATOR IDENTITY GATE NEXT
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
Outcome scoring/join: not authorized by current execution authority.

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
- S0 equivalence PASS.
- frozen S1/S2 mapping/spec established.
- rest_days baseline coverage reconciled.
- performance optimization demonstrated material runtime improvement.
- Runs #1–#12 execution history reconciled.
- Run #12 exact cardinality diagnostic complete.
- S2 stale-handler root cause classified.
- bounded implementation correction persisted/read back on main.

ACTIVE/NEXT:
1. Controlled observation of corrected generator identity.
2. Pin exact corrected generator identity in the isolated candidate-freeze workflow without weakening identity controls.
3. Execute fresh outcome-blind candidate freeze.
4. If generation reaches 55,834 and workflow gate passes, retrieve artifact and independently verify manifest/prediction hash, family counts, exact omission identities, forbidden columns, no 2025, outcomes_joined=false, and all frozen input/generator identities.
5. Persist acceptance evidence and read it back. Runner green alone is not acceptance.

BLOCKED:
- Candidate freeze acceptance until corrected generator is pinned and fresh execution independently passes.
- Outcome scoring remains separately unauthorized.

## DO NOT TOUCH
- Champion v1.193 or production coefficients/scaling.
- 2025 protected TEST.
- outcomes/postgame scoring.
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
