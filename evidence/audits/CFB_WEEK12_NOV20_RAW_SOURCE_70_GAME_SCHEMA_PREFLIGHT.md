# Week12 Nov20 CBS raw source — independent 70-game schema preflight

**Status: STRUCTURAL_PREFLIGHT_PASS_WITH_UNAVAILABLE_MONEYLINES / GOVERNED_NORMALIZER_NOT_EXECUTED**

Input: retained evidence/operational/CFB_WEEK12_CBS_FULL_BOARD_20261120_MANUAL_0700_CATCHUP.md, read freshly through connected GitHub. Independent parse checked all date headers, two following team rows, directed CBS team IDs, and displayed Spread/Moneyline/Total fields. This is a limited structural check, not scripts/cfb_cbs_full_board_normalizer.py lineage/time/identity acceptance.

| Check | Observed |
|---|---|
| Game headers | 70 |
| Day counts | Tue 3, Wed 2, Thu 1, Fri 6, Sat 58 |
| Team rows | 140 |
| Display field positions | 420 (70 x 6) |
| Unique directed CBS ID pairs | 70 |
| Available spread/total cells | 280 / 280 |
| Available moneyline cells | 136 / 140 |
| Unavailable moneyline cells | 4 / 140 |
| Structural errors other than supported unavailable ML | 0 |

Missing moneylines are **Chattanooga @ Alabama** (both sides) and **Samford @ Auburn** (both sides). Raw source uses em dash `—`, explicitly supported as UNAVAILABLE by the governed normalizer's market() parser. Do not invent moneyline prices, mark those fields malformed, or treat unavailable markets as bets.

## Limitations and drift containment
- Previous claim that full source is 128 team rows was incorrect; that is only the 64-game Friday/Saturday working-card subset. Full governed Week12 census is 70/140/420.
- Source-file headers and fields passing this independent parser do NOT prove full baseline game-ID match, recovered-by source clock, lineage blob, kickoff timing or actual normalizer execution.
- Current local shell GitHub DNS lookup failed; authenticated pinned checkout unavailable in this runtime. No compiler or production selector was changed.
- The November20 saved board cannot be reused for a later proposal outside the 15-minute freshness window.
- All 58 Saturday prior PASS statuses remain retained, not re-issued as newly accepted decisions.
