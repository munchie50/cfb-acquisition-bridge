# Week 10 kickoff reconciliation — bounded independent CBS/ESPN check

Status: OPEN; NOT PRODUCTION-QUALIFIED. Identity matching remains 63/63 unique directed pairs to ESPN game IDs, persisted separately in CFB_WEEK10_CBS_ESPN_DIRECTED_IDENTITY_JOIN_20261031.json.

Sources: preserved CBS Week10 odds markdown capture and independent ESPN Week10 full-FBS scoreboard markdown capture in evidence/operational/. This check compares displayed local wall-clock times; ESPN scoreboard does not establish an explicit timezone in the captured time label, so equality of clock displays is not sufficient for UTC kickoff certification.

Initial directed ID-based clock comparison: 53/63 displayed clock strings equal. Nine ESPN event headings display TBD rather than a clock; one is a visible clock conflict: Rutgers @ Wisconsin, ESPN game ID 401858517, CBS Sat Nov 7 1:00pm, ESPN 12:30 PM. The first parser's nine missing values were source TBD labels, not merely missing parsing coverage. Preserve source conflict and do not auto-select one clock.

Required smallest next steps: obtain independent exact kickoff with explicit timezone for nine ESPN TBD games and Rutgers/Wisconsin conflict, then reconcile remaining 53 display-clock agreements to an authoritative timezone. Keep original 63/63 game ID join intact; no normalization profile or Hot Sheet authorized until temporal gates pass. No schedule/task/Champion changes.

## Targeted ESPN ISO timestamp check (Nov 7 scoreboard API)
Independent ESPN scoreboard JSON endpoint `https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=20261107&groups=80&limit=200` returned HTTP 200 with 51 events. All ten exception game IDs were present. Nine ESPN TBD games each have `date: 2026-11-07T05:00Z`, exactly midnight Eastern / 11 PM Central on Nov 6; these are unqualified placeholder timestamps, NOT verified kickoff times. Rutgers @ Wisconsin (401858517) has `date: 2026-11-07T17:30Z`, i.e. 12:30 PM Eastern / 11:30 AM Central, consistent with ESPN's 12:30 PM Eastern display but conflicting with CBS's 1:00pm displayed time. Do not force CBS clocks into ESPN timezone without source qualification. Zero of the nine TBD kickoffs resolved; Rutgers conflict confirmed with ISO date but not arbitrated. Full temporal acceptance still OPEN.
