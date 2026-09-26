# CFB Engine — Challenger B Corrected Fit Authority v1.193

Status: **PASS — v1.192 CONTRADICTION RESOLVED / EXACT v1.183 ARTIFACT RESTORED AS FIT AUTHORITY**
Parents: v1.180, v1.183, v1.184, v1.192
Production v1 remains champion/fallback. 2025 outcomes remain sealed.

## Resolution

The exact accepted v1.179 dataset artifact 10896565577 was independently downloaded and read back.

It contains 6,246 eligible rows with season counts:
- 2016 599
- 2017 679
- 2018 735
- 2019 739
- 2020 463
- 2021 738
- 2022 747
- 2023 762
- 2024 784

Therefore:
- TRAIN 2016–2022 = **4,700**
- SPENT/CORROBORATIVE 2023–2024 = **1,546**
- TEST 2025 = **0**

Dataset SHA-256 independently reproduces the workflow-pinned value:
`f8c479c83abf5dac3be6dcb4bba3d6a0996ae2623297a9a3514465824b7c4af8`.

These counts exactly match v1.183 run 36212803830 and its immutable artifact 10895838069.

## Correct frozen fit identity

The authoritative Challenger-B fit is the exact v1.183 artifact:
- artifact: 10895838069
- ZIP digest: `sha256:3a2cabfcd37e0bcf0cae85efc77eaa6755ffb12734d1e48c4c582ed1de375587`
- selected coefficients SHA-256: `bf15ce41180bfb4e250d311df279e98c13b65432756ae07f7a30264cbae0e221`
- TRAIN scaling SHA-256: `68fb5193ccb8828ac8d34dfe820101181c2bde078a04a6d5afd4c08bcf0cab45`
- selected lambda margin: **0.1**
- selected lambda total: **0.1**
- selected lambda win: **0.01**
- TRAIN rows: **4,700**
- spent/corroborative rows: **1,546**
- 2025 rows: **0**

The v1.183 forward-chain grid and implementation reproduce those selections under the frozen 12-decimal score / larger-lambda tie rule.

## Reclassification

v1.184 is superseded for row counts, selected lambdas, and corroborative metrics. Its incorrect 4,806 / 1,440 and 10 / 100 / 10 values are an evidence-transcription defect.

No refit, recalibration, feature change, or post-performance redesign is required or authorized.

Downstream v1.185/v1.187 references to the incorrect lambda values are corrected by this artifact-backed authority. Their chronology, leakage, no-market, no-refit, and outcome-isolation rules remain in force.

## Next gate

v1.188 may resume using the exact hashes and coefficient rows above. The prospective producer must cryptographically verify the frozen scaling and coefficient files before prediction.

v1.189 must independently reproduce those hashes and recompute predictions from the frozen files before acceptance.

2025 outcomes remain sealed. No scoring or promotion is authorized by this correction.
