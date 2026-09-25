# CFB Engine Phase 4 Minimal Feature Definition Contract — v1.107
Date: 2026-09-25
Status: FROZEN mechanical definitions for first v2 deterministic canary; judgment-bearing definitions remain withheld. No fitting/tuning.

## Purpose
Define only mechanically derivable, market-blind, prospective v2 features whose semantics follow directly from recovered authentic primitives. This does not reconstruct production-v1 formulas and does not choose model weights.

## Population/time rule
TRAIN 2016-2022; VALIDATION 2023-2024; TEST 2025 protected.
Each target row may use only qualified completed prior games under authoritative chronology. Where exact prediction-time qualification is required but unavailable, row/feature is fail-closed rather than substituting kickoff for prediction cutoff.

## Frozen mechanical feature definitions
For each team and qualified prior-game window:
1. points_for_per_game = sum(final team points) / qualified prior games.
2. points_against_per_game = sum(final opponent points) / qualified prior games.
3. offensive_scrimmage_plays_per_game = sum primitive_scrimmage_plays for team / qualified prior games.
4. defensive_scrimmage_plays_per_game = opponent offensive scrimmage plays against team / qualified prior games.
5. offensive_yards_per_play = sum yards_gained on eligible team scrimmage plays / count eligible team scrimmage plays.
6. defensive_yards_per_play = opponent eligible scrimmage yards / opponent eligible scrimmage plays.
7. rush_play_rate = eligible rush plays / eligible offensive scrimmage plays.
8. pass_play_rate = eligible pass plays / eligible offensive scrimmage plays, using the producer's recovered rush/pass/pass_attempt semantics and excluding punts.
9. rush_yards_per_play = yards_gained on eligible rush plays / eligible rush plays.
10. pass_yards_per_play = yards_gained on eligible pass plays / eligible pass plays.
11. interception_rate = offensive interceptions thrown / eligible pass attempts. This remains separate from fumbles/giveaways.
12. home_away_neutral = categorical schedule context from qualified schedule authority; no inference from PBP.
13. rest_days = calendar-day difference between qualified prior game and target game from qualified schedule chronology, only where chronology is authoritative.

Denominator zero => NA, never zero-filled.

## Explicitly not frozen in this contract
- explosive-play threshold/rate;
- success rate / standard-down / passing-down efficiency;
- finishing-drives scoring-opportunity threshold;
- field-position aggregation;
- combined turnover/giveaway rate;
- opponent adjustment / strength of schedule;
- any prediction-cutoff substitution;
- priors, shrinkage, transforms, interactions, weights or fair-line formula.

The first four items above are judgment-bearing prospective v2 definitions and require a separately explicit feature-design contract before use. Combined turnover and opponent-adjustment items remain evidence-bounded.

## Acceptance condition for next step
A deterministic feature canary may implement only the frozen mechanical definitions above, on TRAIN/VALIDATION data, with 2025 excluded. It must emit provenance/denominators and independently reproduce sampled rows before any fitting is allowed.

Governance unchanged: production routine v5; v2 challenger/shadow; production v1 untouched; 2025 TEST protected.
