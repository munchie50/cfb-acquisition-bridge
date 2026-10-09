# Week 6 — Test Routine v6 Saturday decision-window audit

Status: QA PASS for window assignment only. NOT a completed decision run, accepted Hot Sheet or betting authorization.

Sources: evidence/operational/CFB_DECISION_WAIT_LEDGER.md (SHA 07ede9343706473b37a8b509777d68d3a27beec7) and evidence/operational/CFB_WEEK6_OCT08_SATURDAY_KICKOFF_TIME_RECONCILIATION.md (SHA c710642222cd6b81a1f7e917bf01393fac50388a).

## Authority
Sunday Oct 4 opening-board decision boundary defines: Saturday morning 7 games → Friday evening availability review; Saturday afternoon 17 → Saturday 07:00 CT; Saturday evening/night 14 → Saturday 13:00 CT. Each has a final practical pre-kickoff cutoff. A large model/market spread discrepancy alone never earns a bet.

## Deterministic partition test
Using verified Saturday kickoff CT minutes, classify morning [00:00,12:00), afternoon [12:00,17:00), evening [17:00,24:00). This is a section-membership audit, not a newly authorized practical bet cutoff.

### Saturday morning: 7 games — Friday evening availability review
- 11:00 CT — Arizona @ West Virginia (ESPN 401856823)
- 11:00 CT — Texas A&M @ Missouri (ESPN 401856716)
- 11:00 CT — UCF @ Oklahoma State (ESPN 401856824)
- 11:00 CT — North Carolina @ Pittsburgh (ESPN 401858256)
- 11:00 CT — Wake Forest @ NC State (ESPN 401858260)
- 11:00 CT — Sacramento State @ Bowling Green (ESPN 401866436)
- 11:45 CT — South Carolina @ Florida (ESPN 401856714)

### Saturday afternoon: 17 games — Saturday 07:00 CT review
- 12:00 CT — Old Dominion @ App State (ESPN 401869843)
- 13:00 CT — Miami (OH) @ Massachusetts (ESPN 401866440)
- 14:30 CT — Texas @ Oklahoma (ESPN 401856717)
- 14:30 CT — UCLA @ Oregon (ESPN 401858484)
- 14:30 CT — Stanford @ Notre Dame (ESPN 401858257)
- 14:30 CT — Ole Miss @ Vanderbilt (ESPN 401856718)
- 14:30 CT — Illinois @ Michigan State (ESPN 401858480)
- 14:30 CT — Houston @ Kansas State (ESPN 401856825)
- 14:30 CT — Eastern Michigan @ Akron (ESPN 401866435)
- 14:30 CT — Duke @ Georgia Tech (ESPN 401858255)
- 14:30 CT — Central Michigan @ Ohio (ESPN 401866438)
- 14:30 CT — Charlotte @ North Texas (ESPN 401862796)
- 14:30 CT — Buffalo @ Toledo (ESPN 401866437)
- 14:30 CT — Kent State @ Western Michigan (ESPN 401866439)
- 15:00 CT — Rice @ East Carolina (ESPN 401862797)
- 15:15 CT — Maryland @ Ohio State (ESPN 401858483)
- 15:15 CT — Tennessee @ Arkansas (ESPN 401856713)

### Saturday evening/night: 14 games — Saturday 13:00 CT review
- 17:00 CT — San Diego State @ Oregon State (ESPN 401860902)
- 18:00 CT — Nevada @ UTEP (ESPN 401864517)
- 18:00 CT — North Dakota State @ UNLV (ESPN 401864518)
- 18:00 CT — LSU @ Kentucky (ESPN 401856715)
- 18:30 CT — Air Force @ Northern Illinois (ESPN 401864516)
- 18:30 CT — Syracuse @ Virginia (ESPN 401858258)
- 18:30 CT — James Madison @ Georgia Southern (ESPN 401869949)
- 18:30 CT — Georgia @ Alabama (ESPN 401856712)
- 18:30 CT — Louisiana @ Louisiana Tech (ESPN 401869965)
- 18:30 CT — USC @ Penn State (ESPN 401858485)
- 19:00 CT — Minnesota @ Purdue (ESPN 401858486)
- 21:15 CT — Kansas @ Utah (ESPN 401856827)
- 21:30 CT — Hawai'i @ Arizona State (ESPN 401856808)
- 21:30 CT — Boise State @ Fresno State (ESPN 401860901)

Exactly once: 38 / 38. Expected partition 7/17/14: 7/17/14. Zero duplicate or omitted rows by disjoint minute ranges.

## Open execution debt
Friday five modeled games require Thursday evening review and practical Friday cutoff. Saturday decisions must resolve to actionable, governed WAIT with trigger and hard cutoff, or PASS before each practical kickoff boundary. No Caesars-executable timestamped quote, verified acceptable price cutoff, or calibrated EV established by this audit. Do not backfill already-started Thursday games or infer wagers. No canonical ledger, champion, freeze, scheduler topology or betting state changed.
