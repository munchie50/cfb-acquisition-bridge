# CFB Engine — Historical Rules & Statistical Semantics Ledger 2016-2026 v1.117

Status: ACTIVE EVIDENCE LEDGER — pre-fitting gate input
Parent gate: v1.116
Scope: engine-relevant NCAA football rule/statistical regimes only.
Source policy: NCAA primary sources/manuals preferred; absence of an identified change is not yet proof of NO CHANGE until the season review is completed.

| Season | Change / regime | Engine impact | Affected engine domains | Current disposition |
|---|---|---|---|---|
| 2016 | Baseline season for current TRAIN window | baseline to establish | all | REVIEW REQUIRED |
| 2017 | NCAA record-book chronology identifies kick-block leaping/hurdling foul change | likely NONE for current initial feature set; possible penalty/play-nullification edge | play eligibility/penalties | BOUNDED / deeper stat-manual check required |
| 2018 | Free-kick fair catch behind receiving team's 25 becomes touchback at 25 | ENVIRONMENT + field-position semantics for kickoff-derived drives | drive starts, field position, kick returns/touchbacks | ENGINE-RELEVANT; field-position compatibility check required |
| 2019 | Overtime regime changed relative to prior era; statistical manual documents 2019-20 treatment distinct from 2021+ | SEMANTIC + ENVIRONMENT | scrimmage counts, conversion attempts, scoring, pace/rates | ENGINE-RELEVANT; overtime exclusion/versioning check required |
| 2020 | Same 2019-20 overtime statistical regime; COVID playing-rule interpretations also existed | SEMANTIC/ENVIRONMENT; COVID specifics TBD | overtime plus any affected play semantics | ENGINE-RELEVANT; targeted primary-source review required |
| 2021 | Third+ overtime becomes alternating two-point conversion plays; NCAA stats manual says these are conversion attempts, not scrimmage plays | SEMANTIC + ENVIRONMENT | scrimmage denominator, scoring, success/explosiveness eligibility | ENGINE-RELEVANT; producer classification must be verified |
| 2022 | No engine-relevant change yet established in this pass | TBD | TBD | REVIEW REQUIRED |
| 2023 | Division I first-down clock generally continues outside final two minutes of half | ENVIRONMENT | pace, play volume, opportunity counts | PRESERVE REGIME; do not normalize away |
| 2024 | Two-minute timeout/timing synchronization | ENVIRONMENT | pace, play volume, end-half opportunity | PRESERVE REGIME; do not normalize away |
| 2025 | Injury-timeout rule + third-overtime timeout limitation; TEST performance remains sealed | ENVIRONMENT | pace/stoppages, overtime environment | METADATA ONLY; TEST remains protected |
| 2026 | Current NCAA rule regime; LIVE SHADOW only | LIVE ENVIRONMENT | prospective live features | REVIEW CURRENT RULE CHANGES; no historical backfill |

## Primary-source anchors recovered
1. NCAA Football Playing Rules hub: current official rules resources and year-specific updates.
2. NCAA 2018 FBS record book: identifies 2017 kick-block leaping/hurdling foul and 2018 free-kick fair-catch/touchback change.
3. NCAA football statistics manual: overtime statistics are included with regulation stats; third+ OT two-point plays are conversion attempts, not scrimmage plays beginning 2021; during 2019-20 the threshold was after fourth overtime.
4. NCAA 2023 timing approval: Division I/II first-down clock change.
5. NCAA 2024 technology/timing approval: two-minute timeout and timing synchronization.
6. NCAA 2025 approved changes: injury timeout administration and third+ OT timeout limitation.

## Immediate engine checks created by this ledger
A. OVERTIME SEMANTICS: prove the recovered primitive/feature producers do not count 2021+ third-overtime two-point conversion attempts as eligible scrimmage plays. Compare 2019-20 regime handling separately.
B. FIELD POSITION: prove kickoff fair-catch/touchback regime change beginning 2018 does not create a false data-semantic discontinuity in average drive-start yards-to-goal. The environment shift itself is real and must remain.
C. PACE/PLAY VOLUME: mark 2023 and 2024 timing changes as known football-environment regime changes so downstream modeling/diagnostics do not 'correct' them as acquisition drift.
D. 2025: rules metadata may be audited, but no model performance/outcomes may be inspected.
E. Complete 2016, 2017, 2020, 2022, 2026 targeted rule/stat-manual review before fitting.

## Current gate status
PARTIAL / BLOCKS FITTING.
Feature-generation canaries and independent reproduction may continue.
