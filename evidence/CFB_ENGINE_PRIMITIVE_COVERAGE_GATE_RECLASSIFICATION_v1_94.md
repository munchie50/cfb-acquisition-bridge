# CFB Engine Primitive Historical Coverage Gate — Reclassification v1.94
Date: 2026-09-25
Status: gate decomposition/reclassification checkpoint; no model/source/production promotion.

## Test-routine action
Continued v5 from verified/read-back v1.93. Per global dependency reconsideration, separated the literal primitive-coverage obligation from chronology/prediction-time/source-semantic obligations that had accumulated under the same broad label.

## Evidence now established
- 2016: corrected bounded primitive queue 13/13 closed; authentic first-order producer replay resolved 115 previously incomplete downstream rows (v1.42/v1.72 lineage).
- 2017: frozen FBS-vs-FBS candidate primitive_scrimmage_plays coverage 736/736 (v1.28; exact historical chronology separately bounded by v1.75).
- 2018-2019: known bounded pre-2020 missing-game set closed through v1.43-v1.45.
- 2020: primitive/source evidence exists, but P0 source-order proof is separately blocked on lossless common raw-response evidence (v1.74). Do not mislabel that source-order boundary as an unidentified primitive-game absence.
- 2021: authoritative target game-ID primitive coverage 732/732 (v1.93).
- 2022: bounded raw->primitive and primitive->direct-prior vertical slice exists; five corrected primitive values and 43 downstream direct-prior rows identified. Temporal prediction-cutoff qualification is separately UNKNOWN/fail-closed (v1.76).
- 2023: target game-ID primitive coverage 750/750 (v1.93).
- 2024: target game-ID primitive coverage 752/752 (v1.93).
- 2025: target game-ID primitive coverage 762/762 (v1.93).

## Reclassification
The phrase "Primitive Historical Coverage Gate remains OPEN" has become too coarse. It mixes at least four different proof classes:
1. literal primitive game presence / missing-game coverage,
2. primitive semantic correctness,
3. source-order/source-provenance qualification,
4. temporal/prediction-time qualification.

For the seasons with explicit frozen target universes and recovered bounded checks, literal primitive missing-game coverage is now substantially proved and should not remain a generic catch-all OPEN label.

However, a full historical primitive-semantic acceptance gate is NOT declared PASS because 2020 source-order evidence and 2022/other temporal qualification remain bounded separately, and the currently recovered evidence does not justify collapsing those obligations.

## New tracking rule
Track remaining obligations by proof class rather than one omnibus OPEN:
- PRIMITIVE_GAME_PRESENCE: bounded PASS where explicitly proved; no known active missing-game queue.
- PRIMITIVE_SEMANTIC_CORRECTNESS: PARTIAL / season- and field-specific evidence.
- SOURCE_ORDER_PROVENANCE: 2020 P0 BLOCKED/evidence boundary.
- PREDICTION_TIME_QUALIFICATION: UNKNOWN/fail-closed where authoritative cutoff absent.
- SECOND_ORDER_LINEAGE: evidence boundary per v1.77.
- RAW_TURNOVER_RATE: OPEN/bounded, deprioritized absent new discriminator.

## Dependency consequence
Do not keep searching for generic "missing primitive games" unless a new target-universe reconciliation exposes one. Global dependency reconsideration should now select among the remaining real proof classes, prioritizing an executable unresolved semantic/source obligation rather than reopening already-proved game presence.

## Governance
Latest integrated Library ZIP remains v1.73; v1.74-v1.94 are bounded repository evidence checkpoints.
Production/master routine v4; active test routine v5.
Production v1 untouched; v2 challenger/shadow; 2025 TEST protected.
No fitting/tuning/source/model/production promotion.
