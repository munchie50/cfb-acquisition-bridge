# 2026 CFB season betting replay — November 11

Status: verified actual-ticket census and Week 10 ranked replay checkpoint. Historical simulated cohorts and placement-window reconciliation in progress.

## Authority and methods

Pinned main 7b19291ad830c169e753ce011b4f62634251e615. Read current recovery-index lineage through v1.283, production v5.0, accepted v5.1 A/C and v5.2 D/E/F, the November 11 additions to evidence/CFB_ENGINE_WEEKLY_BETA_LEARNING_REVIEW_CONTRACT_v1_233.md, and the GitHub Contents persistence procedure. Source: evidence/operational/CFB_EXECUTION_LEDGER.md, blob 2c0fbcb0314839deb60823e48adbbd24d5423147. One ticket per execution ID, including one parlay counted once. Full-game score grades, actual stakes and accepted odds; prefer printed result terms where available. Estimated settlements round theoretical return to cents per ticket, which makes Week 9 +$10.41 versus the ledger's +$10.40 aggregate convention. At ledger convention season net is +$89.30. Funding and confirmed cash payment are outside this calculation. The historical live Baylor ticket appears solely to reconcile the actual ledger census and is excluded from every pregame comparison.

## Actual tickets

| Week / issue batch | W-L-P | Stake | Gross result return | Net | Weighted ROI |
|---|---:|---:|---:|---:|---:|
| 4 | 4-2-0 | $18.05 | $26.41 | $8.36 | 46.32% |
| 5 | 3-2-0 | $15.40 | $18.04 | $2.64 | 17.14% |
| 6 | 1-2-1 | $20.00 | $14.55 | $-5.45 | -27.25% |
| 7 | 7-2-0 | $34.05 | $51.75 | $17.70 | 51.98% |
| 8 | 5-3-0 | $36.00 | $43.75 | $7.75 | 21.53% |
| 9 | 5-3-0 | $30.00 | $40.41 | $10.41 | 34.70% |
| 10 | 8-3-0 | $55.00 | $102.90 | $47.90 | 87.09% |
| Season recorded | 33-17-1 | $208.50 | $297.81 | +$89.31 | 42.83% |

Weeks 1–3 have no established ticket records in this ledger, so ROI is undefined. Weeks 4–5 and 9 have some odds-derived result returns. Weeks 6–8 and 10 retain printed payout terms. Week 7 ticket grades independently tie to the October 23 audit and original scorecard blob d210d8c51106ef393a23a4fb69c6fcdb219e3f16. Week 8 ticket results use the complete October 25 CBS capture blob 2aa53f5793bb511373eba9bbbf6e6249d3984836. Week 9 uses evidence/operational/CFB_WEEK9_OCT31_EIGHT_TICKET_SCORE_GRADE_20261101.json. Week 10 uses the November 8 closeout, superseding official-finals qualification and the printed result ledger.

| Market | W-L-P | Stake | Net | ROI |
|---|---:|---:|---:|---:|
| SPREAD | 25-15-1 | $172.50 | $40.41 | 23.43% |
| ML | 3-0-0 | $7.00 | $8.43 | 120.43% |
| LIVE | 1-0-0 | $3.00 | $2.42 | 80.67% |
| TOTAL | 3-2-0 | $21.00 | $7.80 | 37.14% |
| PARLAY | 1-0-0 | $5.00 | $30.25 | 605.00% |
| All straight tickets | 32-17-1 | $203.50 | +$59.06 | 29.02% |
| Straights excluding explicitly live Baylor | 31-17-1 | $200.50 | +$56.64 | 28.25% |

Singles priced -110 through -101, excluding explicitly live: 22–12, +$47.03/$144.55 (32.54%). Worse than -110: 6–5–1, +$0.96/$48.95 (1.96%). Plus-money singles: 3–0, +$8.65/$7 (123.57%). This is descriptive with market/selection/size confounding. Removing all of Week 10 gives +$41.41/$153.50 (26.98%). The Week 10 parlay accounted for 33.9% of season net profit and Week 10 as a whole for 53.6%.

## Week 10 published card and parlays

Source revision b566670d2dddfb5d8d64bb53fdc6f88ae7922fa0, November 6 23:25:59 UTC user-facing list, and Week 10 official-finals review evidence/CFB_ENGINE_WEEKLY_BETA_LEARNING_REVIEW_2026-11-08_R2.md. Listed-price per-ticket rounding reproduces 9–1, $50 staked, $86.62 gross, +$36.62 net, 73.24% ROI (10/10 ranks, 10/63 full-slate games represented; this card is a distinct cohort). Ranks 1–5: 5–0, +$23.26/$25 (93.04%). Ranks 6–10: 4–1, +$13.36/$25 (53.44%). Spreads 6–1, +$22.61/$35 (64.60%); totals 3–0, +$14.01/$15 (93.40%). No moneyline in the published Top 10.

Both archived simulated parlays hit at estimated payouts: Utah -4.5, Cincinnati +10.5, Missouri State +4.5 at +618, $35.90 gross/+$30.90 net on $5; add Oregon–Ohio State over 45.5 at +1302, $70.10 gross/+$65.10 net on $5. Combined simulated 2–0, $10 stake, $106 gross, +$96 net (960% ROI), four unique legs and three shared. No authenticated five-leg build recovered. A shared loss would drop the two-build simulation to -$10, a $106 swing. Oregon total alone losing leaves +$25.90. Actual three-leg price +605 gives $35.25 printed gross and +$30.25 ticket-result profit; $0.65 below the estimated three-leg return. Evidence of user-confirmed adoption for Utah, Missouri State and that parlay is at 7b19291ad830c169e753ce011b4f62634251e615.

Actual Week 10 straights 7–3, +$17.65/$50 (35.30%); plus parlay 8–3, +$47.90/$55 (87.09%). Utah and Missouri State each carried $10 of stake across one straight and the same $5 parlay; Cincinnati carried $5 through the parlay. Three unique tickets represented by those groups total $15 stake. All else fixed, Utah alone failing yields +$2.95 portfolio net (−$44.95 swing); Missouri State alone +$3.05 (−$44.85); Cincinnati alone +$12.65 (−$35.25); both Utah and Missouri State losing yields −$6.65, counting the parlay loss once. No opposing positions within those three games. Across the hypothetical combined ranked singles and two builds, each shared leg exposes $15 including the $5 single and both $5 parlays, and Oregon over exposes $10. Total hypothetical portfolio risk $60, across all 12 tickets. Neither the actual single-plus-parlay result nor the two overlapping simulations estimates an independent parlay hit rate.
