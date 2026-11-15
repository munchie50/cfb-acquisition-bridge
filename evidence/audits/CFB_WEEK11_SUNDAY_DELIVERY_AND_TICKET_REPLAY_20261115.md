# Week 11 Sunday QA continuation — delivery, tickets and exposure

Status: scoped delivery and ticket result analysis complete. Week 11 full FIRST_FROZEN evaluation awaits official final for Ole Miss at Oklahoma (401856887), scheduled for noon CT November 15. This addendum supplements the [November 15 R1 Weekly Beta Learning Review](../CFB_ENGINE_WEEKLY_BETA_LEARNING_REVIEW_2026-11-15_R1.md).

## Delivered Friday conditional terms

Cohort fixed by the [selected Friday 3:21 p.m. CT Hot Sheet](../operational/CFB_WEEK11_HOT_SHEET_2026-11-13_1521CT.md), blob `448318f57dabe7a47e3b8e08e9f78c7cf97042f0`. Only Tennessee and Baylor were conditional on that sheet. Market observations, allowed price limits and actual ticket prices are independently labeled.

| Selection | Saved observed quote | Saved minimum price | Actual ticket | Verified result |
|---|---:|---:|---:|---|
| Tennessee -2.5 | -115 | -115 | -110 | Win, Tennessee 22–7 |
| Baylor +7.5 | -112 | -118 | -115 | Loss, BYU 28–7 |

At $5 each on the two saved public quotes, the conditional-price illustration is 1–1, $9.35 gross and **−$0.65 net** rounded to cents. These were retrieval-only public prices with venue confirmation pending. The illustration uses both delivered conditional rows, regardless of outcome, with no claim of fillability, active-at-placement status, or a published ten-pick cohort. Both tickets met the saved number and minimum price. Tennessee was five American-odds points better than the saved public quote and Baylor was three worse. Their two actual $10 tickets had $19.10 in calculated gross returns, or **−$0.90 net** on $20. Their receipt timezone and complete placement-time conditions remain unverified.

The November 12 ranked watch card separately listed Jacksonville State -7.5, Georgia -15.5 and North Texas -2.5. At their archived lines those sides graded loss, win and loss respectively. Friday superseded their placement status. Jacksonville State and Georgia were off the latest conditional card and North Texas's cited -108 was below its -105 minimum. The watch cases do not enter the Friday replay. A complete $5 Top 10 or one-side-per-game baseline remains unavailable because the saved pregame cohort lacks the required eligible priced selections. No genuine published combined parlay quote was found.

## Actual execution and overlap

[Verified outcome and ticket-grade evidence](../operational/CFB_WEEK11_OFFICIAL_OUTCOME_QA_20261115_R1.json) holds each game's source and each ticket's grade. Straight-only was 6–6, **$80 staked, $76.65 calculated gross, −$3.35 net**. Including the $2 parlay gives 6–7, **$82 staked, $76.65 calculated gross, −$5.35 net**. The parlay won Tennessee -2 and Georgia -16.5 legs and lost Baylor +7.5 and Jacksonville State -7.5. Each of those games also had a straight ticket. Straight stake plus the shared $2 parlay stake by game: Tennessee $12, Baylor $12, Jacksonville State $12, Georgia $7. These are overlapping exposures and must not be summed across games. The parlay's own stake is counted once. No sportsbook settlement or cash movement verified.

## Nebraska–Rutgers follow-through

The [archived pregame review](CFB_WEEK11_NEBRASKA_RUTGERS_FULL_REVIEW_20261113.md) shows that the accepted pregame S0 refresh had both teams' input history and projected Nebraska by 7.61 with a 52.58 total. The final was Nebraska 31–0, so the refresh picked the winner and underestimated the margin by 23.39 points while overestimating the total by 21.58. The original exclusion remains `home_prior_points_missing` and stays outside FIRST_FROZEN metrics. The user's Nebraska -13.5 ticket won. The pregame Rutgers +15.5 lean had no earned take-at terms and remains a historical PASS.

Full weekly closure still requires the last official final and a final exact frozen-cohort recomputation. Outstanding settlement and complete historical ticket-to-recommendation linkage stay open. No market, recommendation, wager, cash, model, or task changes.
