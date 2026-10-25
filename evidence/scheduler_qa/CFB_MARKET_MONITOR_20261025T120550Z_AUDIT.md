# CFB Market Monitor audit — 2026-10-25 07:03 CT

Cycle: `CFB_MARKET_MONITOR_20261025T120550Z`

## Earned result

`RUN_INCOMPLETE`

This Sunday cycle completed prior-week Week 8 outcome capture, established-wager final-score grading, and FIRST_FROZEN scorecard closure. It did not publish or select a Week 9 Hot Sheet because the shared Firecrawl balance was zero and no accepted Week 9 original-lineage/publication profile or qualified complete Week 9 opening-board capture was available. A stale Week 8 sheet was not retimed or presented as current Week 9 research.

## Authority and observability

- Recovery index: `evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md` / blob `e53299246bb5cde4f2ef58184f2f839174662837`.
- Football-week cadence: v1.247 / blob `2a41f5cee71152c9f0a84cc3ee2f634020819dc2`.
- Persistence procedure: blob `27e6500d0e4f001d8f71449e15f813e6fb83bedf`.
- Closure contract: blob `501cda05d80229402a485493f10b1a4bbb76d3b8`.
- Firecrawl control: blob `d27ff9d78cf84e29a28b906ffe75e6c7895e82cb`.
- Week 8 publication profile: blob `e43e7e137b7ea1ac5ee60f489c018e8e9f56bf27`.
- RUN_STARTED readback: `evidence/run_receipts/CFB_MARKET_MONITOR_20261025T120550Z_RUN_STARTED.md` / blob `9688a28856586898298c7f68661f5cf08de78136`.
- Supported computation runtime proved in this invocation: Python 3.12.14; Week 8 compiler, publication gate, readiness audit, and recovery-consumer preflight entry points executed successfully.

## Shared acquisition budget

Live provider metadata read before chargeable work: plan credits `1000`; remaining credits `0`; cycle `2026-09-27T17:16:35.203Z` through `2026-10-27T17:16:35.203Z` (30 days). At cycle-day bucket 28, cumulative release is `floor(1000*28/30)=933`; account-observed consumption is `1000`, so available chargeable allowance is `0` before any unsettled reservation. No paid Firecrawl acquisition was attempted.

## Week 8 settlement and scoring

- Fresh complete CBS Week 8 results response: `evidence/operational/CFB_CBS_WEEK8_RESULTS_CAPTURE_20261025T120800Z.md` / blob `2aa53f5793bb511373eba9bbbf6e6249d3984836`; 56/56 game tables, 112 team rows, no missing source lines.
- Execution ledger readback: blob `1a938f42e9f03e723bd50348f8a78dbd8b7098e9`.
- Scorecard readback: blob `1e8e0a9c3cd34c163c32f6782cdfccf30b9e13d8`.
- Six Saturday tickets: 5 wins, 1 loss, $28.00 stake, $43.75 printed result return, +$15.75 result net.
- Complete October 23 Week 8 ticket batch: 5 wins, 3 losses, $36.00 stake, $43.75 printed result return, +$7.75 result net.
- Sportsbook adjudication, redemption, payment, available cash, production-versus-sandbox allocation, and current voucher balance remain unverified.
- Week 8 FIRST_FROZEN: all 49 accepted predictions now joined to authoritative finals; all 7 original exclusions retained unscored. Saturday eligible slice: 25/39 margin-direction correct (64.1%), margin MAE 11.51, total MAE 14.64.
- No Champion, FIRST_FROZEN, accepted REFRESH, Challenger, TIME-HIDDEN, market, decision, or wager record was reconstructed from outcomes.

## Canonical state and publication boundary

- Market state readback at cycle start: blob `0c7d0fd878f1d364674bb89bff8660d164b7ff22`; unchanged.
- Decision ledger readback at cycle start: blob `7f8bfefbe4c943ea35691f7a7db3e43ec4beac6c`; unchanged.
- Money ledger readback: blob `fc24ea6274160eebfef2ba22fe060deabfe81f9f`; unchanged because paid settlement/current balance was not verified.
- Last selected Hot Sheet remains the closed Week 8 view `evidence/operational/CFB_WEEK8_HOT_SHEET_2026-10-24_1310CT.md` / blob `affb3451505c77e2a3a528a74cd78e5f1db316e3`; it has zero active opportunities and was not promoted as a Week 9 sheet.
- Week 9 full relevant-FBS identity census, exact kickoff sectioning, qualified current spreads/totals/moneylines, material availability review, multi-book consensus, Caesars execution offers, and all-market decisions were not earned.
- Therefore exact-once Week 9 section reconciliation and required current Hot Sheet persistence/readback were not available, prohibiting RUN_PASS.

## Blocker and next safe action

Blocker: `FIRECRAWL_BUDGET_EXHAUSTED_AND_WEEK9_PUBLICATION_INPUTS_UNAVAILABLE`.

Next safe action: after the provider cycle resets and live metadata shows released allowance, the next prospective Market Monitor should acquire one fresh complete Week 9 response, recover the accepted Week 9 original-lineage/profile if then available, run the normal typed compiler/readiness/publication gates, perform the full all-market/material review, publish one current Hot Sheet, and complete the recovery-index/selected-publication integration. Do not replay this historical opening cycle or retime Week 8 evidence.
