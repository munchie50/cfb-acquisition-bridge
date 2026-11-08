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


## Week 8 Wednesday FIRST_FROZEN outcome — authoritative final joined 2026-10-22

**Cycle:** `CFB_MARKET_MONITOR_20261022T120427Z`  
**Join rule:** Sam Houston Athletics' final was joined only to the accepted September 26 original FIRST_FROZEN row recovered in `CFB_WEEK8_ORIGINAL_ANCESTRY_RECOVERY_20261020.json`. No market decision, recommendation, wager, execution, or prediction was reconstructed from the outcome.  
**Outcome source:** https://gobearkats.com/game-center/15542

| Game ID | Game | Frozen home margin | Frozen total | Frozen home-win p | Final (away-home) | Actual home margin | Actual total | Margin error | Total error | SU correct |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 401871070 | New Mexico State @ Sam Houston | +13.8 | 53.8 | 0.786 | 30-24 | -6 | 54 | -19.8 | +0.2 | 0 |

No established Week 8 production or $20 sandbox execution was present at this scoring boundary, so no wager settlement was created. Descriptive outcome scoring does not mutate Champion, FIRST_FROZEN, accepted REFRESH, Challenger, TIME-HIDDEN, market, decision, or execution state.


## Week 8 Thursday FIRST_FROZEN outcomes — authoritative finals joined 2026-10-23

**Cycle:** `CFB_MARKET_MONITOR_20261023T115519Z`  
**Join rule:** Official school final-result pages were joined only to accepted September 26 original FIRST_FROZEN lineage recovered in `CFB_WEEK8_ORIGINAL_ANCESTRY_RECOVERY_20261020.json`. Liberty @ Kennesaw State remained the original `away_prior_pbp_missing` exclusion and was not scored. No market decision, recommendation, wager, execution, or prediction was reconstructed from an outcome.  
**Outcome sources:** Memphis Athletics, https://gotigersgo.com/game-center/20061 ; Kennesaw State Athletics, https://ksuowls.com/news/2026/10/22/football-owls-fall-to-flames.aspx ; Appalachian State Athletics, https://appstatesports.com/boxscore.aspx?id=9919

| Game ID | Game | Frozen home margin | Frozen total | Frozen home-win p | Final (away-home) | Actual home margin | Actual total | Margin error | Total error | SU correct |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 401862807 | East Carolina @ Memphis | +15.6 | 55.5 | 0.832 | 34-41 | +7 | 75 | -8.6 | +19.5 | 1 |
| 401869845 | James Madison @ Appalachian State | -3.6 | 52.5 | 0.434 | 31-34 | +3 | 65 | +6.6 | +12.5 | 0 |

**Thursday modeled summary:** 2/2 eligible rows matched; unresolved eligible joins 0; SU direction 1/2 (50.0%); margin MAE 7.60; total MAE 16.00.  
**Excluded final retained without scoring:** `401871056` Liberty 34, Kennesaw State 6 — original FIRST_FROZEN exclusion `away_prior_pbp_missing`.

No established Week 8 production or $20 sandbox execution was present at this scoring boundary, so no wager settlement was created. Descriptive outcome scoring does not mutate Champion, FIRST_FROZEN, accepted REFRESH, Challenger, TIME-HIDDEN, market, decision, or execution state.


## October23 QA — Week7 summary reconciliation, original rows preserved

Run CFB_BALANCED_EFFECTIVENESS_QA_20261023T163207Z; actual recording clock 2026-10-23T16:44:41.030630+00:00. Independent replay of immutable prior scorecard d210d8c51106ef393a23a4fb69c6fcdb219e3f16 and all51 unique Week7 modeled rows found that the existing SU-correct flags sum32, and an independent comparison of each saved frozen margin sign with its actual margin also gives32. Daily slices2+0+1+1+28=32. Therefore this append prospectively corrects the earlier complete-week summary31/51(60.8%) to32/51(62.7%) for MARGIN-DIRECTION accuracy only. No game row, frozen number, exclusion, final result or historical review is rewritten.

Win-probability threshold classification is a different34/51 diagnostic from rounded displays; it is not margin direction or additional correct games. Existing rounded absolute-error rows yield marginMAE12.843137 and totalMAE13.398039. The latter supports reported13.40; published marginMAE12.89 is not independently reconciled to exact original archive precision in this audit, so it remains OPEN/EXACT_RECOMPUTATION_PENDING rather than silently replaced by a rounded-row aggregate. Home Brier from rounded probabilities is0.224284, consistent with reported0.224.

Reproducible immutable-byte evidence: evidence/scheduler_qa/cfb_balanced_effectiveness_replay_20261023.py and evidence/scheduler_qa/CFB_BALANCED_EFFECTIVENESS_QA_20261023T163207Z_RESULTS.json. The original October18 review remains historical/current weekly learning output with this later explicit metric supplement; no weekly-selector replacement, model/routine/scientific promotion or fresh outcome acquisition.


## October23 exact-original-source reconciliation — prior32/51 correction WITHDRAWN

Run CFB_BALANCED_EFFECTIVENESS_QA_20261023T163207Z; actual recording clock 2026-10-23T16:55:21.327894+00:00. This append supersedes the preceding October23 summary reconciliation's32/51 claim. The original complete-week31/51(60.8%) is CORRECT. The prior32/51 append is preserved as a preliminary QA error, not current scoring authority.

Authenticated original artifact10897612260, SHA256772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf, independently joined51/51 modeled Week7 original predictions to the existing saved final results. Exact metrics: margin-direction31/51; separate probability-classifier34/51; marginMAE12.890606189070546;totalMAE13.403172664438008;home-winBrier0.22428589606493665. This corroborates the original rounded31/51,12.89,13.40,0.224 and closes the exact-MAE reconciliation debt.

Derived-row correction, Georgia Southern @ Old Dominion /401869950: original frozen home margin+1.171893195494452 (display+1.2),total41.14884060164428,home-win probability0.47575563478041893. Existing final away23/home15 gives home margin-8,total38,exact margin error-9.171893195494452,total error-3.148840601644281,margin-direction flag0. The historical daily row's-1.2 margin/-6.8 error/flag1 is a derived sign/flag error and is superseded by this note; original row/forecast/final remain unmodified. The probability classifier favors the away team and is independently correct, so Thursday margin-direction is0/2 while probability classification is a different measure. Sum corrected daily margin flags2+0+0+1+28=31.

Full exact51-row evidence `evidence/scheduler_qa/CFB_WEEK7_EXACT_METRIC_RECONCILIATION_20261023.json` and read-only replay `evidence/scheduler_qa/cfb_week7_exact_metric_reconciliation_20261023.py`. Changed archive rejected; no REFRESH substitution, output-dependent prediction choice, fresh final acquisition, model/routine/promotion or money mutation. Original source authority outranks the inconsistent derived display and this QA's preliminary mistaken32/51 correction. Exact writer sign-reversal cause UNKNOWN; natural scoring-source fidelity remains demonstration pending.

## Week 8 Friday FIRST_FROZEN outcomes — authoritative finals joined 2026-10-24

**Cycle:** `CFB_MARKET_MONITOR_20261024T120126Z`

**Join rule:** The fresh complete CBS Week 8 response recovered by `2026-10-24T12:04:02Z` supplied final scores for all five Friday identities. Each eligible row below joins only to the accepted September 26 original FIRST_FROZEN lineage recovered in `CFB_WEEK8_ORIGINAL_ANCESTRY_RECOVERY_20261020.json`. Army @ Tulsa remained the original `away_prior_pbp_missing` exclusion and was not scored. No prediction, decision, recommendation, market observation or execution was reconstructed from an outcome.

**Outcome source:** https://www.cbssports.com/college-football/odds/FBS/2026/regular/week-8/

| Game ID | Game | Frozen home margin | Frozen total | Frozen home-win p | Final (away-home) | Actual home margin | Actual total | Margin error | Total error | SU correct |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 401858271 | Duke @ Virginia | +9.3 | 46.8 | 0.745 | 19-16 | -3 | 35 | -12.3 | -11.8 | 0 |
| 401861965 | Massachusetts @ Connecticut | +3.2 | 52.3 | 0.587 | 16-35 | +19 | 51 | +15.8 | -1.3 | 1 |
| 401864525 | Air Force @ Wyoming | -8.1 | 46.0 | 0.343 | 14-28 | +14 | 42 | +22.1 | -4.0 | 0 |
| 401858272 | NC State @ Stanford | -9.0 | 54.3 | 0.271 | 28-31 | +3 | 59 | +12.0 | +4.7 | 0 |

**Friday modeled summary:** `4/4` eligible rows matched; unresolved eligible joins `0`; SU direction `1/4 (25.0%)`; margin MAE `15.55`; total MAE `5.45`.

**Excluded final retained without scoring:** `401862808` Army 38, Tulsa 35 — original FIRST_FROZEN exclusion `away_prior_pbp_missing`.

The separate execution ledger grades two established Friday tickets from the same finals. That downstream wager evidence does not alter Champion v1.193, FIRST_FROZEN, accepted REFRESH, Challenger, TIME-HIDDEN, market or decision state. No outcome-informed reconstruction occurred.

## Week 8 Saturday FIRST_FROZEN outcomes — authoritative finals joined 2026-10-25

**Cycle:** `CFB_MARKET_MONITOR_20261025T120550Z`  
**Join rule:** The fresh complete CBS Week 8 response recovered by `2026-10-25T12:08:00Z` supplied final scores for all 44 Saturday identities. Each eligible row below joins only to the accepted September 26 original FIRST_FROZEN lineage in `CFB_WEEK8_ORIGINAL_ANCESTRY_RECOVERY_20261020.json`. Five original exclusions remain unscored. No prediction, market decision, recommendation, or execution was reconstructed from an outcome.  
**Outcome source:** `evidence/operational/CFB_CBS_WEEK8_RESULTS_CAPTURE_20261025T120800Z.md` / Git blob `2aa53f5793bb511373eba9bbbf6e6249d3984836` / https://www.cbssports.com/college-football/odds/FBS/2026/regular/week-8/

| Game ID | Game | Frozen home margin | Frozen total | Frozen home-win p | Final (away-home) | Actual home margin | Actual total | Margin error | Total error | SU correct |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 401856837 | Houston @ Utah | +9.7 | 55.6 | 0.743 | 13-21 | +8 | 34 | -1.7 | -21.6 | 1 |
| 401864527 | North Dakota State @ New Mexico | +6.5 | 41.5 | 0.660 | 16-21 | +5 | 37 | -1.5 | -4.5 | 1 |
| 401862811 | UTSA @ Tulane | -1.0 | 50.4 | 0.425 | 42-19 | -23 | 61 | -22.0 | +10.6 | 1 |
| 401856838 | Iowa State @ Arizona | +5.2 | 48.5 | 0.647 | 3-39 | +36 | 42 | +30.8 | -6.5 | 1 |
| 401858500 | USC @ Wisconsin | +0.3 | 55.6 | 0.508 | 7-24 | +17 | 31 | +16.7 | -24.6 | 1 |
| 401860906 | Utah State @ Texas State | +5.9 | 55.8 | 0.624 | 17-20 | +3 | 37 | -2.9 | -18.8 | 1 |
| 401856732 | Ole Miss @ Texas | +7.9 | 53.1 | 0.677 | 27-34 | +7 | 61 | -0.9 | +7.9 | 1 |
| 401858275 | Syracuse @ North Carolina | +6.7 | 47.6 | 0.657 | 31-30 | -1 | 61 | -7.7 | +13.4 | 0 |
| 401856729 | Vanderbilt @ Kentucky | +3.7 | 52.3 | 0.581 | 17-34 | +17 | 51 | +13.3 | -1.3 | 1 |
| 401856836 | Colorado @ Oklahoma State | +12.5 | 52.9 | 0.769 | 24-57 | +33 | 81 | +20.5 | +28.1 | 1 |
| 401869935 | Georgia State @ Arkansas State | -3.5 | 57.8 | 0.439 | 32-38 | +6 | 70 | +9.5 | +12.2 | 0 |
| 401860905 | San Diego State @ Colorado State | +7.6 | 57.1 | 0.691 | 49-56 | +7 | 105 | -0.6 | +47.9 | 1 |
| 401860907 | Boise State @ Washington State | -0.4 | 47.4 | 0.516 | 31-10 | -21 | 41 | -20.6 | -6.4 | 1 |
| 401864528 | San José State @ Nevada | +7.8 | 51.6 | 0.683 | 13-28 | +15 | 41 | +7.2 | -10.6 | 1 |
| 401869967 | Louisiana @ Southern Miss | +1.0 | 55.5 | 0.545 | 31-35 | +4 | 66 | +3.0 | +10.5 | 1 |
| 401871093 | Old Dominion @ Louisiana Tech | +2.4 | 48.8 | 0.563 | 0-26 | +26 | 26 | +23.6 | -22.8 | 1 |
| 401871094 | UL Monroe @ Troy | +17.0 | 51.3 | 0.817 | 21-14 | -7 | 35 | -24.0 | -16.3 | 0 |
| 401866449 | Eastern Michigan @ Ohio | +4.1 | 52.9 | 0.579 | 20-24 | +4 | 44 | -0.1 | -8.9 | 1 |
| 401856839 | Kansas State @ Arizona State | -9.3 | 53.9 | 0.275 | 17-28 | +11 | 45 | +20.3 | -8.9 | 0 |
| 401856731 | Tennessee @ South Carolina | +3.8 | 57.6 | 0.602 | 24-27 | +3 | 51 | -0.8 | -6.6 | 1 |
| 401858499 | Michigan State @ UCLA | +11.2 | 51.5 | 0.751 | 10-28 | +18 | 38 | +6.8 | -13.5 | 1 |
| 401864526 | Hawai'i @ Northern Illinois | -3.6 | 48.6 | 0.371 | 56-21 | -35 | 77 | -31.4 | +28.4 | 1 |
| 401856730 | Oklahoma @ Mississippi State | +9.4 | 50.2 | 0.712 | 23-15 | -8 | 38 | -17.4 | -12.2 | 0 |
| 401858497 | Iowa @ Minnesota | -3.3 | 45.8 | 0.416 | 10-13 | +3 | 23 | +6.3 | -22.8 | 0 |
| 401856727 | Texas A&M @ Alabama | +8.7 | 51.1 | 0.672 | 20-31 | +11 | 51 | +2.3 | -0.1 | 1 |
| 401856835 | BYU @ UCF | -1.5 | 57.5 | 0.463 | 31-39 | +8 | 70 | +9.5 | +12.5 | 0 |
| 401866448 | Bowling Green @ Buffalo | +10.8 | 48.5 | 0.736 | 24-31 | +7 | 55 | -3.8 | +6.5 | 1 |
| 401866447 | Sacramento State @ Ball State | -7.1 | 49.6 | 0.312 | 17-34 | +17 | 51 | +24.1 | +1.4 | 0 |
| 401858273 | Boston College @ Georgia Tech | +6.5 | 50.1 | 0.663 | 49-27 | -22 | 76 | -28.5 | +25.9 | 0 |
| 401858495 | Oregon @ Illinois | +4.5 | 59.1 | 0.660 | 10-21 | +11 | 31 | +6.5 | -28.1 | 1 |
| 401856834 | Baylor @ Kansas | +0.0 | 48.5 | 0.487 | 24-25 | +1 | 49 | +1.0 | +0.5 | 0 |
| 401866446 | Akron @ Kent State | -15.1 | 49.5 | 0.157 | 20-35 | +15 | 55 | +30.1 | +5.5 | 0 |
| 401866476 | Miami (OH) @ Central Michigan | +1.3 | 47.7 | 0.525 | 28-27 | -1 | 55 | -2.3 | +7.3 | 0 |
| 401858274 | Pittsburgh @ Miami | +15.1 | 53.0 | 0.830 | 23-52 | +29 | 75 | +13.9 | +22.0 | 1 |
| 401866450 | Western Michigan @ Toledo | +7.9 | 53.9 | 0.691 | 38-45 | +7 | 83 | -0.9 | +29.1 | 1 |
| 401856840 | Texas Tech @ Cincinnati | +9.4 | 55.3 | 0.719 | 24-37 | +13 | 61 | +3.6 | +5.7 | 1 |
| 401862809 | Rice @ Florida Atlantic | -0.5 | 49.3 | 0.529 | 49-51 | +2 | 100 | +2.5 | +50.7 | 0 |
| 401856728 | LSU @ Auburn | -0.9 | 56.2 | 0.484 | 38-17 | -21 | 55 | -20.1 | -1.2 | 1 |
| 401856841 | West Virginia @ TCU | +6.2 | 53.0 | 0.713 | 24-20 | -4 | 44 | -10.2 | -9.0 | 0 |

**Saturday modeled summary:** `39/39` eligible rows matched; unresolved eligible joins `0`; SU direction `25/39 (64.1%)`; margin MAE `11.51`; total MAE `14.64`.

**Saturday exclusions retained without scoring:**
- `401858276` Virginia Tech 20, Clemson 16 — original `FIRST_FROZEN EXCLUDED — home_prior_points_missing`.
- `401862810` North Texas 49, Navy 39 — original `FIRST_FROZEN EXCLUDED — home_prior_points_missing`.
- `401858496` Indiana 13, Michigan 6 — original `FIRST_FROZEN EXCLUDED — away_prior_points_missing`.
- `401858498` Rutgers 14, Northwestern 42 — original `FIRST_FROZEN EXCLUDED — away_prior_points_missing|home_prior_points_missing`.
- `401858270` California 20, SMU 59 — original `FIRST_FROZEN EXCLUDED — away_prior_points_missing`.

**Complete Week 8 modeled summary:** `49/49` predictions matched; `7/7` original exclusions retained; unresolved eligible joins `0`. Frozen predictions remain unchanged. This descriptive scoring append is downstream outcome evidence only. The separate execution ledger grades established tickets; neither result surface mutates Champion, FIRST_FROZEN, accepted REFRESH, Challenger, TIME-HIDDEN, market, or decision state.



## Week 9 Tuesday FIRST_FROZEN outcomes — authoritative finals joined 2026-10-28

**Cycle:** `CFB_MARKET_MONITOR_20261028T175841Z`  
**Join rule:** Official athletics final reports were joined only to the accepted September 26 Week 9 FIRST_FROZEN lineage in `CFB_WEEK9_ORIGINAL_ANCESTRY_RECOVERY_20261025.json`. No prediction, market decision, recommendation or execution was reconstructed from an outcome.  
**Outcome evidence:** `evidence/operational/CFB_WEEK9_TUESDAY_RESULTS_CAPTURE_20261028T180300Z.md` / Git blob `1f6d0ca4bab568db83582f272de2905b910b43cb`.

| Game ID | Game | Frozen home margin | Frozen total | Frozen home-win p | Final (away-home) | Actual home margin | Actual total | Margin error | Total error | SU correct |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 401871071 | Delaware @ Western Kentucky | -24.6 | 51.6 | 0.067 | 35-21 | -14 | 56 | +10.6 | +4.4 | 1 |
| 401871072 | Sam Houston @ Missouri State | -10.1 | 50.4 | 0.253 | 3-24 | +21 | 27 | +31.1 | -23.4 | 0 |

**Tuesday modeled summary:** `2/2` eligible rows matched; unresolved eligible joins `0`; SU direction `1/2 (50.0%)`; margin MAE `20.83`; total MAE `13.89`.

No Week 9 established wager existed for either game, so the execution ledger has no settlement entry. This descriptive scoring append is downstream outcome evidence only and does not alter Champion, FIRST_FROZEN, accepted REFRESH, Challenger, TIME-HIDDEN, market or decision state.


## Week 9 remaining 15 official final results — independent Sunday verification 2026-11-01

**Run:** CFB_WEEKLY_QA_MANUAL_20261101T174443981Z. **Source evidence:** `evidence/operational/CFB_WEEK9_OFFICIAL_PENDING15_FINALS_VERIFICATION_20261101.json` / Git blob `f59aa77a585853cbf4e2a6a2e8e1721c9da75c70`. Exact game-ID, home/away, original cutoff, original prediction strings and exclusion checks passed against accepted original artifact 10897612260 / `CFB_WEEK9_ORIGINAL_ANCESTRY_RECOVERY_20261025.json`. The 15 were PENDING in October31 R79; each final is independently supported by a dated official athletics postgame report or official team score page, not inferred from ESPN. Retrieval/verification on 2026-11-01; exact per-source fetch clock not supplied. This appends only outcomes, never changes frozen predictions or earlier Tuesday rows.

| Game ID | Game (away @ home) | Frozen home margin | Frozen total | Frozen home p | Final away-home | Actual home margin | Actual total | Margin error | Total error | SU correct | Official source |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|
| 401856733 | Missouri @ Arkansas | -13.1447 | 48.4571 | 0.2203 | 34-10 | -24 | 44 | -10.8553 | -4.4571 | 1 | [official](https://arkansasrazorbacks.com/hogs-fall-to-tigers-in-battle-line-rivalry/) |
| 401856736 | South Carolina @ Oklahoma | 1.9976 | 46.0376 | 0.5441 | 42-25 | -17 | 67 | -18.9976 | 20.9624 | 0 | [official](https://soonersports.com/news/2026/10/31/football-sooners-fall-to-south-carolina) |
| 401856737 | Mississippi State @ Texas | -0.1793 | 55.7939 | 0.5259 | 3-31 | 28 | 34 | 28.1793 | -21.7939 | 0 | [official](https://texaslonghorns.com/news/2026/10/31/no-11-11-football-downs-mississippi-state-31-3) |
| 401856847 | Oklahoma State @ Iowa State | 5.8382 | 47.0539 | 0.6443 | 49-51 | 2 | 100 | -3.8382 | 52.9461 | 1 | [official](https://cyclones.com/sports/football/stats/2026/-24-oklahoma-state/boxscore/18599) |
| 401858280 | Clemson @ Florida State | EXCLUDED | EXCLUDED | EXCLUDED | 36-24 | -12 | 60 | EXCLUDED | EXCLUDED | EXCLUDED | [official](https://seminoles.com/news/2026/10/31/football-seminoles-fall-to-clemson) |
| 401858281 | Georgia Tech @ Pittsburgh | 12.3024 | 49.2962 | 0.7536 | 11-34 | 23 | 45 | 10.6976 | -4.2962 | 1 | [official](https://ramblinwreck.com/news/2026/11/1/fb-recap-pitt-26) |
| 401858282 | Miami @ North Carolina | -8.0364 | 52.1259 | 0.3110 | 38-35 | -3 | 73 | 5.0364 | 20.8741 | 1 | [official](https://goheels.com/news/2026/10/31/football-fb-recap-vs-miami) |
| 401858504 | Washington @ Nebraska | 12.6855 | 50.6162 | 0.7723 | 17-10 | -7 | 27 | -19.6855 | -23.6162 | 0 | [official](https://huskers.com/sports/football) |
| 401858509 | Ohio State @ USC | -3.5107 | 58.1387 | 0.4104 | 18-30 | 12 | 48 | 15.5107 | -10.1387 | 0 | [official](https://usctrojans.com/news/2026/10/31/usc-trojans-football-game-recap-associated-press-ap-ohio-state-buckeyes-lincoln-riley-trent-mosley-mark-bowman) |
| 401860924 | Oregon State @ Fresno State | 4.2658 | 53.2736 | 0.5758 | 22-38 | 16 | 60 | 11.7342 | 6.7264 | 1 | [official](https://gobulldogs.com/news/2026/10/31/football-bulldogs-spook-beavers-in-halloween-night-win) |
| 401862814 | Army @ Memphis | EXCLUDED | EXCLUDED | EXCLUDED | 22-49 | 27 | 71 | EXCLUDED | EXCLUDED | EXCLUDED | [official](https://gotigersgo.com/news/2026/10/31/football-tigers-offensive-dominates-in-49-22-win-over-army) |
| 401869846 | App State @ Georgia Southern | -1.2165 | 47.7357 | 0.4324 | 3-19 | 16 | 22 | 17.2165 | -25.7357 | 0 | [official](https://gseagles.com/news/2026/10/31/football-eagles-run-streak-against-app-to-four-in-19-3-win) |
| 401860909 | Washington State @ San Diego State | 2.8554 | 45.0550 | 0.5698 | 20-26 | 6 | 46 | 3.1446 | 0.9450 | 1 | [official](https://goaztecs.com/news/2026/10/31/aztecs-hold-off-washington-state-for-halloween-victory) |
| 401860908 | Texas State @ Boise State | 11.1863 | 62.0285 | 0.7837 | 45-46 | 1 | 91 | -10.1863 | 28.9715 | 1 | [official](https://broncosports.com/news/2026/11/1/football-no-20-22-broncos-prevail-in-after-dark-thriller) |
| 401864530 | Northern Illinois @ UNLV | 9.1817 | 46.2942 | 0.6523 | 24-31 | 7 | 55 | -2.1817 | 8.7058 | 1 | [official](https://unlvrebels.com/news/2026/11/1/rebel-football-scares-up-halloween-win-over-niu) |

**New official modeled rows:** 13/15; 2 original exclusions preserved. New subset SU direction 8/13, margin MAE 12.097225, total MAE 17.705327, home-win Brier 0.204016. These are subset diagnostics, not complete 45-game accepted metrics.

**Official verification frontier:** 2 pre-existing official Tuesday rows + 15 new independently verified official rows = **17/56 officially qualified final scores** (15 modeled, 2 excluded). October31 R79 additionally contained 39 source-observed ESPN finals **not yet independently official-verified**; do not mislabel those as official, absent or pending live games. All 56 original identities have either an official result or a saved ESPN source-observed result after this capture, but **39 still require official independent corroboration and canonical append** before Week9 complete official acceptance. No user wager settlement, money movement, Champion promotion, current market decision or Hot Sheet is inferred.


## Week 9 remaining 39 ESPN-observed finals independently corroborated by official athletics — 2026-11-01

**Run:** CFB_WEEKLY_QA_MANUAL_20261101T174443981Z. **Official-source verification artifact:** `evidence/operational/CFB_WEEK9_OFFICIAL_39_ESPN_FINALS_VERIFICATION_20261101.json` / Git blob `4aa121e3e475a3c6ef5bbb90ac1aea3090c3e1e3`. Every one of the 39 R79 ESPN-observed finals was independently corroborated against its school's official final recap, box score or completed schedule, exact game ID/home-away/original prediction strings reconciled to accepted original artifact 10897612260. This append is independent of ESPN source-only acceptance and preserves all prior scorecard bytes. Date of independent verification 2026-11-01; per-page retrieval clock unavailable.

| Game ID | Game (away @ home) | Frozen home margin | Frozen total | Frozen home p | Final away-home | Actual home margin | Actual total | Margin error | Total error | SU correct | Official source |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|
| 401871058 | Kennesaw State @ Middle Tennessee | 5.7664 | 49.3580 | 0.6241 | 44-28 | -16 | 72 | -21.7664 | 22.6420 | 0 | [official](https://goblueraiders.com/news/2026/10/28/football-blue-raiders-drop-weeknight-finale-to-kennesaw) |
| 401871057 | Jacksonville State @ New Mexico State | 3.2242 | 53.3686 | 0.5579 | 24-0 | -24 | 24 | -27.2242 | -29.3686 | 0 | [official](https://nmstatesports.com/news/2026/10/28/football-aggies-drop-home-contest-to-jax-state.aspx) |
| 401862812 | Florida Atlantic @ North Texas | 5.3621 | 58.3416 | 0.6127 | 41-48 | 7 | 89 | 1.6379 | 30.6584 | 1 | [official](https://meangreensports.com/news/2026/10/29/football-mean-green-move-to-4-0-in-american-play) |
| 401869963 | Troy @ James Madison | 22.5924 | 48.2915 | 0.9131 | 24-21 | -3 | 45 | -25.5924 | -3.2915 | 0 | [official](https://troytrojans.com/news/2026/10/30/football-troy-storms-back-to-stun-james-madison-in-overtime) |
| 401862813 | Tulane @ Charlotte | -1.9023 | 51.0209 | 0.4673 | 38-31 | -7 | 69 | -5.0977 | 17.9791 | 1 | [official](https://tulanegreenwave.com/news/2026/10/31/football-earns-comeback-38-31-overtime-road-victory-over-charlotte) |
| 401856844 | Baylor @ UCF | 4.5400 | 51.5107 | 0.6122 | 41-9 | -32 | 50 | -36.5400 | -1.5107 | 0 | [official](https://d1nnrx9kca53zl.cloudfront.net/news/2026/10/30/football-recap-at-ucf) |
| 401866451 | Kent State @ Sacramento State | 19.3775 | 49.0823 | 0.8695 | 10-31 | 21 | 41 | 1.6225 | -8.0823 | 1 | [official](https://hornetsports.com/news/2026/10/31/football-football-claims-first-mac-win-with-31-10-victory-over-kent-state.aspx) |
| 401856735 | Auburn @ Ole Miss | 4.3194 | 59.1303 | 0.6322 | 15-45 | 30 | 60 | 25.6806 | 0.8697 | 1 | [official](https://olemisssports.com/news/2026/10/31/football-bounces-back-to-beat-auburn) |
| 401856842 | Arizona @ Texas Tech | -0.7813 | 51.6129 | 0.4906 | 26-34 | 8 | 60 | 8.7813 | 8.3871 | 0 | [official](https://texastech.com/news/2026/10/31/football-no-13-tech-completes-second-half-comeback-over-no-22-arizona-34-26) |
| 401856843 | Arizona State @ BYU | 16.1875 | 56.8364 | 0.8511 | 20-27 | 7 | 47 | -9.1875 | -9.8364 | 1 | [official](https://byucougars.com/news/2026/10/31/byu-vs-asu-103126) |
| 401856845 | Kansas @ TCU | 10.6188 | 49.2196 | 0.7411 | 16-22 | 6 | 38 | -4.6188 | -11.2196 | 1 | [official](https://gofrogs.com/news/2026/11/1/football-craig-rushes-for-game-winning-score-tcu-takes-down-kansas) |
| 401856846 | Kansas State @ Colorado | -14.5998 | 51.1529 | 0.1640 | 24-27 | 3 | 51 | 17.5998 | -0.1529 | 0 | [official](https://www.kstatesports.com/sports/football/schedule) |
| 401856848 | Utah @ Cincinnati | -2.6780 | 54.3554 | 0.4484 | 49-25 | -24 | 74 | -21.3220 | 19.6446 | 1 | [official](https://utahutes.com/news/2026/10/31/football-no-6-utah-blows-past-cincinnati-improves-to-8-0) |
| 401858277 | California @ NC State | EXCLUDED | EXCLUDED | EXCLUDED | 10-31 | 21 | 41 | EXCLUDED | EXCLUDED | EXCLUDED | [official](https://calbears.com/news/2026/10/31/football-bears-fall-to-wolfpack-31-10) |
| 401858278 | SMU @ Syracuse | 0.7535 | 55.7968 | 0.4896 | 27-30 | 3 | 57 | 2.2465 | 1.2032 | 1 | [official](https://cuse.com/news/2026/10/31/football-cuse-rallies-past-19-smu-in-fourth) |
| 401858279 | Boston College @ Duke | 9.9243 | 45.8323 | 0.7094 | 2-47 | 45 | 49 | 35.0757 | 3.1677 | 1 | [official](https://goduke.com/news/2026/10/31/football-sheppard-sets-single-game-record-duke-earns-bowl-eligibility-in-47-2-victory) |
| 401858283 | Stanford @ Louisville | 23.4558 | 60.2403 | 0.9155 | 24-52 | 28 | 76 | 4.5442 | 15.7597 | 1 | [official](https://gocards.com/news/2026/10/31/football-cardinals-roll-in-second-half-past-stanford-52-24) |
| 401858284 | Virginia @ Wake Forest | -5.6903 | 54.5134 | 0.3802 | 7-51 | 44 | 58 | 49.6903 | 3.4866 | 0 | [official](https://godeacs.com/news/2026/10/31/football-no-14-wake-forest-earns-fifth-straight-victory-routs-virginia-51-7) |
| 401858501 | Minnesota @ Indiana | EXCLUDED | EXCLUDED | EXCLUDED | 16-23 | 7 | 39 | EXCLUDED | EXCLUDED | EXCLUDED | [official](https://iuhoosiers.com/sports/football/stats/2026/minnesota/boxscore/28511) |
| 401858502 | Wisconsin @ Iowa | 16.9530 | 47.4333 | 0.8106 | 0-30 | 30 | 30 | 13.0470 | -17.4333 | 1 | [official](https://hawkeyesports.com/news/2026/10/31/hawkeyes-shut-out-wisconsin-30-0) |
| 401858503 | Illinois @ Maryland | 6.6782 | 57.3814 | 0.6252 | 20-17 | -3 | 37 | -9.6782 | -20.3814 | 0 | [official](https://umterps.com/news/2026/10/31/football-vs-illinois-recap) |
| 401858505 | Northwestern @ Oregon | EXCLUDED | EXCLUDED | EXCLUDED | 26-34 | 8 | 60 | EXCLUDED | EXCLUDED | EXCLUDED | [official](https://goducks.com/news/2026/10/31/football-second-half-surge-fuels-win-over-no-20-northwestern) |
| 401858506 | Purdue @ Penn State | 20.6456 | 57.4111 | 0.8788 | 17-31 | 14 | 48 | -6.6456 | -9.4111 | 1 | [official](https://gopsusports.com/news/2026/10/31/nittany-lions-roll-to-b1g-halloween-win-over-purdue-31-17) |
| 401858507 | Michigan @ Rutgers | EXCLUDED | EXCLUDED | EXCLUDED | 28-21 | -7 | 49 | EXCLUDED | EXCLUDED | EXCLUDED | [official](https://d4njeax0ev936.cloudfront.net/news/2026/10/31/football-carrs-all-around-performance-fuels-u-m-victory-over-rutgers) |
| 401858508 | Nevada @ UCLA | 11.4871 | 56.1109 | 0.7593 | 0-27 | 27 | 27 | 15.5129 | -29.1109 | 1 | [official](https://accessibility-05.sidearmsports.com/news/2026/10/31/football-pack-drops-non-conference-finale-at-no-7-7-ucla.aspx) |
| 401862815 | Temple @ East Carolina | EXCLUDED | EXCLUDED | EXCLUDED | 9-17 | 8 | 26 | EXCLUDED | EXCLUDED | EXCLUDED | [official](https://ecupirates.com/news/2026/10/31/football-east-carolina-defeats-temple-17-9) |
| 401862816 | UAB @ South Florida | EXCLUDED | EXCLUDED | EXCLUDED | 10-30 | 20 | 40 | EXCLUDED | EXCLUDED | EXCLUDED | [official](https://gousfbulls.com/news/2026/10/31/football-hicks-record-setting-performance-leads-bulls-in-rout-of-uab-30-10) |
| 401864529 | New Mexico @ San José State | -7.3345 | 44.5566 | 0.3177 | 21-16 | -5 | 37 | 2.3345 | -7.5566 | 1 | [official](https://sjsuspartans.com/news/2026/10/31/late-push-comes-up-short-for-spartans-against-lobos) |
| 401869944 | Coastal Carolina @ Georgia State | EXCLUDED | EXCLUDED | EXCLUDED | 31-20 | -11 | 51 | EXCLUDED | EXCLUDED | EXCLUDED | [official](https://georgiastatesports.com/news/2026/10/31/football-panthers-come-up-short-in-a-31-20-loss-to-coastal-carolina.aspx) |
| 401871095 | Southern Miss @ UL Monroe | -8.1065 | 56.8091 | 0.3137 | 35-21 | -14 | 56 | -5.8935 | -0.8091 | 1 | [official](https://ulmwarhawks.com/news/2026/10/31/football-warhawk-comeback-comes-up-short-vs-golden-eagles.aspx) |
| 401871096 | Marshall @ Old Dominion | 10.5313 | 45.0652 | 0.7236 | 36-23 | -13 | 59 | -23.5313 | 13.9348 | 0 | [official](https://odusports.com/news/2026/10/31/football-drops-homecoming-contest-to-marshall-36-23) |
| 401871097 | Louisiana Tech @ South Alabama | 5.7005 | 51.6180 | 0.6363 | 35-20 | -15 | 55 | -20.7005 | 3.3820 | 0 | [official](https://usajaguars.com/news/2026/10/31/football-south-alabama-falls-to-louisiana-tech-35-20.aspx) |
| 401859185 | Notre Dame @ Navy | EXCLUDED | EXCLUDED | EXCLUDED | 35-13 | -22 | 48 | EXCLUDED | EXCLUDED | EXCLUDED | [official](https://navysports.com/news/2026/10/31/football-navy-battles-no-5-notre-dame-before-falling-35-13.aspx) |
| 401866452 | Bowling Green @ Western Michigan | 24.7911 | 45.2407 | 0.9258 | 10-23 | 13 | 33 | -11.7911 | -12.2407 | 1 | [official](https://wmubroncos.com/news/2026/10/31/football-broncos-bowl-eligible-after-downing-bowling-green.aspx) |
| 401861966 | UConn @ Air Force | 4.4952 | 50.6465 | 0.6546 | 26-35 | 9 | 61 | 4.5048 | 10.3535 | 1 | [official](https://goairforcefalcons.com/news/2026/10/31/football-hodges-rumbles-for-200-yards-to-lead-air-force-to-35-26-win-over-uconn) |
| 401856734 | Florida @ Georgia | 13.3585 | 65.9962 | 0.7886 | 8-27 | 19 | 35 | 5.6415 | -30.9962 | 1 | [official](https://georgiadogs.com/news/2026/10/31/football-takeaways-power-bulldogs-past-gators) |
| 401860910 | Colorado State @ Utah State | -4.6867 | 51.6112 | 0.3760 | 14-31 | 17 | 45 | 21.6867 | -6.6112 | 0 | [official](https://utahstateaggies.com/news/2026/10/31/football-aggie-defense-leads-the-way-in-31-14-win-over-colorado-state.aspx) |
| 401864531 | UTEP @ North Dakota State | 20.3115 | 49.2037 | 0.8747 | 7-31 | 24 | 38 | 3.6885 | -11.2037 | 1 | [official](https://gobison.com/news/2026/11/1/football-north-dakota-state-defeats-utep-31-7) |
| 401871059 | Florida International @ Liberty | EXCLUDED | EXCLUDED | EXCLUDED | 10-49 | 39 | 59 | EXCLUDED | EXCLUDED | EXCLUDED | [official](https://libertyflames.com/news/2026/10/31/football-defense-shines-in-49-10-homecoming-win-over-fiu) |

**This official batch:** 39/39 qualified, 30 modeled, 9 exclusions preserved.

### Week 9 COMPLETE exact ORIGINAL FIRST_FROZEN modeled-cohort results

- Cohort: 56/56 official school-final outcomes independently verified and exact-ID joined; **45/45 modeled predictions scored**, 11/11 original exclusions retained unscored; zero unresolved original IDs. Sources: two pre-existing official Tuesday rows + 15 official pending-result capture `f59aa77a585853cbf4e2a6a2e8e1721c9da75c70` + 39 independent official capture `4aa121e3e475a3c6ef5bbb90ac1aea3090c3e1e3`.
- Correct home-winner margin direction: **28/45 (62.22%)**; margin MAE **14.262253024** points; total MAE **13.747495097** points; home-win Brier **0.218465691**. Calculated from exact immutable original numeric strings, not rounded display values; excludes all 11 original missing-data games. No in-week retune or hindsight rerun.
- Earlier accepted Weeks4–8 original modeled baseline: 249 games, 153 correct directions, margin MAE 14.006623340516, total MAE 13.190502012127, Brier 0.239225353872. Week9 is one prospective descriptive cohort, not causal evidence of model improvement or promotion readiness.
- Official school results do not prove sportsbook settlement, redeemed cash, wager profit, recommendation lineage, CLV, or current execution offers. The separately governed actual-user execution ledger is downstream and does not feed model training.
- This scorecard result earns complete Week9 **outcome-source coverage and deterministic scoring**. Final weekly QA RUN_PASS still requires independently reconciled ticket settlement/QA integration/terminal evidence as applicable; this scorecard append alone is not weekly QA closure.


## Week10 incremental official final-score reconciliation — November7 CT

Run CFB_WEEK10_CLOSEOUT_20261108T044606Z. Exact source/scoring artifact: evidence/operational/CFB_WEEK10_INCREMENTAL_CLOSEOUT_20261108T044606Z.json, Git blob eb7b3a51acb43eb5e4ea39f5a119c70858497c1f. Original artifact10897612260 ZIP SHA256772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf replayed exactly; 63 identities/55predictions/8exclusions/165strings preserved. Raw CBS capture evidence/operational/CFB_WEEK10_CBS_RESULT_CAPTURE_20261108T044606Z.html.gz.b64 at 123ebd03e3cdb17a31f64da25504d8f72e371853.

This is downstream postgame evidence. Original frozen predictions and exclusions remain unchanged. CBS snapshot at 2026-11-08T04:46:54.652100+00:00: 58 final, five not final. Only 42 officially corroborated games are appended to the canonical scorecard; 16 other CBS finals remain source-only. This is not complete Week10 acceptance or Sunday learning closure.

| Game ID | Away @ home | Original home margin | Original total | Original home p | Official final away-home | Margin error | Total error | Direction correct | Official source |
|---|---|---:|---:|---:|---|---:|---:|---|---|
| 401858517 | Rutgers @ Wisconsin | EXCLUDED | EXCLUDED | EXCLUDED | 10-31 | EXCLUDED | EXCLUDED | EXCLUDED | [official](https://uwbadgers.com/news/2026/11/7/football-wisconsin-defeats-rutgers-31-10) |
| 401856742 | Vanderbilt @ Mississippi State | 15.549626345548761 | 55.56747078426483 | 0.8182005921246576 | 25-23 | -17.549626 | -7.567471 | 0 | [official](https://vucommodores.com/news/2026/11/07/taylor-helps-dores-top-mississippi-state) |
| 401871074 | Missouri State @ Florida International | 6.471677799283147 | 50.89495186078102 | 0.6322299211493579 | 20-23 | -3.471678 | -7.894952 | 1 | [official](https://missouristatebears.com/sports/football/stats/2026/fiu/boxscore/7865) |
| 401864534 | Northern Illinois @ San José State | 12.216751671820077 | 50.109095593377916 | 0.7444111196736232 | 19-30 | -1.216752 | -1.109096 | 1 | [official](https://niuhuskies.com/news/2026/11/7/football-big-third-quarter-powers-san-jos-state-past-niu.aspx) |
| 401871098 | Louisiana Tech @ Troy | 7.926645201733717 | 46.55365876102345 | 0.6579231620303794 | 41-17 | -31.926645 | 11.446341 | 0 | [official](https://latechsports.com/news/2026/11/7/football-bulldogs-showcase-defensively-down-troy-to-remain-undefeated-in-sun-belt-play) |
| 401862821 | Rice @ North Texas | 2.6227721809273334 | 52.735543039826865 | 0.604848752521358 | 23-52 | 26.377228 | 22.264457 | 1 | [official](https://meangreensports.com/sports/football/schedule/) |
| 401856850 | UCF @ Kansas | 1.060836045636887 | 50.082973477839204 | 0.5283457173006264 | 33-32 | -2.060836 | 14.917027 | 0 | [official](https://ucfknights.com/sports/football/schedule) |
| 401858290 | Merrimack @ Wake Forest | 27.119872949618784 | 53.799730938597165 | 0.931919335067152 | 0-77 | 49.880127 | 23.200269 | 1 | [official](https://godeacs.com/news/2026/11/7/football-dominant-overall-team-performance-by-no-16-wake-forest-leads-to-77-0-victory-over-merrimack) |
| 401871076 | Western Kentucky @ Middle Tennessee | 27.857095018909256 | 50.53624715269643 | 0.9392086588608907 | 42-51 | -18.857095 | 42.463753 | 1 | [official](https://goblueraiders.com/news/2026/11/7/football-late-heroics-lead-the-way-as-blue-raiders-down-wku-on-homecoming) |
| 401858516 | Penn State @ Washington | -3.1495475114994615 | 47.804352616275885 | 0.4333079293071188 | 28-25 | 0.149548 | 5.195647 | 1 | [official](https://gopsusports.com/news/2026/11/8/penn-state-football-secures-28-25-road-victory-at-washington) |
| 401862819 | Charlotte @ UAB | EXCLUDED | EXCLUDED | EXCLUDED | 12-23 | EXCLUDED | EXCLUDED | EXCLUDED | [official](https://uabsports.com/news/2026/11/7/football-uab-pulls-away-from-charlotte-in-fourth-quarter-for-23-12-victory) |
| 401856740 | Alabama @ LSU | 3.5090584473900757 | 54.06402401878285 | 0.5694578967572295 | 31-13 | -21.509058 | -10.064024 | 0 | [official](https://lsusports.net/news/2026/11/7/football-falls-to-no-5-alabama-31-13) |
| 401856851 | Cincinnati @ Houston | 7.466094858371314 | 57.33789708596704 | 0.6907526229114599 | 24-31 | -0.466095 | -2.337897 | 1 | [official](https://gobearcats.com/news/2026/11/7/cincinnati-falls-at-no-17-houston-31-24) |
| 401858514 | Oregon @ Ohio State | 12.6572944597905 | 57.45625252704641 | 0.7870052211880744 | 41-28 | -25.657294 | 11.543747 | 0 | [official](https://ohiostatebuckeyes.com/news/2026/11/8/football-buckeyes-drop-home-contest-to-oregon) |
| 401862820 | Temple @ Navy | EXCLUDED | EXCLUDED | EXCLUDED | 35-42 | EXCLUDED | EXCLUDED | EXCLUDED | [official](https://navysports.com/news/2026/11/7/football-gutierrez-accounts-for-six-touchdowns-as-navy-holds-off-temple-42-35.aspx) |
| 401869951 | Marshall @ Georgia Southern | 15.029841107961314 | 45.052484119214846 | 0.7962656210758162 | 13-49 | 20.970159 | 16.947516 | 1 | [official](https://gseagles.com/news/2026/11/7/football-johnson-leads-eagles-to-big-win-over-marshall) |
| 401871073 | Delaware @ Kennesaw State | 0.17558159017670696 | 50.113302706890565 | 0.4896759060405278 | 40-42 | 1.824418 | 31.886697 | 1 | [official](https://ksuowls.com/news/2026/11/7/football-postgame-notes-kennesaw-state-clips-fightin-blue-hens-42-40.aspx) |
| 401856854 | Oklahoma State @ Kansas State | 15.665675902746544 | 51.31526209623849 | 0.8288305481594604 | 66-28 | -53.665676 | 42.684738 | 0 | [official](https://okstate.com/news/2026/11/7/cowboy-football-cowboys-dominate-k-state-66-28) |
| 401869945 | Old Dominion @ Coastal Carolina | EXCLUDED | EXCLUDED | EXCLUDED | 21-8 | EXCLUDED | EXCLUDED | EXCLUDED | [official](https://odusports.com/news/2026/11/7/six-takeaways-power-odu-to-21-8-win-at-coastal-carolina) |
| 401856738 | Arkansas @ Auburn | 16.28981148199242 | 54.4504980271418 | 0.8089180472483015 | 23-26 | -13.289811 | -5.450498 | 1 | [official](https://auburntigers.com/news/2026/11/7/auburn-rallies-beats-arkansas-26-23-on-last-minute-drive) |
| 401858515 | Maryland @ Purdue | -8.130447755193787 | 60.3956097237796 | 0.3016866232676576 | 34-29 | 3.130448 | 2.604390 | 1 | [official](https://umterps.com/news/2026/11/7/football-purdue-recap) |
| 401858286 | Duke @ NC State | 4.228345707284807 | 48.620614746519706 | 0.6292798334885475 | 41-3 | -42.228346 | -4.620615 | 0 | [official](https://goduke.com/news/2026/11/7/football-duke-explodes-in-second-quarter-tops-ncsu-41-3) |
| 401858512 | UCLA @ Minnesota | 2.747681980467277 | 55.15854610269629 | 0.5840991961017751 | 34-20 | -16.747682 | -1.158546 | 0 | [official](https://uclabruins.com/news/2026/11/7/no-5-ucla-remains-unbeaten-after-34-20-win-at-minnesota) |
| 401858289 | Florida State @ Boston College | 5.987680854824376 | 53.704571945553646 | 0.6564435069397415 | 31-24 | -12.987681 | 1.295428 | 0 | [official](https://seminoles.com/news/2026/11/7/football-seminoles-battle-past-boston-college-for-road-victory) |
| 401858292 | North Carolina @ UConn | 4.074878832877464 | 51.38182660353894 | 0.6021837924567134 | 38-21 | -21.074879 | 7.618173 | 0 | [official](https://goheels.com/news/2026/11/7/football-fb-recap-at-uconn) |
| 401858285 | Clemson @ Syracuse | EXCLUDED | EXCLUDED | EXCLUDED | 18-13 | EXCLUDED | EXCLUDED | EXCLUDED | [official](https://clemsontigers.com/news/2026/11/7/clemson-defense-lifts-tigers-to-18-13-road-victory) |
| 401856743 | Texas @ Missouri | 2.9866386354064347 | 47.6316901644869 | 0.5336080010391044 | 34-20 | -16.986639 | 6.368310 | 0 | [official](https://texaslonghorns.com/sports/football/stats/2026/missouri/boxscore/22502) |
| 401856853 | Iowa State @ Baylor | 4.822221860731134 | 46.37501164360453 | 0.610435274455332 | 31-42 | 6.177778 | 26.624988 | 1 | [official](https://baylorbears.com/sports/football/stats/2026/iowa-state/boxscore/29752) |
| 401862822 | Tulsa @ Tulane | -7.453381995487822 | 45.36973741035307 | 0.3078800631681831 | 60-10 | -42.546618 | 24.630263 | 1 | [official](https://tulsahurricane.com/sports/football/stats/2026/tulane/boxscore/16255) |
| 401856849 | BYU @ Utah | 7.736699271390598 | 55.90234467514159 | 0.6922489559371883 | 20-28 | 0.263301 | -7.902345 | 1 | [official](https://utahutes.com/news/2026/11/7/football-no-3-utah-moves-to-9-0-with-rivalry-win-over-no-9-byu) |
| 401856855 | TCU @ Arizona | 1.5517727433164694 | 48.752150569762044 | 0.5446892660956925 | 28-29 | -0.551773 | 8.247849 | 1 | [official](https://arizonawildcats.com/news/2026/11/7/football-salgado-medina-late-field-goal-pushes-no-22-arizona-over-tcu-29-28) |
| 401864533 | New Mexico @ Nevada | -3.3784963393467207 | 42.162809399335046 | 0.42443467359009246 | 31-3 | -24.621504 | -8.162809 | 1 | [official](https://golobos.com/news/2026/11/6/nationally-ranked-lobos-dismantle-nevada-31-3) |
| 401858510 | Nebraska @ Illinois | -1.761681196539541 | 55.71166433271795 | 0.522416791937179 | 13-24 | 12.761681 | -18.711664 | 0 | [official](https://huskers.com/news/2026/11/6/huskers-fall-at-illinois-24-13) |
| 401862818 | South Florida @ East Carolina | -11.807863806889149 | 48.45215367034799 | 0.22121155105652215 | 17-20 | 14.807864 | -11.452154 | 0 | [official](https://ecupirates.com/news/2026/11/7/football-conrad-drills-55-yard-game-winning-field-goal-to-lift-ecu-past-south-florida-20-17) |
| 401858288 | Virginia Tech @ SMU | -2.8565813934429176 | 57.50370019732571 | 0.4098040927761556 | 28-51 | 25.856581 | 21.496300 | 0 | [official](https://smumustangs.com/game-center/14455) |
| 401869964 | James Madison @ Southern Miss | -14.404067861695497 | 52.98662341636999 | 0.20791881268972284 | 54-23 | -16.595932 | 24.013377 | 1 | [official](https://jmusports.com/news/2026/11/6/football-evans-leads-dukes-in-road-win-at-southern-miss) |
| 401862817 | UTSA @ Florida Atlantic | -5.195659872391833 | 54.315494919956976 | 0.3571857491486996 | 29-60 | 36.195660 | 34.684505 | 0 | [official](https://fausports.com/news/2026/11/6/football-owls-bowl-bound-after-scoring-60-against-first-place-utsa) |
| 401866456 | Central Michigan @ Eastern Michigan | -2.7860217274720576 | 42.92255127170241 | 0.3934278618775662 | 35-7 | -25.213978 | -0.922551 | 1 | [official](https://cmuchippewas.com/news/2026/11/5/football-chippewas-roll-past-eastern-in-motor-city-maction) |
| 401866455 | Ball State @ Massachusetts | 26.11695812114495 | 50.971213997264655 | 0.9319500450031746 | 30-31 | -25.116958 | 10.028786 | 1 | [official](https://umassathletics.com/news/2026/11/5/football-minutemen-outlast-ball-state-in-overtime-thriller-31-30) |
| 401866457 | Toledo @ Sacramento State | -5.156938754516926 | 54.25392295084098 | 0.3464234810248434 | 20-17 | 2.156939 | -17.253923 | 1 | [official](https://utrockets.com/news/2026/11/4/football-rockets-swarm-hornets-for-mac-win-in-california-20-17) |
| 401866454 | Buffalo @ Miami (OH) | 11.720713530764943 | 53.6393554794765 | 0.769956822513323 | 34-31 | -14.720714 | 11.360645 | 0 | [official](https://ubbulls.com/news/2026/11/4/football-bulls-clip-redhawks-in-overtime-34-31) |
| 401866453 | Ohio @ Akron | 10.365389485491425 | 52.76064387323792 | 0.7411891720882852 | 28-20 | -18.365389 | -4.760644 | 0 | [official](https://ohiobobcats.com/news/2026/11/3/ohio-football-wins-on-the-road-at-akron) |

Official subset:42 games, 37 modeled, 5 original exclusions. Margin-sign direction 20/37; probability classifier 20/37; margin MAE 18.053524068, total MAE 13.807902564, Brier 0.262030916. Exact original strings used; independent Decimal recomputation agrees. Rounded row errors are display only.

CBS-only 58-final descriptive subset:50 modeled/8 excluded; margin direction26/50, probability classifier27/50. It is deliberately NOT merged into the official subset or treated as complete weekly metrics. Five in-progress games remain unscored.

Official corroboration still required for these CBS finals: 401870795 Liberty @ New Mexico State, 401856739 Oklahoma @ Florida, 401862823 Air Force @ Army, 401856852 Colorado @ Arizona State, 401856741 Georgia @ Ole Miss, 401858513 Iowa @ Northwestern, 401858291 Miami @ Notre Dame, 401858511 Michigan State @ Michigan, 401858287 Louisville @ Georgia Tech, 401871075 Sam Houston @ Jacksonville State, 401856745 Kentucky @ Tennessee, 401860911 Boise State @ Colorado State, 401869968 South Alabama @ Louisiana, 401869936 UL Monroe @ Arkansas State, 401856744 Texas A&M @ South Carolina, 401869927 Georgia State @ App State.

Not-final identities at captured boundary: 401860913 Fresno State @ Utah State, 401864532 Hawai'i @ UTEP, 401856856 West Virginia @ Texas Tech, 401864535 Wyoming @ UNLV, 401860912 Texas State @ Oregon State.

All eleven actual tickets are consistent with final-score evidence: ten underlying games independently official-verified, ASU20-10 corroborated by CBS final and AP recap while school sources remain stale. Reported8WIN3LOSS/$55stake/$102.90printedreturn/+$47.90net retained. These results do not prove sportsbook payment, current available cash, CLV, recommendation attribution or a model promotion. No model/market/decision/task change.


## Week10 four additional official finals and R2 source-clock qualification — November7 CT

Run CFB_WEEK10_CLOSEOUT_20261108T044606Z. R2 artifact evidence/operational/CFB_WEEK10_INCREMENTAL_CLOSEOUT_20261108T044606Z_R2.json, blob 0f107b4e4c990f754a7477e58a4296ed7127d8ad. Only these four rows are new official results. Preserve prior42rows; cumulative46games=41modeled+5originalexclusions. TwelveCBSonlyfinals andfivependingfinals remain outside fullofficialacceptance.

| Game ID | Away @ home | Final away-home | Original home margin | Original total | Original home p | Official source |
|---|---|---|---:|---:|---:|---|
| 401856739 | Oklahoma @ Florida | 23-7 | 9.171592972348307 | 51.110471208670816 | 0.7164656477262331 | [official](https://floridagators.com/news/2026/11/7/football-final-florida-vs-oklahoma-nov-7-2026) |
| 401860911 | Boise State @ Colorado State | 64-38 | 0.7553368849316238 | 56.848435210772486 | 0.5526660742301289 | [official](https://csurams.com/sports/football/stats/2026/boise-state/boxscore/21971) |
| 401856744 | Texas A&M @ South Carolina | 9-17 | 12.715251331697846 | 50.5036568944936 | 0.7454572368140134 | [official](https://12thman.com/news/2026/11/07/aggies-at-south-carolina) |
| 401869927 | Georgia State @ App State | 39-23 | 7.049278887884242 | 56.118010249830874 | 0.6756862377995193 | [official](https://appstatesports.com/news/2026/11/7/football-postgame-notes-from-app-state-vs-georgia-state.aspx) |

Updated officialsubset metrics {"n": 41, "margin_direction_correct": 21, "probability_classifier_correct": 21, "margin_mae": 18.235898795300695, "total_mae": 14.818050671421819, "home_win_brier": 0.2691524541958868}. Exact fullprecisionoriginalstrings; independentlyDecimalchecked. Earlier42subsetmetrics remain historically correct for their own population.

Source clocks: requeststarted04:46:54.652100Z; responsecomplete by retainedfilewrite04:47:00.013653Z. R1earlyclocklabels qualified, not silently retimed. Official direct request-start fields likewise separated from completed-response bounds. Providerupdateclockunknown.

Sourceclockclarification supersedes earlierlabels only: CBS04:46:54.652100Z was requeststart, complete response by retainedfilewrite04:47:00.013653Z. Not a providerupdateclock. Official HTMLrequeststart and responsebounds are separately preserved in R2. No outcome, score, wager timing or prediction changed.
