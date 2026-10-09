# Saturday kickoff-time report presentation correction — Test Routine v6

Status: QA presentation correction; prior numeric comparisons remain intact.

Original audit: evidence/operational/CFB_WEEK6_OCT08_SATURDAY_KICKOFF_TIME_RECONCILIATION.md (blob c710642222cd6b81a1f7e917bf01393fac50388a). Independent frozen time labels: evidence/operational/CFB_WEEK6_OCT08_SATURDAY_EXACT_IDENTITY_RECONCILIATION.md (blob 52c1921768058e2025e4f2307a2cba9338da7a75).

The original report mislabeled minute-of-day values (e.g., 660) as human-readable Frozen kickoff CT. For all 38 games, the minute-of-day value was independently re-derived from the frozen Sat h:mm AM/PM label and matched exactly (38/38). No kickoff mismatches or source identity mismatches were found. The original report is preserved as immutable prior evidence. The corrected readable column follows.

| Frozen game | Frozen kickoff CT (readable) | ESPN game ID | ESPN UTC kickoff | Derived CT (24h) | Check |
|---|---|---|---|---|---|
| Arizona @ West Virginia | Sat 11:00 AM | 401856823 | 2026-10-10T16:00Z | 11:00 | PASS |
| Texas A&M @ Missouri | Sat 11:00 AM | 401856716 | 2026-10-10T16:00Z | 11:00 | PASS |
| UCF @ Oklahoma State | Sat 11:00 AM | 401856824 | 2026-10-10T16:00Z | 11:00 | PASS |
| North Carolina @ Pittsburgh | Sat 11:00 AM | 401858256 | 2026-10-10T16:00Z | 11:00 | PASS |
| Wake Forest @ NC State | Sat 11:00 AM | 401858260 | 2026-10-10T16:00Z | 11:00 | PASS |
| Sacramento State @ Bowling Green | Sat 11:00 AM | 401866436 | 2026-10-10T16:00Z | 11:00 | PASS |
| South Carolina @ Florida | Sat 11:45 AM | 401856714 | 2026-10-10T16:45Z | 11:45 | PASS |
| Old Dominion @ App State | Sat 12:00 PM | 401869843 | 2026-10-10T17:00Z | 12:00 | PASS |
| Miami (OH) @ Massachusetts | Sat 1:00 PM | 401866440 | 2026-10-10T18:00Z | 13:00 | PASS |
| Texas @ Oklahoma | Sat 2:30 PM | 401856717 | 2026-10-10T19:30Z | 14:30 | PASS |
| UCLA @ Oregon | Sat 2:30 PM | 401858484 | 2026-10-10T19:30Z | 14:30 | PASS |
| Stanford @ Notre Dame | Sat 2:30 PM | 401858257 | 2026-10-10T19:30Z | 14:30 | PASS |
| Ole Miss @ Vanderbilt | Sat 2:30 PM | 401856718 | 2026-10-10T19:30Z | 14:30 | PASS |
| Illinois @ Michigan State | Sat 2:30 PM | 401858480 | 2026-10-10T19:30Z | 14:30 | PASS |
| Houston @ Kansas State | Sat 2:30 PM | 401856825 | 2026-10-10T19:30Z | 14:30 | PASS |
| Eastern Michigan @ Akron | Sat 2:30 PM | 401866435 | 2026-10-10T19:30Z | 14:30 | PASS |
| Duke @ Georgia Tech | Sat 2:30 PM | 401858255 | 2026-10-10T19:30Z | 14:30 | PASS |
| Central Michigan @ Ohio | Sat 2:30 PM | 401866438 | 2026-10-10T19:30Z | 14:30 | PASS |
| Charlotte @ North Texas | Sat 2:30 PM | 401862796 | 2026-10-10T19:30Z | 14:30 | PASS |
| Buffalo @ Toledo | Sat 2:30 PM | 401866437 | 2026-10-10T19:30Z | 14:30 | PASS |
| Kent State @ Western Michigan | Sat 2:30 PM | 401866439 | 2026-10-10T19:30Z | 14:30 | PASS |
| Rice @ East Carolina | Sat 3:00 PM | 401862797 | 2026-10-10T20:00Z | 15:00 | PASS |
| Maryland @ Ohio State | Sat 3:15 PM | 401858483 | 2026-10-10T20:15Z | 15:15 | PASS |
| Tennessee @ Arkansas | Sat 3:15 PM | 401856713 | 2026-10-10T20:15Z | 15:15 | PASS |
| San Diego State @ Oregon State | Sat 5:00 PM | 401860902 | 2026-10-10T22:00Z | 17:00 | PASS |
| Nevada @ UTEP | Sat 6:00 PM | 401864517 | 2026-10-10T23:00Z | 18:00 | PASS |
| North Dakota State @ UNLV | Sat 6:00 PM | 401864518 | 2026-10-10T23:00Z | 18:00 | PASS |
| LSU @ Kentucky | Sat 6:00 PM | 401856715 | 2026-10-10T23:00Z | 18:00 | PASS |
| Air Force @ Northern Illinois | Sat 6:30 PM | 401864516 | 2026-10-10T23:30Z | 18:30 | PASS |
| Syracuse @ Virginia | Sat 6:30 PM | 401858258 | 2026-10-10T23:30Z | 18:30 | PASS |
| James Madison @ Georgia Southern | Sat 6:30 PM | 401869949 | 2026-10-10T23:30Z | 18:30 | PASS |
| Georgia @ Alabama | Sat 6:30 PM | 401856712 | 2026-10-10T23:30Z | 18:30 | PASS |
| Louisiana @ Louisiana Tech | Sat 6:30 PM | 401869965 | 2026-10-10T23:30Z | 18:30 | PASS |
| USC @ Penn State | Sat 6:30 PM | 401858485 | 2026-10-10T23:30Z | 18:30 | PASS |
| Minnesota @ Purdue | Sat 7:00 PM | 401858486 | 2026-10-11T00:00Z | 19:00 | PASS |
| Kansas @ Utah | Sat 9:15 PM | 401856827 | 2026-10-11T02:15Z | 21:15 | PASS |
| Hawai'i @ Arizona State | Sat 9:30 PM | 401856808 | 2026-10-11T02:30Z | 21:30 | PASS |
| Boise State @ Fresno State | Sat 9:30 PM | 401860901 | 2026-10-11T02:30Z | 21:30 | PASS |

No model, market quote, canonical Hot Sheet, decision, scheduler configuration or betting state changed. This correction is not a production Market Monitor closure or executable price validation.
