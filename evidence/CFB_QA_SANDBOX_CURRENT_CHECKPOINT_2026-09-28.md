# CFB QA Sandbox — Current Checkpoint and Handoff Index — 2026-09-28

Status: CURRENT QA SANDBOX HANDOFF ENTRY POINT — EXECUTION IN PROGRESS
Scope: QA Sandbox only. Production/Champion authority is unchanged.
Parent recovery doorway: evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_243.md
Routine: Production Routine v5.

## Purpose
Provide one deterministic recovery point for the active opponent-strength/small-sample stabilization QA experiment so a new chat/operator does not reconstruct state from conversation history, GitHub Actions icons, or filename order.

## Governing science
Primary contract: evidence/CFB_QA_SANDBOX_OPPONENT_STRENGTH_STABILIZATION_CONTRACT_2026-09-27.md
Transform: evidence/CFB_QA_SANDBOX_S1_S2_TRANSFORM_SPEC_2026-09-27.md
Population baseline freeze: evidence/CFB_QA_SANDBOX_POOLED_BASELINE_MAPPING_FREEZE_2026-09-27.md
Completion-safe chronology: evidence/CFB_QA_SANDBOX_COMPLETION_SAFE_POPULATION_CHRONOLOGY_2026-09-27.md
S0 proof: evidence/CFB_QA_SANDBOX_S0_EQUIVALENCE_PROOF_2026-09-27.md
Rest-days correction: evidence/CFB_QA_SANDBOX_REST_DAYS_BASELINE_COVERAGE_RECONCILIATION_2026-09-27.md
S2 cardinality correction: evidence/CFB_QA_SANDBOX_S2_FAIL_CLOSED_CARDINALITY_CORRECTION_2026-09-27.md

Frozen candidate families: S0; S1_K1/K2/K4/K8; S2_K1/K2/K4/K8.
Expected accepted target games: 6,246.
Expected prediction rows: 55,834 = S0 6,246 + S1 24,816 + S2 24,772.
Expected S1 omitted games: 42.
Expected S2 omitted games: 53.
2025 protected TEST access: forbidden.
Outcome scoring/join: not authorized by current execution authority.

## Authoritative input identities
- dataset: f8c479c83abf5dac3be6dcb4bba3d6a0996ae2623297a9a3514465824b7c4af8
- mechanical primitives: bc02b5cc41eee5cd6f109ccef625c73258efd6347c5d81a8754be4b3a93f4563
- derived primitives: f5a4fac267109cc4b06ceccfa883f1ffaec0ed789aee6c69b25a783a708b8782
- mechanical features: 57aefddf68afdd996c914e5a98bf0ba31710d2a83cf11b192354e93328872a9b
- derived features: 2d36ab91b5d5660e5a7d713b6b89480b93f4ccc31fa6dc30034f9eeba5d60c58
- scaling: 68fb5193ccb8828ac8d34dfe820101181c2bde078a04a6d5afd4c08bcf0cab45
- coefficients: bf15ce41180bfb4e250d311df279e98c13b65432756ae07f7a30264cbae0e221

## Current implementation identity
Generator: scripts/cfb_qa_sandbox_candidate_generator_2026_09_27.py
Optimized generator commit: 73f37fa3da6ca01c2f95ca551a7aca84b9d73f1b
Generator Git blob: 30fa400fe09a05a48ad3fda18df35899ffc374a8
Generator SHA-256 observed by controlled Run #10: ad2609f14bc4b30d61d19ffb90083a9dc7a5b171dc9e60f513dec5d0a4145641
Workflow execution pin commit: 496d5b0b501ac200ab034db55b9ffab47841bcce
Workflow: .github/workflows/cfb_qa_sandbox_candidate_freeze_2026_09_27.yml

Performance-only changes at 73f37fa3:
1. memoize frozen population baseline values by feature/cutoff/season;
2. build feature-history index/completion booleans once;
3. cache identical team prior-history slices.
These are classified IMPLEMENTATION/PERFORMANCE, not scientific changes.

Known implementation debt deliberately not mixed into the performance patch:
- s2() contains stale legacy exception-name handling around mapped opponent baseline lookup. Do not silently patch it during the active run. Reconcile separately if execution evidence shows the path matters or after the freeze is accepted.

## Change classification
SCIENTIFIC / CANDIDATE-AVAILABILITY:
- completion-safe population chronology;
- zero-history S1 baseline-only limit;
- fail-closed S2 context rules;
- rest_days feature-specific baseline availability correction;
- corrected S1/S2 omission identities/cardinalities.
These changes require scientific evidence and explicit reconciliation.

IMPLEMENTATION / PERFORMANCE:
- baseline memoization;
- pre-indexed feature-history lookup;
- cached prior-team histories.
No formula, chronology, candidate, coefficient, input, omission, or target change is intended.

INFRASTRUCTURE / EXECUTION:
- isolated GitHub Actions workflow;
- timeout change 30 -> 90 minutes;
- identity-observation runs;
- exact generator SHA pinning.
Infrastructure changes do not establish scientific acceptance.

## Current frontier
DONE:
- S0 equivalence PASS.
- construction sentinels PASS.
- frozen S1/S2 mapping/spec established.
- rest_days baseline coverage reconciled.
- expected cardinality reconciled to 55,834.
- optimized generator identity observed and pinned.

ACTIVE:
- GitHub Actions Run #11, ID 36413551460, head 496d5b0b501ac200ab034db55b9ffab47841bcce.
- Purpose: generate outcome-blind frozen candidates with optimized implementation under unchanged frozen contract.

BLOCKED:
- Candidate freeze acceptance until Run #11 completes and artifact is independently verified.
- Outcome scoring remains separately unauthorized.

NEXT:
1. Check Run #11 status.
2. If success: inspect job logs; retrieve artifact; independently verify manifest/prediction SHA, 55,834 cardinality, S0/S1/S2 counts, exact omission identities, forbidden columns, no 2025, outcomes_joined=false, and input/generator hashes.
3. Persist execution-acceptance evidence and read it back. Runner green alone is not acceptance.
4. If failure: classify exact failure before mutation; do not patch blindly.
5. Only after accepted prediction freeze may a separately authorized outcome-scoring phase be considered.

DO NOT TOUCH during active Run #11:
- Champion v1.193 or production coefficients/scaling;
- 2025 protected TEST;
- outcomes or postgame scoring;
- frozen S1/S2 formulas, mapping, k-grid, chronology, expected omission sets;
- market/wager/execution data as model inputs;
- production promotion;
- generator/workflow while Run #11 is executing.

## Process learning captured
Repeated expensive execution failure is a structural-investigation trigger. After a repeated costly timeout/failure, inspect/profile repeated work before increasing resources again. Resource extension is not a substitute for root-cause analysis. Preserve semantics with bounded optimization and identity/equivalence gates.

## Recovery rule
Start here for the active QA Sandbox, then read the governing files above. Do not infer current state from GitHub Actions color alone. Historical evidence remains preserved and is not superseded except where an explicit correction file says so.
