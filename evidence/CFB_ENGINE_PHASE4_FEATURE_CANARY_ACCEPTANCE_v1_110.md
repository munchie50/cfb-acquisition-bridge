# CFB Engine — Phase 4 Deterministic Feature Canary Acceptance v1.110

Status: BOUNDED PASS — deterministic mechanical feature canary accepted for the frozen v1.107 feature subset. This does not authorize formula/weight fitting, source promotion, model promotion, or production promotion.

## Authority and execution
- Frozen mechanical feature definitions: v1.107.
- Qualified schedule input: evidence/phase4_qualified_schedule_2016_2024.csv.
- Corrected implementation commit: 227076d99791ac3a6f4e6ed988c146809bb09f97.
- GitHub Actions run: 36199477506, conclusion SUCCESS.
- Artifact ID: 10890704969.
- Artifact digest: sha256:e3faad13b57a9573efe5ce923dae0758784714d0ac7ff5a7b5fd136f8370201.
- 2025 TEST remains excluded.

## Season-boundary correction
The first optimized v1.109 diagnostic run inherited prior seasons. Frozen Phase 4 authority does not authorize an implicit previous-season prior; previous-season information requires separate definition/versioning/leakage testing and the baseline assumes no preseason prior. Commit 227076d therefore resets feature histories by (season, team). The earlier successful cross-season artifact is diagnostic only and is not accepted.

## Acceptance audit
Corrected artifact:
- feature rows: 12,718
- team-game primitive rows: 12,718
- duplicate (season, game_id, team) feature keys: 0
- duplicate primitive keys: 0
- 2025 feature rows: 0
- season-team populations: 1,173
- season-team opening rows with nonzero qualified_prior_games: 0
- maximum qualified prior games by season: 2016 12; 2017 12; 2018 12; 2019 12; 2020 11; 2021 12; 2022 12; 2023 12; 2024 12.
- feature CSV SHA-256: f65fca56b3c975437d5a12ccb4fae6583be6c6a5f670cf091771a93b326b7ecb
- primitive CSV SHA-256: 092b4abbb6c1dfc2817c7d6c2737fff741c9b091da82e5553565c22fb511e75e

## Independent row reproduction
A separate audit path selected deterministic rows and recomputed every frozen numeric feature directly from earlier same-season team-game primitive rows, rather than using the canary cumulative-feature implementation.

Exact agreement (zero mismatched audited fields) was obtained for:
- 2016 Air Force target game 400869199 with 1 prior game.
- 2020 Akron target game 401249886 with 5 prior games.
- 2022 Air Force target game 401415256 with 8 prior games.
- 2024 Arizona State target game 401673465 with 12 prior games.

Audited fields: qualified_prior_games, points_for_per_game, points_against_per_game, offensive_scrimmage_plays_per_game, defensive_scrimmage_plays_per_game, offensive_yards_per_play, defensive_yards_per_play, rush_play_rate, pass_play_rate, rush_yards_per_play, pass_yards_per_play, interception_rate, rest_days.

## Classification
DETERMINISTIC_FEATURE_CANARY: BOUNDED PASS for the frozen mechanical v1.107 subset.
INDEPENDENT_SAMPLE_REPRODUCTION: PASS for four deterministic samples spanning TRAIN and VALIDATION seasons.
PREVIOUS_SEASON_PRIORS: NOT AUTHORIZED / not part of this canary.
2025 TEST: PROTECTED / excluded.
FORMULA_WEIGHT_FITTING: NOT AUTHORIZED.
Judgment-bearing feature definitions (explosiveness, success/efficiency, finishing drives, field position), combined turnover rate, opponent adjustment/SOS, and exact prediction-cutoff-dependent features remain outside this acceptance.
