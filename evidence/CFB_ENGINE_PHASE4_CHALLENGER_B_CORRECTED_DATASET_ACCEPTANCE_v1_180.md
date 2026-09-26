# CFB Engine — Challenger B Corrected Dataset Acceptance v1.180

Status: **PASS — CORRECTED DATASET FREEZE ACCEPTED / FITTING NOT AUTHORIZED**
Parents: v1.173, v1.178
Producer: v1.179
Run: 36212604067
Head: cdf076d3da0c23d18ad1db5328c8fa8fc4cd82ac
Artifact: 10896565577
Artifact digest: sha256:8eeb67f5da87df4a75f2f785838553679928e370eefeea3945f2b2e688e69780

## Independent acceptance
The immutable v1.179 artifact was downloaded and independently audited against the prospectively frozen v1.178 contract and committed v1.180 auditor logic.

PASS:
- full corrected target population accounted: 7,701 = 6,246 model-eligible + 1,455 excluded;
- eligible and excluded game IDs are unique and disjoint;
- population/competition-class target totals equal eligible+excluded disposition totals across all five represented class combinations;
- exactly 34 numeric predictors plus frozen venue state;
- no NA among accepted model-eligible predictors;
- source corrected-feature artifact pinned to 10895523493 / sha256:702930b2ba905c9f917acbc627d12342e8190cfb44a4c8afd1aee49fbf59e239;
- partitions frozen as TRAIN 2016–2022, SPENT/CORROBORATIVE 2023–2024, protected TEST 2025;
- no 2025 rows/inputs;
- no market-like predictor names;
- producer manifest file hashes independently reproduced;
- no copied v1.128 temporal-blacklist exclusion reason;
- every excluded game has explicit current-input-derived reason.

## Exclusion interpretation
The 1,455 exclusions are dominated by prospectively expected opening/no-prior complete-case failures and corrected history-incomplete failures. One game required specific review because it had only `home_required_feature_na` without opening/history-incomplete status:
- 2021 game 401282182, Florida International vs Texas State.
- FIU had one qualified prior game and complete source history, but zero prior rushing plays.
- `rush_yards_per_play` is therefore NA under the frozen zero-denominator=>NA rule.
- Complete-case exclusion is correct; this is not a data-loss or identity defect.

No exclusion rule was changed after observing the count.

## Frozen artifact contents
- challenger_b_dataset_v1_179.csv
- challenger_b_exclusion_ledger_v1_179.csv
- challenger_b_population_contract_v1_179.csv
- challenger_b_population_disposition_v1_179.csv
- challenger_b_config_v1_179.json
- manifest_v1_179.json

## Gate effect
The corrected-population Challenger-B dataset layer is accepted.

**This acceptance does not authorize fitting or scoring.** The next step is pre-fitting reconciliation against all frozen authority and an explicit fitting-authorization checkpoint. 2025 remains protected; no market join; production v1 remains champion/fallback.
