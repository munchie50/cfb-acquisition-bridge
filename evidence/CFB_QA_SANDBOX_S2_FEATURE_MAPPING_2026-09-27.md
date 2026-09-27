# CFB QA Sandbox S2 Feature Mapping Table — 2026-09-27

Status: FROZEN BEFORE CANDIDATE GENERATION OR SCORING
Parent: CFB_QA_SANDBOX_S1_S2_TRANSFORM_SPEC_2026-09-27
Production effect: NONE

## Rule
Only explicit same-domain offense/defense relationships in the accepted 17-feature schema receive an S2 opponent-context correction. Ambiguous or unmatched features remain S1-only. No result-dependent mapping changes are permitted.

## Frozen mapping
| Target-side feature | Opponent pregame context feature | S2 |
|---|---|---|
| points_for_per_game | points_against_per_game | CORRECT |
| points_against_per_game | points_for_per_game | CORRECT |
| offensive_scrimmage_plays_per_game | defensive_scrimmage_plays_per_game | CORRECT |
| defensive_scrimmage_plays_per_game | offensive_scrimmage_plays_per_game | CORRECT |
| offensive_yards_per_play | defensive_yards_per_play | CORRECT |
| defensive_yards_per_play | offensive_yards_per_play | CORRECT |
| rush_play_rate | NONE | S1_ONLY |
| pass_play_rate | NONE | S1_ONLY |
| rush_yards_per_play | NONE | S1_ONLY |
| pass_yards_per_play | NONE | S1_ONLY |
| interception_rate | NONE | S1_ONLY |
| rest_days | NONE | S1_ONLY |
| offensive_explosive_play_rate | defensive_explosive_play_rate | CORRECT |
| defensive_explosive_play_rate | offensive_explosive_play_rate | CORRECT |
| offensive_success_rate | defensive_success_rate_allowed | CORRECT |
| defensive_success_rate_allowed | offensive_success_rate | CORRECT |
| average_starting_yards_to_goal | NONE | S1_ONLY |

Mapped features: 10.
S1-only features: 7.

## Sign rule
For a target offensive-production feature paired with opponent defensive allowance/context:
- opponent context above its same-feature population baseline means the opponent was easier than baseline; normalize the target observation downward;
- opponent context below baseline means harder than baseline; normalize upward.

For a target defensive-allowance feature paired with opponent offensive production/context:
- opponent offense above baseline means harder than baseline; normalize defensive allowance downward;
- opponent offense below baseline means easier than baseline; normalize upward.

Equivalent implementation: correction sign is negative relative to the paired opponent residual for both offense-production and defense-allowance pairs after the pair is expressed in its natural higher-means-more production/allowance orientation.

No correction is applied to S1-only features.

## Locks
- Mapping is frozen before candidate predictions or outcome scoring.
- No 2025.
- No target outcome, market, wager, or later-game information.
- No S2 recursion.
- No cross-domain proxy substitution.
- Any required opponent pregame row missing or temporally invalid fails closed.

Scientific effect at mapping freeze: none.
