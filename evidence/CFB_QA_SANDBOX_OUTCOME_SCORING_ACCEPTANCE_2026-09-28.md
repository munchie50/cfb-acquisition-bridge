# CFB QA Sandbox — Historical Outcome Scoring Acceptance — 2026-09-28

## Status
**OUTCOME SCORING ACCEPTED AS VALID EVIDENCE / CANDIDATE DISPOSITION NOT YET MADE**

This acceptance is bounded to the authorized historical scoring phase. It does not mutate or promote the Champion, refit any model, access protected 2025 TEST, or admit market/wager/execution information.

## Immutable authorities
- Frozen candidate artifact: GitHub artifact `10970862853`
- Frozen artifact ZIP SHA-256: `8955c64f72ea8068279aed3b4ac1f062200394fbc1eb278cb1864de4da9fe5c9`
- Frozen prediction CSV SHA-256: `ed858f1bd72decd93d02aec4de507c3217470b8d01294c2cf677a2d79ed78ee3`
- Accepted v1.179 ZIP SHA-256: `8eeb67f5da87df4a75f2f785838553679928e370eefeea3945f2b2e688e69780`
- Accepted v1.179 dataset SHA-256: `f8c479c83abf5dac3be6dcb4bba3d6a0996ae2623297a9a3514465824b7c4af8`
- Scorer SHA-256: `0a229ddb38304b38e366853f6b8a095e8008970f16f2620c55805ecf28d61b23`
- Scorer Git blob: `2336002317b4ba0a73acb5c012884f34c6999c67`

## Authoritative scoring execution
- Workflow run: `36491252415`
- Head: `0d0e66f0822e5773f15abd9b76c66558f1266388`
- Result: SUCCESS
- Scored rows: 55,834
- Artifact: `11000219253`
- Artifact ZIP SHA-256: `9fd59b3e98cdf6644cde707ebc991165caacd03ddd48680bce0f463b880e48a3`
- Artifact status: `EXECUTED_NOT_ACCEPTED` at production time; this document records the later independent evidence acceptance.
- Seasons: 2016–2024 only
- 2025 accessed: false
- Market joined: false
- Predictions modified: false
- Refit performed: false

## Independent reproduction
The artifact was downloaded outside the producing runner. Row count, season boundary, artifact ZIP digest, and aggregate candidate metrics were independently recomputed from `scored_predictions.csv`.

S0 full-control metrics:
- margin MAE 14.257939; RMSE 18.200266; signed bias 0.010030
- total MAE 13.446297; RMSE 16.985663; signed bias -0.027768
- win Brier 0.197433; log loss 0.581021; winner-direction accuracy 0.701729

S2_K1 common-game comparison (6,193 exact shared games):
- margin MAE: S0 14.243810 -> S2_K1 14.151976
- total MAE: S0 13.434863 -> S2_K1 13.449582
- win Brier: S0 0.197534 -> S2_K1 0.196344
- win log loss: S0 0.581389 -> S2_K1 0.576034
- winner-direction accuracy: S0 0.701599 -> S2_K1 0.698531

S2_K1 margin MAE improved versus exact common-game S0 in 7 of 9 seasons; it worsened in 2022 and 2024. Heavier S1/S2 shrinkage generally degraded aggregate performance.

## Predeclared large-disagreement QA
Slices were defined outcome-blind in the frozen scorer relative to S0.

For S2_K1 versus exact same-game S0:
- margin disagreement >=7 points, n=696: margin MAE delta -0.481153; total MAE delta -0.236932; Brier delta -0.008975; log-loss delta -0.045895; direction-accuracy delta +0.002874.
- total disagreement >=7 points, n=76: margin MAE delta -1.937679; total MAE delta -1.737441; Brier delta -0.039701; log-loss delta -0.133637; direction-accuracy delta +0.026316. Small sample; descriptive only.
- win-probability disagreement >=0.10, n=1,290: margin MAE delta -0.578468; total MAE delta -0.052322; Brier delta -0.004527; log-loss delta -0.023905; direction-accuracy delta -0.002326.

These slices support a real S2_K1 signal but do not themselves authorize selection or promotion.

## History-depth diagnostic
The immutable frozen prediction artifact does not contain the required history-depth field. Per the predeclared outcome-evaluation rules, this diagnostic is **UNAVAILABLE** and must not be reconstructed after outcomes are visible.

## Interpretation boundary
Historical outcome scoring is accepted as valid QA evidence. S2_K1 is the only current candidate warranting deeper bounded disposition review, but the evidence is mixed: broad margin/proper-win-metric improvement coexists with slight aggregate total-MAE and winner-direction degradation plus season exceptions. No candidate is accepted, rejected, refit, recalibrated, redesigned, or promoted by this document.
