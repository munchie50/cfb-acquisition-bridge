# CFB Engine — Phase 4 Challenger-A Modeling & Evaluation Contract v1.126

Status: FROZEN PROSPECTIVELY — BEFORE ANY CHALLENGER-A MODEL PERFORMANCE
Scope: first fitted v2 challenger only
Production effect: NONE
2025 TEST: PROTECTED / UNTOUCHED
Fitting: NOT AUTHORIZED BY THIS CHECKPOINT
Parents: frozen Phase 4 redesign/evaluation methodology; v1.121; v1.123; v1.124; v1.125

## Purpose

Freeze the model-stage degrees of freedom that could otherwise be chosen after seeing TRAIN/VALIDATION performance. Challenger A is deliberately a simple, auditable baseline challenger, not an unrestricted model search.

## 1. Input eligibility and NA handling

The model matrix may contain only features authorized by v1.123 and rows qualified by v1.124/v1.125.

No model-stage zero-fill is permitted.

For history-derived numeric features:
- a row is eligible for fitting/scoring only when every required Challenger-A numeric input has a qualified value;
- opening-game/no-prior rows therefore fail closed for Challenger A rather than receiving invented zeros or population means;
- missing play/context observations already excluded at feature-construction level remain governed by the frozen feature denominators; model stage does not reinterpret them;
- no median/mean/model-based imputation is authorized in Challenger A.

Categorical home_away_neutral must be known from qualified schedule authority. Rest-days must be qualified and non-missing where required.

The executable dataset builder must emit row-level eligibility and exclusion-reason diagnostics before fitting.

## 2. First-challenger model family

Challenger A uses transparent regularized linear/generalized-linear models only.

Targets:
- scoring margin: Gaussian linear regression;
- total points: Gaussian linear regression;
- home win probability: binomial logistic regression.

Allowed regularization:
- ridge / L2 only.

Not authorized in Challenger A:
- lasso/elastic-net selection;
- trees, random forests, boosting, neural networks;
- splines or learned nonlinear basis expansions;
- feature interactions;
- post-hoc feature additions;
- market/external-rating inputs;
- target leakage or outcome-derived feature construction.

Rationale: establish the smallest reproducible multivariate challenger before expanding model complexity.

## 3. Transformations and standardization

Numeric predictors may be centered/scaled using TRAIN-only parameters.
Those parameters must be persisted and applied unchanged to VALIDATION.
No target-informed transformation is allowed.
No winsorization, clipping, log transform, polynomial term, interaction, or manual direction flip is authorized in Challenger A unless already inherent in the frozen feature definition.

Categorical home_away_neutral may be represented with a fixed deterministic dummy/reference encoding documented in the executable config.

## 4. Hyperparameter search

Only the ridge penalty may be tuned.

Freeze the candidate grid before execution:
lambda = {0, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100}.

lambda=0 is the unregularized control within the same linear family.

No adaptive grid expansion after viewing VALIDATION results is permitted for Challenger A. A materially different grid becomes a new prospectively versioned challenger.

## 5. Time-respecting fitting/evaluation

Preserve frozen partitions:
- TRAIN: 2016–2022
- VALIDATION: 2023–2024
- TEST: 2025 protected
- LIVE SHADOW: 2026 prospective

Primary development remains time ordered. No random train/test shuffling.

Within TRAIN, penalty selection must use forward-chaining season blocks, never random folds. At each fold, training seasons precede evaluation season.

VALIDATION 2023–2024 is used only after TRAIN-side penalty selection to evaluate the frozen candidate. It may not be used to redesign features, garbage-time rules, missingness, population, or the lambda grid.

## 6. Primary metrics

As required by frozen Phase 4 methodology:

Margin:
- MAE
- RMSE
- signed bias

Total:
- MAE
- RMSE
- signed bias

Win probability:
- Brier score
- log loss
- calibration/reliability summary

Report sample counts and exclusions with every metric.

## 7. Candidate selection rule

For each target, choose lambda using TRAIN forward-chaining evidence only.

Primary selection metric:
- margin: mean fold MAE;
- total: mean fold MAE;
- win probability: mean fold Brier score.

Tie/near-tie discipline:
- if candidates are numerically tied at reported precision, choose the larger lambda (simpler/more regularized);
- do not invent a post-hoc composite score;
- retain all grid results, not only selected lambda.

VALIDATION does not choose a new lambda. It evaluates the already selected TRAIN-side candidate.

## 8. Required controls / negative controls

Required comparators:
- permanent simple baseline named by frozen Phase 4 methodology, where exact comparable output is recoverable;
- lambda=0 within-family control.

Required leakage negative control:
- construct a deliberately invalid future-information sentinel only in an isolated QA path, never in the candidate dataset. The QA must prove the production dataset/config does not contain the sentinel or any 2025 rows.

No market benchmark is permitted until blind fair predictions are frozen. Market/external ratings are post-freeze diagnostics only.

## 9. Calibration and uncertainty

Win-probability Challenger A emits raw logistic probabilities.
No Platt/isotonic/post-hoc recalibration is authorized before first VALIDATION evaluation because selecting a recalibration method from VALIDATION would add an unfrozen degree of freedom.

Calibration must be reported via reliability bins plus Brier/log loss.

For margin/total, report residual distribution and empirical error summaries on TRAIN folds and VALIDATION. No fitted prediction-interval method is authorized in Challenger A yet. Any interval/calibration layer requires a separately frozen version.

## 10. Stability slices

Report, without using them for post-hoc feature/model redesign:
- season;
- early vs later season using a deterministic week/history-depth definition frozen in executable config;
- home/away/neutral;
- FBS-vs-FBS vs FBS-vs-FCS when present;
- conference where qualified;
- large predicted-margin bucket;
- known historical regime labels from v1.123.

Favorite/underdog and market-relative slices are prohibited until blind predictions are frozen and market data are joined only for diagnostics.

## 11. Reproducibility requirements

Before execution, freeze and persist:
- exact row population and row-level eligibility/exclusion ledger;
- exact feature column list/order;
- target construction;
- TRAIN-only standardization parameters procedure;
- categorical encoding;
- lambda grid;
- fold definitions;
- software/script/config identity;
- dataset/code/config hashes;
- 2025 exclusion assertion;
- market/external-rating absence assertion.

A run is not accepted merely because it completes. Artifact identity, hashes, diagnostics and independent readback/replay evidence remain required.

## 12. Decision-before-evidence lock

After this checkpoint, Challenger-A model family, transformations, lambda grid, TRAIN selection metrics, NA handling, and calibration policy may not be changed in response to observed TRAIN/VALIDATION performance.

Any such change creates a separately versioned prospective challenger and must not reuse the same held-out evidence as though the redesign were pre-specified.

## Gate effect

This closes v1.121's model-stage NA-handling and first-challenger modeling/search/evaluation/calibration-definition blockers.

Still required before fitting:
1. build and freeze the exact Challenger-A executable dataset/config under v1.123–v1.126;
2. prove row-level temporal qualification/fail-closed exclusions;
3. run final market-blind/leakage/2025-exclusion audit;
4. persist/read back dataset/code/config identities and hashes;
5. perform final pre-fitting readiness reconciliation;
6. obtain fitting authorization required by existing governance.

No fitting or TEST evaluation is authorized by this checkpoint.
