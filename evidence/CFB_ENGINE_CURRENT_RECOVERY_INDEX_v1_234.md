# CFB Engine — Current Recovery Index v1.234

Status: **CURRENT ENTRY POINT — CFB BETA PRODUCTION CHAMPION ACTIVE**
Date: 2026-09-26
Supersedes v1.232 as the current entry point. Historical evidence remains preserved.

## Read first
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

## Current production authority
The model historically developed as Challenger B is the **CFB Beta Production Champion** under v1.222 plus the maturity clarification in v1.229. It is operational production under controlled real-world beta use; production does not imply a fully mature or fully validated betting system.

The former production-v1 model is retired as a non-operational historical reference. It is not the current champion or a represented working fallback.

Historical filenames and artifacts retain Challenger B terminology for audit integrity. New operational, maintenance, hot-sheet, and recovery language should use CFB Beta Production Champion / Beta Champion where maturity matters, with Champion acceptable shorthand.

## Beta production maturity
v1.229 classifies the working Champion as Beta Production: operational in the real-world controlled workflow while prospective evidence, market comparison, execution behavior, outcomes, and missing controls are evaluated. The retired production-v1 state was primarily the prior framework/engine state and is not a working fallback. Removal of Beta requires a later explicit maturity checkpoint; it is not automatic.

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

## Betting-layer evidence and research
v1.226 activates prospective capture of market/price history, executable-vs-benchmark separation, qualified closing-line comparison/CLV, key-number context, timing/execution quality, and PASS/WAIT/no-bet opportunities. These are evidence/diagnostic controls only; raw point edge is not cover probability or EV.

v1.227 preserves the governed research path for edge calibration, disagreement decomposition, side/total/ML expression, uncertainty, book dispersion/line shopping, cover/total probability, EV, alternative-line price tradeoffs, staking, portfolio exposure, correlation and parlays. These remain candidate research topics subject to prerequisites, frozen tests, independent acceptance, and applicable promotion authorization.

## Closed-loop Beta learning
v1.231 requires material real-world Beta observations to remain traceable from observation through classification, disposition, testing, prospective Beta exposure, independent evaluation, and explicit closure or supersession. Sunday QA is the principal reconciliation point; unresolved learning items remain visible across cycles. Sandbox success establishes controlled viability only and cannot by itself establish real-world validity or authorize production change. Learning layers remain separated so prediction, data, operations, market, decision, timing, execution, close, and outcome evidence teach the correct lesson.

## Weekly Beta learning review
v1.233 requires the post-Sunday-QA/Q&A Weekly Beta Learning Review to be persisted as durable development evidence. Future material builds/reviews must consult accumulated weekly reviews and unresolved learning items, explicitly incorporating/testing, deferring with rationale, superseding, or marking non-applicable relevant lessons. The review includes an outcome-blind reconstruction of the Beta Champion's pre-event matchup assessment versus each wager Adam actually executed, followed separately by close/result/postgame learning. Adam wagers remain observational execution evidence and never Champion inputs.

## Current frontier
Build the Champion production refresh/compatibility entry point around the proven preflight, prediction, acceptance, and lineage components so existing scheduled CFB tasks consume current accepted Champion state without modifying their schedules.

## Superseded warnings
- v1.232 is superseded as current entry point by this file; its Beta authority, closed-loop learning control, and engineering frontier remain inherited, with v1.233 adding the weekly learning output and future-build consumption contract.
- v1.230 is superseded as current entry point by this file; its Beta Production authority and engineering frontier remain inherited, with v1.231 adding closed-loop learning governance.
- v1.228 is superseded as current entry point by this file; its Champion-refresh frontier and betting evidence/research governance remain inherited, with v1.229 clarifying current maturity as Beta Production.
- v1.225 is historical and was superseded by v1.228.
- v1.223 is historical; its production authority was carried forward through v1.225 and this index.
- v1.221 is historical and its statement that production v1 remains champion/fallback is no longer current.
- v1.176 is historical/stale.
- v1.184 fit details are superseded by v1.193.
- v1.185 stale lambda details are superseded by v1.193.
