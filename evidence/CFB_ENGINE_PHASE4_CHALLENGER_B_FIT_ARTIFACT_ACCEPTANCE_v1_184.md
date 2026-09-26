# CFB Engine — Challenger B Fit Artifact Acceptance v1.184

Status: **PASS — AUTHORIZED FIT ARTIFACT ACCEPTED / NO TEST OR MARKET ACCESS**
Parents: v1.180, v1.181, v1.182
Fit implementation: v1.183
Run: 36212803830
Head: ae95c752402904704f036b94d8fb4a065df7fce4
Artifact: 10895838069
Artifact digest: sha256:3a2cabfcd37e0bcf0cae85efc77eaa6755ffb12734d1e48c4c582ed1de375587

## Independent artifact acceptance
The immutable fit artifact was downloaded and independently inspected before interpretation.

PASS:
- workflow dataset identity/digest gate passed;
- compile and authorized fit steps passed;
- TRAIN rows: 4,806;
- 2023–2024 spent/corroborative rows: 1,440;
- 2025 rows: 0;
- forward-chain grid retains every frozen lambda across 2017–2022 folds plus mean score;
- selected lambdas reproduce the frozen 12-decimal/tie rule:
  - margin: 10
  - total: 100
  - win: 10
- coefficient artifact contains 36 terms per target (intercept + 34 numeric predictors + venue dummy);
- TRAIN scaling contains all 34 numeric predictors;
- predictions contain all 1,440 corroborative rows with margin/total/win outputs and actuals;
- win probabilities are finite and within [0,1];
- all artifact files covered by producer manifest independently reproduce their SHA-256 hashes;
- no 2025 evidence was accessed;
- no market/external-rating data was joined;
- no recalibration or post-performance redesign occurred.

## Corroborative performance
These are **spent/corroborative**, not fresh validation results:
- margin: MAE 12.8050, RMSE 16.5265, bias -1.6646;
- total: MAE 13.5177, RMSE 17.2699, bias -1.7857;
- home-win probability: Brier 0.172826, log loss 0.518799.

These results do not by themselves authorize redesign, TEST access, market joining, promotion, or champion replacement.

## Gate effect
Challenger B has now been fitted and its authorized 2023–2024 corroborative evaluation is accepted as a reproducible artifact.

Next work must reconcile this corrected-population result against the frozen Phase-4 evaluation/governance requirements and determine what additional evidence is permitted before any TEST, market, or promotion boundary is crossed.

Production v1 remains champion/fallback. 2025 remains protected.
