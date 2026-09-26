# CFB Engine — Challenger A First Fit Execution Checkpoint v1.137

Status: EXECUTED / PERFORMANCE EXPOSED / ACCEPTANCE PENDING
Scope: Challenger A shadow only
Production v1: unchanged
2025 TEST: untouched

## Execution identity
Workflow run: 36205223971
Head: 505d236b4ec3c381f7211f10265c39485c2559db
Conclusion: SUCCESS
Artifact ID: 10892848773
Artifact digest: sha256:7d33dde3244cf764757467a62a04b6c93e40918e1ce04cb22ba9a5938a67aa50
Artifact size: 67343 bytes
Fitter blob: 37db8a2c34d4fe4ddfd9592845777cdf84c7bb16

The preceding attempt 36205078168 failed before performance because of a config-key mismatch. Dataset/config SHA checks had passed. The only correction was numeric_predictor_order -> numeric_predictors; no scientific degree of freedom changed.

## Frozen population
TRAIN rows: 3935 (2016–2022)
VALIDATION rows: 1229 (2023–2024)
2025 rows: 0

## TRAIN forward-chain selections
Margin lambda: 0.1
Total lambda: 1
Win lambda: 0.01

Selection was performed on TRAIN forward-chain folds under v1.126/v1.135; VALIDATION did not select lambda.

## First blind VALIDATION results
Margin: n=1229; MAE=13.134943739927614; RMSE=16.68184258483601; signed bias=-0.187663745399088.
Total: n=1229; MAE=13.319683140960914; RMSE=16.621947930420458; signed bias=0.8802837290920154.
Win probability: n=1229; Brier=0.19430066658361062; log loss=0.5705372752779593.

## Acceptance boundary
These numbers are now exposed historical evidence and MUST NOT be used to retroactively change Challenger A's frozen feature definitions, population, lambda grid, transformations, or model family while treating the same 2023–2024 validation as fresh.

Workflow success and summary metrics establish execution, not full substantive acceptance. Acceptance remains pending artifact-level audit of retained grid results, predictions, calibration, coefficients/scaling, stability slices, hashes, and required-control coverage.

Two v1.126 requested stability slices are explicitly unavailable in the frozen matrix: FBS-vs-FCS classification and conference. This is a bounded reporting gap, not permission to join new metadata after performance and silently rerun the same challenger.

No 2025 TEST evaluation, market join, production promotion, or Challenger redesign is authorized by this checkpoint.
