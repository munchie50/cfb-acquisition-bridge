# CFB Engine — Challenger A First-Fit Acceptance v1.140

Status: BOUNDED PASS / FIRST CHALLENGER-A FIT ACCEPTED
Scope: Challenger A shadow only
Production v1: unchanged champion/fallback
2025 TEST: protected / unexposed
Market join: not authorized by this checkpoint
Production promotion: not authorized

## Accepted evidence chain
- v1.131 corrected frozen dataset: BOUNDED PASS
- v1.134 pre-fit reconciliation: technical blockers closed
- v1.135 explicit fitting authorization + prospective numerical convention
- v1.136 executable fit
- successful fit run 36205223971 at head 505d236b4ec3c381f7211f10265c39485c2559db
- artifact 10892848773; digest sha256:7d33dde3244cf764757467a62a04b6c93e40918e1ce04cb22ba9a5938a67aa50
- v1.137 execution checkpoint
- v1.138 independent artifact audit
- v1.139 isolated future-information sentinel QA run 36205474886 PASS

## Population and selection
TRAIN: 3935 games, 2016–2022
VALIDATION: 1229 games, 2023–2024
2025 rows exposed to model: 0

TRAIN forward-chain selected:
- margin lambda 0.1
- total lambda 1
- win lambda 0.01

Retained grid independently reproduced those selections. Lambda=0 within-family control is retained.

## Accepted first blind validation evidence
Margin:
- MAE 13.134943739927614
- RMSE 16.68184258483601
- signed bias -0.187663745399088

Total:
- MAE 13.319683140960914
- RMSE 16.621947930420458
- signed bias 0.8802837290920154

Win probability:
- Brier 0.19430066658361062
- log loss 0.5705372752779593

These values are accepted as historical Challenger-A validation evidence, not as proof of production superiority.

## Artifact audit
All retained manifest hashes independently matched.
Grid: 168 records = 3 targets x 8 lambdas x (6 evaluation seasons + mean).
Predictions: 1229 unique games; only 2023/2024.
Coefficients: 36 finite terms per target.
Scaling: 34 finite numeric parameters, all SD > 0.
Calibration: all 10 decile bins populated; counts sum 1229.
Available stability slices retained: season, venue, deterministic early/later, predicted-margin bucket, regime.

FBS-vs-FCS and conference stability slices were unavailable because qualified metadata were absent from the frozen matrix. They are not silently added after performance.

## Required controls
- lambda=0 within-family control: PASS / retained.
- permanent simple baseline: NOT RECOVERED from repository authority; no baseline invented. This is recorded as bounded absence rather than a candidate failure because v1.126 required it only where exact comparable output was recoverable.
- future-information sentinel: PASS in isolated v1.139 QA.
  - absent from frozen dataset
  - absent from frozen predictor config
  - injected sentinel detected by exact-column gate
  - 2025 rows = 0
  - no fit or score performed by QA

## Decision lock
2023–2024 validation evidence is now spent for Challenger A. Do not alter Challenger A's frozen feature definitions, population, lambda grid, transforms, model family, or calibration policy in response to these results and then reuse 2023–2024 as fresh validation evidence.

Any redesign requires a separately prospectively frozen challenger and an honest evidence plan.

## Gate effect
The first Challenger-A TRAIN/VALIDATION fit is substantively accepted as a BOUNDED PASS for shadow/challenger research.

This does NOT authorize:
- 2025 TEST exposure;
- market/odds joining before blind fair predictions are appropriately frozen under the next contract;
- production promotion;
- replacement of production v1;
- post-hoc Challenger-A redesign disguised as the same candidate.

Next dependency must be selected by global reconsideration under the master objective and governance, not by chasing the observed validation metrics.
