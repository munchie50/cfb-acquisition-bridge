# CFB QA Sandbox Pooled-Baseline Mapping Freeze — 2026-09-27

Status: PRE-EXECUTION CORRECTION / FROZEN BEFORE PREDICTION GENERATION
Production effect: NONE
Champion effect: NONE
Outcome scoring: NOT STARTED

The prior Sandbox generator used a mean of prior pregame feature rates. That does not satisfy the already-frozen requirement to use pooled primitive components where those components exist. This correction restores the generator to the frozen experiment semantics before any candidate prediction is generated.

## Season/cutoff rule
Population baselines are season-local and strictly cutoff-local. For a target/source kickoff T in season Y, only eligible primitive information from season Y with source kickoff strictly before T may contribute. No full-season aggregate, later kickoff, target game, or cross-season carryover is allowed.

## Mechanical component mappings
- points_for_per_game = sum(game_points_for) / completed team-games
- points_against_per_game = sum(game_points_against) / completed team-games
- offensive_scrimmage_plays_per_game = sum(off_plays) / completed team-games
- defensive_scrimmage_plays_per_game = sum(def_plays) / completed team-games
- offensive_yards_per_play = sum(off_yards) / sum(off_plays)
- defensive_yards_per_play = sum(def_yards) / sum(def_plays)
- rush_play_rate = sum(rush_plays) / sum(off_plays)
- pass_play_rate = sum(pass_plays) / sum(off_plays)
- rush_yards_per_play = sum(rush_yards) / sum(rush_plays)
- pass_yards_per_play = sum(pass_yards) / sum(pass_plays)
- interception_rate = sum(interceptions) / sum(pass_attempts)

## Derived component mappings
- offensive_explosive_play_rate = sum(off_exp) / sum(off_scr)
- defensive_explosive_play_rate = sum(def_exp) / sum(def_scr)
- offensive_success_rate = sum(off_succ) / sum(off_succ_q)
- defensive_success_rate_allowed = sum(def_succ) / sum(def_succ_q)
- average_starting_yards_to_goal = sum(start_ytg_sum) / sum(start_drive_n)

## Rest days
rest_days has no primitive numerator/denominator pair. Its baseline is the season-local mean of valid strictly-prior rest intervals available before cutoff T.

Incomplete primitive sources are not imputed into component pools. A zero or unavailable denominator fails closed for that baseline.

S1/S2 equations, k={1,2,4,8}, frozen S2 mappings/sign, accepted eligibility, Champion coefficients/scaling, 2025 prohibition, and freeze-before-score gate are unchanged.
