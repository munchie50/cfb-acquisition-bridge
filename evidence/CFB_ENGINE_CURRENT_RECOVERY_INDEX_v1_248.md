# CFB Engine — Current Recovery Index v1.248

Status: CURRENT RECOVERY DOORWAY — incremental provenance pointer only
Date: 2026-11-01
Supersedes compact v1.246 as recovery doorway, inheriting **all** v1.246/v1.245 authority, active contracts, v1.247 football-week cadence, controls, locks and historical ancestry unchanged. No model, Champion, challenger, betting, financial, routine, schedule or task promotion.

## Mandatory ancestry
- v1.246: `evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_246.md` exact blob `6b25766c90e3ae212efd529dc2b545c226e6abc7`.
- v1.245: `evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md` exact blob `57327859afb17ca42451189d3661f4c16fae4f90` (4.23 MB; recover exact SHA without reserializing).
- This compact successor does not supersede or erase later independently accepted canonical artifacts or production contracts. Verify live repo main and latest canonical state before acting.

## Week10 market investigation and preparation — persisted, not production accepted
- Independent bottleneck classification: `evidence/audits/CFB_WEEK10_MARKET_MONITOR_BOTTLENECK_ROOT_CAUSE_20261101.md` blob `534e22528b5a8a77774895fa6772afa656d39efe`. R91 60/63 CBS displayed, 360/378 branches displayed; R93 all 378 WAIT, zero certified. Model boundary, bookmaker provenance, material review and publication are separate blockers.
- Early Tue–Fri 12-game priority register: `evidence/operational/CFB_WEEK10_EARLY_GAME_QUALIFICATION_PRIORITY_20261101.json` blob `fffbb17a8e54150617d90ccb0955e11e2f185b2d`. Planning only.
- Tuesday two-game official kickoff/market/availability source review: `evidence/operational/CFB_WEEK10_TUESDAY_P0_EXTERNAL_PROVENANCE_20261101.json` blob `9348d7da13108485ec0b30ebaeec9e6ed6e741ec`; triangulation `evidence/operational/CFB_WEEK10_TUESDAY_P0_MARKET_MATERIAL_SOURCE_TRIANGULATION_20261101.json` blob `8611622176966a7e4b97cbed60e06445c7d9d582`.
- Wednesday/Thursday five-game official kickoff evidence: `evidence/operational/CFB_WEEK10_WED_THU_OFFICIAL_KICKOFF_PROVENANCE_20261101.json` blob `8df78ac8abd1f94423ef92f0a4679e9acfdf1153`.
- Friday five-game official kickoff evidence: `evidence/operational/CFB_WEEK10_FRIDAY_OFFICIAL_KICKOFF_PROVENANCE_20261101.json` blob `8a9ce163a877ba2adde582b11ecb06a6bb838bad`.
- Six-branch market provenance gate code: `scripts/cfb_week10_market_qualification_gate.py` blob `698238580629a489da84c0b67e6cdfe0ac854f84`. Regression tests: `scripts/test_cfb_week10_market_qualification_gate.py` blob `94fafc76151c1eb928b42e3cdbcaa8ee15e4e620`. **Both persisted/read back; test execution and production Monitor integration NOT verified**. Gate is market-provenance only, not full bet authorization.

## Next dependency-ordered execution
1. Execute six gate regression tests, record actual result, repair if needed; tighten proof authenticity/timestamp validation before trusting producer input.
2. Integrate tested gate into existing Monitor evidence-producing path, independent readback and production verification. Do not create a fifth scheduled task or substitute GitHub workflow green for scientific acceptance.
3. Continue Monday source readiness / Tuesday accepted S0 FIRST_FROZEN and current operator+venue+offer clock / official game-day availability, prioritizing Tuesday games before kickoff.
4. Only after qualified model, market, material and decisions publish current Hot Sheet; preserve Week9 QA/ledger and authentic settlement boundaries.

## Unresolved
All 378 R93 market branches WAIT at last independently evidenced snapshot; no accepted Week10 Champion six-market decision handoff, no current certified Hot Sheet. Existing four production tasks unchanged. Week9 actual sportsbook settlement and financial classifications remain unresolved. S2_K1 challenger HOLD; v6 candidate not production promoted. Big Nine PAUSED.

## Week 9 manual closeout — latest verified successor evidence (November 1)
- Complete 56/56 official-score frozen-cohort join: `evidence/operational/CFB_WEEK9_CANONICAL_56_OFFICIAL_OUTCOME_RECONCILIATION_20261101.json` blob `296b18dd97c1bb0c2d68281fe24506bf27fe7dbc`; 45 modeled/11 excluded; 28/45 correct direction; margin MAE 14.262253; total MAE 13.747495. Original freeze preserved; no model promotion.
- Eight actual October31 wagers independently score-graded 5 WIN/3 LOSS/$30 stake: `evidence/operational/CFB_WEEK9_OCT31_INDEPENDENT_TICKET_RECONCILIATION_20261101.json` blob `9cd7905693a3186c02f060744c3dbb89c96f92e3`. Per-ticket cent rounding gives hypothetical return $40.41/net +$10.41 versus earlier $40.40/net +$10.40 estimate; this is a documented one-cent estimate variance, NOT confirmed book payout or a posted ledger cash movement.
- Closeout boundary: `evidence/run_receipts/CFB_WEEK9_MANUAL_CLOSEOUT_DISPOSITION_20261101.md` blob `dbbb7c7ea89bd959fd2809afb0bea8a9eb728dbc`. Historical outcome and score-derived ticket grade complete; original Week9 pregame publication failure remains explicitly historical/unrecoverable as a live bet authorization. Sportsbook settlement, redemption and current cash holdings **OPEN** until independent user/book evidence. Existing October31 $69.05 user-confirmed holdings snapshot remains pre-settlement; do not invent withdrawal, duplicate ticket or book hypothetical proceeds.
- This is a narrow recovery pointer update only. All earlier v1.248 Week10 priorities and four scheduled tasks remain unchanged. Week9 historical QA can be considered closed for outcomes/score grades only; do not mark financial closeout accepted.
