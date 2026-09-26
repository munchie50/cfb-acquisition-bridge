# CFB Engine — Current Recovery Index v1.221

Status: **CURRENT ENTRY POINT / AUTHORITY READBACK REFRESHED**
Date: 2026-09-26
Supersedes v1.176 as entry-point index only. Historical evidence remains preserved.

## Read first
1. `CFB_ENGINE_PHASE4_CHALLENGER_B_2026_FIRST_LIVE_SHADOW_FREEZE_ACCEPTANCE_v1_208.md`
2. `CFB_ENGINE_PHASE4_CHALLENGER_B_2026_FIRST_LIVE_SHADOW_EXCLUSION_ACCOUNTING_v1_215.md`
3. `CFB_ENGINE_PHASE4_CHALLENGER_B_2026_ROLLING_LIVE_SHADOW_LINEAGE_CONTRACT_v1_216.md`
4. `CFB_ENGINE_PHASE4_CHALLENGER_B_2026_REFRESH_PREFLIGHT_NOOP_v1_218.md`
5. `CFB_ENGINE_PHASE4_CHALLENGER_B_CORRECTED_FIT_AUTHORITY_v1_193.md`
6. `CFB_ENGINE_PHASE4_CHALLENGER_B_2025_OUTCOME_EVALUATION_ACCEPTANCE_v1_198.md`

## Current substantive state
Challenger B is fitted under corrected v1.193 authority and has independently accepted 2025 prospective holdout evaluation under v1.198. The 2025 holdout is now spent evidence; v1.201 diagnostics are descriptive only and cannot drive redesign. Raw 2025 outcome-source identity was recovered append-only in v1.219.

The first 2026 live-shadow freeze is independently accepted under v1.208:
- cutoff 2026-09-26T03:47:37.497112+00:00
- 622 future relevant-FBS targets
- 526 FIRST_FROZEN fair predictions
- 96 immutable first-freeze exclusions
- no market, refit, recalibration, redesign, or target-outcome exposure.

All 96 exclusions are exactly reconciled by v1.215. v1.216 defines repeated-target lineage: FIRST_FROZEN is primary prospective evidence; later REFRESH_SNAPSHOT predictions are separate secondary evidence and never overwrite first-frozen records. Cadence is weekly.

v1.217/v1.218 performed an immediate refresh preflight and found source state unchanged; therefore no redundant second prediction snapshot was generated. Next refresh waits for the weekly cadence unless a separately documented operational exception applies.

2026 FBS membership remains 138 teams under v1.203 with source provenance appended in v1.220.

## Model identity
Current accepted Challenger-B fit authority is v1.193:
- TRAIN 2016–2022: 4,700 eligible games
- spent/corroborative 2023–2024: 1,546
- lambdas: margin 0.1, total 0.1, win 0.01
- coefficients SHA `bf15ce41180bfb4e250d311df279e98c13b65432756ae07f7a30264cbae0e221`
- scaling SHA `68fb5193ccb8828ac8d34dfe820101181c2bde078a04a6d5afd4c08bcf0cab45`

## 2025 accepted holdout metrics
On 793 frozen eligible predictions:
- margin MAE 14.010470081844714; RMSE 17.694958135481073; bias -1.4919042623636025
- total MAE 12.774138217188336; RMSE 15.750997258972797; bias 0.6666706131303731
- win Brier 0.20027568921840097; log loss 0.5833894429766344

## Current locks
- Production v1 remains champion/fallback.
- No Challenger-B production promotion without separate required evidence/checkpoint and explicit authorization.
- No refit/recalibration/feature redesign/threshold optimization from 2025 or 2026 shadow outcomes.
- Historical market diagnostics remain blocked by v1.144 source-semantic qualification; no market join is authorized.
- Never retroactively create prospective predictions for games at/before a snapshot cutoff.
- Preserve frozen predictions/exclusions and append outcomes/evaluations separately.

## Current frontier
1. Wait for the next weekly 2026 live-shadow cadence point.
2. At that point run a fresh source preflight before any REFRESH_SNAPSHOT producer.
3. If source state materially advances, generate a separately labeled refresh for then-future targets under v1.216 and independently audit it.
4. Keep FIRST_FROZEN as the primary prospective evidence lineage.
5. Market work remains blocked unless its source/semantic contract is separately qualified.
6. Production promotion remains unavailable absent a separate promotion gate and explicit authorization.

## Superseded entry-point warnings
- v1.176 is historical and stale as a current entry point; its statements that Challenger-B fitting and 2025 scoring are unauthorized were later superseded.
- v1.184 fit details are superseded by v1.193.
- v1.185 stale lambda transcription is superseded by v1.193 while its boundary concepts remain historical.
- v1.99/v1.142/v1.174 remain historical integration/recovery evidence, not the current frontier.
