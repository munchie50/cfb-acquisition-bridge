# CFB Established Execution Ledger

Status: ACTIVE APPEND-ONLY OPERATIONAL SURFACE
Initialized: 2026-09-27

## Recovery semantics
Canonical durable ledger for actual established wager executions only. Candidate slips and recommendations are not executions.

## Required fields
- execution timestamp/source when established
- game/market
- exact accepted line/odds/stake
- production or sandbox classification
- execution evidence reference
- linked pre-event Champion/decision references when genuinely available
- settlement state/result when later established

## Contamination boundary
Execution evidence is observational downstream evidence only. It is never a Champion model input, calibration/training input, or basis for retroactively changing a frozen prediction or decision.

## Initial state
Do not backfill from memory. Previously established execution evidence may be appended only when its original evidence can be recovered and classified under the active screenshot/execution controls.

## Write-path validation — 2026-09-27 13:03 CT
- Purpose: controlled repair validation for canonical existing-file mutation.
- Governance effect: none; no decision, execution, settlement, prediction, score, or outcome state created.
- Method: SHA-guarded existing-file update followed by direct repository readback.

## Original-ticket recovery — 2026-10-09 16:59 CT

Run: CFB_EXECUTION_RECOVERY_20261009T215917Z; recorded now from recovered original issued tickets, not manufactured historical decisions.
Evidence manifest: evidence/operational/CFB_ORIGINAL_TICKET_EXECUTION_RECOVERY_2026-10-09.json, blob 2ea1f35c353665c373eb19961aa52692f680dbea; each row maps to original image identity and SHA256.
Common fields: Caesars Sportsbook / Harrah's Columbus; ACTUAL_REAL_MONEY; production/sandbox budget classification UNASSIGNED/UNVERIFIED; printed clock timezone UNSPECIFIED; pre-event Champion/decision links UNRECONCILED; settlement and CLV UNVERIFIED. No automatic recommendation attribution. All event times below are receipt display only, not independently verified kickoffs. Ten tickets are not live-labelled; that alone does not certify pregame timing. Baylor is explicitly live/in-game and excluded from pregame evaluation.

| Execution ID | Issued date/time as printed | Game | Selection / market | Accepted line | American odds | Stake USD | Receipt event time | Timing |
|---|---|---|---|---|---|---|---|---|
| CFB_SEP26-01 | 2026-09-26 12:32 PM | Nebraska at Michigan State | Nebraska / SPREAD | -5.5 | -110 | $5.05 | 2026-09-26 04:00 PM | NOT_LIVE_LABELLED |
| CFB_SEP26-02 | 2026-09-26 12:31 PM | Iowa at Michigan | Iowa / MONEYLINE | N/A | +180 | $2.00 | 2026-09-26 02:30 PM | NOT_LIVE_LABELLED |
| CFB_SEP26-03 | 2026-09-26 12:28 PM | South Florida at Bowling Green | South Florida / SPREAD | -18.5 | -104 | $2.00 | 2026-09-26 04:08 PM | NOT_LIVE_LABELLED |
| CFB_SEP26-04 | 2026-09-26 12:25 PM | Oklahoma at Georgia | Georgia / SPREAD | -13.5 | -109 | $3.00 | 2026-09-26 02:45 PM | NOT_LIVE_LABELLED |
| CFB_SEP26-05 | 2026-09-26 12:25 PM | Wisconsin at Penn State | Penn State / SPREAD | -10 | -107 | $3.00 | 2026-09-26 04:10 PM | NOT_LIVE_LABELLED |
| CFB_SEP26-06 | 2026-09-26 12:26 PM | Colorado at Baylor | Baylor / SPREAD_LIVE | -9.5 | -124 | $3.00 | 2026-09-26 11:03 AM | LIVE_IN_GAME |
| CFB_OCT02-01 | 2026-10-02 07:50 PM | Syracuse at Connecticut | Connecticut / SPREAD | +6.5 | +100 | $3.00 | 2026-10-03 11:05 AM | NOT_LIVE_LABELLED |
| CFB_OCT02-02 | 2026-10-02 07:51 PM | Alabama at Mississippi State | Mississippi State / SPREAD | +5.5 | -107 | $3.00 | 2026-10-03 11:10 AM | NOT_LIVE_LABELLED |
| CFB_OCT02-03 | 2026-10-02 07:51 PM | Ohio State at Iowa | Iowa / SPREAD | +14.5 | -117 | $3.00 | 2026-10-03 02:40 PM | NOT_LIVE_LABELLED |
| CFB_OCT02-04 | 2026-10-02 07:52 PM | Marshall at James Madison | James Madison / SPREAD | -18.5 | -106 | $3.00 | 2026-10-03 02:50 PM | NOT_LIVE_LABELLED |
| CFB_OCT02-05 | 2026-10-02 07:54 PM | Michigan State at Wisconsin | Wisconsin / SPREAD | -9.5 | -121 | $3.40 | 2026-10-03 11:35 AM | NOT_LIVE_LABELLED |

Reconciliation: six Sep26-issued wagers $18.05 plus five Oct2-issued wagers $15.40 = 11 actual wagers / $33.45 staked. One separate historical market board excluded. No raw serials/barcodes, model inputs, market benchmark, closing prices, outcomes or retroactive decisions created. Earlier initial/write-probe history preserved.
