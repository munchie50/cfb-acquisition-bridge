# CFB Week 6 Saturday kickoff-time verification — Test Routine v6

Status: QA PASS for matchup identity + scheduled kickoff time only; NOT a production Market Monitor completion or bet recommendation.

Parent: evidence/operational/CFB_WEEK6_OCT08_SATURDAY_EXACT_IDENTITY_RECONCILIATION.md (read SHA 52c1921768058e2025e4f2307a2cba9338da7a75).
Source: https://www.espn.com/college-football/odds, live Firecrawl scrape maxAge=0 during Oct 8 CT evening test session.

Method: match ESPN game URL slug, retain ESPN game ID and ISO UTC kickoff, convert to America/Chicago (UTC-5 on October 10 2026), compare minute-for-minute against frozen Hot Sheet CT time. Preserve both raw and converted values. No assumption that these are real-time game-state or bookmaker quote timestamps.

- Frozen modeled Saturday games: 38
- Matched ESPN game IDs: 38
- Exact CT kickoff matches: 38
- Time mismatches: 0

| Frozen game | Frozen kickoff CT | ESPN game ID | ESPN UTC kickoff | Derived CT | Check |
|---|---|---|---|---|---|
| Arizona @ West Virginia | 660 | 401856823 | 2026-10-10T16:00Z | 11:00 | PASS |
| Texas A&M @ Missouri | 660 | 401856716 | 2026-10-10T16:00Z | 11:00 | PASS |
| UCF @ Oklahoma State | 660 | 401856824 | 2026-10-10T16:00Z | 11:00 | PASS |
| North Carolina @ Pittsburgh | 660 | 401858256 | 2026-10-10T16:00Z | 11:00 | PASS |
| Wake Forest @ NC State | 660 | 401858260 | 2026-10-10T16:00Z | 11:00 | PASS |
| Sacramento State @ Bowling Green | 660 | 401866436 | 2026-10-10T16:00Z | 11:00 | PASS |
| South Carolina @ Florida | 705 | 401856714 | 2026-10-10T16:45Z | 11:45 | PASS |
| Old Dominion @ App State | 720 | 401869843 | 2026-10-10T17:00Z | 12:00 | PASS |
| Miami (OH) @ Massachusetts | 780 | 401866440 | 2026-10-10T18:00Z | 13:00 | PASS |
| Texas @ Oklahoma | 870 | 401856717 | 2026-10-10T19:30Z | 14:30 | PASS |
| UCLA @ Oregon | 870 | 401858484 | 2026-10-10T19:30Z | 14:30 | PASS |
| Stanford @ Notre Dame | 870 | 401858257 | 2026-10-10T19:30Z | 14:30 | PASS |
| Ole Miss @ Vanderbilt | 870 | 401856718 | 2026-10-10T19:30Z | 14:30 | PASS |
| Illinois @ Michigan State | 870 | 401858480 | 2026-10-10T19:30Z | 14:30 | PASS |
| Houston @ Kansas State | 870 | 401856825 | 2026-10-10T19:30Z | 14:30 | PASS |
| Eastern Michigan @ Akron | 870 | 401866435 | 2026-10-10T19:30Z | 14:30 | PASS |
| Duke @ Georgia Tech | 870 | 401858255 | 2026-10-10T19:30Z | 14:30 | PASS |
| Central Michigan @ Ohio | 870 | 401866438 | 2026-10-10T19:30Z | 14:30 | PASS |
| Charlotte @ North Texas | 870 | 401862796 | 2026-10-10T19:30Z | 14:30 | PASS |
| Buffalo @ Toledo | 870 | 401866437 | 2026-10-10T19:30Z | 14:30 | PASS |
| Kent State @ Western Michigan | 870 | 401866439 | 2026-10-10T19:30Z | 14:30 | PASS |
| Rice @ East Carolina | 900 | 401862797 | 2026-10-10T20:00Z | 15:00 | PASS |
| Maryland @ Ohio State | 915 | 401858483 | 2026-10-10T20:15Z | 15:15 | PASS |
| Tennessee @ Arkansas | 915 | 401856713 | 2026-10-10T20:15Z | 15:15 | PASS |
| San Diego State @ Oregon State | 1020 | 401860902 | 2026-10-10T22:00Z | 17:00 | PASS |
| Nevada @ UTEP | 1080 | 401864517 | 2026-10-10T23:00Z | 18:00 | PASS |
| North Dakota State @ UNLV | 1080 | 401864518 | 2026-10-10T23:00Z | 18:00 | PASS |
| LSU @ Kentucky | 1080 | 401856715 | 2026-10-10T23:00Z | 18:00 | PASS |
| Air Force @ Northern Illinois | 1110 | 401864516 | 2026-10-10T23:30Z | 18:30 | PASS |
| Syracuse @ Virginia | 1110 | 401858258 | 2026-10-10T23:30Z | 18:30 | PASS |
| James Madison @ Georgia Southern | 1110 | 401869949 | 2026-10-10T23:30Z | 18:30 | PASS |
| Georgia @ Alabama | 1110 | 401856712 | 2026-10-10T23:30Z | 18:30 | PASS |
| Louisiana @ Louisiana Tech | 1110 | 401869965 | 2026-10-10T23:30Z | 18:30 | PASS |
| USC @ Penn State | 1110 | 401858485 | 2026-10-10T23:30Z | 18:30 | PASS |
| Minnesota @ Purdue | 1140 | 401858486 | 2026-10-11T00:00Z | 19:00 | PASS |
| Kansas @ Utah | 1275 | 401856827 | 2026-10-11T02:15Z | 21:15 | PASS |
| Hawai'i @ Arizona State | 1290 | 401856808 | 2026-10-11T02:30Z | 21:30 | PASS |
| Boise State @ Fresno State | 1290 | 401860901 | 2026-10-11T02:30Z | 21:30 | PASS |

Remaining: quote-source freshness and executable Caesars price validation; accepted cutoff and decision reconciliation; append-only canonical Hot Sheet and market/decision ledger updates; terminal receipt and separate closure. Thursday retrospective decisions prohibited; Indiana @ Nebraska remains unmodeled. Frozen predictions and schedules unchanged.
