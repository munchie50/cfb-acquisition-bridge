# CFB Engine — Current Recovery Index v1.225

Status: **CURRENT ENTRY POINT — CFB PRODUCTION CHAMPION ACTIVE**
Date: 2026-09-26
Supersedes v1.223 as the current entry point. Historical evidence remains preserved.

## Read first
1. CFB_ENGINE_PRODUCTION_CHAMPION_NAMING_AUTHORITY_v1_222.md
2. CFB_ENGINE_PHASE4_CHALLENGER_B_2026_FIRST_LIVE_SHADOW_FREEZE_ACCEPTANCE_v1_208.md
3. CFB_ENGINE_PHASE4_CHALLENGER_B_2026_FIRST_LIVE_SHADOW_EXCLUSION_ACCOUNTING_v1_215.md
4. CFB_ENGINE_PHASE4_CHALLENGER_B_2026_ROLLING_LIVE_SHADOW_LINEAGE_CONTRACT_v1_216.md
5. CFB_ENGINE_PHASE4_CHALLENGER_B_CORRECTED_FIT_AUTHORITY_v1_193.md
6. CFB_ENGINE_PHASE4_CHALLENGER_B_2025_OUTCOME_EVALUATION_ACCEPTANCE_v1_198.md
7. CFB_ENGINE_ADAM_SCREENSHOT_INGESTION_BOUNDARY_v1_224.md

## Current production authority
The model historically developed as Challenger B is now the **CFB Production Champion** under v1.222.

The former production-v1 model is retired as a non-operational historical reference. It is not the current champion or a represented working fallback.

Historical filenames and artifacts retain Challenger B terminology for audit integrity. New operational, maintenance, hot-sheet, and recovery language uses CFB Champion / Production Champion.

## Champion identity
The Champion is unchanged from accepted v1.193:
- TRAIN 2016–2022: 4,700 eligible games
- spent/corroborative 2023–2024: 1,546
- lambdas: margin 0.1, total 0.1, win 0.01
- coefficients SHA bf15ce41180bfb4e250d311df279e98c13b65432756ae07f7a30264cbae0e221
- scaling SHA 68fb5193ccb8828ac8d34dfe820101181c2bde078a04a6d5afd4c08bcf0cab45

## Accepted evidence
2025 prospective holdout v1.198: 793 frozen eligible predictions, independently scored and accepted.

2026 first prospective production lineage derives from v1.208:
- cutoff 2026-09-26T03:47:37.497112+00:00
- 622 future relevant-FBS targets
- 526 FIRST_FROZEN predictions
- 96 frozen exclusions
- independent recomputation/hash audit passed.

v1.215 reconciles all 96 exclusions. v1.216 governs repeated-target lineage and refresh snapshots.

## Production maintenance direction
Existing scheduled CFB tasks remain the operational clock and should not be duplicated or rescheduled.

Production integration must ensure the CFB Champion state is current at task execution before downstream market, availability, health, or QA work consumes it. Refreshes preserve frozen model identity and prospective chronology. FIRST_FROZEN is immutable; later valid predictions are REFRESH_SNAPSHOT records.

If no material source state changed, refresh is a no-op. If refresh/audit fails, fail closed and retain the last accepted Champion state.

## Locks
- No outcome-driven refit, recalibration, feature redesign, or retroactive prediction rewrite.
- Market inputs remain subject to their separate source/semantic qualification.
- Never create a prospective prediction after target kickoff.
- Preserve accepted predictions/exclusions and append later state.
- No statistical superiority over the retired model is claimed because no valid comparable 2025 legacy artifact exists.

## Adam-provided screenshot boundary
v1.224 is an active procedural input control for Adam-provided screenshots. Screenshots are evidence containers, not trusted model-input containers. Mixed screenshot content must be decomposed observation-by-observation, classified, provenance/time attached where available, and routed only to contract-authorized destinations. Successful extraction does not grant model-input permission. Market/execution, factual, third-party evaluative, outcome, irrelevant, and ambiguous content remain separated under their existing downstream contracts. This control does not change the Champion model, features, fit, predictions, or market/outcome authorization boundaries.

## Current frontier
Build the Champion production refresh/compatibility entry point around the proven preflight, prediction, acceptance, and lineage components so existing scheduled CFB tasks consume current accepted Champion state without modifying their schedules.

## Superseded warnings
- v1.223 is superseded as current entry point by this file; its production authority and frontier remain inherited except for addition of the v1.224 screenshot boundary.
- v1.221 is historical and its statement that production v1 remains champion/fallback is no longer current.
- v1.176 is historical/stale.
- v1.184 fit details are superseded by v1.193.
- v1.185 stale lambda details are superseded by v1.193.
