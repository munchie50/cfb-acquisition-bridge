# CFB Engine — Post-Validation Evidence and Holdout Contract v1.143

Status: PROSPECTIVELY FROZEN / NO NEW PERFORMANCE EXPOSED
Parent: v1.142 integrated recovery package
Candidate: Challenger A only; production v1 unchanged.

## Purpose
Freeze the next evidence sequence before any market join or 2025 TEST exposure. This contract does not alter Challenger A and does not authorize production promotion.

## Existing evidence state
- TRAIN 2016–2022 used for fitting/lambda selection.
- VALIDATION 2023–2024 has been exposed and is spent evidence for Challenger A.
- 2025 TEST remains hidden/protected.
- LIVE SHADOW 2026 remains prospective.
- Challenger A v1.140 is accepted only as a bounded challenger/shadow fit.

## Fair-model freeze
The exact Challenger A fair-model identity entering any later evidence stage is the accepted v1.140/v1.136 candidate:
- same 34 numeric predictors plus frozen venue representation;
- same targets and eligible-population rules;
- same transformations/scaling conventions;
- selected lambdas margin 0.1, total 1, win 0.01;
- no post-hoc calibration;
- no market/external rating input;
- no feature, transform, model-family, weighting, or parameter redesign based on 2023–2024 results.

Any substantive change creates a new challenger identity and may not reuse 2023–2024 as fresh validation evidence.

## Next-stage sequence
A. POST-FREEZE DIAGNOSTIC PREPARATION
1. Preserve exact fair predictions/model identity before joining external market information.
2. Freeze market-source semantics, timestamp/cutoff, game identity, line/price representation, missingness and join policy before evaluating market-relative results.
3. Market/ratings may be used only as post-freeze diagnostics; they cannot alter Challenger A fair predictions.
4. Diagnostic evidence must distinguish football prediction quality from betting/price/timing/execution quality.

B. 2025 HOLDOUT OPENING GATE
2025 is not automatically opened by v1.140. Before any 2025 outcomes are scored:
1. candidate identity above must remain frozen;
2. exact 2025 eligible population and temporal availability rules must be generated without using 2025 outcomes;
3. all 2025 fair predictions must be generated and durably frozen with game IDs and hashes before outcomes are joined/scored;
4. no 2025 case may be inspected for debugging, feature correction, parameter choice, calibration, threshold choice, or market-rule tuning before the full prediction freeze;
5. an independent pre-outcome audit must verify no outcome/market leakage into the fair-model inputs and prove candidate identity;
6. opening/scoring 2025 requires a separate explicit checkpoint/authorization after the prediction freeze proof.

If any 2025 case is used for debugging before freeze, it is contaminated as holdout evidence and must be classified accordingly rather than silently retained.

C. 2025 EVALUATION
If separately authorized after freeze, evaluate the frozen candidate once on the full qualified 2025 holdout using the already-frozen football metrics:
- margin MAE/RMSE/bias;
- total MAE/RMSE/bias;
- win Brier/log loss/calibration;
- prospectively defined stability slices available from qualified pregame metadata.
Do not choose new model parameters, calibration, feature rules, or betting thresholds from TEST.

D. LIVE SHADOW 2026
2026 remains prospective shadow evidence. Fair predictions must be frozen before game outcomes and before any market comparison can feed back into model construction. Outcome, selection, timing, execution and realized result are evaluated separately.

## Market diagnostic boundary
No historical market data is fetched/joined by this contract. Before such work, freeze:
- source/provider and retrieval provenance;
- line type(s): spread/total/moneyline as applicable;
- timestamp(s) and definition of opening/current/closing where used;
- home/away sign convention;
- odds/price convention and vig handling;
- missing/stale/conflicting market policy;
- game-ID mapping;
- diagnostic metrics and any betting-decision thresholds.
Observed market-relative results cannot retroactively change Challenger A while preserving the same candidate identity.

## Promotion boundary
Neither favorable validation, TEST, market-relative, nor shadow evidence automatically promotes Challenger A. Production v1 remains champion/fallback until a separate promotion contract/checkpoint proves required evidence, rollback, operational readiness and receives explicit promotion authorization.

## Immediate next work
Recover/freeze the market-diagnostic data contract and source semantics without fetching/evaluating prices, OR prepare the 2025 pre-outcome prediction-freeze machinery without exposing outcomes. Global dependency reconsideration chooses between these based on existing qualified substrates and contamination risk.

Locks: 2025 outcomes unexposed; no market join; no redesign; no promotion.
