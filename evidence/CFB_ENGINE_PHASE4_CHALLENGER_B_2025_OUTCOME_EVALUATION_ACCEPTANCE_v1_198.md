# CFB Engine — Challenger B 2025 Outcome Evaluation Acceptance v1.198

Status: **PASS — FROZEN 2025 HOLDOUT EVALUATION INDEPENDENTLY ACCEPTED**
Parents: v1.194, v1.195
Scorer: v1.196
Independent auditor: v1.197

## Canonical scoring evidence
Run: **36215340850**
Scoring artifact: **10897190974**
ZIP digest: `sha256:d2b27f45b3e83ac014676702873424a416faac9613a5c767de97a0feb83085db`

Scored only the canonical frozen v1.188 eligible predictions:
- target population: **934**
- frozen scored predictions: **793**
- frozen exclusions preserved: **141**
- no prediction changes authorized
- market joined: **false**
- refit/recalibration/redesign: **false**

## Independent acceptance evidence
Run: **36215607213**
Head: `ce3b72f6b67a2fa21d106798e1f48121b7bd742f`
Audit artifact: **10896839520**
Audit ZIP digest: `sha256:33a2efbc3dde5cd0376c926f14155d64bd02c76959dcf9999ea06d791ec14ae0`

Independent audit proved:
- exact 934-game target key;
- all target outcomes complete;
- exact 793 scored / 141 frozen-exclusion accounting;
- prediction values numerically unchanged across scoring serialization at atol 1e-12;
- observed maximum serialization delta: margin 3.552713678800501e-15, total 3.552713678800501e-15, win 0.0;
- all scoring artifact hashes reproduced;
- all headline metrics independently recomputed.

## Accepted 2025 holdout metrics
Margin (n=793):
- MAE **14.010470081844714**
- RMSE **17.694958135481073**
- prediction-minus-actual bias **-1.4919042623636025**

Total (n=793):
- MAE **12.774138217188336**
- RMSE **15.750997258972797**
- prediction-minus-actual bias **+0.6666706131303731**

Home-win probability (n=793):
- Brier **0.20027568921840097**
- log loss **0.5833894429766344**

## Interpretation boundary
These are now accepted prospective holdout measurements. Acceptance does not itself establish whether Challenger B is superior or inferior to the production champion, nor authorize tuning to 2025.

2025 may be used for descriptive post-evaluation diagnostics and error attribution, but no refit, recalibration, redesign, threshold optimization, market join, production promotion, or champion replacement follows automatically. Production v1 remains champion/fallback pending the required comparative evidence and explicit promotion authorization.
