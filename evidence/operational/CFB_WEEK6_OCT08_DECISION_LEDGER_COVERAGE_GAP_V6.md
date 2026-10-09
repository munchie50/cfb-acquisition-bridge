# Week 6 decision-ledger coverage gap — Test Routine v6

Status: QA FINDING / OPEN EXECUTION DEBT; no betting recommendation or production acceptance.

Readback inputs:
- evidence/operational/CFB_DECISION_WAIT_LEDGER.md (blob 07ede9343706473b37a8b509777d68d3a27beec7)
- evidence/operational/CFB_WEEK6_OCT08_DECISION_WINDOW_AUDIT_TEST_V6.md (blob d87782f19834f4533247aa04cb7a78eeb87e7576)
- evidence/operational/CFB_WEEK6_OCT08_FRIDAY_FIVE_GAME_REQUOTE_QA_V6.md
- evidence/operational/CFB_WEEK6_OCT08_SATURDAY_DK_REQUOTE_DELTA_TEST_V6.md

## Finding
The active decision ledger contains a Sunday October 4 prospective *schedule of review boundaries* for 49 Week 6 modeled games, but its latest Week 6 decision entries still stop at Tuesday October 6 recovery. It does not contain completed prospective Thursday-evening Friday-five decisions or Friday-evening Saturday-morning-seven decisions. The separate research quote and kickoff audits verify source consistency and section membership only; they cannot close the ledger's decision obligation.

Required partition: Friday 5 → Thursday evening review and final practical Friday cutoff; Saturday morning 7 → Friday evening review and practical Saturday pre-kickoff cutoff; Saturday afternoon 17 → Saturday 07:00 CT; Saturday evening 14 → Saturday 13:00 CT. Each unresolved game must transition to a justified actionable state, governed WAIT with trigger and hard cutoff, or PASS. These review times are not themselves hard betting cutoffs.

## Blockers and disposition
No qualified executable Caesars price, accepted minimum-price/line threshold, calibrated EV, or current player/football reconciliation was established by the source QA. No retroactive recommendation is authorized. Do not label all games PASS merely because research evidence is insufficient at an earlier review; preserve INCONCLUSIVE / RUN_INCOMPLETE with explicit future gate until a valid prospective decision window. For games already underway, do not backfill pregame decisions.

This finding does not mutate the canonical decision ledger, Champion/FIRST_FROZEN, market snapshot, Hot Sheet, scheduler configuration, or wager record. Scheduler production closure remains independently OPEN.
