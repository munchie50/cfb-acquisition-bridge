# CFB Engine Semantic Obligation Inventory — v1.95
Date: 2026-09-25
Status: dependency-selection checkpoint; no semantic/model/source/production promotion.

## Test-routine action
Continued v5 from verified/read-back v1.94. Inspected the authentic full-season semantic producer to identify unresolved proof classes from executable evidence rather than from the old omnibus gate label.

Producer: .github/workflows/Main.yml
Blob SHA: e69c381f1e76f1c322645a54e3404a195bf0085f

## Producer-supported semantic proof surfaces
The current producer already exports:
- seasonal_semantic_audit.csv
- possession_event_taxonomy.csv
- team_game_primitives.csv
- team_game_primitive_integrity.csv
- lineage_join_readiness.csv
- primitive_field_coverage_by_game.csv
- primitive_missing_field_context.csv
- downs_turnover_counterexamples.csv
- fourth_down_unexplained.csv
- range_exception_rows.csv
- canary_contract_v05.dput

The producer explicitly distinguishes:
- promoted FOURTH_DOWN_ATTEMPT semantics,
- candidate TURNOVER_ON_DOWNS semantics,
- possession-event priority INTERCEPTION > FUMBLE > MISSED_FIELD_GOAL > PUNT > TURNOVER_ON_DOWNS,
- provider turnover composites retained as evidence rather than promoted,
- fumble_recovered_stat not promoted as lost-fumble identity.

## Highest-value executable semantic branch
The producer contains an existing bounded missing-field diagnostic with a hard assertion that the target missing-field case count remains 10. It exports exact source context for those cases in primitive_missing_field_context.csv.

This is a stronger next target than reopening turnover semantics:
- authentic producer exists;
- exact bounded exception population exists;
- source context is already exported;
- no new reconstruction is required;
- resolving/classifying it directly advances PRIMITIVE_SEMANTIC_CORRECTNESS.

## Dependency order
Next action: audit the 10 preserved missing-field cases from the successful v19 artifact, classify which primitive fields are absent, whether absence is structurally explainable or semantically unsafe, and whether any target team-game primitive is affected.

Do not promote candidate TURNOVER_ON_DOWNS merely because the workflow computes promotion_ready internally; current manifest explicitly records turnover_on_downs_semantic_promotion=false.

## Governance
Latest integrated Library ZIP remains v1.73; v1.74-v1.95 are bounded repository evidence checkpoints.
Production/master routine v4; active test routine v5.
Production v1 untouched; v2 challenger/shadow; 2025 TEST protected.
No fitting/tuning/source/model/production promotion.
