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
