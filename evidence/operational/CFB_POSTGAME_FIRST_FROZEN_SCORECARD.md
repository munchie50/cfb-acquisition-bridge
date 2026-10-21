# CFB Postgame FIRST_FROZEN Scorecard

Status: ACTIVE APPEND-ONLY DERIVED EVALUATION SURFACE
Initialized: 2026-09-27

## Purpose
Canonical governed scorecard joining immutable FIRST_FROZEN Champion predictions to independently sourced final results after games are final.

## Required fields
- game identity
- FIRST_FROZEN prediction artifact/reference and freeze timestamp
- projected margin/total/win probability as frozen
- final score/result source and retrieval timestamp
- realized margin/total/winner
- signed/absolute margin error and total error where computable
- win-probability outcome pairing without retroactive recalibration
- exclusion/unresolved status
- scoring-run receipt/reference

## Chronology locks
Results may be joined only after the corresponding prediction was genuinely frozen pre-event. Outcome knowledge never creates, edits, or fills a missing prediction. Ambiguous game/result joins remain UNRESOLVED.

## Initial state
This file defines the durable surface. Historical 2026 scoring is populated only by a governed scoring run from the accepted frozen prediction artifact plus authoritative final results; it is not reconstructed from memory.

## Write-path validation — 2026-09-27 13:03 CT
- Purpose: controlled repair validation for canonical existing-file mutation.
- Governance effect: none; no decision, execution, settlement, prediction, score, or outcome state created.
- Method: SHA-guarded existing-file update followed by direct repository readback.


## Week 4 QA summary — 2026-09-27
- 53 frozen games matched to 53 final results; no unresolved matches.
- Winner direction: 36/53 (67.9%).
- Margin mean absolute error: 14.781 points.
- Total mean absolute error: 11.071 points.
- Frozen prediction source: artifact 10897612260.
- Final result source: CBS Sports Week 4 FBS scoreboard retrieved 2026-09-27.
- This append does not alter any frozen prediction.


## Week 5 partial final-result join — 2026-10-03 morning
Final-result source boundary: authoritative/public final-score recovery after games were final. Only genuinely pre-event v1.208 FIRST_FROZEN predictions are joined. Explicit exclusions are not scored.

- Western Kentucky @ New Mexico State — FIRST_FROZEN: NMSU by 26.5495; projected total 55.5829. Final: NMSU 34, WKU 13. Realized home margin +21; realized total 47. Signed margin error (actual minus frozen) -5.5495; absolute margin error 5.5495. Signed total error -8.5829; absolute total error 8.5829.
- North Texas @ Tulsa — FIRST_FROZEN: Tulsa by 15.1102; projected total 56.2123. Final: North Texas 45, Tulsa 44 (OT). Realized Tulsa margin -1; realized total 89. Signed margin error -16.1102; absolute margin error 16.1102. Signed total error +32.7877; absolute total error 32.7877.
- Pittsburgh @ Virginia Tech — FIRST_FROZEN: Virginia Tech by 7.8503; projected total 51.6457. Final: Pittsburgh 35, Virginia Tech 33. Realized Virginia Tech margin -2; realized total 68. Signed margin error -9.8503; absolute margin error 9.8503. Signed total error +16.3543; absolute total error 16.3543.
- Liberty @ Delaware and Penn State @ Northwestern: explicit v1.208 FIRST_FROZEN exclusions/unmodeled; finals are not used to manufacture predictions or score rows.

Win-probability pairing is omitted for these rows where the exact frozen win-probability value was not recovered in this scoring step. No probability is invented. Champion unchanged.


## Week 5 complete governed final-result join — recovered 2026-10-05 from incomplete 2026-10-04 Sunday QA

Recovery purpose: complete the scorecard write that the 2026-10-04 09:00 CT Sunday QA attempted but could not persist. The historical RUN_INCOMPLETE receipt is not rewritten.

Frozen prediction boundary: accepted v1.208 FIRST_FROZEN producer artifact 10897612260, digest sha256:772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf, frozen 2026-09-26T03:47:37.497112+00:00. The original artifact was recovered directly and its Week 5 rows, including frozen win probabilities, were used unchanged.

Final-result boundary: ESPN Week 5 FBS scoreboard, live-retrieved 2026-10-05 during governed QA recovery. Game identity was joined by the frozen away/home team pair; all 47 modeled Week 5 games matched exactly once. The three Thursday/Friday rows already persisted above were independently reverified and are included in the aggregate metrics below but not duplicated as row appends. Explicit v1.208 exclusions/unmodeled remain unscored.

Aggregate Week 5 modeled scoring:
- 47/47 frozen modeled games matched to finals; unresolved joins: 0.
- Winner direction: 32/47 (68.1%).
- Margin MAE: 15.525 points; signed margin error (actual home margin minus frozen): -1.332.
- Total MAE: 14.116 points; signed total error (actual minus frozen): -0.620.
- Home-win Brier score from the genuinely frozen v1.208 probability: 0.2183.
- No refit, recalibration, prediction edit, exclusion conversion, market join, wager join, or Champion mutation occurred.

Remaining Saturday modeled rows:
- Vanderbilt @ Georgia — frozen home margin +24.5805; total 57.5598; home win 0.922243. Final: 14-38. Realized home margin +24; total 52. Margin error -0.5805; total error -5.5598; home-win outcome 1.
- Alabama @ Mississippi State — frozen home margin +9.8652; total 60.0377; home win 0.743319. Final: 56-23. Realized home margin -33; total 79. Margin error -42.8652; total error +18.9623; home-win outcome 0.
- Notre Dame @ North Carolina — frozen home margin -3.1262; total 45.3242; home win 0.406569. Final: 37-26. Realized home margin -11; total 63. Margin error -7.8738; total error +17.6758; home-win outcome 0.
- Middle Tennessee @ Kansas — frozen home margin +8.3809; total 49.6897; home win 0.657775. Final: 0-55. Realized home margin +55; total 55. Margin error +46.6191; total error +5.3103; home-win outcome 1.
- UCF @ Houston — frozen home margin +9.0491; total 57.6581; home win 0.732349. Final: 17-27. Realized home margin +10; total 44. Margin error +0.9509; total error -13.6581; home-win outcome 1.
- West Virginia @ Iowa State — frozen home margin +5.3540; total 50.0779; home win 0.699171. Final: 42-45. Realized home margin +3; total 87. Margin error -2.3540; total error +36.9221; home-win outcome 1.
- Boston College @ SMU — frozen home margin +11.0613; total 57.2873; home win 0.746306. Final: 16-25. Realized home margin +9; total 41. Margin error -2.0613; total error -16.2873; home-win outcome 1.
- Stanford @ Wake Forest — frozen home margin +13.4691; total 57.6392; home win 0.791886. Final: 3-57. Realized home margin +54; total 60. Margin error +40.5309; total error +2.3608; home-win outcome 1.
- Syracuse @ UConn — frozen home margin +6.8817; total 55.6316; home win 0.670083. Final: 42-41. Realized home margin -1; total 83. Margin error -7.8817; total error +27.3684; home-win outcome 0.
- Michigan @ Minnesota — frozen home margin +5.6597; total 45.2986; home win 0.614391. Final: 14-20. Realized home margin +6; total 34. Margin error +0.3403; total error -11.2986; home-win outcome 1.
- Michigan State @ Wisconsin — frozen home margin +8.8743; total 47.4395; home win 0.711063. Final: 3-31. Realized home margin +28; total 34. Margin error +19.1257; total error -13.4395; home-win outcome 1.
- Western Michigan @ Buffalo — frozen home margin -9.3382; total 48.0437; home win 0.275996. Final: 20-17. Realized home margin -3; total 37. Margin error +6.3382; total error -11.0437; home-win outcome 0.
- Toledo @ Ball State — frozen home margin -15.5050; total 60.1738; home win 0.173546. Final: 39-24. Realized home margin -15; total 63. Margin error +0.5050; total error +2.8262; home-win outcome 0.
- Florida @ Missouri — frozen home margin -0.4673; total 60.3527; home win 0.491110. Final: 17-45. Realized home margin +28; total 62. Margin error +28.4673; total error +1.6473; home-win outcome 1.
- Auburn @ Tennessee — frozen home margin +14.3585; total 59.1096; home win 0.824342. Final: 14-24. Realized home margin +10; total 38. Margin error -4.3585; total error -21.1096; home-win outcome 1.
- Louisville @ NC State — frozen home margin -0.3801; total 63.1780; home win 0.524416. Final: 28-31. Realized home margin +3; total 59. Margin error +3.3801; total error -4.1780; home-win outcome 1.
- Virginia @ Florida State — frozen home margin -10.1444; total 56.4679; home win 0.295540. Final: 7-38. Realized home margin +31; total 45. Margin error +41.1444; total error -11.4679; home-win outcome 1.
- Ohio State @ Iowa — frozen home margin +6.2898; total 51.1058; home win 0.593141. Final: 31-14. Realized home margin -17; total 45. Margin error -23.2898; total error -6.1058; home-win outcome 0.
- Memphis @ Charlotte — frozen home margin -10.0046; total 61.3418; home win 0.290588. Final: 59-8. Realized home margin -51; total 67. Margin error -40.9954; total error +5.6582; home-win outcome 0.
- Wyoming @ North Dakota State — frozen home margin +15.2997; total 47.1535; home win 0.807867. Final: 0-28. Realized home margin +28; total 28. Margin error +12.7003; total error -19.1535; home-win outcome 1.
- Akron @ Central Michigan — frozen home margin +2.0817; total 42.7465; home win 0.527542. Final: 17-41. Realized home margin +24; total 58. Margin error +21.9183; total error +15.2535; home-win outcome 1.
- Eastern Michigan @ Massachusetts — frozen home margin +22.0802; total 49.0269; home win 0.894632. Final: 38-14. Realized home margin -24; total 52. Margin error -46.0802; total error +2.9731; home-win outcome 0.
- Ohio @ Kent State — frozen home margin -8.9498; total 54.6341; home win 0.269265. Final: 13-10. Realized home margin -3; total 23. Margin error +5.9498; total error -31.6341; home-win outcome 0.
- Bowling Green @ Miami (OH) — frozen home margin +18.2081; total 55.2210; home win 0.868879. Final: 24-20. Realized home margin -4; total 44. Margin error -22.2081; total error -11.2210; home-win outcome 0.
- Old Dominion @ Georgia State — frozen home margin +11.1151; total 52.7631; home win 0.767988. Final: 10-42. Realized home margin +32; total 52. Margin error +20.8849; total error -0.7631; home-win outcome 1.
- Marshall @ James Madison — frozen home margin +29.5062; total 51.9170; home win 0.955715. Final: 17-45. Realized home margin +28; total 62. Margin error -1.5062; total error +10.0830; home-win outcome 1.
- Maryland @ Nebraska — frozen home margin +10.5205; total 56.0116; home win 0.733503. Final: 23-48. Realized home margin +25; total 71. Margin error +14.4795; total error +14.9884; home-win outcome 1.
- UTEP @ New Mexico — frozen home margin +22.5994; total 46.0268; home win 0.898590. Final: 7-61. Realized home margin +54; total 68. Margin error +31.4006; total error +21.9732; home-win outcome 1.
- Kentucky @ South Carolina — frozen home margin +13.7709; total 58.7110; home win 0.792395. Final: 35-34. Realized home margin -1; total 69. Margin error -14.7709; total error +10.2890; home-win outcome 0.
- Purdue @ Illinois — frozen home margin +13.4782; total 63.6174; home win 0.826129. Final: 24-17. Realized home margin -7; total 41. Margin error -20.4782; total error -22.6174; home-win outcome 0.
- Oregon State @ Colorado State — frozen home margin +3.8167; total 63.3473; home win 0.587505. Final: 56-26. Realized home margin -30; total 82. Margin error -33.8167; total error +18.6527; home-win outcome 0.
- Arkansas @ Texas A&M — frozen home margin +16.8044; total 51.3709; home win 0.828440. Final: 7-34. Realized home margin +27; total 41. Margin error +10.1956; total error -10.3709; home-win outcome 1.
- BYU @ TCU — frozen home margin -0.0910; total 55.7493; home win 0.503540. Final: 17-10. Realized home margin -7; total 27. Margin error -6.9090; total error -28.7493; home-win outcome 0.
- UTSA @ Rice — frozen home margin -2.1790; total 47.5316; home win 0.414154. Final: 16-14. Realized home margin -2; total 30. Margin error +0.1790; total error -17.5316; home-win outcome 0.
- UL Monroe @ South Alabama — frozen home margin +14.8742; total 57.0966; home win 0.805511. Final: 35-52. Realized home margin +17; total 87. Margin error +2.1258; total error +29.9034; home-win outcome 1.
- Texas Tech @ Colorado — frozen home margin -1.7697; total 53.2790; home win 0.410558. Final: 29-7. Realized home margin -22; total 36. Margin error -20.2303; total error -17.2790; home-win outcome 0.
- Washington @ USC — frozen home margin +4.3657; total 54.5806; home win 0.617463. Final: 21-25. Realized home margin +4; total 46. Margin error -0.3657; total error -8.5806; home-win outcome 1.
- Utah State @ Boise State — frozen home margin +15.3268; total 51.1393; home win 0.810986. Final: 18-37. Realized home margin +19; total 55. Margin error +3.6732; total error +3.8607; home-win outcome 1.
- Arkansas State @ Louisiana — frozen home margin +3.7956; total 53.8490; home win 0.605205. Final: 20-23. Realized home margin +3; total 43. Margin error -0.7956; total error -10.8490; home-win outcome 1.
- Fresno State @ Washington State — frozen home margin +1.8704; total 45.2591; home win 0.566948. Final: 26-6. Realized home margin -20; total 32. Margin error -21.8704; total error -13.2591; home-win outcome 0.
- Baylor @ Arizona State — frozen home margin -0.7218; total 53.0693; home win 0.482301. Final: 55-19. Realized home margin -36; total 74. Margin error -35.2782; total error +20.9307; home-win outcome 0.
- Texas State @ San Diego State — frozen home margin +4.6979; total 59.6326; home win 0.651553. Final: 29-31. Realized home margin +2; total 60. Margin error -2.6979; total error +0.3674; home-win outcome 1.
- Cincinnati @ Arizona — frozen home margin +4.3762; total 55.6380; home win 0.627383. Final: 7-34. Realized home margin +27; total 41. Margin error +22.6238; total error -14.6380; home-win outcome 1.
- San José State @ Hawai'i — frozen home margin +1.3578; total 52.9283; home win 0.516507. Final: 20-16. Realized home margin -4; total 36. Margin error -5.3578; total error -16.9283; home-win outcome 0.

Scientific effect: descriptive prospective evaluation only. Champion v1.193 unchanged.


## Week 6 authoritative postgame join — 2026-10-11 07:18 CT

**Cycle:** CFB_MARKET_MONITOR_20261011T120436Z  
**Join rule:** Only genuine pre-event Week 6 FIRST_FROZEN rows joined to authoritative finals. These four rows are appended prospectively; no missing prediction is reconstructed from an outcome. Champion remains unchanged.

| Game | Engine Prediction (Frozen) | Frozen home margin | Frozen total | Frozen home-win probability | Authoritative final | Realized home margin | Realized total | Margin error | Total error | Home outcome | Source |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|
| Old Dominion @ Appalachian State | Appalachian State -14.3 | +14.3 | 50.1 | .823 | Old Dominion 10, Appalachian State 3 | -7 | 13 | -21.3 | -37.1 | 0 | https://appstatesports.com/sports/football |
| Miami (OH) @ Massachusetts | Massachusetts -14.8 | +14.8 | 54.6 | .818 | Miami (OH) 20, Massachusetts 19 | -1 | 39 | -15.8 | -15.6 | 0 | https://umassathletics.com/news/2026/10/10/football-minutemen-comeback-falls-one-point-short-to-miami-oh-20-19 |
| James Madison @ Georgia Southern | James Madison -8.0 | -8.0 | 46.7 | .291 | James Madison 27, Georgia Southern 24 | -3 | 51 | +5.0 | +4.3 | 0 | https://jmusports.com/news/2026/10/11/football-dukes-grind-out-road-win-at-georgia-southern |
| Boise State @ Fresno State | Fresno State -1.6 | +1.6 | 49.6 | .560 | Boise State 38, Fresno State 31 | -7 | 69 | -8.6 | +19.4 | 0 | https://www.reuters.com/sports/top-25-roundup-south-carolina-hands-no-16-florida-second-straight-loss--flm-2026-10-10/ |

**Scientific effect:** Descriptive prospective evaluation only. No automatic Champion mutation, Challenger promotion, S2 acceptance, probability revision, or outcome-informed reconstruction.


## Week 6 full-slate completion join — 2026-10-11 09:02 CT

**Cycle:** CFB_WEEKLY_QA_20261011T135620Z  
**Scope:** 45 previously unscored genuine pre-event Week 6 FIRST_FROZEN rows joined to final results from the CBS Sports FBS Week 6 scoreboard retrieved 2026-10-11. Four established-ticket games were already appended from official/authoritative sources by the 07:04 CT Market Monitor and are not duplicated. Union: 49/49 modeled games; unresolved joins 0. Nebraska remains an explicit unmodeled exclusion outside this denominator.  
**Outcome source:** https://www.cbssports.com/college-football/scoreboard/FBS/2026/regular/6/?layout=compact

| Game | Frozen home margin | Frozen total | Frozen home-win probability | Final (away-home) | Realized home margin | Realized total | Margin error | Total error | Home outcome |
|---|---:|---:|---:|---|---:|---:|---:|---:|---:|
| Southern Miss @ Troy | +6.4 | 51.9 | 0.612 | 34-55 | +21 | 89 | +14.6 | +37.1 | 1 |
| Jacksonville State @ Kennesaw State | +3.6 | 52.1 | 0.579 | 27-26 | -1 | 53 | -4.6 | +0.9 | 0 |
| New Mexico State @ FIU | +3.2 | 52.2 | 0.530 | 3-22 | +19 | 25 | +15.8 | -27.2 | 1 |
| Missouri State @ Western Kentucky | -17.3 | 55.7 | 0.150 | 13-34 | +21 | 47 | +38.3 | -8.7 | 1 |
| South Florida @ UTSA | -3.1 | 54.8 | 0.447 | 24-31 | +7 | 55 | +10.1 | +0.2 | 1 |
| South Alabama @ Arkansas State | +2.3 | 54.8 | 0.613 | 56-49 | -7 | 105 | -9.3 | +50.2 | 0 |
| Florida State @ Louisville | +17.5 | 64.8 | 0.873 | 20-44 | +24 | 64 | +6.5 | -0.8 | 1 |
| Iowa @ Washington | -1.9 | 46.0 | 0.457 | 41-24 | -17 | 65 | -15.1 | +19.0 | 0 |
| Washington State @ Utah State | -1.7 | 44.9 | 0.446 | 16-17 | +1 | 33 | +2.7 | -11.9 | 1 |
| Wyoming @ San José State | +5.1 | 50.1 | 0.602 | 16-13 | -3 | 29 | -8.1 | -21.1 | 0 |
| Iowa State @ BYU | +11.8 | 51.7 | 0.804 | 10-24 | +14 | 34 | +2.2 | -17.7 | 1 |
| Arizona @ West Virginia | +3.4 | 53.8 | 0.564 | 52-31 | -21 | 83 | -24.4 | +29.2 | 0 |
| Texas A&M @ Missouri | +7.7 | 48.5 | 0.643 | 6-27 | +21 | 33 | +13.3 | -15.5 | 1 |
| UCF @ Oklahoma State | +4.3 | 55.1 | 0.600 | 28-42 | +14 | 70 | +9.7 | +14.9 | 1 |
| North Carolina @ Pittsburgh | +8.3 | 46.7 | 0.680 | 21-17 | -4 | 38 | -12.3 | -8.7 | 0 |
| Wake Forest @ NC State | +9.3 | 59.3 | 0.704 | 38-14 | -24 | 52 | -33.3 | -7.3 | 0 |
| Sacramento State @ Bowling Green | -12.7 | 45.8 | 0.200 | 10-38 | +28 | 48 | +40.7 | +2.2 | 1 |
| South Carolina @ Florida | +7.1 | 61.9 | 0.693 | 38-19 | -19 | 57 | -26.1 | -4.9 | 0 |
| Texas vs Oklahoma | +3.4 | 42.8 | 0.519 | 24-27 | +3 | 51 | -0.4 | +8.2 | 1 |
| UCLA @ Oregon | +5.1 | 62.8 | 0.655 | 17-15 | -2 | 32 | -7.1 | -30.8 | 0 |
| Stanford @ Notre Dame | +27.6 | 49.3 | 0.943 | 7-58 | +51 | 65 | +23.4 | +15.7 | 1 |
| Ole Miss @ Vanderbilt | +1.9 | 54.7 | 0.520 | 52-17 | -35 | 69 | -36.9 | +14.3 | 0 |
| Illinois @ Michigan State | -4.4 | 50.9 | 0.359 | 38-37 | -1 | 75 | +3.4 | +24.1 | 0 |
| Houston @ Kansas State | +10.6 | 55.0 | 0.757 | 35-16 | -19 | 51 | -29.6 | -4.0 | 0 |
| Eastern Michigan @ Akron | +11.1 | 50.1 | 0.746 | 25-23 | -2 | 48 | -13.1 | -2.1 | 0 |
| Duke @ Georgia Tech | +0.9 | 47.9 | 0.568 | 25-28 | +3 | 53 | +2.1 | +5.1 | 1 |
| Central Michigan @ Ohio | -1.1 | 48.4 | 0.483 | 14-31 | +17 | 45 | +18.1 | -3.4 | 1 |
| Charlotte @ North Texas | +7.8 | 62.1 | 0.669 | 10-50 | +40 | 60 | +32.2 | -2.1 | 1 |
| Buffalo @ Toledo | +22.1 | 56.1 | 0.900 | 23-8 | -15 | 31 | -37.1 | -25.1 | 0 |
| Kent State @ Western Michigan | +26.7 | 48.3 | 0.939 | 7-38 | +31 | 45 | +4.3 | -3.3 | 1 |
| Rice @ East Carolina | +0.4 | 44.9 | 0.544 | 12-28 | +16 | 40 | +15.6 | -4.9 | 1 |
| Maryland @ Ohio State | +11.4 | 56.4 | 0.759 | 16-45 | +29 | 61 | +17.6 | +4.6 | 1 |
| Tennessee @ Arkansas | -19.0 | 54.7 | 0.144 | 24-17 | -7 | 41 | +12.0 | -13.7 | 0 |
| San Diego State @ Oregon State | +7.7 | 56.9 | 0.678 | 14-66 | +52 | 80 | +44.3 | +23.1 | 1 |
| Nevada @ UTEP | -5.1 | 49.6 | 0.368 | 30-13 | -17 | 43 | -11.9 | -6.6 | 0 |
| North Dakota State @ UNLV | -8.7 | 46.1 | 0.273 | 7-13 | +6 | 20 | +14.7 | -26.1 | 1 |
| LSU @ Kentucky | -2.5 | 55.1 | 0.453 | 34-35 | +1 | 69 | +3.5 | +13.9 | 1 |
| Air Force @ Northern Illinois | -16.1 | 48.4 | 0.180 | 28-7 | -21 | 35 | -4.9 | -13.4 | 0 |
| Syracuse @ Virginia | +10.1 | 50.8 | 0.732 | 25-28 | +3 | 53 | -7.1 | +2.2 | 1 |
| Georgia @ Alabama | -7.0 | 61.7 | 0.329 | 20-17 | -3 | 37 | +4.0 | -24.7 | 0 |
| Louisiana @ Louisiana Tech | +0.1 | 54.5 | 0.497 | 31-32 | +1 | 63 | +0.9 | +8.5 | 1 |
| USC @ Penn State | +11.8 | 55.0 | 0.749 | 31-23 | -8 | 54 | -19.8 | -1.0 | 0 |
| Minnesota @ Purdue | -5.8 | 58.6 | 0.345 | 13-41 | +28 | 54 | +33.8 | -4.6 | 1 |
| Kansas @ Utah | +18.9 | 52.2 | 0.873 | 24-41 | +17 | 65 | -1.9 | +12.8 | 1 |
| Hawai'i @ Arizona State | +14.1 | 53.4 | 0.781 | 12-30 | +18 | 42 | +3.9 | -11.4 | 1 |

**Week 6 full 49-game diagnostic summary (45 rows here + 4 prior rows):** margin MAE 15.13; mean margin error +0.9; total MAE 13.54; mean total error -0.89; straight-up direction 25/49 (51.0%); home-win Brier 0.284. Descriptive one-week evidence only; not a calibration or promotion basis.

**Scientific effect:** NONE. Champion v1.193, FIRST_FROZEN/accepted REFRESH lineage, exclusions, Challenger status, and betting rules remain unchanged. No outcome-informed reconstruction occurred.


## Week 7 Tuesday FIRST_FROZEN outcomes — authoritative finals joined 2026-10-14

**Join boundary:** Authoritative CBS Sports finals were joined only to genuinely pre-event Week 7 FIRST_FROZEN rows. These games had no established production or $20 sandbox execution, so this is model scoring only and not wager settlement. Frozen predictions were not reconstructed or mutated.

| Game | FIRST_FROZEN home margin | FIRST_FROZEN total | FIRST_FROZEN home win p | Authoritative final | Actual home margin | Actual total | Margin error | Total error | SU direction correct |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Delaware @ Middle Tennessee | +1.8 | 50.6 | 0.530 | 30-33 | +3 | 63 | +1.2 | +12.4 | 1 |
| Florida International @ Jacksonville State | +4.5 | 47.7 | 0.614 | 24-27 | +3 | 51 | -1.5 | +3.3 | 1 |

**Source:** CBS Sports Week 7 schedule/odds finals, retrieved 2026-10-14T12:03:33Z; https://www.cbssports.com/college-football/odds/FBS/2026/regular/week-7/  
**Scientific effect:** NONE. Champion v1.193, FIRST_FROZEN/accepted REFRESH lineage, exclusions, Challenger status, and betting rules remain unchanged. No outcome-informed reconstruction occurred.


## Week 7 Wednesday FIRST_FROZEN outcomes — authoritative finals joined 2026-10-15

**Cycle:** CFB_MARKET_MONITOR_20261015T115839Z  
**Join rule:** Authoritative school finals were joined only to genuine pre-event Week 7 FIRST_FROZEN rows. Neither game had an established production or $20 sandbox execution, so this is model scoring only and not wager settlement. Frozen predictions were not reconstructed or mutated.

| Game | FIRST_FROZEN home margin | FIRST_FROZEN total | FIRST_FROZEN home win p | Authoritative final | Actual home margin | Actual total | Margin error | Total error | SU direction correct |
|---|---:|---:|---:|---|---:|---:|---:|---:|---:|
| Kennesaw State @ Missouri State | -0.6 | 52.6 | 0.469 | Kennesaw State 21, Missouri State 24 | +3 | 45 | +3.6 | -7.6 | 0 |
| Western Kentucky @ Sam Houston | +36.5 | 52.7 | 0.972 | Western Kentucky 16, Sam Houston 3 | -13 | 19 | -49.5 | -33.7 | 0 |

**Sources:** Missouri State Athletics, https://missouristatebears.com/news/2026/10/14/football-bears-walk-off-kennesaw-state-in-cusa-home-opener ; Western Kentucky Athletics, https://wkusports.com/news/2026/10/14/football-hilltoppers-claim-16-3-road-win-at-sam-houston  
**Scientific effect:** NONE. Champion v1.193, FIRST_FROZEN/accepted REFRESH lineage, exclusions, Challenger status, and betting rules remain unchanged. No outcome-informed reconstruction occurred.


## Week 7 Thursday FIRST_FROZEN outcomes — authoritative finals joined 2026-10-16

**Cycle:** CFB_MARKET_MONITOR_20261016T115625Z  
**Join rule:** Authoritative school finals were joined only to genuine pre-event Week 7 FIRST_FROZEN rows. East Carolina @ UAB remained a governed FIRST_FROZEN exclusion and was not scored. None of the three Thursday games had an established production or $20 sandbox execution, so this is model scoring only and not wager settlement. Frozen predictions were not reconstructed or mutated.

| Game | FIRST_FROZEN home margin | FIRST_FROZEN total | FIRST_FROZEN home win p | Authoritative final | Actual home margin | Actual total | Margin error | Total error | SU direction correct |
|---|---:|---:|---:|---|---:|---:|---:|---:|---:|
| Georgia Southern @ Old Dominion | -1.2 | 41.1 | 0.476 | Georgia Southern 23, Old Dominion 15 | -8 | 38 | -6.8 | -3.1 | 1 |
| Colorado State @ Texas State | -2.4 | 63.4 | 0.456 | Colorado State 27, Texas State 66 | +39 | 93 | +41.4 | +29.6 | 0 |

**Sources:** Old Dominion Athletics, https://odusports.com/boxscore/14878 ; Colorado State Athletics, https://csurams.com/boxscore.aspx?id=21975  
**Scientific effect:** NONE. Champion v1.193, FIRST_FROZEN/accepted REFRESH lineage, exclusions, Challenger status, and betting rules remain unchanged. No outcome-informed reconstruction occurred.


## Week 7 Friday FIRST_FROZEN outcomes — authoritative finals joined 2026-10-17

**Cycle:** CFB_MARKET_MONITOR_20261017T120424Z  
**Join rule:** Authoritative school finals were joined only to genuine pre-event Week 7 FIRST_FROZEN rows. Appalachian State @ Coastal Carolina remained a governed FIRST_FROZEN exclusion (`home_prior_pbp_missing`) and was not scored. None of the Friday games had an established production or $20 sandbox execution, so this is model scoring only and not wager settlement. Frozen predictions were not reconstructed or mutated.

| Game | FIRST_FROZEN home margin | FIRST_FROZEN total | FIRST_FROZEN home win p | Authoritative final | Actual home margin | Actual total | Margin error | Total error | SU direction correct |
|---|---:|---:|---:|---|---:|---:|---:|---:|---:|
| Memphis @ Tulane | -4.0 | 55.0 | 0.398 | Memphis 17, Tulane 31 | +14 | 48 | +18.0 | -7.0 | 0 |
| Washington @ Purdue | -5.6 | 57.5 | 0.363 | Washington 38, Purdue 26 | -12 | 64 | -6.4 | +6.5 | 1 |

**Excluded final retained without scoring:** Appalachian State 35, Coastal Carolina 32.  
**Sources:** Tulane Athletics, https://tulanegreenwave.com/game-center/23453 ; Washington Athletics, https://gohuskies.com/game-center/25204 ; Appalachian State Athletics, https://appstatesports.com/sports/football/schedule/2026  
**Scientific effect:** NONE. Champion v1.193, FIRST_FROZEN/accepted REFRESH lineage, exclusions, Challenger status, and betting rules remain unchanged. No outcome-informed reconstruction occurred.

## Week 7 Saturday FIRST_FROZEN completion join — 2026-10-18

**Cycle:** `CFB_MARKET_MONITOR_20261018T115603Z`  
**Join rule:** A fresh complete CBS Week 7 board recovered at `2026-10-18T12:03:00Z` supplied final scores for all 62 governed identities. This append contains the 43 previously unscored Saturday rows that had genuine pre-event FIRST_FROZEN predictions. Nine Saturday FIRST_FROZEN exclusions are retained below without scoring. No prediction, exclusion, market decision, recommendation, wager, or execution record was reconstructed from an outcome.  
**Outcome source:** https://www.cbssports.com/college-football/odds/FBS/2026/regular/week-7/

| Game ID | Game | Frozen home margin | Frozen total | Frozen home-win p | Final (away-home) | Actual home margin | Actual total | Margin error | Total error | SU correct |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 401858492 | Nebraska @ Oregon | -1.8 | 59.0 | 0.471 | 14-17 | +3 | 31 | +4.8 | -28.0 | 0 |
| 401864521 | New Mexico @ Hawai'i | -9.8 | 43.5 | 0.268 | 21-10 | -11 | 31 | -1.2 | -12.5 | 1 |
| 401860904 | Fresno State @ San Diego State | -0.3 | 46.4 | 0.515 | 23-26 | +3 | 49 | +3.3 | +2.6 | 0 |
| 401856833 | Utah @ Colorado | -13.9 | 52.0 | 0.180 | 27-24 | -3 | 51 | +10.9 | -1.0 | 1 |
| 401866445 | Ohio @ Sacramento State | +9.1 | 52.4 | 0.691 | 48-7 | -41 | 55 | -50.1 | +2.6 | 0 |
| 401864523 | San José State @ UTEP | -1.5 | 50.8 | 0.447 | 24-11 | -13 | 35 | -11.5 | -15.8 | 1 |
| 401871091 | Louisiana Tech @ UL Monroe | -6.2 | 53.8 | 0.373 | 24-0 | -24 | 24 | -17.8 | -29.8 | 1 |
| 401856722 | Kentucky @ Oklahoma | +10.0 | 48.3 | 0.730 | 21-13 | -8 | 34 | -18.0 | -14.3 | 0 |
| 401856831 | Oklahoma State @ Houston | +8.7 | 57.0 | 0.711 | 32-35 | +3 | 67 | -5.7 | +10.0 | 1 |
| 401858265 | Louisville @ Syracuse | -1.9 | 60.4 | 0.459 | 34-26 | -8 | 60 | -6.1 | -0.4 | 1 |
| 401856809 | Notre Dame @ BYU | +6.0 | 51.1 | 0.658 | 24-28 | +4 | 52 | -2.0 | +0.9 | 1 |
| 401858494 | Wisconsin @ UCLA | +7.3 | 57.4 | 0.665 | 7-17 | +10 | 24 | +2.7 | -33.4 | 1 |
| 401856832 | TCU @ Baylor | +1.5 | 48.5 | 0.518 | 17-6 | -11 | 23 | -12.5 | -25.5 | 0 |
| 401862806 | Kent State @ South Florida | +31.3 | 53.4 | 0.964 | 2-29 | +27 | 31 | -4.3 | -22.4 | 1 |
| 401858263 | Florida State @ Miami | +27.7 | 60.8 | 0.949 | 35-43 | +8 | 78 | -19.7 | +17.2 | 1 |
| 401864520 | Nevada @ North Dakota State | +10.4 | 49.0 | 0.728 | 17-31 | +14 | 48 | +3.6 | -1.0 | 1 |
| 401869934 | Arkansas State @ Southern Miss | +1.7 | 56.4 | 0.559 | 23-13 | -10 | 36 | -11.7 | -20.4 | 0 |
| 401856726 | Arkansas @ Vanderbilt | +15.4 | 50.7 | 0.794 | 31-21 | -10 | 52 | -25.4 | +1.3 | 0 |
| 401860903 | Washington State @ Oregon State | +6.1 | 53.1 | 0.641 | 30-48 | +18 | 78 | +11.9 | +24.9 | 1 |
| 401869966 | Troy @ Louisiana | +4.3 | 48.3 | 0.616 | 6-33 | +27 | 39 | +22.7 | -9.3 | 1 |
| 401862805 | Tulsa @ Rice | -8.6 | 42.5 | 0.299 | 38-17 | -21 | 55 | -12.4 | +12.5 | 1 |
| 401856723 | Alabama @ Tennessee | +10.2 | 56.2 | 0.753 | 10-26 | +16 | 36 | +5.8 | -20.2 | 1 |
| 401864522 | Northern Illinois @ Wyoming | +10.6 | 46.7 | 0.725 | 23-41 | +18 | 64 | +7.4 | +17.3 | 1 |
| 401864524 | UNLV @ Air Force | +17.2 | 45.5 | 0.877 | 31-41 | +10 | 72 | -7.2 | +26.5 | 1 |
| 401856828 | Arizona State @ Texas Tech | +5.6 | 54.8 | 0.664 | 25-53 | +28 | 78 | +22.4 | +23.2 | 1 |
| 401856721 | Missouri @ Ole Miss | +2.0 | 54.6 | 0.580 | 3-31 | +28 | 34 | +26.0 | -20.6 | 1 |
| 401858264 | Georgia Tech @ Virginia Tech | +15.1 | 54.4 | 0.806 | 24-34 | +10 | 58 | -5.1 | +3.6 | 1 |
| 401858490 | Penn State @ Michigan | -3.9 | 42.3 | 0.420 | 18-21 | +3 | 39 | +6.9 | -3.3 | 0 |
| 401866478 | Akron @ Miami (OH) | +3.4 | 55.1 | 0.571 | 14-34 | +20 | 48 | +16.6 | -7.1 | 1 |
| 401856719 | Auburn @ Georgia | +22.5 | 61.7 | 0.915 | 27-24 | -3 | 51 | -25.5 | -10.7 | 0 |
| 401866444 | Toledo @ Eastern Michigan | -10.7 | 55.7 | 0.249 | 34-14 | -20 | 48 | -9.3 | -7.7 | 1 |
| 401858266 | North Carolina @ Duke | +2.5 | 44.5 | 0.539 | 24-20 | -4 | 44 | -6.5 | -0.5 | 0 |
| 401866443 | Western Michigan @ Central Michigan | -3.6 | 40.0 | 0.415 | 21-14 | -7 | 35 | -3.4 | -5.0 | 1 |
| 401856725 | The Citadel @ Texas A&M | +14.3 | 59.6 | 0.852 | 0-41 | +41 | 41 | +26.7 | -18.6 | 1 |
| 401866442 | Massachusetts @ Buffalo | -14.3 | 47.4 | 0.181 | 18-24 | +6 | 42 | +20.3 | -5.4 | 0 |
| 401858267 | Pittsburgh @ Boston College | -6.3 | 47.4 | 0.344 | 21-27 | +6 | 48 | +12.3 | +0.6 | 0 |
| 401866441 | Ball State @ Bowling Green | -2.4 | 51.8 | 0.432 | 32-31 | -1 | 63 | +1.4 | +11.2 | 1 |
| 401856829 | Cincinnati @ West Virginia | +4.0 | 55.7 | 0.617 | 42-45 | +3 | 87 | -1.0 | +31.3 | 1 |
| 401869957 | Georgia State @ James Madison | +17.0 | 55.8 | 0.856 | 22-49 | +27 | 71 | +10.0 | +15.2 | 1 |
| 401856830 | Kansas @ Kansas State | +19.6 | 50.6 | 0.878 | 24-35 | +11 | 59 | -8.6 | +8.4 | 1 |
| 401856720 | Mississippi State @ LSU | -0.9 | 60.3 | 0.470 | 0-31 | +31 | 31 | +31.9 | -29.3 | 0 |
| 401858268 | Virginia @ SMU | -0.1 | 57.0 | 0.515 | 13-23 | +10 | 36 | +10.1 | -21.0 | 0 |
| 401856724 | Florida @ Texas | +0.9 | 58.6 | 0.556 | 27-24 | -3 | 51 | -3.9 | -7.6 | 0 |

**Saturday exclusions retained without scoring:**
- `401858269` Wake Forest @ California — FIRST_FROZEN exclusion `home_prior_points_missing`; final 41-7 retained only as outcome context.
- `401862804` Navy @ UTSA — FIRST_FROZEN exclusion `away_prior_points_missing`; final 34-38 retained only as outcome context.
- `401858262` Elon @ Stanford — FIRST_FROZEN exclusion `away_opening_no_prior`; final 7-34 retained only as outcome context.
- `401862803` Charlotte @ Temple — FIRST_FROZEN exclusion `home_prior_pbp_missing`; final 38-31 retained only as outcome context.
- `401858489` Rutgers @ Maryland — FIRST_FROZEN exclusion `away_prior_points_missing`; final 37-30 retained only as outcome context.
- `401858491` Northwestern @ Michigan State — FIRST_FROZEN exclusion `away_prior_points_missing`; final 24-21 retained only as outcome context.
- `401862802` Florida Atlantic @ Army — FIRST_FROZEN exclusion `home_prior_pbp_missing`; final 24-56 retained only as outcome context.
- `401858261` Charleston Southern @ Clemson — FIRST_FROZEN exclusion `home_prior_points_missing`; final 0-37 retained only as outcome context.
- `401858488` Ohio State @ Indiana — FIRST_FROZEN exclusion `home_prior_points_missing`; final 19-15 retained only as outcome context.

**Saturday modeled summary:** 43/43 matched; unresolved 0; SU direction 28/43 (65.1%); margin MAE 12.25; total MAE 13.49.
**Complete Week 7 modeled summary:** 51/51 matched; unresolved 0; SU direction 31/51 (60.8%); margin MAE 12.89; total MAE 13.40; home-win Brier 0.224.

No established Week 7 production or $20 sandbox execution was present in the canonical execution ledger at this scoring boundary, so no wager settlement was created. Descriptive outcome scoring does not mutate Champion v1.193, FIRST_FROZEN, accepted REFRESH, Challenger, TIME-HIDDEN, market, decision, or execution state.



## Week 8 Tuesday FIRST_FROZEN outcomes — authoritative finals joined 2026-10-21

**Cycle:** `CFB_MARKET_MONITOR_20261021T120721Z`  
**Join rule:** The fresh CBS Week 8 response recovered at `2026-10-21T12:07:21Z` supplied final scores for the three Tuesday identities. Each row below joins only to the accepted September 26 original FIRST_FROZEN lineage recovered in `CFB_WEEK8_ORIGINAL_ANCESTRY_RECOVERY_20261020.json`. No market decision, recommendation, wager, execution, or prediction was reconstructed from an outcome.  
**Outcome source:** https://www.cbssports.com/college-football/odds/FBS/2026/regular/week-8/

| Game ID | Game | Frozen home margin | Frozen total | Frozen home-win p | Final (away-home) | Actual home margin | Actual total | Margin error | Total error | SU correct |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 401871069 | Missouri State @ Delaware | +11.1 | 55.3 | 0.768 | 38-61 | +23 | 99 | +11.9 | +43.7 | 1 |
| 401871055 | Middle Tennessee @ Florida International | +3.2 | 47.3 | 0.507 | 26-23 | -3 | 49 | -6.2 | +1.7 | 0 |
| 401871092 | South Alabama @ Marshall | -4.4 | 50.2 | 0.420 | 13-20 | +7 | 33 | +11.4 | -17.2 | 0 |

**Tuesday modeled summary:** 3/3 matched; unresolved 0; SU direction 1/3 (33.3%); margin MAE 9.83; total MAE 20.87.

No established Week 8 production or $20 sandbox execution was present at this scoring boundary, so no wager settlement was created. Descriptive outcome scoring does not mutate Champion, FIRST_FROZEN, accepted REFRESH, Challenger, TIME-HIDDEN, market, decision, or execution state.
