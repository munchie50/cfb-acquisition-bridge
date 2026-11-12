# CFB Integrated Betting Intelligence — Governed Implementation Roadmap
Version: PLAN v0.1 | Created: 2026-11-11 | Status: PLANNED / NOT BUILT / NOT PROMOTED
Owner: CFB Engine established governance | Scope: 2026 learning and 2027 readiness
Authority: This is a tracking/implementation plan only, NOT a new master contract, Champion change, betting rule, or production authorization.

## North-star objective
Use every authentic pregame game evaluation, archived odds/market quote, ranked recommendation, actual execution, and final result to discover, test and eventually promote evidence-supported betting advantages. Maximize reproducible net value and practical opportunity coverage while containing downside, avoiding overfitting, preserving user-facing straight-bet consistency, and maintaining reliable weekly delivery. No strategy guarantees profits.

## Governing authority and anchors
Follow current constitution/master spec/contracts and latest recoverable current-state/recovery frontier before every build/write. This plan is subordinate to them.
- Existing weekly learning contract: evidence/CFB_ENGINE_WEEKLY_BETA_LEARNING_REVIEW_CONTRACT_v1_233.md (including November 11 confidence, season backfill, shared exposure and missed-opportunity additions).
- Existing execution ledger: evidence/operational/CFB_EXECUTION_LEDGER.md (actual tickets only; no prediction/training contamination).
- Existing season replay: evidence/audits/CFB_2026_SEASON_BETTING_REPLAY_BACKFILL_20261111.md (November 11 checkpoint; historical cohort and timing work remains incomplete).
- Established production Champion/fallback v5.0 and accepted governed controls as determined by FRESH current authority (never infer from this plan alone).
- Preserve the existing four production scheduled tasks; no new scheduled task is authorized by this plan. Reuse existing Sunday weekly QA/learning cycle.
- Original frozen Champion predictions must remain unchanged; actual wager tickets are execution evidence, not model inputs. No hindsight odds/rank reconstruction.
- Historical read-only simulation is not bookmaker execution evidence. Preserve provenance and qualifiers.

## Design commitments (user-confirmed November 11)
1. Whole-slate game-by-game examination, not merely tickets or Top 10: independently evaluate spread, moneyline and over/under where authentic original model/prospective decision and quoted market evidence exist.
2. Two-track outputs sharing one evidence foundation: stable independently chosen Top 10 straight-bet recommendations; separate value-ranked parlay research with overlap permitted and explicitly measured. Do NOT automatically demote parlays to ranks 11–30, or automatically exclude ranks 1–10.
3. Sliding-scale parlay matrix: confidence depth Top 10, 15, 20, 25, 30 crossed with 2, 3, 4, 5 legs (extend only on justified evidence). Mixed spreads/ML/totals allowed; no same-game multi-leg builder without qualified joint offer and specific authorization. Four-leg Top 30 is first research benchmark, not mandatory final output.
4. For each valid time snapshot analyze candidate success probability, offered odds, payout, expected net return, loss probability, calibration error, correlation/dependence, shared-leg exposure, max drawdown, and opportunity count. High payout alone and high hit rate alone never qualify a strategy.
5. Illustrative research: 10 distinct hypothetical parlays at $5 each ($50 risk) with observed hit count and gross/net payout. Do not force 10 picks/week. User also values meaningful high-payout two-leg tickets (e.g. $2 returning $20–$30 gross) IF plausibly positive-value; break-even joint probability must be computed at actual offered odds.
6. Avoid runaway over-tightening: no automatic restriction of confidence window, markets, recommendation coverage or betting frequency. Track coverage and missed opportunities, foregone EV, delivery time, and operational burden alongside any projected ROI improvement. The best filter must beat unchanged baseline on comparable forward evidence and benefit/cost. No blind retrofitting.
7. Autonomous READ-ONLY pattern discovery and hypothesis generation permitted within already authorized runs; promotion, model tuning, changed selection thresholds, changed betting risk rules, or production output modifications require explicit governed validation/approval.
8. Keep proven pregame/published recommendations, published parlay builds, unrecommended but pre-event documented watch/PASS cases, actual tickets, and shadow simulations separate. Do not rewrite what was recommended. Preserve absent price/rank evidence as missing.
9. Preserve operational reliability and 1–2 weekly execution-trip practical window; no added operational block, source gate, extra schedule or unnecessary maintenance load.
10. Weekly learning should generate its own falsifiable, prioritized hypotheses (including what went RIGHT and missed opportunities), compare against alternatives, independently verify, and carry unresolved items to the existing learning ledger; do not create a competing hypothesis ledger.

## Study methods and evidence boundaries
- Rank only by authentic published frozen decision window; use a consistent prospective cutoff. Track frozen line vs decision quote vs execution quote vs qualified close separately, with UTC and source reference.
- Grade game-by-game outcome using authentic final results, keeping market-specific definitions, pushes, voids, and payout rules.
- Price evidence classes: VERIFIED_EXECUTABLE (proof of actual combined odds/offer in shared window), INDICATIVE_REPLAY (genuine synchronized pregame leg quotes but combination inferred), RESEARCH_ONLY (insufficient chronology/offer), EXCLUDED. No invented lines/odds, synthetic available offers or hindsight-selected winners.
- For 30 distinct eligible legs, C(30,4)=27,405 theoretical four-leg combinations before qualification. If a game has alternative selections, do not put two selections from the same game in the same standard combination. Deduplicate and identify mutually related bets.
- Evaluate joint probabilities with explicit independence benchmark plus correlation/model-error sensitivity; reject unsupported exact confidence claims. Track odds-to-probability implied thresholds and price drift.
- Rank hypothetical portfolios using PREDECLARED selection policy, not selection after outcomes. Compare top-k 0 through 10 builds, flat theoretical $2 and $5 stakes, payout and portfolio net returns, overlap and adverse shared-loss scenarios. Use time-split historical discovery vs later prospective validation; avoid treating overlapping parlays as independent observations.
- Baselines: existing straight Top 10, full eligible slate, existing archived parlays, no-parlay portfolio; compare like-for-like time windows, price availability, and sample coverage. Track net profit/ROI, expected value uncertainty, calibration/Brier where applicable, drawdown, CLV when qualified, coverage, timing, misses, and execution burden.
- The objective is positive prospective risk-adjusted net value with usable coverage, not an arbitrary 70–80% four-leg hit promise or fixed number of picks. Small samples and confounded results are hypotheses, not proven edges.

## Milestone tracker (must be updated with hard evidence, not optimistic colors)
M0 — PLAN_PERSISTED: Create, read back and reference this roadmap; record exact commit/blob and future resume instruction. Acceptance: verified persisted text. Status: VERIFIED — initial creation commit d91c9ec7f096014545505445d828664fe113651f, original blob 699d1ed66eb3fdadfcc9816e13a7992cab90425a independently fetched with milestone and recovery sections intact. This status-update commit requires its own readback.
M1 — AUTHORITY_AND_DATA_INVENTORY: Pin current recovery/current-state, original weekly frozen outputs, quotes, actual published cards, result grades, execution ledger; inventory weeks and gaps by field, source revision and cutoff; resolve precedence without guessing. Acceptance: evidence manifest with true coverage and exact source IDs. Status: NOT_STARTED.
M2 — SEASON_BASELINES: Extend the existing November 11 historical replay, source-grounded game/market performance and published vs missed opportunities; separate actual and shadow returns. Acceptance: reproducible populated week/market/rank rows with priced denominators, gaps and exact arithmetic. Status: NOT_STARTED.
M3 — READ_ONLY_MATRIX_IMPLEMENTATION: Enumerate depth x legs x market combinations and freeze historical selections/quotes, shared exposure; compare payout eligibility. Acceptance: deterministic rerun, validity and missing-evidence tests, no production changes. Status: NOT_STARTED.
M4 — DISCOVERY_AND_HYPOTHESIS_REVIEW: Study rank depth, leg count, price bands, mixed markets, probability calibration, edge/ROI, concentration, price timing, missed recommendations and opportunity loss; generate falsifiable hypotheses and negative controls. Acceptance: claims tied to counts and alternative explanations in existing weekly learning review. Status: NOT_STARTED.
M5 — PROSPECTIVE_SHADOW_VALIDATION: Freeze selected methods BEFORE future kickoffs; evaluate later untouched games/weeks, no result-based edits. Acceptance: documented out-of-sample performance, stability, uncertainty, opportunity coverage and weekly repeatability. Status: NOT_STARTED.
M6 — GOVERNED_PROMOTION_DECISION: Assess whether limited analytical/Hot Sheet improvements materially beat unchanged baseline without harming production reliability or losing valuable bets; explicit authorization and rollback. Acceptance: source/QA evidence + specific promotion approval, independent production readback and natural-cycle verification. Status: NOT_AUTHORIZED.
M7 — SUSTAINED_OPERATION: Sunday learning outputs reproducibly consume data, retain lessons, show measured changes and watch opportunity coverage/operational burden. Acceptance: multiple natural scheduled cycles and independent readback with unchanged authorized governance. Status: NOT_STARTED.

## Current starting evidence / established incomplete work (November 11)
- Current replay checkpoint commit b8f4c69188f8df8197ff3808deca61c2e922f05c: actual wager census and Week 10 ranked replay, simulated historical cohorts and window reconciliation incomplete. Read exact file above before proceeding.
- November 11 weekly learning contract already orders season backfill, confidence replay, shared exposure, missed opportunities, and one useful weekly diagnostic. Do not duplicate tasks.
- Week 10 archived simulated three- and four-leg builds were overlapping; one win is not independent support. One actual three-leg ticket does not prove durable four-leg hit rate.
- Existing market monitor stability and current user-facing recommendation delivery outrank discretionary research work.
- No data inventory, completed four-leg Top30 historical matrix, candidate outcome statistics, or promotion has been established by this roadmap.

## Recovery / anti-loss protocol
On any future 'continue plan' or routine request: (1) read live current authority/recovery frontier and this plan; (2) re-read last verified evidence/checkpoints; (3) pick the highest-priority unaccepted milestone or narrowly useful independent subtask; (4) do smallest bounded work without altering production; (5) persist dated evidence and explicit resume point; (6) independently read back; (7) update THIS plan's milestone status only with a concrete evidence link/commit and next actionable step. Keep changes serialized where dependent and reconcile independent runner outputs. NEVER mark built as executed, verified, accepted, or production by implication. Preserve failed/negative attempts and supersession. If blocked, audit original records/logs selectively before asking user.
Use the existing weekly learning review and recovery conventions, not a new monitoring task or parallel authority structure.

## Decision log
2026-11-11: User confirmed integrated plan and requested durable long-lived tracking. Scope approved for design and read-only research; production promotions NOT authorized. Top 30 four-leg research broadened into sliding-scale matrix, including all three market styles and protected Top 10.

## M1 continuation checkpoint — November 11, 2026

M1 — **IN_PROGRESS / bounded inventory VERIFIED**, superseding the initial NOT_STARTED entry above. [Source inventory](../audits/CFB_INTEGRATED_BETTING_INTELLIGENCE_M1_INVENTORY_20261111.md) persisted at commit `3c22ace02ec8fd21dd7a293678d7c957a58fd2fa`, blob `903606c040c7fa3a0fe370505128fbd938fddbdc`, and fetched back with identical text. Verified source coverage includes 349 modeled final joins across Weeks 4–10, 199/200 modeled rows displaying all three market pairs across the selected Weeks 7–10 sheets, and one recovered 10-rank card for Week 10. The archive quotes and published ranks retain separate denominators.

Resume at the Week 10 exact directed-ID join of original forecasts, original quote records and qualified finals. Validate kickoff and decision timing, then record priced denominators by market before baseline scoring. M1 remains open for exact quote and cutoff qualification, Weeks 1–6 inventory gaps, and additional authentic ranked-card recovery. M2–M7 statuses remain governed by their original acceptance criteria.

## M1 Week 10 timed-quote checkpoint — November 11, 2026

**Verified bounded join.** [Week 10 exact-ID evidence](../audits/CFB_WEEK10_TIMED_QUOTE_JOIN_20261111.json) commit `b8e7d5f580a162b16ad8957f27a379bc7be3d324`, blob `ba103de23e25b16d9c869a52e1202c1c7b755417`. All 63 directed game IDs join to qualified finals, preserving 55 original forecasts and eight exclusions. The fixed November 1 CBS board has 53/55 modeled prices per branch. Of those, 25 have an evidenced kickoff after retrieval, and 18 also have an immutable later planning cutoff. The snapshot predates those reviews and supports exploratory opening-board replay only. A later original capture supplies the two missing displayed quote pairs outside that fixed cohort. The published ten remains separate.

**Resume.** Establish a predeclared Week 10 exploratory opening-board baseline for the 25 timing-qualified rows, using exact branch prices and reporting excluded denominators. In parallelizable research, recover remaining kickoff evidence and the original later quote observations actually bound to the 18 reviews. Use those for the separate decision-window replay. M1 remains open for remaining week and timing gaps.

## Week 10 opening-board and reviewed-quote replay checkpoint — November 11, 2026

[M1/M2 replay evidence](../audits/CFB_WEEK10_OPENING_AND_REVIEW_REPLAY_20261111.json) commit `8ac83ad07d456791e11e7af379cbc97d3598548a`, blob `3ed68ebea809591b0b44af70e1df0a0a5fe8d494`, read back exactly. M1 remains open and M2 is **IN_PROGRESS / bounded Week 10 replay verified**. The fixed opening-board rule graded 75 hypothetical selections from 25 games at $5 per selection: spreads 14–11 (+$8.46), moneylines 16–9 (+$8.45), totals 11–14 (−$19.39); combined −$2.48 on $375. Thirty modeled games still lack qualified kickoff in the join, including two without fixed-board prices. All 18 retained review-time quote bindings passed and graded 12–6, +$24.37 on $90 at the observed benchmark prices. These are separately selected historical cohorts, distinct from the published Top 10 and actual tickets. Eleven of the 18 reviewed selections match the opening rule on the same game/market. Selection, timing and price differ, so no incremental review edge is established.

**Resume.** Qualify remaining Week 10 kickoff clocks from retained original evidence and expand the opening denominator with the identical rule. Then bind Week 9's dated CBS snapshot, original predictions and official finals to qualified kickoff evidence and apply the same rule for a second weekly baseline. Keep documented missed windows separate. Authentic ranks beyond the Week 10 Top 10 and synchronized combined offers still gate the ranked parlay matrix.

## Two-week opening-board replay checkpoint — November 11, 2026

[Verified Week 9 and Week 10 replay](../audits/CFB_WEEK9_WEEK10_OPENING_BASELINE_COMPARISON_20261111.json) commit `18319f0e2bb8f4030e794a823f87a34fcd8fdf08`, blob `a48415c51c3892c69526df2d1fd0700918d96bd7`. M1 and M2 remain **IN_PROGRESS**. Week 10 modeled kickoff coverage is now 55/55, with 53/55 fully priced on the fixed board. Expanded Week 10 at $5 each: spread −$8.60, moneyline −$35.02, total −$25.58, combined −$69.20 on $795. The earlier 25-game subset was reproduced exactly and its combined −$2.48 does not represent the wider cohort. Week 9: 26/45 pass both original snapshot and independent kickoff requirements; spread +$18.78, moneyline +$13.28, total −$34.10, combined −$2.04 on $390. Neither week establishes a market-selection rule or calibrated edge.

**Resume.** For Week 9, recover kickoff evidence for the ten unresolved modeled IDs and preserve the nine fixed-board price gaps. Recover Week 8's comparable snapshot, kickoff and result bindings for another unchanged-rule replay. Track whether totals weakness persists on broader evidence and compare against alternate explanations such as price, selection mix and week coverage. Keep hypothesis evaluation within weekly learning and retain the authentic rank/offer gate for the parlay matrix.

## Week 8 replay and Week 9 timing expansion — November 11, 2026

[Verified replay continuation](../audits/CFB_WEEK8_WEEK9_OPENING_REPLAY_CONTINUATION_20261111.json) commit `98b5b3431400d0f6f0db8641ad4488bbe32b7477`, blob `243da617787e24154c77a0953d6641eed1761d39`. M1/M2 remain **IN_PROGRESS**. Week 9 recovered five more kickoff bindings and expanded the eligible fixed-board cohort from 26 to 31 modeled games. At $5 per selection: spread +$31.68, moneyline +$17.15, total −$30.37, combined +$18.46 on $465. Five kickoff gaps and nine incomplete-price rows remain, with overlap.

Week 8 joined all 49 original forecasts and canonical finals to the fixed October 18 CBS board. Four modeled games had both a corroborated exact kickoff and all six prices, returning +$7.16 on $60. A separate 31-game sensitivity replay using agreeing schedule dates returned −$0.47 on $465, including +$16.78 on totals. This overlaps the four-game sample and carries weaker timing evidence. The broader Week 8 result changes the direction of the totals observation from Weeks 9–10, so retain it as a coverage-sensitive hypothesis only.

**Resume.** Recover independent Week 8 kickoff clocks for fully priced rows first, then reconcile the remaining Week 9 kickoff IDs. Extend the unchanged rule to Week 7 after binding its fixed capture, forecast archive and finals. Continue to require authentic ranks and time-bound combined offers before qualifying the ranked parlay matrix.

## Week 7 ranked-card recovery — November 11, 2026

[Verified ranked-card and combination coverage](../audits/CFB_WEEK7_RANKED_CARD_AND_PARLAY_COVERAGE_20261111.json) commit `0b0f96f37eedb28a11e7724cbcc8db0c47b19e1c`, blob `0ea28b8c02c27c1b3c7d7a79fdda90d286094b08`. Recovered the five authentic ranked pregame selections, matched the canonical publication to all five immutable quotes, confirmed pre-cutoff chronology and joined the final scores. Result: 4–1 and +$13.00 on $25 hypothetical. This is the second authentic ranked cohort after Week 10 and is separate from the opening-board baselines.

Enumerated distinct 2–5 leg subsets as a coverage audit. Week 7 has 26 subsets and Week 10 has 627; none of the enumeration counts establishes an offered payout or an independent hit rate. The archived Week 7 two-leg idea lacks a combined quote. M1/M2 remain **IN_PROGRESS** and M3 implementation acceptance remains open. Resume with Week 7 fixed opening-board recovery, then the remaining Week 8/9 kickoff bindings. The price-aware matrix still needs genuine deeper ranks and synchronized offer evidence.

## Week 7 fixed opening-board replay — November 11, 2026

[Verified replay](../audits/CFB_WEEK7_OPENING_BOARD_REPLAY_20261111.json) commit `85bb9e3d6ed5855344eb8c01b6b34a1f323f8858`, blob `a19979dc708e2337f75cc85933f4893893e02c8f`. Bound the October 11 07:08 CT CBS fallback to the scheduled closure, reconciled all 62 directed identities, and joined all 51 modeled original forecasts and qualified finals. Thirty modeled games had all six prices. Two had corroborated exact kickoff and returned −$2.75 on $30 hypothetical. The overlapping 30-game schedule-date sensitivity returned +$51.88 on $450, including +$13.38 on totals, with weaker kickoff evidence. The original five ranked selections remain a separate cohort.

M1/M2 remain in progress. Resume with exact kickoff recovery for the 28 fully priced Week 7 games still lacking corroboration, the corresponding Week 8 and Week 9 gaps, and the Week 6 fixed snapshot inventory. Keep the identical scoring rule and avoid extrapolating returns from timing sensitivity cohorts into selection policy.

## Week 6 opening coverage and fixed Friday benchmark — November 11, 2026

[Verified coverage and replay](../audits/CFB_WEEK6_OPENING_COVERAGE_AND_FRIDAY_REPLAY_20261111.json) commit `bbd0a93f9eae97ec9ebf5bd3b5ce7fd072c0d450`, blob `55a6b5274f3f806acb155e07629cecc1a4837dc6`. The October 4 saved opening sheet has 49 modeled games, 18 with displayed lines and zero with six priced branches. The Tuesday and Saturday displays mix observation clocks. The October 7 paired eight-game research has no exact retrieval clock in that document.

The October 9 fixed pregame DraftKings benchmark qualified all five Friday games for a separate exploratory replay. Exact original forecast bytes, directed game identity, kickoff and canonical finals were bound. The established rule graded 15 hypothetical selections: spread 4–1 (+$13.31), ML 3–2 (+$0.16), total 2–3 (−$5.78), combined 9–6 and +$7.69 on $75. All five historical Friday decisions remain PASS. M1/M2 stay open. Resume with original October 4 producer records for missing price fields and the remaining Week 7–9 kickoff gaps; use Week 5 archive inventory if the opening prices remain unavailable.

## Week 6 producer and Week 5 Saturday replay — November 11, 2026

[Verified evidence](../audits/CFB_WEEK6_PRODUCER_AND_WEEK5_SATURDAY_REPLAY_20261111.json) commit `d5e8ca60314906d202f8ec8cbfbba7f2e246308d`, blob `ecbbbc5e35cc94e40c8382f79f67f01a190094fa`. The original Week 6 October 4 market-state append confirms 18 modeled spread/total observations without price or moneyline fields, and 31 unavailable rows. The fixed opening payout cohort is unscorable from these producer records.

The original Week 5 October 3 producer commit supplies 44 complete Saturday price rows and joins to the exact original forecast/final audit and contemporaneous Hot Sheet. Under the established $5 hypothetical rule: spread 24–19–1 (+$12.69), moneyline 31–13 (+$2.67), totals 19–25 (−$39.29), combined 74–57–1 and −$23.93 on $660. The receipt identifies the 07:19 CT run start, followed by prospective retrieval. Exact response-completion and independent kickoff clocks were unavailable in the inspected records; retain the Saturday replay as a late-week cohort using saved schedule evidence. Three earlier modeled games are outside it. M1/M2 remain in progress.

Resume with Week 5 first-observation exact-book subset recovery and Week 4 opening provenance. Continue the existing Week 7–9 exact kickoff gaps. Compare market results only with explicit cohort, timing and price coverage.

## Week 5 early prices and Week 4 opening provenance — November 11, 2026

[Verified early-price evidence](../audits/CFB_WEEK5_EARLY_PRICES_AND_WEEK4_PROVENANCE_20261111.json) commit `ce882537290036b6ae662c7a7f238435099b6e4e`, blob `022fabead5c92e2d018da71789911f55790eae15`. The September 27 13:08 CT record contains four Week 5 games with named-book prices. Seven forecast-rule selections qualified across those games and graded 3–4, −$10.79 on $35 hypothetical. Five market rows were unscorable because branch prices were absent or the displayed total price was not assigned to a side. The later 44-game Saturday result remains a separate overlapping cohort.

Week 4 has 44 archived Saturday side comparators for directional QA and 53 modeled final joins. The canonical producer history begins September 27, after the Week 4 Saturday slate. A synchronized, priced Week 4 opening cohort remains unestablished. M1/M2 remain in progress. Resume with the fully priced Week 7–9 rows missing exact kickoff, then cross-week baseline synthesis with source, market and timing denominators. Week 4 remains directional QA evidence unless original price and observation records surface.

## Weeks 7–10 opening baseline synthesis — November 11, 2026

[Verified synthesis](../audits/CFB_WEEKS7_TO10_OPENING_BASELINE_SYNTHESIS_20261111.json) commit `4a135249533fe5a511be4fa61c934ae93b117d1a`, blob `095a3fe7b22c7e6fa35a16fd93ce37b2fc8b97b4`. Official school schedules corroborate two more Week 7 kickoffs against the original board, bringing the strict Week 7 cohort to four games and +$20.03 on $60. Week 8 remains at four, Week 9 at 31 and Week 10 at 53. Across 92 timing-qualified games, $5 hypothetical replay net was spread +$26.87, moneyline −$2.47 and total −$47.95, combined −$23.55 on $1,380. Totals stayed negative when dropping each week in turn. Date-only Week 7 and Week 8 sensitivities had positive totals and overlap with these cohorts. Week 10 accounts for 53 of 92 games. Keep this as a coverage-sensitive research question.

M1/M2 remain in progress. Resume with exact kickoff provenance on the remaining fully priced Week 7/8/9 rows (26/27/5). Recompute only newly eligible rows and compare price, over/under mix and week-level effects. Do not tighten coverage from these historical results.

## Weeks 7–9 kickoff provenance extension — November 11, 2026

[Verified replay extension](../audits/CFB_WEEKS7_TO9_KICKOFF_REPLAY_EXTENSION_20261111.json) commit `5ec6facbf6e3cb11483ae4ec1fbd3425841fd3eb`, blob `451e3f6392cbb2c7b4768400fa59bb5ef97e423b`. Published scheduled kickoff clocks matched the fixed CBS board on 47 additional fully priced modeled games (Week 7 +21, Week 8 +22, Week 9 +4). The strict Weeks 7–10 pool grew from 92 to 139 games. At hypothetical $5 per market per game, net was spread −$7.59, moneyline −$26.36, totals −$72.40, combined −$106.35 on $2,085. Totals remained negative when omitting each week in turn (−$81.92, −$66.43, −$22.03, −$46.82). Newly admitted totals were 28 overs (−$5.86) and 19 unders (−$18.59). Prior same-game date-only sensitivity tickets for Weeks 7–8 were reused after clock qualification. Week 9 used the unchanged forecast and price rules with original board prices and qualified finals. This remains retrospective research.

M1/M2 remain in progress. Eleven fully priced rows still need kickoff corroboration or source-conflict resolution (Weeks 7/8/9: 5/5/1). Resume with the exact unresolved identities in the audit, then apply the frozen rule to an untouched eligible cohort and compare week-level, price and side-mix effects.

## Historical clock sweep and Week 11 prospective replay — November 11, 2026

[Verified audit and protocol](../audits/CFB_OPENING_REPLAY_CLOCK_CLOSEOUT_AND_WEEK11_PROTOCOL_20261111.json) commit `923c0ca9fd0af3c7bc0d88aa69d8c4f66aebebf5`, blob `4b5e9cf56fccb46594af4674c327d52323fa2f1d`. Reviewed all 11 remaining fully priced kickoff gaps. Two Week 7 games had corroborating schedules and joined the fixed board. Nine clock disagreements stay outside the strict historical replay. Across 141 games the $5 hypothetical replay returned spread −$8.04, moneyline −$12.75 and totals −$63.09, combined −$83.88 on $2,115. Totals remained negative when each week was removed in turn.

Registered the same rule for Week 11 before the remaining modeled games were scheduled to start. Matched 67 directed identities to the November 10 6:17 p.m. CT archived CBS board and accepted original ancestry. Of 59 modeled games, three had already started and 56 had all six quoted branches and a future board clock. Eight original forecast exclusions remain excluded. The 56 candidates still require exact independent scheduled kickoff matches after registration and qualified official finals. No later prices enter this replay. Report per-market coverage, net, over/under counts and prices. M1/M2 remain in progress. Grade after Week 11 finals are qualified.

## Week 11 kickoff and selection verification — November 11, 2026

[Verified schedule and selections](../audits/CFB_WEEK11_PROSPECTIVE_REPLAY_SCHEDULE_AND_SELECTIONS_20261111.json) commit `df1183184a7b351c43d857b4bc7393acb970c11f`, blob `93dd7729ad0375a5f0f484a3ddc88c2b748008e2`. NCAA.com published kickoff clocks agreed with the archived CBS board for all 56 directed candidates. Held Sacramento State at Central Michigan because the host's preview gives 7:30 p.m. ET in the headline and 7:32 p.m. ET in the game details. The 55 corroborated games have 165 fixed hypothetical selections at $5 each, including 27 overs and 28 unders. The held game retains its three ungraded selections in the audit for traceability.

M1/M2 remain in progress. Join the 55 corroborated identities to qualified official finals, reconcile any intervening schedule changes, and resolve or retain the single clock hold under the original criterion. Report market coverage, payout, and over/under and price mix against the historical replay. At this checkpoint no eligible finals were available.

## Opening replay side and price baseline — November 11, 2026

[Verified comparison](../audits/CFB_OPENING_REPLAY_PRICE_AND_TOTAL_SIDE_COMPARISON_20261111.json) commit `17b3f1d10f5767cf95c6fafeebf06024bfb7bd67`, blob `78d4032d3ae38d1b6600cf12cb23195988d231ef`. Reconstructed and reconciled all 423 historical selections. Of the 141 total selections, overs went 41–40 (−$12.08 on $405) and unders went 26–34 (−$51.01 on $300). The average quote-implied probabilities were 52.32% for overs and 52.36% for unders. Unders were negative in each leave-one-week-out comparison. Overs were positive when Week 9 was omitted. The Week 11 qualified candidate mix is 27 overs and 28 unders, with mean quote-implied probabilities of 52.15% and 52.25%, respectively.

Treat this as descriptive research. Keep both sides in the Week 11 test. M1/M2 remain open pending qualified official finals. Compare net, coverage, side and price mix once the frozen selections are graded.

## Parlay matrix archive coverage — November 11, 2026

[Verified coverage audit](../audits/CFB_PARLAY_MATRIX_EVIDENCE_COVERAGE_20261111.json) commit `ac97a5c87bf952d66ebb654cfedb6527e1c02b85`, blob `722020ccb69010f7113f5dabd683e55ecc25c55c`. M3 coverage work started. Evaluated evidence availability across the 20 depth/leg cells for each of Weeks 7–11. Week 7 supports five documented ranks. The inspected Week 8 and 9 sheets do not establish ordinal cross-market ranks. Weeks 10 and 11 each have one inspected ten-rank card. Week 11 includes five leans. No inspected card reaches ranks 11–30 or supplies a qualified contemporaneous combined offer for the research opportunity matrix.

Week 10's executed three-leg ticket verifies +605 for that specific execution. Its leg numbers match ranks 1, 2 and 4, and its printed leg prices differ from the original card's displayed prices. The published three- and four-leg estimates share three legs. Preserve the two documented separate-straight overlaps with the actual parlay. M3 implementation and acceptance remain open. Resume with a deterministic read-only evaluator for exact game/leg identity, synchronized quote and cutoff validation, and shared exposure. The Week 11 opening-board test continues to await qualified finals.

## Read-only parlay evaluator — November 11, 2026

[Verified evaluator](../../scripts/cfb_parlay_matrix.py) commit `515af6659f69ec41cab726f90f4b17f91a32da65`, blob `2655fd41fa6a3c3cf2f2f8445da13aa170e3453b`. M3 is in progress. The standalone evaluator runs all 20 depth/leg cells for one archived ranked card, counts distinct-game combinations by market mix, checks exact game/market/side/line and offer timing against card, cutoff and kickoff, and reports actual combined-quote break-even, straight-card overlap and shared-game exposure. It accepts archived MONEYLINE and ML labels. Estimates and execution receipts do not enter the offer denominator.

Executed the Week 7 archived five-rank fixture through the CLI. It reproduced 10, 10, 5 and 1 candidate combinations for two through five legs and zero qualified offers. Synthetic positives and negatives verified deterministic output, timing, leg mismatch, same-game rejection, rank gaps, duplicate quotes, break-even and overlap. Synthetic offers are implementation fixtures only. Authentic synchronized offer replay, deeper rank coverage and portfolio outcome/payout evaluation remain open. Resume by binding available archived leg/game identities and eligible combined offers, then demonstrate payout and shared-loss evaluation using qualified finals. Week 11 opening-board grading remains pending official finals.

## Parlay payout and shared-loss evaluation — November 11, 2026

[Verified evaluator extension](../../scripts/cfb_parlay_matrix.py) commit `717878552e857a2da0b7cd8f6d2e7cf36ffc0709`, blob `5523147216737d3863d31265559d9753499faff6`. M3 now grades exact spread, moneyline and total legs from qualified directed final scores and computes separate $2 and $5 gross/net scenarios at each accepted combined quote. It reports per-cell loss counts by shared losing game. Missing qualified finals remain pending. A winning build containing a push requires documented repricing, while an all-push scenario refunds the stake. Builds and alternate observations are not aggregated into a selected portfolio.

Executed the archived Week 7 finals (blob `0ea28b8c02c27c1b3c7d7a79fdda90d286094b08`) with synthetic combined quotes. Verified wins, losses, multiple builds losing through the same game, deterministic order, rounding, pending finals and push cases. The actual Week 7 archive still has zero qualified combined offers. M3 remains open for authentic combined-price replay, deeper ranked coverage and a predeclared portfolio selection policy. Week 11 opening-board replay still awaits qualified finals.
