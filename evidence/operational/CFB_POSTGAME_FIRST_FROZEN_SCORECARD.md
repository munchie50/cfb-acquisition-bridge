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
