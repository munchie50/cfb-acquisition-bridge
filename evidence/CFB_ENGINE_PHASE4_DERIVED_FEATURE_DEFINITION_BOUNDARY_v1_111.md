# CFB Engine — Phase 4 Derived-Feature Definition Boundary v1.111

Date: 2026-09-25
Status: BOUNDED PASS — DEFINITION FRONTIER CLASSIFIED
Mode: v2 challenger/shadow only
Production effect: NONE
Predecessor: CFB_ENGINE_PHASE4_FEATURE_CANARY_ACCEPTANCE_v1_110.md

## Authority recovered
The frozen Phase 4 Feature/Data Inventory v0.1 requires explosiveness, down/situation efficiency, finishing drives, and field position in the initial scope, but explicitly requires their definitions to be frozen before tuning. The frozen Evaluation Methodology requires feature definitions and deterministic independent reproduction before formula/weight fitting. The redesign contract does not authorize thresholds, priors, transforms, or predictive formulas.

## Substrate
Recovered PBP producer exposes the mechanical inputs needed to construct candidate definitions: down, distance, yards_gained, drive_id, yards_to_goal/yards_to_goal_end, drive_result/drive_result_detailed, offense/defense identity, period, and rush/pass/pass_attempt semantics. Existing semantic audits protect scrimmage and selected event meanings.

## Classification
1. Explosiveness — DERIVABLE, definition NOT YET FROZEN. A yardage threshold or value transform is a new modeling choice; no authoritative threshold survives.
2. Success/down-situation efficiency — DERIVABLE, definition NOT YET FROZEN. Required gain fractions and standard/passing-down cutoffs are new modeling choices; no authoritative formula survives.
3. Finishing drives — DERIVABLE, definition NOT YET FROZEN. The scoring-opportunity entry threshold and drive aggregation rule are new modeling choices; no authoritative threshold survives.
4. Field position — DERIVABLE with drive/play substrate, definition NOT YET FROZEN. Start-of-drive identification and aggregation convention must be explicitly versioned; do not silently substitute first observed play without a validated drive-start rule.
5. Combined turnover/giveaway rate remains outside this definition freeze because fumble-loss semantics are bounded/open.
6. Opponent adjustment/SOS remains outside this definition freeze because second-order lineage/formula is an evidence boundary.
7. Prediction-cutoff-dependent features remain fail-closed where exact cutoff authority is absent.

## Gate consequence
The v1.110 mechanical canary remains accepted and is not reopened. The next legitimate task is a prospective v2 candidate-definition package for the four judgment-bearing derived domains, followed by semantic canaries and independent reproduction. These definitions must be selected before any model fitting and cannot be chosen by looking at VALIDATION/TEST performance.

No formula/weight fitting is authorized by this checkpoint. 2025 TEST remains untouched.
