# CFB Engine — Phase 4 First-Challenger Feature & Play Eligibility Contract v1.123

Status: FROZEN PROSPECTIVELY — BEFORE MODEL PERFORMANCE
Scope: first fitted v2 challenger only
Production effect: NONE
2025 TEST: PROTECTED
Model fitting: NOT YET AUTHORIZED

## Purpose

Freeze the smallest evidence-supported first-challenger feature set and play-eligibility behavior before any TRAIN/VALIDATION model performance is inspected. This closes conditional semantic blockers by exclusion rather than inventing missing lineage.

## Included first-challenger features

Only features already mechanically defined and canary-accepted may enter Challenger A:

Mechanical v1.107 / accepted v1.110:
1. points_for_per_game
2. points_against_per_game
3. offensive_scrimmage_plays_per_game
4. defensive_scrimmage_plays_per_game
5. offensive_yards_per_play
6. defensive_yards_per_play
7. rush_play_rate
8. pass_play_rate
9. rush_yards_per_play
10. pass_yards_per_play
11. interception_rate
12. home_away_neutral
13. rest_days

Derived v1.112 / accepted v1.120:
14. offensive_explosive_play_rate
15. defensive_explosive_play_rate
16. offensive_success_rate
17. defensive_success_rate_allowed
18. average_starting_yards_to_goal

No additional feature may enter Challenger A after validation performance is seen without becoming a new prospectively versioned challenger.

## Explicit Challenger-A exclusions

The following are excluded from Challenger A:
- points_per_scoring_opportunity / finishing drives — drive-point attribution not yet validated;
- combined turnover/giveaway rate — fumble-lost semantics remain bounded;
- opponent adjustment / strength of schedule — authentic second-order formula/lineage unrecovered;
- standard-down/passing-down splits — not frozen in v1.112;
- preseason priors / previous-season priors / shrinkage — not authorized for first no-prior challenger;
- personnel, injuries, weather, recruiting and other optional enrichments;
- market prices, spreads, totals, external power ratings or any market-derived feature in the fair-model core.

These exclusions are evidence/governance choices, not conclusions that the features lack predictive value.

## Play eligibility

### Baseline scrimmage eligibility
Preserve the already accepted producer semantics used by v1.110/v1.120:
- rush OR pass OR pass_attempt flag;
- punt excluded;
- required yards/context present for the affected feature;
- explicit 2021+ third-and-later overtime Two Point Pass/Two Point Rush conversion records are not admitted merely because conversion text exists; v1.119/v1.120 bounded audit found no systemic contamination.

### Kneels
Do NOT introduce a new universal kneel filter in Challenger A.
Reason: the accepted canaries were built with recovered producer semantics, and no prospectively frozen evidence-supported kneel transformation preceded them. Removing kneels now would change already accepted rate/yards/play populations and create a new feature version.
Disposition: retain current source/producer treatment for Challenger A. A kneel-excluded alternative requires a separately versioned future challenger frozen before performance.

### Spikes
Do NOT introduce a new universal spike filter in Challenger A for the same reason. Preserve current source/producer treatment. A spike-specific exclusion may be tested only in a future prospectively defined challenger.

### Overtime
Include regulation and NCAA-statistically eligible overtime scrimmage plays under the source/producer semantics already audited.
Do not count 2021+ third-and-later-OT two-point conversion attempts as scrimmage plays.
Do not normalize 2019–20 and 2021+ OT environments into one artificial regime; retain historical environment labels for diagnostics.

### Garbage time
Challenger A uses NO garbage-time exclusion or downweighting.
Reason: no authoritative frozen garbage-time definition exists, and selecting one after viewing validation performance would create researcher degrees of freedom. Full eligible-game play population is the prospective baseline.
Any future garbage-time definition/exclusion must be frozen in a new challenger before its performance is inspected.

## Missingness

For Challenger A:
- zero denominator => NA, never zero;
- missing required context excludes only the affected observation from the affected feature denominator;
- no imputation value is authorized by this contract;
- opening-game/no-prior-history feature values remain NA where the definition requires prior history;
- model-stage handling of NA must be frozen separately before fitting and may not silently reinterpret NA as zero.

## Early season

Challenger A is the no-preseason-prior baseline:
- history resets at each season boundary;
- no previous-season carryover;
- no recruiting/external preseason prior;
- no shrinkage toward prior season or population mean unless separately authorized in a future challenger;
- opening-game history-based features therefore have no prior-game estimate.

This preserves the already accepted canary semantics and creates an auditable baseline. It is not a claim that priors are undesirable.

## Historical regime labels

The first-fit dataset/config must preserve diagnostic labels for known environment/semantic regimes where applicable:
- 2018 kickoff fair-catch/touchback environment;
- 2019–20 OT regime;
- 2020 distinct COVID environment;
- 2021+ OT regime;
- 2023 Division I first-down timing regime;
- 2024 two-minute timing regime.

These labels are diagnostic/context metadata only for Challenger A unless a later contract explicitly authorizes them as model features. They may not be used post hoc to exclude/downweight seasons after validation performance is seen.

## Gate effect

This contract closes the v1.121 conditional blockers for finishing drives, combined turnover rate, and opponent adjustment/SOS by prospectively excluding them from Challenger A.
It also freezes Challenger-A treatment for kneels, spikes, overtime, garbage time, missing feature construction, and early-season history.

Still unresolved before fitting:
1. exact target and game-population contract;
2. temporal/prediction-time qualification for the included first-fit population;
3. model-stage NA handling;
4. allowed model/search/evaluation/calibration contract;
5. exact frozen first-fit dataset/code/config and final market-blind/leakage audit;
6. fitting authorization under existing governance.

No fitting is authorized by this checkpoint.
