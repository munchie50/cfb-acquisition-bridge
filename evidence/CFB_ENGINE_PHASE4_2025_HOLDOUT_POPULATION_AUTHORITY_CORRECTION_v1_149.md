# CFB Engine — 2025 Holdout Population Authority Correction v1.149

Status: CORRECTION / v1.147 762-COUNT GATE SUPERSEDED FOR CHALLENGER-A TEST POPULATION
Parent execution: v1.148 run 36206863616
No 2025 outcomes scored.

## What v1.148 proved
Fresh SportsDataverse schedule reacquisition succeeded:
- upstream Git blob: 570c54364e0a8bc35bc2bda09bf3a392ef87d140
- upstream blob size: 101502 bytes
- downloaded raw SHA-256: a9b131aec16fa32540882f9438c81feb5a57c3279ee4b9fa6c95d91675e02a3c
- raw 2025 rows: 3831
- diagnostic regular completed provider-division FBS-vs-FBS rows: 762 unique game IDs
- projection SHA-256: 200852d19ac092e82cac4597a8bd3b38c962a533c3b1cacf9a52f49122576594
- no outcome/market fields in projection
- no model fit/score performed
- artifact 10894860302, digest sha256:196fd673d8d046840d24f7e711dcfc4daee3808f46928c87ec5f2ff43e2852a8

This independently reproduces the v1.92 legacy primitive-universe 3831 raw / 762 regular FBS-vs-FBS counts. It is useful source-reacquisition evidence.

## Authority correction
v1.92's 762-ID universe was built for the older Primitive Historical Coverage Gate and is NOT the frozen Challenger-A target population.

Higher/current Phase-4 authority v1.124 states:
- full relevant-FBS population, not bet-selected;
- FBS-FCS retained if in the frozen universe;
- postseason included;
- canonical schedule home/away retained.

Therefore v1.147's requirement to use historical 762 admitted IDs as the Challenger-A holdout population gate was an authority-layer error. The 762 comparison is demoted to a diagnostic source-reacquisition control only.

Do NOT use the v1.148 762-row projection as the Challenger-A 2025 prediction population.

## Required corrected gate
The 2025 holdout schedule must extend the exact population semantics embodied by the accepted 2016-2024 qualified schedule and v1.124, not the legacy primitive FBS-vs-FBS scope.

Before feature construction:
1. recover the qualification logic/provenance that produced evidence/phase4_qualified_schedule_2016_2024.csv;
2. apply that same frozen population logic to 2025 schedule metadata without outcome use;
3. include postseason and qualified FBS-FCS exactly as v1.124 requires;
4. independently compare schema/rules to the accepted 2016-2024 schedule;
5. freeze/hash the corrected 2025 outcome-blind qualified schedule;
6. only then build chronology-safe features.

## Learning enforcement
This is a dependency-transition correction: a legacy proof population must not silently become the current model's target population merely because its counts reproduce exactly. Population-scope matching outranks numerical coincidence.

Locks unchanged: 2025 outcomes unscored; no market join; no model redesign; no promotion.
