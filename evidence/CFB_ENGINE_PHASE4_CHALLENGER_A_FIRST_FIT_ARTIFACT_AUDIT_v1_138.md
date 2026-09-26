# CFB Engine — Challenger A First-Fit Artifact Audit v1.138

Status: SUBSTANTIVE ACCEPTANCE BLOCKED — REQUIRED CONTROL GAP
Scope: v1.136 fit artifact 10892848773
Candidate performance is historical/exposed; no redesign authorized.

## Artifact integrity
Downloaded exact GitHub Actions artifact 10892848773.
Artifact ZIP digest from GitHub: sha256:7d33dde3244cf764757467a62a04b6c93e40918e1ce04cb22ba9a5938a67aa50.

Eight retained files were inspected. Every file hash in manifest.json independently recomputed exactly:
- blind predictions 34ab0104a7521d2523266ea89e395393a4087d1098bcaa17dc28bd3abd6988c2
- coefficients fc75478f46f5db391b6e59e2280c1ff39c9c9217a1846d34a033a5af381f6422
- summary 1072100dcb377c30370373d9fcad3dfd5afbc1245678d6758687e0b7d20749bd
- forward-chain grid 981587c4c9f62c02688d7c003b21eaf6594107a4d3b1bc06b6a863448e4aeb7d
- scaling bfe1441b9b778b3fe6b9cfac90e195e973c1e1a966bf958eed4554a7ce045fba
- stability 455dad407b0ecf1fa5912043903eee180bb52370d1a4258b4db7edbdb779743a
- calibration f0267917b1ea739266c2fdaba019abfb62b801af915eacf57991dc03a3347263

## Reproduction checks
Forward-chain grid has 168 records = 3 targets x 8 lambdas x (6 season folds + 1 mean).
Grid minima reproduce frozen selections exactly:
- margin lambda 0.1, mean fold MAE 14.109387
- total lambda 1, mean fold MAE 13.721023
- win lambda 0.01, mean fold Brier 0.200352

Blind validation predictions:
- 1229 rows
- 0 duplicate game IDs
- seasons only 2023 and 2024
- raw win probabilities finite and within [0.008875, 0.992969]

Selected coefficients:
- 36 terms per target (intercept + 34 numeric + venue)
- no nonfinite coefficients

TRAIN scaling:
- 34 numeric features
- no nonfinite mean/SD
- minimum SD > 0

Calibration:
- 10 populated decile bins
- bin counts sum exactly 1229

Stability output:
- season, venue_state, deterministic early/later season, predicted-margin bucket, regime
- FBS-vs-FCS and conference remain unavailable because those metadata were not in the frozen matrix; do not post-performance join and silently rerun Challenger A.

## Required-control gap
v1.126 required:
1. lambda=0 within-family control — PRESENT in retained grid.
2. permanent simple baseline where exact comparable output is recoverable — repository search did not locate a named/recoverable comparable baseline at this checkpoint; classify NOT RECOVERED, do not invent one.
3. deliberately invalid future-information sentinel in an isolated QA path proving the candidate dataset/config excludes it and 2025 — NOT EXECUTED by v1.136.

Therefore v1.136 is not yet substantively accepted. The missing sentinel is a QA/control defect, not permission to alter the fitted candidate or reuse validation as fresh evidence.

Exact next action: execute an isolated sentinel QA against the frozen accepted dataset/config. It must not fit, score, alter, or regenerate Challenger A performance. Persist the result, then reconsider acceptance.

2025 TEST remains unexposed to model evaluation.
