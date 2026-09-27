# CFB Engine — Current Recovery Index v1.240

Status: **CURRENT ENTRY POINT — CFB BETA PRODUCTION CHAMPION ACTIVE**
Date: 2026-09-27
Supersedes v1.234 as the current entry point. Historical evidence remains preserved.

## Recovery rule
This file is the single current recovery doorway. Scheduled tasks and manual recovery must discover the newest accepted Current Recovery Index from repository state rather than pinning an older index in prose. Read back this file and required dependencies before downstream work.

## Read first / active authority
1. CFB_ENGINE_BETA_PRODUCTION_MATURITY_CLASSIFICATION_v1_229.md
2. CFB_ENGINE_PRODUCTION_CHAMPION_NAMING_AUTHORITY_v1_222.md
3. CFB_ENGINE_PHASE4_CHALLENGER_B_2026_FIRST_LIVE_SHADOW_FREEZE_ACCEPTANCE_v1_208.md
4. CFB_ENGINE_PHASE4_CHALLENGER_B_2026_FIRST_LIVE_SHADOW_EXCLUSION_ACCOUNTING_v1_215.md
5. CFB_ENGINE_PHASE4_CHALLENGER_B_2026_ROLLING_LIVE_SHADOW_LINEAGE_CONTRACT_v1_216.md
6. CFB_ENGINE_PHASE4_CHALLENGER_B_CORRECTED_FIT_AUTHORITY_v1_193.md
7. CFB_ENGINE_PHASE4_CHALLENGER_B_2025_OUTCOME_EVALUATION_ACCEPTANCE_v1_198.md
8. CFB_ENGINE_ADAM_SCREENSHOT_INGESTION_BOUNDARY_v1_224.md
9. CFB_ENGINE_PROSPECTIVE_BETTING_EVIDENCE_LAYER_CONTRACT_v1_226.md
10. CFB_ENGINE_BETTING_LAYER_RESEARCH_TEST_ROADMAP_v1_227.md
11. CFB_ENGINE_BETA_LEARNING_CLOSURE_CONTRACT_v1_231.md
12. CFB_ENGINE_WEEKLY_BETA_LEARNING_REVIEW_CONTRACT_v1_233.md
13. CFB_ENGINE_CHAMPION_CHALLENGER_VISIBILITY_AND_DECISION_CADENCE_v1_235.md
14. CFB_ENGINE_WEEKLY_FULL_SLATE_AND_HOT_SHEET_OUTPUT_CONTRACT_v1_236.md
15. CFB_ENGINE_EARLY_EXPOSURE_AND_LEARNING_CADENCE_CONTROL_v1_237.md
16. CFB_ENGINE_CONTROLLED_EXPERIMENTAL_CAPITAL_AND_PARLAY_EXPOSURE_v1_238.md
17. CFB_ENGINE_SCHEDULED_RUN_COMPLETION_PERSISTENCE_OBSERVABILITY_v1_239.md

## Current production authority
The model historically developed as Challenger B remains the **CFB Beta Production Champion** under v1.222 and v1.229. The former production-v1 model is retired/non-operational historical reference and is not a current Champion or working fallback.

Champion identity remains the accepted v1.193 identity:
- TRAIN 2016–2022: 4,700 eligible games
- spent/corroborative 2023–2024: 1,546
- lambdas: margin 0.1, total 0.1, win 0.01
- coefficients SHA bf15ce41180bfb4e250d311df279e98c13b65432756ae07f7a30264cbae0e221
- scaling SHA 68fb5193ccb8828ac8d34dfe820101181c2bde078a04a6d5afd4c08bcf0cab45

Accepted 2025 prospective holdout remains v1.198: 793 frozen eligible predictions, independently scored/accepted.

2026 first prospective production lineage remains rooted in v1.208:
- cutoff 2026-09-26T03:47:37.497112+00:00
- 622 future relevant-FBS targets
- 526 FIRST_FROZEN predictions
- 96 frozen exclusions
- independent recomputation/hash audit passed.
v1.215 reconciles exclusions; v1.216 governs repeated-target lineage/refresh.

## Active operational additions since v1.234
- v1.235 makes Champion-vs-Challenger status prominent and governs decision cadence.
- v1.236 governs weekly full-slate / Hot Sheet output.
- v1.237 requires early prospective exposure at earned maturity and explicit TIME-HIDDEN review.
- v1.238 authorizes and governs the separate $20 experimental sandbox and parlay exposure; production and sandbox ledgers remain separate.
- v1.239 makes repository recovery-index discovery authoritative for scheduled runs and requires explicit RUN_PASS/RUN_INCOMPLETE/RUN_FAIL, durable run receipts, persistence proof, independent artifact readback, and separate delivery state.

## Scheduled-run completion
Existing scheduled tasks remain the operational clock and should not be duplicated merely to implement this control. They must consume this recovery doorway and v1.239.

A scheduler/platform success is not engine success. Sunday QA is RUN_PASS only when its required Weekly Beta Learning Review is persisted and independently read back and the run receipt is persisted/read back. Missing required artifacts must be RUN_INCOMPLETE or RUN_FAIL with exact blockers.

## Production maintenance
FIRST_FROZEN is immutable; later valid predictions are append-only REFRESH_SNAPSHOT. Never create a prospective prediction after kickoff. If no material source state changed, refresh may be a no-op. If refresh/audit fails, fail closed and retain last accepted Champion.

## Evidence separation and locks
Keep prediction, market, decision, execution, qualified close/CLV, and outcome separate. User screenshots/wagers remain observational/execution evidence only and never Champion model inputs. No outcome-driven refit, retroactive prediction rewrite, invented probability/EV/confidence, automatic Champion mutation, or automatic Challenger promotion.

## Weekly learning
Sunday QA remains the principal weekly reconciliation point. v1.233 review requirements, v1.235 Champion/Challenger prominence, v1.237 TIME-HIDDEN/early-exposure learning, and v1.238 sandbox/parlay learning all apply. Future material builds/reviews must consume accumulated Weekly Beta Learning Reviews and unresolved learning items.

## Superseded warnings
- v1.234 is superseded as current entry point by this file. Its Beta authority and weekly-learning lineage remain inherited.
- v1.232, v1.230, v1.228, v1.225, v1.223, v1.221 and v1.176 remain historical/superseded as already documented.
- v1.221's production-v1 champion/fallback statement is not current.
- v1.184 fit details and v1.185 lambda details remain superseded by v1.193.

Scientific effect: none. This index integrates current recovery/operational authority without changing the frozen Beta Champion.
