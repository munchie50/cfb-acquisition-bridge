# CFB Engine — Challenger-A Population Conformance Defect v1.150

Status: MATERIAL CONTRACT/IMPLEMENTATION MISMATCH / 2025 HOLDOUT PREPARATION PAUSED
Parent: v1.149 correction
No 2025 outcomes scored.

## Direct conformance audit
Frozen v1.124 requires the evaluation population to include, when present in the authoritative relevant-FBS schedule and inputs qualify: FBS-vs-FBS, FBS-vs-FCS, regular season, conference championships, bowls and CFP/postseason.

The actual schedule file consumed by accepted v1.131 and therefore v1.136/v1.140 is evidence/phase4_qualified_schedule_2016_2024.csv, 6,398 rows.

Its scope distribution is:
- 2016: 719 2016_PROVISIONAL_FBS_VS_FBS
- 2017: 736 PRIMARY_REGULAR_PROVISIONAL
- 2018: 733 PRIMARY_REGULAR_PROVISIONAL
- 2019: 734 PRIMARY_REGULAR_PROVISIONAL
- 2020: 508 PRIMARY_REGULAR_PROVISIONAL
- 2021: 732 PRIMARY_REGULAR_PROVISIONAL
- 2022: 724 primary + 10 conference championship pending
- 2023: 740 primary + 10 conference championship pending
- 2024: 743 primary + 9 conference championship pending

The file embodies the legacy v0.22 FBS-vs-FBS primary/championship scope, not the full population stated by v1.124. FBS-vs-FCS and bowls/CFP are not represented as required by v1.124.

## Consequence
v1.140 remains valid evidence for the exact dataset/model actually executed, but its acceptance is narrower than previously stated. It is NOT proof that Challenger A as defined by v1.124 has been evaluated over its full frozen population.

Do not silently repair the population and call the result the same blind Challenger-A validation. 2023–2024 performance has already been exposed; changing the population after exposure changes the candidate/evaluation implementation; 2023–2024 cannot become fresh validation evidence again.

2025 holdout preparation is paused because extending the legacy 762-style scope would perpetuate the defect, while switching only TEST to the broader v1.124 population would create a population mismatch against TRAIN/VALIDATION.

## Required governance resolution
Before further TEST preparation, recover the authoritative historical Phase-4 population implementation if possible and determine whether:
A. v1.124 accurately froze the intended population and v1.108/v1.131 were implementation-incomplete; or
B. a superseding pre-performance authority narrowed the actual Challenger-A universe and v1.124 wording must be corrected.

If A, preserve v1.140 as Challenger-A legacy-scope execution evidence and create a prospectively named corrected challenger/evidence plan without pretending 2023–2024 is fresh.
If B, prove the superseding authority before changing v1.124 classification.

No 2025 TEST scoring or population construction should continue until this is reconciled.

## Learning
Population-scope matching must compare actual persisted schedule membership/status distribution to the frozen population contract before dataset acceptance. Count/hash checks alone were insufficient. This is a completion-proof defect in the earlier acceptance path and must be installed into future dataset acceptance.

Locks: production v1 unchanged; no market join; no 2025 scoring; no post-hoc silent redesign; no promotion.
