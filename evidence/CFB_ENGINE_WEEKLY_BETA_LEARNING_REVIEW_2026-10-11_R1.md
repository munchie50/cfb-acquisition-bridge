# CFB Engine Weekly Beta Learning Review — 2026-10-11 — R1

Status: AUTHORITATIVE SUNDAY LEARNING OUTPUT CANDIDATE
Run identity: CFB_WEEKLY_QA_20261011T135620Z
Scope: Week 6 real-world Beta closure plus Week 7 Sunday carry-forward
Scientific effect: NONE
Champion effect: NONE
Challenger promotion: NONE

## 1. Executive state

The accepted Beta Production Champion remains **v1.193**. Genuine pre-event Week 6 **FIRST_FROZEN v1.208** predictions remain immutable. Market, decisions, ticket executions, final scores, and this review are downstream evidence only.

Week 6 source scope remains 58 targets: 49 modeled predictions and nine governed exclusions. The final operational Hot Sheet displayed all 49 modeled games exactly once and retained Nebraska as a mandatory explicit unmodeled exclusion. The full postgame join is now **49/49 modeled games with zero unresolved identities**: four ticket games had already been appended from official result sources; this QA appended the remaining 45 from the CBS Sports Week 6 final scoreboard without duplicating the first four.

The accepted weekly S0 REFRESH_SNAPSHOT from the natural Tuesday artifact remains a distinct prospective source boundary: cutoff 2026-10-06T15:11:29.838398Z, 498 targets, 495 predictions plus three exclusions. It did not mutate Champion v1.193. The same-cutoff S2_K1 target-baseline substrate is accepted, but no S2_K1 prediction consumer or S2 prediction set is accepted.

The current Week 7 Sunday Hot Sheet was independently read back at blob b0131986d8bf6c0f3f964852a362eecf4a4b4b6f: 62 unique games, zero duplicates, section union 62, Nebraska included. It honestly carries **no earned Week 7 Engine Prediction (Frozen)** before Monday readiness / Tuesday candidate and independent acceptance. Every current market row is a labelled CBS mixed-book fallback; **CONSENSUS_UNAVAILABLE** and **Caesars UNVERIFIED** are preserved.

Unresolved authority/data issues:
- no qualified three-operator non-Caesars consensus for Week 6 or Week 7;
- no independently verified current Caesars offer;
- no qualified Week 6 closing-market capture, so CLV is unavailable;
- four Week 6 tickets and the eleven earlier actual tickets remain budget-class UNASSIGNED between production and sandbox;
- printed ticket timezone, sportsbook settlement/redemption/payment, and causal recommendation attribution remain unverified unless separately proved;
- five early-week games closed as prior INCONCLUSIVE after their required reconciliation was missed; no hindsight decisions are manufactured.

## 2. Weekly performance summary

| Diagnostic | Week 6 result | Interpretation |
|---|---:|---|
| Modeled games scored | 49/49 | Complete identity join; not model acceptance |
| Margin MAE | 15.13 | Large one-week error; investigate tails and matchup/context gaps |
| Mean margin error | +0.90 | Small aggregate bias hides large two-sided misses |
| Total MAE | 13.54 | Large one-week total error |
| Mean total error | -0.89 | Aggregate near zero hides severe over/under tails |
| Straight-up direction | 25/49 (51.0%) | Weak one-week classification result |
| Home-win Brier | 0.2840 | Descriptive diagnostic only; no recalibration from one week |
| Final decisions | 3 executed actionable, 1 actual execution against prospective PASS, 40 PASS/no-bet, 5 closed prior INCONCLUSIVE | Decision layer remains separate from prediction layer |
| Established Week 6 tickets | 1 win, 2 losses, 1 push | $20 staked; $14.55 returned; -$5.45 net |

This is a small, noisy weekly sample. It is sufficient to create hypotheses and prioritize diagnostics, but not to refit, recalibrate, promote a Challenger, change thresholds, or infer durable profitability.

## 3. Game-level learning

| Game | Engine Prediction (Frozen) | Final | Margin error | Total error | Preserved decision / market learning |
|---|---|---|---:|---:|---|
| Southern Miss @ Troy | home +6.4; total 51.9; home p 0.612 | Southern Miss 34, Troy 55 | +14.6 | +37.1 | PASS; -10.5 unchanged; total +1.0; consensus unavailable / Caesars unverified / CLV unavailable |
| Jacksonville State @ Kennesaw State | home +3.6; total 52.1; home p 0.579 | Jacksonville State 27, Kennesaw State 26 | -4.6 | +0.9 | CLOSED—prior INCONCLUSIVE; +4.5 first → +3.5; consensus unavailable / Caesars unverified / CLV unavailable |
| New Mexico State @ FIU | home +3.2; total 52.2; home p 0.530 | New Mexico State 3, FIU 22 | +15.8 | -27.2 | CLOSED—prior INCONCLUSIVE; FIU -4.5 first → -6; consensus unavailable / Caesars unverified / CLV unavailable |
| Missouri State @ Western Kentucky | home -17.3; total 55.7; home p 0.150 | Missouri State 13, Western Kentucky 34 | +38.3 | -8.7 | CLOSED—prior INCONCLUSIVE; N/A; consensus unavailable / Caesars unverified / CLV unavailable |
| South Florida @ UTSA | home -3.1; total 54.8; home p 0.447 | South Florida 24, UTSA 31 | +10.1 | +0.2 | CLOSED—prior INCONCLUSIVE; N/A; consensus unavailable / Caesars unverified / CLV unavailable |
| South Alabama @ Arkansas State | home +2.3; total 54.8; home p 0.613 | South Alabama 56, Arkansas State 49 | -9.3 | +50.2 | CLOSED—prior INCONCLUSIVE; N/A; consensus unavailable / Caesars unverified / CLV unavailable |
| Florida State @ Louisville | home +17.5; total 64.8; home p 0.873 | Florida State 20, Louisville 44 | +6.5 | -0.8 | PASS; LOU -7 first → -3.5; consensus unavailable / Caesars unverified / CLV unavailable |
| Iowa @ Washington | home -1.9; total 46.0; home p 0.457 | Iowa 41, Washington 24 | -15.1 | +19.0 | PASS; WASH -1.5 first → -2.5; total -2.0; consensus unavailable / Caesars unverified / CLV unavailable |
| Washington State @ Utah State | home -1.7; total 44.9; home p 0.446 | Washington State 16, Utah State 17 | +2.7 | -11.9 | PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| Wyoming @ San José State | home +5.1; total 50.1; home p 0.602 | Wyoming 16, San José State 13 | -8.1 | -21.1 | PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| Iowa State @ BYU | home +11.8; total 51.7; home p 0.804 | Iowa State 10, BYU 24 | +2.2 | -17.7 | PASS; BYU -14.5 first → -10.5; total -4.0; consensus unavailable / Caesars unverified / CLV unavailable |
| Arizona @ West Virginia | home +3.4; total 53.8; home p 0.564 | Arizona 52, West Virginia 31 | -24.4 | +29.2 | PASS / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| Texas A&M @ Missouri | home +7.7; total 48.5; home p 0.643 | Texas A&M 6, Missouri 27 | +13.3 | -15.5 | PASS / TOTAL PASS; MIZZ -2.5 first → -3.5; consensus unavailable / Caesars unverified / CLV unavailable |
| UCF @ Oklahoma State | home +4.3; total 55.1; home p 0.600 | UCF 28, Oklahoma State 42 | +9.7 | +14.9 | PASS / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| North Carolina @ Pittsburgh | home +8.3; total 46.7; home p 0.680 | North Carolina 21, Pittsburgh 17 | -12.3 | -8.7 | PASS / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| Wake Forest @ NC State | home +9.3; total 59.3; home p 0.704 | Wake Forest 38, NC State 14 | -33.3 | -7.3 | PASS / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| Sacramento State @ Bowling Green | home -12.7; total 45.8; home p 0.200 | Sacramento State 10, Bowling Green 38 | +40.7 | +2.2 | PASS / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| South Carolina @ Florida | home +7.1; total 61.9; home p 0.693 | South Carolina 38, Florida 19 | -26.1 | -4.9 | PASS / TOTAL PASS; Florida -13.5 first → -12.5; consensus unavailable / Caesars unverified / CLV unavailable |
| Old Dominion @ App State | home +14.3; total 50.1; home p 0.823 | Old Dominion 10, App State 3 | -21.3 | -37.1 | BET NOW CONDITIONAL — EXECUTED / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| Miami (OH) @ Massachusetts | home +14.8; total 54.6; home p 0.818 | Miami (OH) 20, Massachusetts 19 | -15.8 | -15.6 | BET NOW CONDITIONAL — EXECUTED / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| Texas vs Oklahoma | home +3.4; total 42.8; home p 0.519 | Texas 24, Oklahoma 27 | -0.4 | +8.2 | PASS / TOTAL PASS; Texas -9.5 first → -8.5; consensus unavailable / Caesars unverified / CLV unavailable |
| UCLA @ Oregon | home +5.1; total 62.8; home p 0.655 | UCLA 17, Oregon 15 | -7.1 | -30.8 | PASS / TOTAL PASS; Oregon -13 first → -11.5; consensus unavailable / Caesars unverified / CLV unavailable |
| Stanford @ Notre Dame | home +27.6; total 49.3; home p 0.943 | Stanford 7, Notre Dame 58 | +23.4 | +15.7 | PASS / TOTAL PASS; ND -35.5 first → -38.5; consensus unavailable / Caesars unverified / CLV unavailable |
| Ole Miss @ Vanderbilt | home +1.9; total 54.7; home p 0.520 | Ole Miss 52, Vanderbilt 17 | -36.9 | +14.3 | PASS / TOTAL PASS; VAN +10.5 first → +10; consensus unavailable / Caesars unverified / CLV unavailable |
| Illinois @ Michigan State | home -4.4; total 50.9; home p 0.359 | Illinois 38, Michigan State 37 | +3.4 | +24.1 | PASS / TOTAL PASS; MSU +2.5 first; spread unchanged; consensus unavailable / Caesars unverified / CLV unavailable |
| Houston @ Kansas State | home +10.6; total 55.0; home p 0.757 | Houston 35, Kansas State 16 | -29.6 | -4.0 | PASS / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| Eastern Michigan @ Akron | home +11.1; total 50.1; home p 0.746 | Eastern Michigan 25, Akron 23 | -13.1 | -2.1 | PASS / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| Duke @ Georgia Tech | home +0.9; total 47.9; home p 0.568 | Duke 25, Georgia Tech 28 | +2.1 | +5.1 | PASS / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| Central Michigan @ Ohio | home -1.1; total 48.4; home p 0.483 | Central Michigan 14, Ohio 31 | +18.1 | -3.4 | PASS / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| Charlotte @ North Texas | home +7.8; total 62.1; home p 0.669 | Charlotte 10, North Texas 50 | +32.2 | -2.1 | PASS / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| Buffalo @ Toledo | home +22.1; total 56.1; home p 0.900 | Buffalo 23, Toledo 8 | -37.1 | -25.1 | PASS / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| Kent State @ Western Michigan | home +26.7; total 48.3; home p 0.939 | Kent State 7, Western Michigan 38 | +4.3 | -3.3 | PASS / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| Rice @ East Carolina | home +0.4; total 44.9; home p 0.544 | Rice 12, East Carolina 28 | +15.6 | -4.9 | PASS / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| Maryland @ Ohio State | home +11.4; total 56.4; home p 0.759 | Maryland 16, Ohio State 45 | +17.6 | +4.6 | PASS / TOTAL PASS; OSU -34.5 first → source divergence; consensus unavailable / Caesars unverified / CLV unavailable |
| Tennessee @ Arkansas | home -19.0; total 54.7; home p 0.144 | Tennessee 24, Arkansas 17 | +12.0 | -13.7 | PASS / TOTAL PASS; TENN -14.5 first → -13.5; consensus unavailable / Caesars unverified / CLV unavailable |
| San Diego State @ Oregon State | home +7.7; total 56.9; home p 0.678 | San Diego State 14, Oregon State 66 | +44.3 | +23.1 | PASS / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| Nevada @ UTEP | home -5.1; total 49.6; home p 0.368 | Nevada 30, UTEP 13 | -11.9 | -6.6 | PASS / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| North Dakota State @ UNLV | home -8.7; total 46.1; home p 0.273 | North Dakota State 7, UNLV 13 | +14.7 | -26.1 | PASS / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| LSU @ Kentucky | home -2.5; total 55.1; home p 0.453 | LSU 34, Kentucky 35 | +3.5 | +13.9 | PASS / TOTAL PASS; LSU -10.5 first → -8.5; consensus unavailable / Caesars unverified / CLV unavailable |
| Air Force @ Northern Illinois | home -16.1; total 48.4; home p 0.180 | Air Force 28, Northern Illinois 7 | -4.9 | -13.4 | PASS / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| Syracuse @ Virginia | home +10.1; total 50.8; home p 0.732 | Syracuse 25, Virginia 28 | -7.1 | +2.2 | PASS / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| James Madison @ Georgia Southern | home -8.0; total 46.7; home p 0.291 | James Madison 27, Georgia Southern 24 | +5.0 | +4.3 | PASS / TOTAL PASS; ACTUAL EXECUTION RECORDED; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| Georgia @ Alabama | home -7.0; total 61.7; home p 0.329 | Georgia 20, Alabama 17 | +4.0 | -24.7 | PASS / TOTAL PASS; Alabama +1.5 first → -1.5; consensus unavailable / Caesars unverified / CLV unavailable |
| Louisiana @ Louisiana Tech | home +0.1; total 54.5; home p 0.497 | Louisiana 31, Louisiana Tech 32 | +0.9 | +8.5 | PASS / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| USC @ Penn State | home +11.8; total 55.0; home p 0.749 | USC 31, Penn State 23 | -19.8 | -1.0 | PASS / TOTAL PASS; Penn State +2.5 first → -1.5; consensus unavailable / Caesars unverified / CLV unavailable |
| Minnesota @ Purdue | home -5.8; total 58.6; home p 0.345 | Minnesota 13, Purdue 41 | +33.8 | -4.6 | PASS / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| Kansas @ Utah | home +18.9; total 52.2; home p 0.873 | Kansas 24, Utah 41 | -1.9 | +12.8 | PASS / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| Hawai'i @ Arizona State | home +14.1; total 53.4; home p 0.781 | Hawai'i 12, Arizona State 30 | +3.9 | -11.4 | PASS / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |
| Boise State @ Fresno State | home +1.6; total 49.6; home p 0.560 | Boise State 38, Fresno State 31 | -8.6 | +19.4 | BET NOW CONDITIONAL — EXECUTED / TOTAL PASS; No qualified Oct 4 baseline; consensus unavailable / Caesars unverified / CLV unavailable |


Largest absolute margin misses:

| Game | Frozen home margin | Final | Margin error | Diagnostic direction |
|---|---:|---|---:|---|
| San Diego State @ Oregon State | +7.7 | 14-66 | +44.3 | Home performance above frozen expectation |
| Sacramento State @ Bowling Green | -12.7 | 10-38 | +40.7 | Home performance above frozen expectation |
| Missouri State @ Western Kentucky | -17.3 | 13-34 | +38.3 | Home performance above frozen expectation |
| Buffalo @ Toledo | +22.1 | 23-8 | -37.1 | Home performance below frozen expectation |
| Ole Miss @ Vanderbilt | +1.9 | 52-17 | -36.9 | Home performance below frozen expectation |
| Minnesota @ Purdue | -5.8 | 13-41 | +33.8 | Home performance above frozen expectation |
| Wake Forest @ NC State | +9.3 | 38-14 | -33.3 | Home performance below frozen expectation |
| Charlotte @ North Texas | +7.8 | 10-50 | +32.2 | Home performance above frozen expectation |


Largest absolute total misses:

| Game | Frozen total | Final total | Total error |
|---|---:|---:|---:|
| South Alabama @ Arkansas State | 54.8 | 105 | +50.2 |
| Southern Miss @ Troy | 51.9 | 89 | +37.1 |
| Old Dominion @ App State | 50.1 | 13 | -37.1 |
| UCLA @ Oregon | 62.8 | 32 | -30.8 |
| Arizona @ West Virginia | 53.8 | 83 | +29.2 |
| New Mexico State @ FIU | 52.2 | 25 | -27.2 |
| North Dakota State @ UNLV | 46.1 | 20 | -26.1 |
| Buffalo @ Toledo | 56.1 | 31 | -25.1 |


The errors are not uniformly directional. Mean margin and total errors are close to zero only because large misses cancel. Priority investigation should therefore focus on variance/tails, opponent-strength context, roster/availability timing, FCS/FBS transition or sparse-history cases, and whether small-sample stabilization behaves differently across the extreme misses. These are hypotheses, not established causes.

## 4. Champion versus market

No Week 6 observation qualifies as the user-approved market consensus because three distinct identified non-Caesars constituent books, paired prices, synchronized clocks, and dispersion were not preserved. CBS values remain mixed-book fallback observations. No actual current Caesars offer was independently verified. No qualified CLOSE observation exists. Therefore:
- quantitative consensus comparison is unavailable;
- Caesars-versus-consensus comparison is unavailable;
- CLV is unavailable;
- no market disagreement becomes calibrated EV or an automatic bet.

Useful descriptive flags remain:
- Massachusetts: frozen Champion favored Massachusetts by 14.8 while the retained fallback showed Massachusetts +4.5; the actual +5 ticket won ATS despite a 20-19 loss. This is a large opposite-favorite investigation flag, not proof of edge.
- Fresno State: frozen Champion favored Fresno by 1.6 while the fallback showed Fresno +7.5; Fresno lost by seven and the +7 ticket pushed.
- Wake Forest–NC State, Sacramento State–Bowling Green, Eastern Michigan–Akron, and several other games showed opposite-favorite or large-magnitude disagreements. Several resolved toward the market, but one week cannot establish market superiority or a trading rule.
- Appalachian State aligned directionally with the frozen Champion and ticket but lost outright; a favorable model-versus-market gap did not guarantee outcome quality.

## 5. Betting and decision assessment

### Established Week 6 user wagers only

| Execution | Printed issue time (timezone unverified) | Ticket | Engine Prediction (Frozen) | Prospective decision / limit | Preserved market state | Final / grade | Learning disposition |
|---|---|---|---|---|---|---|---|
| CFB_OCT09-03 | Oct 9 8:26 PM | Appalachian State -10 (-110), $5 | App State -14.3 / 50.1 / .823 home | BET NOW conditional; -10 or better, max -115 | Consensus unavailable; Caesars current offer unverified; later fallback App -9.5 (-115) | Old Dominion 10, App State 3 — LOSS, -$5 | Prediction, selection, and threshold aligned; outcome was a large model miss. Investigate, do not rewrite. |
| CFB_OCT09-04 | Oct 9 8:26 PM | Massachusetts +5 (-110), $5 | Massachusetts -14.8 / 54.6 / .818 home | BET NOW conditional; +4.5 or better, max -115 | Consensus unavailable; current Caesars unverified; fallback showed UMass +4.5 | Miami (OH) 20, UMass 19 — WIN, +$4.55 | Ticket sided with Champion direction and obtained points; extreme model-market disagreement remains a study item. |
| CFB_OCT09-01 | Oct 9 8:31 PM | James Madison -7.5 (-107), $5 | James Madison -8.0 / 46.7 / .291 home | Prospective Hot Sheet PASS; no acceptable execution established | Consensus unavailable; current Caesars unverified; fallback JMU -7.5 (-105) | James Madison 27, Georgia Southern 24 — LOSS, -$5 | Actual wager aligned with frozen model direction but conflicted with the preserved decision layer. Keep execution separate; no retroactive recommendation. |
| CFB_OCT09-02 | Oct 9 8:27 PM | Fresno State +7 (-113), $5 | Fresno State -1.6 / 49.6 / .560 home | BET NOW conditional; +7 or better, max -115 | Consensus unavailable; current Caesars unverified; later fallback Fresno +7.5 (-105) | Boise State 38, Fresno State 31 — PUSH, $0 | Threshold discipline avoided a loss at +7; without a qualified close, do not call this CLV. |

Portfolio result: four straight-spread tickets, $5 each, one trip, $20 total stake, $14.55 return, **-$5.45 net**. Three tickets followed actionable decisions; James Madison did not. All four selected the side favored by the frozen model, but only one won ATS and one pushed. This is too small and exposure-homogeneous to infer a stable human-versus-engine advantage. The single-trip batch respected the 1–2 trip constraint and created no duplicate exposure or chase.

Forty other final side decisions were PASS/no-bet. Five Wednesday/Thursday games remained historical CLOSED—prior INCONCLUSIVE because their reconciliation was missed. Their eventual outcomes do not create retroactive bets. Final Saturday WAIT count was zero.

## 6. Real-world Beta failures and control performance

| Observation | Classification | Control response | Consequence |
|---|---|---|---|
| Five early-week reconciliation windows missed | Operations/timing failure | Historical INCONCLUSIVE closed; no hindsight state invented | Lost prospective decision evidence remains visible |
| No qualified consensus | Source/semantic gap | CONSENSUS_UNAVAILABLE, fallback labelled | No false consensus or EV |
| Caesars current offer not verified | Execution-source gap | UNVERIFIED retained; ticket proves accepted execution only | No present offer inferred from ticket |
| No Week 6 close | Closing-market evidence gap | CLV left unavailable; no backfill | Timing quality cannot be measured |
| Ticket budget class unassigned | Accounting/authority gap | Production and $20 sandbox not commingled | Balances remain honest but attribution unresolved |
| Large frozen prediction errors | Football/model diagnostic | Outcomes appended after freeze; Champion untouched | Creates Challenger hypotheses only |
| Sunday Market Monitor persisted full Week 7 opening state and two-phase closure | Operations control success | Canonical/Hot Sheet/receipt readbacks passed | Natural current-cycle evidence exists without repairing older gaps |
| Consensus/Caesars schema labels carried into Week 7 Hot Sheet | Presentation/control success | Source roles remain distinct | No mixed-book fallback relabeling |

## 7. Exclusion and fail-closed learning

Nebraska–Indiana remained an explicit v1.208 exclusion (away_prior_points_missing) and was displayed as UNMODELED rather than omitted or assigned a manufactured Champion opinion. Nebraska lost 20-17, but the result does not justify reconstructing a prediction. The wider Week 6 source scope retained nine exclusions outside the 49-game scoring denominator.

The safe improvement target is prospective coverage repair: determine why each exclusion lacked usable strict-prior inputs and test a bounded source/feature remedy in Challenger/Sandbox. Outcomes may prioritize the work but may not populate the missing pre-event inputs.

## 8. Challenger, Sandbox, TIME-HIDDEN, and parlay findings

**Champion/Challenger:** Champion v1.193 remains production. The Oct. 7 S0 REFRESH_SNAPSHOT is accepted prospective source evidence. The same-cutoff S2_K1 target-baseline substrate is accepted, but S2_K1 remains study-only because an exact prediction consumer and prospective prediction set have not been accepted. No promotion gate is met.

**TIME-HIDDEN:** Week 5 replay is demonstrated complete for recoverable governed evidence. It proved the visibility firewall, no-backfill behavior, deadline failure classification, and postgame separation. It remains replay evidence, not proof that every natural producer cycle is reliable. The successful current Sunday Market Monitor is useful natural evidence but does not erase prior start-only/incomplete cycles.

**$20 sandbox:** Starting $20.00; current available $20.00; committed $0.00; cumulative established sandbox risk $0.00; established sandbox wagers 0. The four Week 6 tickets are actual real-money executions but remain budget-class UNASSIGNED, so this review does not debit the sandbox or credit production.

**Parlays:** No established Week 6 parlay execution and no qualified reproducible parlay recommendation. Silence is explained by unavailable consensus/Caesars/close evidence and no separately earned joint-probability framework. No probability, EV, or independence is invented. Singles remain the only established Week 6 exposures.

**WAIT learning:** Final Saturday WAIT count was zero. The five missed early-game INCONCLUSIVE cases remain UNRESOLVED as timing-process evidence; outcomes cannot reclassify them HELPED or HURT.

## 9. Learning-loop ledger

| ID | Observation → classification | Diagnosis / uncertainty | Disposition | Evidence required to close | Status |
|---|---|---|---|---|---|
| W6-L1 | Week 6 scorecard incomplete → operations/evaluation | 45 valid frozen rows lacked joined finals at Sunday start | Append exact results without duplicating four prior rows | 49/49 readback | CLOSED this cycle |
| W6-L2 | Five early games missed decision reconciliation → timing | Producer/closure gaps prevented prospective terminal decisions | Preserve gap; test next Tue–Thu natural cadence | Timely durable decisions before kickoff | OPEN |
| W6-L3 | Consensus unavailable → source acquisition | Constituents/books/clocks not qualified | Continue bounded three-book non-Caesars acquisition work | Named paired quotes, count/dispersion/clocks | OPEN |
| W6-L4 | Caesars unverified → execution source | Public fallback and ticket history do not prove a current offer | Verify actual Caesars paired offer prospectively | Line/price/clock/availability evidence | OPEN |
| W6-L5 | CLV unavailable → closing evidence | No qualified close was captured | Prospective closing-market capture only | Pre-kickoff qualified close readback | OPEN |
| W6-L6 | Four Week 6 tickets unassigned to production/sandbox → accounting authority | User intent is not proved by ticket alone | Retain UNASSIGNED; do not move money | Explicit governed allocation evidence | OPEN |
| W6-L7 | Margin MAE 15.13 with severe two-sided tails → Challenger hypothesis | Possible context/small-sample/availability/schedule drivers; cause unproved | Outlier decomposition under time-hidden inputs | Reproducible subgroup diagnostics across weeks | OPEN |
| W6-L8 | Total MAE 13.54 with offsetting tails → Challenger hypothesis | Mean near zero masks volatility | Analyze pace/scoring-environment tails prospectively | Multiweek time-hidden diagnostics | OPEN |
| W6-L9 | Week 7 Sunday opening board completed 62/62 → operations success | Current natural path passed | Monitor repeated natural cycles | Sustained readback/closure evidence | MONITOR |
| W6-L10 | JMU wager conflicted with PASS but stayed separate → control success | User execution is not recommendation truth | Preserve distinction in future reviews | Continued exact execution/decision joins | MONITOR |
| W6-L11 | S2_K1 substrate accepted but consumer absent → Challenger gate | Prediction layer not executable/accepted | Build/test exact consumer only under authorization | Frozen prospective predictions + independent acceptance | OPEN |
| W6-L12 | Nebraska exclusion visible, not manufactured → exclusion control success | Strict-prior input missing | Prospective coverage-repair hypothesis | Pre-event source repair and bounded acceptance | OPEN |

## 10. Exposure and operational accounting

- Week 6 established exposure: four tickets, $20 stake, all settled arithmetically from finals; sportsbook redemption/payment remains unverified.
- Week 6 result: $14.55 return, -$5.45 net.
- Cumulative canonical history before allocation: 15 actual tickets, $53.45 stake, all budget-class UNASSIGNED unless separately governed.
- Sandbox remains $20 available with zero assigned exposure.
- No duplicated Week 6 tickets, no live label, no third trip, no chase.
- Correlation concentration: all four Week 6 tickets were spread sides; model-direction agreement existed across all four, increasing shared model-risk exposure.
- No qualified consensus, current Caesars comparison, close, or CLV was available for portfolio quality scoring.

## 11. Next-week learning agenda

1. Prove timely Tuesday–Thursday decision reconciliation with durable readback; no lingering INCONCLUSIVE beyond deadlines.
2. Capture at least three identified qualified non-Caesars constituent books in one bounded window or preserve CONSENSUS_UNAVAILABLE with exact reason.
3. Independently verify actual Caesars line/price/clock before any executable recommendation; do not infer from a later ticket.
4. Capture qualified close prospectively for actionable and representative PASS games so timing/CLV can finally be evaluated.
5. Run time-hidden diagnostics on the largest Week 6 margin and total misses, prioritizing opponent-strength, sparse-history, roster availability, schedule/context, and FCS/FBS transition hypotheses.
6. Preserve budget-class separation until explicit allocation evidence resolves production versus $20 sandbox.
7. Continue S2_K1 only through the accepted substrate lineage; do not fabricate or promote a prediction consumer.
8. Maintain exact Week 7 section/cardinality and frozen-lineage gates when the Monday readiness and Tuesday candidate boundaries occur.
9. Recheck exclusion causes prospectively, especially missing strict-prior inputs, without outcome-informed repair.
10. Require repeated natural persistence/closure success; a current PASS does not erase prior incomplete cycles.

Important falsifiers:
- If outlier magnitude does not repeat by the proposed context groups across time-hidden weeks, retire or narrow those hypotheses.
- If consensus/close acquisition remains semantically incomplete, unavailable labels—not approximate substitutes—remain correct.
- If S2_K1 prospective predictions fail independent acceptance or do not outperform under governed evaluation, do not promote.
- If timely reconciliation still fails despite healthy writes, investigate producer cadence/ownership rather than market/model logic.

## 12. What we know now that we did not know seven days ago

- Week 6 has a complete 49-game frozen-to-final join, and its one-week prediction performance is materially weaker than aggregate bias alone would suggest.
- Large two-sided margin and total misses cancel in the mean; tail behavior deserves more attention than a simple directional-bias correction.
- All four Week 6 tickets followed the frozen model's directional opinion, but only three followed an actionable decision; recommendation quality and model direction are not the same thing.
- Threshold discipline mattered on Fresno: +7 produced a push, but without a qualified close this is not CLV evidence.
- The new consensus/Caesars control correctly prevents a mixed-book board or a historical ticket from masquerading as either consensus or a current executable offer.
- Current-cycle persistence and two-phase closure can succeed naturally, while earlier incomplete cycles and missing decision evidence remain honestly unresolved.
- Complete postgame learning can be added without mutating Champion, filling missing pre-event evidence, or promoting S2_K1.

## Provenance / readback targets

Repository authority and inputs:
- recovery index v1.245 blob 11ceb95907a1a2411331669255fe9077bb0debb2
- cadence v1.247 blob 2a41f5cee71152c9f0a84cc3ee2f634020819dc2
- Week 6 final Hot Sheet blob 1d64f2bc69414ea9816a08eb8fef22edd47decc3
- Week 7 Sunday Hot Sheet blob b0131986d8bf6c0f3f964852a362eecf4a4b4b6f
- market state blob 444d42107c646c379b2b51ac643460f3123ea9e6
- decision ledger blob 4c6b3468f0e0839ce85be0c96a5e9498b94d692a
- execution ledger blob 75caee4052e02ea7d2453d1d37fd3866e13ecc07
- completed postgame scorecard blob 6f7650d340bf63f8f93a2b825e35f8b8e41fa80b
- Week 6 results: https://www.cbssports.com/college-football/scoreboard/FBS/2026/regular/6/?layout=compact
- official established-ticket result sources are retained in the execution ledger.

Final classification is earned only after this review is persisted/read back, followed by terminal-candidate readback and separate RUN_CLOSURE.
