# CFB Week 6 Saturday — Exact source-identity reconciliation

Status: RESEARCH QA PASS (identity only); production Market Monitor remains RUN_INCOMPLETE.

Parent: evidence/operational/CFB_WEEK6_OCT08_SATURDAY_SOURCE_COVERAGE_AUDIT.md, read SHA cab9d35705d3b260d8a1e84f9e38cbe56e01b567.

Method: Split each of 38 immutable Saturday frozen-game rows into away/home; normalize case, accents, punctuation and explicitly enumerated team-name abbreviations; match full ordered away-home key to ESPN game URL slug from the retrieved odds source. Require exactly one source match per frozen row and no reused source slug. This verifies matchup identity but **does not verify kickoff timestamp** (the source index stores no times), executable quotes, or decisions.

- Frozen rows: 38
- Unique exact normalized ordered source matches: 38
- Unmatched or ambiguous: 0
- Extra ESPN Saturday matchups not in frozen modeled set: 8

| Frozen kickoff CT | Frozen matchup | Matched ESPN game slug | ESPN source linked away/home spreads (unqualified) |
|---|---|---|---|
| Sat 11:00 AM | Arizona @ West Virginia | arizona-west-virginia | -3 (-115) / +3 (-105) |
| Sat 11:00 AM | Texas A&M @ Missouri | texas-am-missouri | +3.5 (-115) / -3.5 (-105) |
| Sat 11:00 AM | UCF @ Oklahoma State | ucf-oklahoma-st | +10.5 (-108) / -10.5 (-105) |
| Sat 11:00 AM | North Carolina @ Pittsburgh | north-carolina-pitt | +3.5 (-108) / -3.5 (-112) |
| Sat 11:00 AM | Wake Forest @ NC State | wake-forest-nc-state | -3.5 (-105) / +3.5 (-115) |
| Sat 11:00 AM | Sacramento State @ Bowling Green | sacramento-st-bowling-green | +7.5 (-110) / -7.5 (-110) |
| Sat 11:45 AM | South Carolina @ Florida | south-carolina-florida | +11.5 (-112) / -11.5 (-108) |
| Sat 12:00 PM | Old Dominion @ App State | old-dominion-app-state | +9.5 (-105) / -9.5 (-115) |
| Sat 1:00 PM | Miami (OH) @ Massachusetts | miami-oh-umass | -2.5 (-108) / +2.5 (-112) |
| Sat 2:30 PM | Texas @ Oklahoma | texas-oklahoma | -7.5 (-110) / +7.5 (-110) |
| Sat 2:30 PM | UCLA @ Oregon | ucla-oregon | +11.5 (-110) / -11.5 (-110) |
| Sat 2:30 PM | Stanford @ Notre Dame | stanford-notre-dame | +39.5 (-115) / -39.5 (-105) |
| Sat 2:30 PM | Ole Miss @ Vanderbilt | ole-miss-vanderbilt | -9.5 (-108) / +9.5 (-112) |
| Sat 2:30 PM | Illinois @ Michigan State | illinois-michigan-st | -2.5 (-120) / +2.5 (+100) |
| Sat 2:30 PM | Houston @ Kansas State | houston-kansas-st | +2.5 (-105) / -2.5 (-115) |
| Sat 2:30 PM | Eastern Michigan @ Akron | e-michigan-akron | -6.5 (-118) / +6.5 (-102) |
| Sat 2:30 PM | Duke @ Georgia Tech | duke-georgia-tech | -6.5 (-115) / +6.5 (-105) |
| Sat 2:30 PM | Central Michigan @ Ohio | c-michigan-ohio | +3 (-112) / -3 (-108) |
| Sat 2:30 PM | Charlotte @ North Texas | charlotte-north-texas | +28.5 (-108) / -28.5 (-112) |
| Sat 2:30 PM | Buffalo @ Toledo | buffalo-toledo | +21 (-112) / -21 (-108) |
| Sat 2:30 PM | Kent State @ Western Michigan | kent-state-w-michigan | +13.5 (+100) / -13.5 (-120) |
| Sat 3:00 PM | Rice @ East Carolina | rice-east-carolina | +10 (-112) / -10 (-108) |
| Sat 3:15 PM | Maryland @ Ohio State | maryland-ohio-state | +32.5 (-110) / -32.5 (-110) |
| Sat 3:15 PM | Tennessee @ Arkansas | tennessee-arkansas | -13.5 (-110) / +13.5 (-110) |
| Sat 5:00 PM | San Diego State @ Oregon State | san-diego-st-oregon-st | +15.5 (-108) / -15.5 (-112) |
| Sat 6:00 PM | Nevada @ UTEP | nevada-utep | -10 (-108) / +10 (-112) |
| Sat 6:00 PM | North Dakota State @ UNLV | n-dakota-st-unlv | -3 (-118) / +3 (-102) |
| Sat 6:00 PM | LSU @ Kentucky | lsu-kentucky | -8.5 (-112) / +8.5 (-108) |
| Sat 6:30 PM | Air Force @ Northern Illinois | air-force-n-illinois | -7.5 (-108) / +7.5 (-112) |
| Sat 6:30 PM | Syracuse @ Virginia | syracuse-virginia | +10 (-110) / -10 (-110) |
| Sat 6:30 PM | James Madison @ Georgia Southern | james-madison-ga-southern | -7.5 (-105) / +7.5 (-115) |
| Sat 6:30 PM | Georgia @ Alabama | georgia-alabama | +1.5 (-108) / -1.5 (-112) |
| Sat 6:30 PM | Louisiana @ Louisiana Tech | louisiana-louisiana-tech | +3 (-112) / -3 (-108) |
| Sat 6:30 PM | USC @ Penn State | usc-penn-state | +1.5 (-112) / -1.5 (-108) |
| Sat 7:00 PM | Minnesota @ Purdue | minnesota-purdue | -2.5 (-110) / +2.5 (-110) |
| Sat 9:15 PM | Kansas @ Utah | kansas-utah | +15.5 (-110) / -15.5 (-110) |
| Sat 9:30 PM | Hawai'i @ Arizona State | hawaii-arizona-st | +20.5 (-105) / -20.5 (-115) |
| Sat 9:30 PM | Boise State @ Fresno State | boise-st-fresno-st | -6.5 (-110) / +6.5 (-110) |

## Extra ESPN games excluded from modeled recommendation set
- indiana-nebraska
- tulane-army
- ball-state-northwestern
- virginia-tech-california
- tulsa-navy
- uconn-temple
- uab-memphis
- coastal-marshall

## Remaining gates
Validate kickoff timestamps from source and authoritative schedule; verify sportsbook quote freshness, price, source and executability; preserve frozen predictions and original acceptable cutoffs; reconcile governed decision deadlines and full Hot Sheet; persist canonical changes only with readback and terminal receipt plus separate closure. No BET NOW or BET EARLY certified by this artifact.

## Readback correction
Initial artifact incorrectly counted UCF @ Oklahoma State as unmatched because the deterministic abbreviation dictionary omitted Oklahoma State → oklahoma-st. Source audit independently includes slug `ucf-oklahoma-st`. This revision corrects that matching alias, reconciles counts to 38/38, and retains the failed first-pass finding as evidence. No other source match was changed.
