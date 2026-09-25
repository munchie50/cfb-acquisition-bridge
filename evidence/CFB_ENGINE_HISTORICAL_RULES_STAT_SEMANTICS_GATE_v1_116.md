# CFB Engine — Historical Rules & Statistical Semantics Compatibility Gate v1.116

Status: FROZEN GOVERNANCE GATE — CHALLENGER/SHADOW ONLY
Production effect: NONE
Model fitting/tuning: NOT AUTHORIZED until this gate is satisfied for the feature population being fitted.
2025 TEST: rule/statistical metadata may be inspected; model outcomes/performance remain protected.

## Purpose
Prevent historical NCAA playing-rule or official-statistical-definition regime changes from being mistaken for data defects, feature drift, or stable cross-season semantics.

## Placement
Phase 4 sequence becomes:
1. verify primitive coverage;
2. freeze TRAIN/VALIDATION/TEST;
3. freeze initial feature definitions;
4. build deterministic feature-generation dataset/canary;
5. independently reproduce sample feature rows;
6. HISTORICAL RULES & STATISTICAL SEMANTICS COMPATIBILITY GATE;
7. only then formula/weight fitting.

This gate does not block ongoing feature-generation/reproduction work. It blocks fitting.

## Required scope
For each season 2016-2026, review authoritative NCAA playing-rule and official-statistical-definition changes only where they can affect engine-observed or engine-derived football semantics.

Required impact domains:
- official play/statistical-attempt eligibility and nullification;
- possession/turnovers/fumbles/interceptions;
- sacks and rush/pass statistical treatment;
- scoring and defensive scores;
- overtime structure;
- clock/timing rules capable of shifting pace/play volume;
- down/distance/first-down semantics;
- kickoffs/punts/returns/touchbacks;
- field position/drive boundaries;
- penalty administration where it changes recorded play/stat treatment;
- any official-statistics definition affecting current/future primitives or features.

Administrative/equipment/eligibility rules with no plausible data-semantic impact are classified NOT ENGINE-RELEVANT and need no deeper implementation work.

## Ledger schema
season/effective_period | authoritative_source | change | affected_raw_fields | affected_primitives | affected_features | impact_type | comparability | action | proof_status

Impact types:
- SEMANTIC: same football event can be officially represented/statistically credited differently.
- ENVIRONMENT: official rule changes football opportunity/distribution (e.g. clock/overtime) without changing our formula.
- NONE: no engine-relevant effect.

## Acceptance
For every engine-relevant regime change:
1. effective season/population is established;
2. affected fields/primitives/features are mapped;
3. semantic change is either normalized/versioned or explicitly bounded;
4. environment change is preserved as real football context, not 'corrected' as data error;
5. no protected 2025 performance is consulted;
6. unresolved ambiguity fails closed for affected feature/population.

A year need not contain a change to PASS; authoritative review may establish NO ENGINE-RELEVANT CHANGE.

## Current known regime anchors
- 2023 Division I first-down timing changed: outside the final two minutes of a half, the game clock generally continues after an in-bounds first down. Treat as ENVIRONMENT impact on pace/play volume, not a historical-data defect.
- 2024 two-minute timeout/timing synchronization added. Treat as ENVIRONMENT impact on pace/play volume/end-of-half opportunity.
- 2026 rules are LIVE SHADOW semantics; they do not alter frozen TRAIN 2016-2022 / VALIDATION 2023-2024 / protected TEST 2025 partitions.

## Governance
This gate is reusable: whenever an engine training/evaluation population spans multiple rule/statistical regimes, historical compatibility must be audited before fitting/accepting cross-regime comparability.
