# CFB Engine Phase 4 Initial Feature Executability — v1.106
Date: 2026-09-25
Status: bounded pre-feature classification; no fitting/tuning/promotion.

Authority: frozen Phase 4 Feature/Data Inventory v0.1 recovered from authoritative Schedule Acquisition v0.22 package; reconciled against recovered full-season 2016-2025 PBP producer and later bounded evidence through v1.105.

## Classification
Executable substrate exists for a first deterministic canary built from prior-game scoring, scrimmage play volume, simple offense/defense yards-per-play, rush/pass raw splits, prospectively defined explosiveness, prospectively defined finishing drives, prospectively defined field position, home/away/neutral, rest, and potentially interception rate as a separate component.

Not ready for first canary:
- combined raw turnover/giveaway rate: fumble-lost semantics remain unresolved/bounded;
- opponent adjustment and strength of schedule: SECOND_ORDER_LINEAGE remains an evidence boundary; do not invent the missing formula;
- any feature row requiring an unrecovered exact prediction cutoff: UNKNOWN/fail-closed; schedule kickoff must not silently substitute for prediction cutoff.

Derived domains still require prospective v2 definition freeze before implementation: explosiveness threshold, efficiency/success definitions, scoring-opportunity definition, field-position aggregation, and exact rate denominators.

## Gate
INITIAL_FEATURE_SCOPE = historically frozen.
RAW_SUBSTRATE = substantial/bounded.
EXACT_EXECUTABLE_V2_FEATURE_DEFINITIONS = not yet frozen.
DETERMINISTIC_FEATURE_CANARY = not yet authorized.
FORMULA/WEIGHT_FITTING = not authorized.

Next: freeze the minimal leakage-safe prospective v2 feature definitions from recovered authentic primitives, then build deterministic feature canary and independently reproduce sample rows.

Governance: production routine v5; v4 fallback; v6 candidate lane. Production model v1 champion/fallback; v2 challenger/shadow; 2025 TEST protected; no V37; no source/model/production promotion.
