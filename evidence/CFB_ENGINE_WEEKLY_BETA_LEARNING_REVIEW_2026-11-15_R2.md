# CFB Weekly Beta Learning Review — November 15, 2026 R2

Manual continuation of [Sunday R1](CFB_ENGINE_WEEKLY_BETA_LEARNING_REVIEW_2026-11-15_R1.md), immutable blob `a4abff45236b7cbdbd413e691c33029b12a18c0e`. Week 11 outcome and score-grading work is complete. Retains the scheduled R1 receipt as historical RUN_INCOMPLETE and leaves broader production and financial gates open.

## Champion and model outcomes

CBS and the NCAA Game Center feed both reported Oklahoma 24, Ole Miss 17 as final for the rescheduled game. The [final supplement](https://github.com/munchie50/cfb-acquisition-bridge/blob/7d668770ccd4679dd48a93517ff0100a11fe1330/evidence/operational/CFB_WEEK11_OFFICIAL_OUTCOME_QA_20261115_R2.json) and [canonical scorecard](https://github.com/munchie50/cfb-acquisition-bridge/blob/8072c694a4b3e502ddf9bbf6e053a111a7d051ea/evidence/operational/CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md) were independently read back. Cohort: 67/67 qualified finals, 59/59 modeled FIRST_FROZEN games, eight original exclusions.

| Winner direction | Margin MAE | Total MAE | Brier |
|---:|---:|---:|---:|
| 35/59 | 15.966430 | 14.117354 | 0.269502 |

Oklahoma covered the direction predicted by the frozen model and won by 7 against a projected 7.85. The actual total was 41 against 46.72. Nebraska–Rutgers remains an original exclusion. Its known pregame refresh is documented separately in the Week 11 delivery audit and does not enter the table. Champion v1 S0 remains production; S2_K1 remains HOLD under the prior matched comparison. No matched new Week 11 Challenger cohort or production promotion is claimed.

## Bets, delivery and learning

- All 13 real-money Week 11 tickets are score-graded. Six wins, seven losses, zero pushes, $82 staked, $76.65 calculated gross and −$5.35 net. Sole parlay loss cost $2 and shared four games with straight wagers. Actual settlement and cash redemption are unverified.
- The two Friday conditional rows split 1–1. A $5-per-row illustration at archived public prices gives −$0.65. Venue confirmation was pending. The equivalent actual $10 tickets net −$0.90 from ticket terms. No priced and eligible complete Top 10, full-slate baseline, or genuine published combined parlay existed in the reviewed artifact, so those broader replays remain ungradable.
- Independently reconciled the October 31 Week 9 ticket batch against its historical decision sources, and the November 6 Week 10 score grades against accepted finals. Full-season recommendation chronology, settlement, and production-versus-sandbox assignment remain open.

[Week 11 delivery and exposure audit](audits/CFB_WEEK11_SUNDAY_DELIVERY_AND_TICKET_REPLAY_20261115.md) · [Week 9 linkage audit](audits/CFB_WEEK9_OCT31_TICKET_TO_SAVED_REVIEW_AUDIT_20261115.md) · [Week 10 ticket score audit](audits/CFB_WEEK10_NOV06_INDEPENDENT_SCORE_GRADE_20261115.md)

## Operations and next open work

The November 15 1 p.m. CT Monitor closed RUN_INCOMPLETE. Its GitHub connector recovered the helper; the scheduled Python runtime failed DNS at api.github.com during immutable byte transfer, before checkout. The saved Friday Hot Sheet remains the last accepted publication. Next Monitor owns prospective Week 12 capture and review once it has a verified checkout and current profile. Preserve the specific missed windows and exact evidence gaps for later comparison. This R2 completes the weekly outcome analysis without advancing scheduled reliability, accepting a new Hot Sheet, or changing the recovery selector, frozen model, bets, schedules or money.
