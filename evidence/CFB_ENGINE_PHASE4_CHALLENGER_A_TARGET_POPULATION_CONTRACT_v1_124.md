# CFB Engine — Phase 4 Challenger-A Target & Population Contract v1.124

Status: FROZEN PROSPECTIVELY — BEFORE MODEL PERFORMANCE
Scope: Challenger A / v2 shadow only
Production effect: NONE
2025 TEST: PROTECTED
Model fitting: NOT YET AUTHORIZED

## Recovered authority

This contract is derived from the authentic historical Phase 4 package, including CFB_V2_PHASE4_EVALUATION_METHODOLOGY_v0_1 (PASS/FROZEN), CFB_V2_PHASE4_REDESIGN_CONTRACT_v0_1, and CFB_V2_MASTER_SPEC. It does not reconstruct target/population rules from conversation memory.

Frozen historical methodology requires:
- every relevant FBS game in the evaluation population receives a prediction when required input state is available;
- rolling/forward-chaining evaluation;
- market is not a training target;
- FBS-vs-FBS vs FBS-vs-FCS is an evaluation stability slice when applicable;
- spread metrics: MAE, RMSE, signed bias;
- total metrics: MAE, RMSE, signed bias;
- win probability metrics: Brier, log loss, calibration/reliability;
- TRAIN/VALIDATION/TEST remain temporally ordered.

Current frozen split remains:
TRAIN 2016–2022
VALIDATION 2023–2024
TEST 2025 protected
LIVE SHADOW 2026 prospective

## Challenger-A prediction targets

Challenger A must produce market-blind football predictions for:
1. expected home-team scoring margin, defined as home final points minus away final points;
2. expected combined final points, defined as home final points plus away final points;
3. home-team win probability.

Neutral-site games retain canonical home/away schedule identity for target construction while home_away_neutral supplies venue context. No betting-market favorite/underdog identity enters target construction.

Final official game scores include NCAA-recognized overtime. Do not attempt to manufacture a regulation-only target from final-score data. Overtime regime is retained as historical context/diagnostic metadata.

The market spread, total, moneyline, consensus, closing line, external rating, wager outcome, CLV, or selected-bet result is never a Challenger-A training target.

## Evaluation population

Unit: one canonical scheduled game with at least one FBS participant that belongs to the frozen relevant-FBS evaluation universe and satisfies all required input/identity/temporal qualification.

Include:
- FBS-vs-FBS games;
- FBS-vs-FCS games when present in the authoritative relevant-FBS schedule and required inputs qualify;
- regular-season games;
- conference championship games, bowls and CFP/postseason games when present in the authoritative relevant-FBS schedule and required inputs qualify.

Do not create a bet-selected population. Games are evaluated regardless of whether a downstream wager would ever be recommended.

Exclude/fail closed:
- cancelled games;
- games without a played final result for supervised target construction;
- unresolved duplicate/identity conflicts;
- rows lacking required qualified pregame input state under the temporal contract;
- any game outside the frozen authoritative schedule population;
- 2025 during development/tuning.

Forfeits/vacated results: use the official on-field final-score representation present in the authoritative game record unless a separately documented data-integrity defect makes the target ambiguous; ambiguous cases fail closed rather than being manually rewritten from later administrative action.

## Sample weighting

Challenger A uses one game = one evaluation/training observation at the target level. No conference, season, favorite status, margin size, FBS/FCS status, postseason status, or regime-based performance weighting is authorized.

If the fitted model architecture creates team-side rows internally, it must preserve one-game target influence and avoid double-counting the same game as two independent outcomes.

No 2020 downweighting or exclusion is authorized. 2020 remains a distinct diagnostic environment label.

## Stability / diagnostic slices

Preserve, but do not use as post-hoc target filters:
- season/week;
- early vs later season;
- home/away/neutral;
- FBS-vs-FBS vs FBS-vs-FCS;
- conference;
- large predicted-margin games;
- 2018 kickoff environment;
- 2019–20 OT regime;
- 2020 distinct environment;
- 2021+ OT regime;
- 2023 first-down timing regime;
- 2024 two-minute timing regime.

Favorite/underdog is permitted only after blind fair prediction freeze as a market diagnostic, per historical methodology.

## Target availability and leakage

A target outcome may be joined only for training/evaluation after the prediction row's features and prediction-time state are frozen. Final score must never enter feature construction for its own target game.

TRAIN outcomes may estimate parameters only for later predictions. VALIDATION outcomes may evaluate/select under the later modeling contract. TEST 2025 outcomes remain untouched until candidate/version freeze and required authorization.

## Gate effect

This closes v1.121's exact-target and game-population-definition blocker for Challenger A.

Still unresolved before fitting:
1. prediction-time qualification / acceptable cutoff rule for included rows;
2. model-stage NA handling;
3. allowed model family/search/transforms/interactions and evaluation/selection/calibration contract;
4. exact frozen first-fit dataset/code/config plus final market-blind/leakage audit;
5. fitting authorization under existing governance.

No fitting is authorized by this checkpoint.
