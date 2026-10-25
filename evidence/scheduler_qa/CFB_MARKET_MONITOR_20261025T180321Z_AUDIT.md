# CFB Market Monitor audit — 2026-10-25 13:08 CT

- Cycle: `CFB_MARKET_MONITOR_20261025T180321Z`
- Audit observed at: `2026-10-25T18:09:10Z`
- Authority recovery: newest accepted `evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md`; active football-week cadence v1.247; Week9 publication profile `67b519927f6526cccbb57aec94349de83633c29d`.
- RUN_STARTED: `evidence/run_receipts/CFB_MARKET_MONITOR_20261025T180321Z_RUN_STARTED.md`, independently read-back Git blob `432d7de67c58113afd62a1050dbdfcb3dc8851f7` before source acquisition or canonical mutation.

## Source and budget

- Firecrawl account state was read before chargeable work: plan credits `1000`, remaining credits `0`, billing period `2026-09-27T17:16:35.203Z` through `2026-10-27T17:16:35.203Z`. No paid request or zero-credit probe was issued.
- The accepted Week9 profile's direct CBS browser fallback was used.
- Fresh capture: `evidence/operational/CFB_CBS_WEEK9_TEXT_TABLE_CAPTURE_20261025T180500Z.md`, read-back Git blob `b51a5a2a3d19b39d4d6286a2af7cc0fcefa0c7f5`; 56 unique tables, 112 team rows, all future at capture.
- Current-cell operator names disclosed by CBS are preserved per cell in the capture. The capture remains a mixed-book field-level fallback, not a qualified consensus; Caesars is unverified; book update clocks and executability are unknown.

## Computation and canonical publication

- Runtime: Python `3.12.14` in this invocation.
- `scripts/cfb_week9_publication.py` normal advance validated 56 governed games, 45 original predictions and 11 original exclusions.
- Market proposal/readback Git blob: `3fe4dff0f2057a196f5af3ada2741c6b84e87fd5`.
- Decision proposal/readback Git blob: `014db27bb226b48681d570029d0fcd8be476d3fd`.
- Execution ledger unchanged/read: `1a938f42e9f03e723bd50348f8a78dbd8b7098e9`; no execution was inferred from intent or market display.
- Scorecard unchanged/read: `1e8e0a9c3cd34c163c32f6782cdfccf30b9e13d8`; no outcome-informed reconstruction or Champion mutation.
- Independent renderer and whole-view audit verdict: `PASS_NEUTRAL_CANONICAL_PRESENTATION_ONLY`.
- Current sole Hot Sheet: `evidence/operational/CFB_WEEK9_HOT_SHEET_2026-10-25_1308CT.md`, read-back Git blob `c5c7d2d42a1bb2d56bd60b655d63709057088da3`; 56 exactly-once rows, Nebraska present, chronological sections plus priority/full-slate views.

## Earned decision status

- 56 `INCONCLUSIVE`; 0 `PASS`; 0 actionable or conditional recommendations; no established acceptable number, execution window or preferred parlay.
- No reconciliation deadline is overdue at the publication boundary.
- Readiness diagnostic found 56 review-required identities: 45 `NOT_CERTIFIED` original-prediction rows and 11 `ORIGINAL_EXCLUSION` rows. Every row still lacks a qualified material review, decision-rule review, market reference, practical cutoff and line/price limit; the 11 exclusions also lack an original model review by design.
- Both spread sides, both moneylines and over/under are numerically displayed when offered, but were not converted into recommendations. Alternates/team totals and bounded parlays were not independently quoted or reviewed in this cycle; `NO_PREFERRED_PARLAY` is not claimed from missing research.

## Terminal disposition

`RUN_INCOMPLETE` is earned even though source capture, typed canonical append, rendering and readbacks succeeded. Exact blocker: the standing full-evaluation requirement remains unserved for all 56 Week9 games; queue membership and numerical market movement are not football research, and zero Firecrawl balance prevented the prioritized broad external research phase. Next safe action: in the next existing Monitor cycle, re-read provider budget, obtain independently qualified material/kickoff/market evidence within the released allowance or approved no-charge sources, and prospectively complete the due reviews before the existing reconciliation deadlines without changing frozen predictions or schedules.
