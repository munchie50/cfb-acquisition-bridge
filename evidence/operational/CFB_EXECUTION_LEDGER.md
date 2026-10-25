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

## Verified final-score result grades — October 9 prospective reconciliation

Run: CFB_WAGER_RESULT_RECONCILIATION_20261009T223030Z. Evidence: evidence/operational/CFB_ORIGINAL_WAGER_FINAL_RESULT_RECONCILIATION_2026-10-09.json, blob c84336516210f55fbd5d130275202da2b8899092, with exact original source identities, official final-result URLs/date, session retrieval bounds and deterministic signed-line comparison.
These are derived full-game FINAL_SCORE_GRADES, not confirmation of sportsbook settlement/adjudication, ticket redemption or cash payment. Original execution entries remain unchanged. Overtime included in official finals. Book void/cancellation/special rules unverified. Budget classification, receipt timezone, genuine pre-event prediction/decision attribution and CLV remain unverified.

| Execution ID | Official final (selection first) | Accepted market / line | Selection final margin | Signed grade comparison | Final-score grade |
|---|---|---|---|---|---|
| CFB_SEP26-01 | Nebraska 31, Michigan State 13 | SPREAD / -5.5 | 18 | 12.5 | WIN |
| CFB_SEP26-02 | Iowa 20, Michigan 19 | MONEYLINE / N/A | 1 | 1 | WIN |
| CFB_SEP26-03 | South Florida 14, Bowling Green 6 | SPREAD / -18.5 | 8 | -10.5 | LOSS |
| CFB_SEP26-04 | Georgia 41, Oklahoma 13 | SPREAD / -13.5 | 28 | 14.5 | WIN |
| CFB_SEP26-05 | Penn State 20, Wisconsin 24 | SPREAD / -10 | -4 | -14 | LOSS |
| CFB_SEP26-06 | Baylor 23, Colorado 13 | SPREAD_LIVE / -9.5 | 10 | 0.5 | WIN |
| CFB_OCT02-01 | Connecticut 41, Syracuse 42 (OT) | SPREAD / +6.5 | -1 | 5.5 | WIN |
| CFB_OCT02-02 | Mississippi State 23, Alabama 56 | SPREAD / +5.5 | -33 | -27.5 | LOSS |
| CFB_OCT02-03 | Iowa 14, Ohio State 31 | SPREAD / +14.5 | -17 | -2.5 | LOSS |
| CFB_OCT02-04 | James Madison 45, Marshall 17 | SPREAD / -18.5 | 28 | 9.5 | WIN |
| CFB_OCT02-05 | Wisconsin 31, Michigan State 3 | SPREAD / -9.5 | 28 | 18.5 | WIN |

Arithmetic: selected-team final margin + signed accepted spread; moneyline uses final winner only. Positive WIN, negative LOSS, zero PUSH. Eleven distinct actual wagers = 7 WIN / 4 LOSS / 0 PUSH. Ten not-live-labelled tickets = 6 WIN / 4 LOSS (this does not certify their pregame timing); separate Baylor LIVE_IN_GAME = 1 WIN, +0.5 after accepted -9.5. Preserve Baylor outside pregame evaluation. Staked total remains $33.45; cash profit and paid status UNVERIFIED. No model, prediction, historical recommendation, market/close or FIRST_FROZEN scorecard modification.

## Original FIRST_FROZEN row-reference lookup — October 9

Run CFB_WAGER_FROZEN_REFERENCE_QA_20261009T224012Z; audit evidence/operational/CFB_ORIGINAL_WAGER_FROZEN_REFERENCE_AUDIT_2026-10-09.json, blob b13ef5bacf7a47199ca139a429137427f0346fca. Authenticated original artifact10897612260 / producer36216090860 / archiveSHA256 772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf; accepted cutoff2026-09-26T03:47:37.497112+00:00. Eleven unique exact ordered team-pair/date references, one original prediction and zero exclusions each. Only alias Connecticut->UConn. Original CSV physical line references below include header. Original prediction values retained in audit unchanged; HOME margin/win semantics explicit. These are accepted pre-GAME artifact references, not proof of predictions before execution or engine recommendations. Independent official game-id certification UNVERIFIED.

| Execution ID | Original game ID | Target CSV line | Prediction CSV line | Source schedule clock |
|---|---|---|---|---|
| CFB_SEP26-01 | 401858464 | 35 | 31 | Date consistent; exact kickoff unverified |
| CFB_SEP26-02 | 401858463 | 25 | 22 | Date consistent; exact kickoff unverified |
| CFB_SEP26-03 | 401862785 | 37 | 33 | Date consistent; exact kickoff unverified |
| CFB_SEP26-04 | 401856700 | 21 | 19 | Date consistent; exact kickoff unverified |
| CFB_SEP26-05 | 401858466 | 36 | 32 | Date consistent; exact kickoff unverified |
| CFB_SEP26-06 | 401856813 | 4 | 4 | Date consistent; exact kickoff unverified |
| CFB_OCT02-01 | 401858252 | 81 | 73 | Date consistent; exact kickoff unverified |
| CFB_OCT02-02 | 401856707 | 73 | 66 | CONFLICT; unresolved |
| CFB_OCT02-03 | 401858473 | 92 | 82 | Date consistent; exact kickoff unverified |
| CFB_OCT02-04 | 401869962 | 101 | 90 | Date consistent; exact kickoff unverified |
| CFB_OCT02-05 | 401858479 | 84 | 75 | Date consistent; exact kickoff unverified |

Mississippi State original frozen start2026-10-03 04:00UTC converts to Oct2 23:00CT; official final page establishes Oct3 event and displays11:07AM kickoff. Preserve original source clock as CONFLICT, cause unresolved; do not use it as authoritative kickoff/deadline. Exact ordered pair and original UTC date give a unique reference; local-date/kickoff lineage certification remains OPEN. No frozen source repair or outcome-selected prediction substitution. Baylor reference does not qualify live execution for pregame analysis. Receipt timezone, pre-execution chronology, genuine Champion/decision attribution, book payment, budget and CLV remain UNVERIFIED. This append supersedes UNRECONCILED only for original FIRST_FROZEN row lookup, not those other fields.

## Original wager historical decision references — October 9

Run CFB_WAGER_DECISION_REFERENCE_QA_20261009T232630Z; audit evidence/operational/CFB_ORIGINAL_WAGER_HISTORICAL_DECISION_REFERENCE_AUDIT_2026-10-09.json, blob 59eab5836ff4716cb44953285b72094ad4752f33. Immutable decision ledger commits aff7c227fac581adcdd80668ff7c9c4bbb26fb81 (October2 23:24:02Z /18:24:02CT, blob6a506b727ce9ece41c64ce6d10c2a88afc95f937) and09c479bca87e08b92b9d3e42b539b27c21be8120 (October3 00:43:58Z /October2 19:43:58CT, blobe2b0f4f7fa72ba793f5c468958f4c25162897c1b) independently read back. Currentledger preserves those bytes; compare API confirms pinnedcommit is main ancestor. Four unique ordered-team/selection/SPREAD references recovered:

| Execution ID | Recorded selection and minimum line | Max negative price | Accepted ticket | Reference comparison |
|---|---|---|---|---|
| CFB_OCT02-01 | UConn +6.5 or better | -115 | +6.5 / +100 | Within recorded limits |
| CFB_OCT02-02 | Mississippi State +5.5 or better | -115 | +5.5 / -107 | Within recorded limits |
| CFB_OCT02-03 | Iowa +14 or better; prefer +14.5 | -120 | +14.5 / -117 | Within recorded limits |
| CFB_OCT02-04 | James Madison -18.5 or better | -115 | -18.5 / -106 | Within recorded limits |

Four matched tickets total$12; all11original wagers remain$33.45. Reference and cutoff compatibility supersede UNRECONCILED only for these four historical-text lookups. This does NOT certify decision quality, calibrated rules, pre-execution sequence, recommendation delivery/causal attribution, budget, settlement or CLV. No outcomes used to select matches. Connecticut/UConn explicit alias only; independent decision-to-execution game-id certification remains unverified. Prior frozen-row references remain unchanged.
Receipt timezone remains UNSPECIFIED. IF printedOctober2 19:50–19:52times are America/Chicago, the19:43:58CTconfirmationcommit precedes them by362/422/422/482seconds; this is labelled conditional, not an established sequence. No receipt timezone or pre-execution status is silently promoted. ForWisconsin CFB_OCT02-05, no explicit BETNOWmatch exists in this pinnedledger; do not substitute UMass (recorded candidate without a recovered ticket). For all sixSeptember26tickets, this ledgerhistory is not pre-execution evidence: its initializationSeptember27postdates tickets. No claim that recommendations were absent elsewhere. Baylor stays LIVE_IN_GAME outside pregame comparisons. Seven references remain not recovered in this scope; all11causal/pre-execution links remain UNVERIFIED.
Disposition: IMMUTABLE_REFERENCES_RECOVERED / FOUR_RECORDED_LIMIT_COMPARISONS_VERIFIED / GENUINE_PREEXECUTION_ATTRIBUTION_INCOMPLETE. Separate terminal closure will retain RUN_INCOMPLETE for this attribution workload. Existing production/scheduler/opaque-write/raw-clock debts remain unchanged. Scientific/Champion effect:NONE; no historical decision/model/market/HotSheet/scorecard/task changes.

## Historical October2 execution-card lineage and bounded search

Run CFB_HISTORICAL_CARD_LINEAGE_QA_20261009T233144Z; audit evidence/operational/CFB_ORIGINAL_WAGER_EXECUTION_CARD_LINEAGE_AUDIT_2026-10-09.json, blob ff6e1274c08ebc734e1ae3d822e49e49e4182535. Exact HotSheet evidence/operational/CFB_WEEK5_HOT_SHEET_2026-09-29_2020CT.md at commit 093a8c978e4441ebda5168ba871ff99e9f9bd826, blob a018b009d6ed4cf29fc5f774e39194ab2815378e, persisted October3 00:44:04Z /October2 19:44:04CT. Internaltitle establishes October2Fridayeveningrefresh despite September29filename; never use filename as timestamp. Commit is direct child of decisionledger09c479bca87e08b92b9d3e42b539b27c21be8120, recorded6seconds earlier. Immutable versions, not currenthead prose, govern historicalreference.
Ten actual-data checks passed:fiveuniquecardgames,47uniquemodeleddisplayrows,allfivecardgamesinfullslateandexplicitpinnedBETNOWledger,4of5actualOct2ticketsoncard,Wisconsinsoleoff-cardticketandpresentonceinfullslate,UMasssolecardentrywithoutoriginalticket,directparentlineage,unverifiedlinks preserved. AliasesConnecticut/UConn andMassachusetts/UMass explicit. Initial local extraction excluded four-column cardrows, then missed UMassalias; both failed closed before auditfile creation; corrected extraction and alltenchecks passed. These probe corrections did not modify historicalcards or create productiondecisions.
Wisconsin is PRESENT in full modeledslate, not missingfromthepublishedboard; it is absentfromtheexplicitfive-selectionexecutioncard. This narrows prior no-BETNOW-match finding without inferring a recommendation from its frozen/benchmark display. Originalactualwager remains validexecutionevidence; off-card describes membershiponly, not userauthorization. UMassrecommendation remains without executionevidence, not assumedplaced. Prior4cutoffcomparisons remainvalid but genuinepreexecution/causal attribution stillUNVERIFIED.
Scoped conversationcontext search recovered reportedwager/grading summaries, market-only observations and five-card summaries; no originalpreexecution Wisconsin/September26recommendation message orreceipt-timezoneconfirmation recovered. Retrievalsummary is not originaltranscript/deliveryproof; inconsistentrelative-age labels excluded. Searchcompleteness NOT_CERTIFIED: neverinfer noearlierrecommendationexistedsomewhereelse. SixSeptember26links remainunrecovered;BaylorLIVE staysoutsidepregamecomparisons. No additionalgeneralhistorysearch is repeated without anewspecificlead.
Disposition:CARD_LINEAGE_VERIFIED / ATTRIBUTION_RUN_INCOMPLETE. Persisted checkpoint does not close receiptclock,independentgameidentity/delivery/causalchoice,budget,settlement,CLV orsource-rulequalification. Olderfailure/rawclock403debts unchanged. No currentHotSheet/market/decision/scorecard/model/scheduler change;scientific/Champion effect:NONE.

## October9 issued tickets — original intake October10 10:45 CT

Run:CFB_OCT09_TICKET_INTAKE_20261010T154541Z; original-source manifest evidence/operational/CFB_OCT09_ORIGINAL_TICKET_INTAKE_2026-10-10.json, blobfbcc829cedaedf6d35c99f8e947e1b2553a8a850. Two visually distinct issued Caesars Sportsbook / Harrah's Columbus tickets establish ACTUAL_REAL_MONEY execution. Original images remain in the user's uploaded-file store; untouched SHA256/source IDs in manifest. Cashable serials, barcode/QR contents and raw images excluded from public repository. Duplicate sweep against current ledger and original eleven-ticket manifest found no equivalent October9-issued rows; these are two new distinct wagers, not repeat photos of prior tickets.

| Execution ID | Issued date/time as printed | Game | Selection / market | Accepted line | American odds | Stake USD | Max win / payout printed USD | Receipt event time |
|---|---|---|---|---|---|---|---|---|
| CFB_OCT09-01 | 2026-10-09 08:31 PM | James Madison at Georgia Southern | James Madison / SPREAD | -7.5 | -107 | $5.00 | $4.65 / $9.65 | 2026-10-10 06:35 PM |
| CFB_OCT09-02 | 2026-10-09 08:27 PM | Boise State at Fresno State | Fresno State / SPREAD | +7 | -113 | $5.00 | $4.40 / $9.40 | 2026-10-10 09:35 PM |

Common qualification: budgetallocation UNASSIGNED production/sandbox; receipt timezone UNSPECIFIED; NOT_LIVE_LABELLED; independent execution/kickoff chronology, genuine recommendation attribution, settlement/redemption/payment and CLV UNVERIFIED. Printed next-day event dates are receipt facts, not independent kickoff certification. Both event clocks are five minutes later than saved operational displays; do not replace those clocks or extend a cutoff. Intake date is not wager-issued date.

Bounded decision-reference comparison: canonicaldecision blob2fa8428caad7e57204c1c9ca6ce5fee4d9acaa5c records Fresno+7-or-better/max-115; accepted+7/-113 is compatible with those numbers. This is numericcompatibility only, not proof of receipt-timezone, preexecutiondecision sequence or causalrecommendation. Its prior public+6.5WAIT remains preserved; an executed+7ticket does not rewrite that observation. Current saved JMU side is PASS; actual ticket is recorded separately without turning PASS into BETNOW or asserting no other prior advice existed. No outcome-driven attribution or frozen prediction alteration.

New actualstake$10.00; printed combinedmaxwin$9.05 / combinedmaxpayout$19.05 ifbothwin, not guaranteed realized returns. Prior11wagers/$33.45 plus these2 =13establishedactualwagers/$43.45 totalhistoricalstake. No new settlement or profit booked. Execution prices certify what these tickets accepted at their printed issue clocks only, not currently available Caesars offers or marketconsensus.

## Additional October9 issued tickets — original intake October10

Run: CFB_OCT09_ADDITIONAL_TICKET_INTAKE_20261010T155228Z; source manifest evidence/operational/CFB_OCT09_ADDITIONAL_ORIGINAL_TICKET_INTAKE_2026-10-10.json, blob 0eaed6f744bdb47f4dc475730a0cdc210a161641. Two additional visually distinct original issued Caesars Sportsbook / Harrah's Columbus tickets establish ACTUAL_REAL_MONEY execution. Private ticket identity and original-byte hash comparison found no duplicates among prior thirteen wagers. Raw images and cashable identifiers excluded from this repository.

| Execution ID | Issued date/time as printed | Game | Selection / market | Accepted line | American odds | Stake USD | Max win / payout printed USD | Receipt event time |
|---|---|---|---|---|---|---|---|---|
| CFB_OCT09-03 | 2026-10-09 08:26 PM | Old Dominion at Appalachian State | Appalachian State / SPREAD | -10 | -110 | $5.00 | $4.55 / $9.55 | 2026-10-10 12:05 PM |
| CFB_OCT09-04 | 2026-10-09 08:26 PM | Miami (OH) at Massachusetts | Massachusetts / SPREAD | +5 | -110 | $5.00 | $4.55 / $9.55 | 2026-10-10 01:05 PM |

Common fields: budget UNASSIGNED production/sandbox; receipt timezone UNSPECIFIED; NOT_LIVE_LABELLED; authoritative kickoff/execution chronology, genuine pre-execution recommendation attribution, settlement/redemption/payment and CLV UNVERIFIED. Receipt event times do not replace operational kickoff clocks or extend practical cutoffs. App State -10/-110 and Massachusetts +5/-110 numerically satisfy saved -10-or-better and +4.5-or-better/max-115 limits; this is numeric compatibility only, not causal recommendation or pre-execution sequence certification. Current offers/consensus are not certified by historical tickets.

Additional actual stake $10.00; prior thirteen wagers/$43.45 plus two = fifteen actual wagers/$53.45 cumulative historical stake. All four October9-issued tickets now total $20.00 staked; combined printed maximum payout $38.15 if all four win, not realized cash. No settlement or profit booked. User instruction "Also add 20 to money ledger" retained as PENDING_CLARIFICATION: additional bankroll funding versus the four-ticket stake total unspecified. No additional $20 debit or capital credit booked, no budget assignment or changed sandbox balance inferred. No model, frozen prediction, decision, market, Hot Sheet, scorecard or scheduler change.


## Week 6 authoritative settlement — 2026-10-11 07:18 CT

**Cycle:** CFB_MARKET_MONITOR_20261011T120436Z  
**Scope:** Settlement of four established October 9-issued tickets only. Ticket identity, accepted line/price, and unassigned production/sandbox classification remain unchanged. Results do not prove causal recommendation attribution, receipt timezone, or execution chronology and do not alter frozen predictions or earlier decisions.

| Execution ID | Selection | Stake | Accepted price | Authoritative final | Grade | Return | Net P/L | Result source |
|---|---|---:|---|---|---|---:|---:|---|
| CFB_OCT09-03 | Appalachian State -10 | $5.00 | -110 | Old Dominion 10, Appalachian State 3 | LOSS | $0.00 | -$5.00 | Appalachian State Athletics: https://appstatesports.com/sports/football |
| CFB_OCT09-04 | Massachusetts +5 | $5.00 | -110 | Miami (OH) 20, Massachusetts 19 | WIN | $9.55 | +$4.55 | Massachusetts Athletics: https://umassathletics.com/news/2026/10/10/football-minutemen-comeback-falls-one-point-short-to-miami-oh-20-19 |
| CFB_OCT09-01 | James Madison -7.5 | $5.00 | -107 | James Madison 27, Georgia Southern 24 | LOSS | $0.00 | -$5.00 | James Madison Athletics: https://jmusports.com/news/2026/10/11/football-dukes-grind-out-road-win-at-georgia-southern |
| CFB_OCT09-02 | Fresno State +7 | $5.00 | -113 | Boise State 38, Fresno State 31 | PUSH | $5.00 | $0.00 | Reuters: https://www.reuters.com/sports/top-25-roundup-south-carolina-hands-no-16-florida-second-straight-loss--flm-2026-10-10/ |

**Settlement arithmetic:** $20.00 stake; $14.55 return; **-$5.45 net P/L**. No redemption/payment status is inferred. The prior “additional $20” ambiguity remains unresolved; no additional debit, capital credit, or budget assignment is booked.


## October17 issued tickets — original intake October23 QA

Run: CFB_BALANCED_EFFECTIVENESS_QA_20261023T163207Z. Observed intake recording clock 2026-10-23T16:44:40.998961+00:00. Original evidence: evidence/operational/CFB_OCT17_ORIGINAL_TICKET_INTAKE_2026-10-23.json at Git blob ebddadf7b10d6b2e7a0442aa282185d872500517. Nine distinct issued Caesars Sportsbook / Harrah's Columbus tickets, individually visually inspected and privately deduplicated, establish ACTUAL_REAL_MONEY executions. This corrects absent intake; records were not invented from recommendations or outcomes.

| Execution ID | Issued date/time as printed | Game | Selection / market | Accepted line | American odds | Stake USD | Max payout printed USD | Receipt event time |
|---|---|---|---|---|---|---|---|---|
| CFB_OCT17-01 | 2026-10-17 13:26 | North Carolina at Duke | North Carolina / SPREAD | +3 | -110 | $5.00 | $9.55 | 2026-10-17 14:40 |
| CFB_OCT17-02 | 2026-10-17 13:22 | Penn State at Michigan | Penn State / SPREAD | +6 | -110 | $5.00 | $9.55 | 2026-10-17 14:45 |
| CFB_OCT17-03 | 2026-10-17 13:31 | Alabama at Tennessee | Tennessee / SPREAD | +7.5 | -110 | $2.50 | $4.75 | 2026-10-17 14:50 |
| CFB_OCT17-04 | 2026-10-17 13:25 | Kentucky at Oklahoma | Oklahoma / SPREAD | -6.5 | -117 | $2.00 | $3.70 | 2026-10-17 18:45 |
| CFB_OCT17-05 | 2026-10-17 13:24 | Nebraska at Oregon | Nebraska / SPREAD | +7.5 | -110 | $5.00 | $9.55 | 2026-10-17 18:05 |
| CFB_OCT17-06 | 2026-10-17 13:23 | Oklahoma State at Houston | Houston / SPREAD | -4 | -112 | $5.00 | $9.45 | 2026-10-17 18:40 |
| CFB_OCT17-07 | 2026-10-17 13:21 | Georgia Tech at Virginia Tech | Virginia Tech / SPREAD | -8.5 | -112 | $5.00 | $9.45 | 2026-10-17 14:40 |
| CFB_OCT17-08 | 2026-10-17 13:20 | UNLV at Air Force | Air Force / MONEYLINE | N/A | +102 | $2.00 | $4.05 | 2026-10-17 14:40 |
| CFB_OCT17-09 | 2026-10-17 13:29 | Missouri at Ole Miss | Ole Miss / SPREAD | -4 | -112 | $2.55 | $4.85 | 2026-10-17 14:45 |

Common qualification: budget UNASSIGNED production/sandbox; receipt timezone UNSPECIFIED; NOT_LIVE_LABELLED does not certify pregame timing. Displayed event times do not replace independent kickoffs or extend cutoffs. No current offer, recommendation delivery/causal adoption, paid return, bank movement or CLV is inferred. All nine printed ticket identities are distinct and are not prior September26/October2/October9 tickets. Image source IDs/SHA256/size and Nebraska display-order qualification are retained in the manifest; raw serials/barcodes/QR/images excluded from repository. New stake $34.05; prior15/$53.45 plus9 =24 actual wagers/$87.50 cumulative historical stake. The money ledger funding reference remains its unchanged historical15-ticket snapshot, not a claim current total is15. No new funding/allocation or changed sandbox ceiling.

### Derived Week7 final-score grades and saved recommendation comparison

Sources: evidence/scheduler_qa/CFB_BALANCED_EFFECTIVENESS_QA_20261023T163207Z_RESULTS.json; immutable scorecard Git blob d210d8c51106ef393a23a4fb69c6fcdb219e3f16 and pre-event review Git blob 35d11b59ee76d1876060c869efd0950313657fa9. Complete individual references/rationales and reproducible arithmetic in evidence/scheduler_qa/CFB_BALANCED_EFFECTIVENESS_QA_20261023T163207Z_AUDIT.md.

| Execution ID | Grade | Result return using printed payout | Result net | Historical recommendation comparison |
|---|---|---|---|---|
| CFB_OCT17-01 | WIN | $9.55 | $4.55 | OUTSIDE_FINAL_FIVE_RECOMMENDATIONS |
| CFB_OCT17-02 | WIN | $9.55 | $4.55 | WITHIN_RECORDED_LIMITS |
| CFB_OCT17-03 | WIN | $4.75 | $2.25 | OUTSIDE_FINAL_FIVE_RECOMMENDATIONS |
| CFB_OCT17-04 | LOSS | $0.00 | $-2.00 | OUTSIDE_FINAL_FIVE_RECOMMENDATIONS |
| CFB_OCT17-05 | WIN | $9.55 | $4.55 | WITHIN_RECORDED_LIMITS |
| CFB_OCT17-06 | LOSS | $0.00 | $-5.00 | OUTSIDE_RECORDED_PRICE_LIMIT |
| CFB_OCT17-07 | WIN | $9.45 | $4.45 | OUTSIDE_RECORDED_PRICE_LIMIT |
| CFB_OCT17-08 | WIN | $4.05 | $2.05 | WITHIN_RECORDED_LIMITS |
| CFB_OCT17-09 | WIN | $4.85 | $2.30 | OUTSIDE_FINAL_FIVE_RECOMMENDATIONS |

Aggregate7WIN/2LOSS/0PUSH, $34.05 stake, $51.75 result return, +$17.70 result net using printed payouts and ordinary full-game grading. This is not verified book settlement/adjudication/redemption/payment or available cash. Printed cents are not silently replaced by theoretical odds arithmetic. Three within-limit tickets (Nebraska, Penn State, Air Force) graded3–0; VT/Houston prices-112 exceeded preserved-110 floors (1–1); four other tickets were outside final five (3–1). Receipt timezone/pre-execution/causal attribution remain UNVERIFIED. No historical decision is changed to match the actual ticket or its result; original five-card shadow4–1 remains a separate population. This prospective intake supersedes prior no-established-Week7-execution descriptions only from now onward. Historical weekly review bytes and its earlier ledger boundary remain intact.


## October23 issued tickets — canonical backlog integration

Run: CFB_BACKLOG_20261023T231844Z. Source: evidence/operational/CFB_OCT23_ORIGINAL_TICKET_INTAKE_2026-10-23.json at 98d5f3fe20584e79856906b63d9b81f4d1812a54; private saved intake version 2. Eight distinct actual real-money spread tickets at Caesars Sportsbook / Harrah's Columbus. Historical deduplication: all prior 24 executions have earlier issue dates, no October23 rows exist at this fresh boundary, and the saved intake contains eight distinct private ticket identities. Raw images/serials excluded; original image-byte hash replay not performed here.

| Execution ID | Issued date/time as printed | Game | Selection / market | Accepted line | American odds | Stake USD | Max win / payout printed USD | Receipt event time |
|---|---|---|---|---|---|---|---|---|
| CFB_OCT23-01 | 2026-10-23 15:47 | Air Force at Wyoming | Air Force / SPREAD | -5.5 | -110 | $5.00 | $4.55 / $9.55 | 2026-10-23 20:10 |
| CFB_OCT23-02 | 2026-10-23 15:55 | NC State at Stanford | NC State / SPREAD | -7.5 | -107 | $3.00 | $2.80 / $5.80 | 2026-10-23 21:40 |
| CFB_OCT23-03 | 2026-10-23 15:48 | LSU at Auburn | Auburn / SPREAD | +7.5 | -110 | $5.00 | $4.55 / $9.55 | 2026-10-24 11:10 |
| CFB_OCT23-04 | 2026-10-23 15:51 | Texas Tech at Cincinnati | Cincinnati / SPREAD | +11.5 | -106 | $5.00 | $4.70 / $9.70 | 2026-10-24 11:05 |
| CFB_OCT23-05 | 2026-10-23 15:52 | West Virginia at TCU | West Virginia / SPREAD | +10.5 | -108 | $5.00 | $4.65 / $9.65 | 2026-10-24 11:05 |
| CFB_OCT23-06 | 2026-10-23 15:54 | Bowling Green at Buffalo | Buffalo / SPREAD | -3 | -115 | $5.00 | $4.35 / $9.35 | 2026-10-24 14:35 |
| CFB_OCT23-07 | 2026-10-23 15:49 | Michigan State at UCLA | UCLA / SPREAD | -14.5 | -112 | $5.00 | $4.45 / $9.45 | 2026-10-24 14:35 |
| CFB_OCT23-08 | 2026-10-23 15:56 | Ole Miss at Texas | Texas / SPREAD | -3 | -115 | $3.00 | $2.60 / $5.60 | 2026-10-24 18:40 |

Common fields: ACTUAL_REAL_MONEY; budget UNASSIGNED production/sandbox; receipt timezone UNSPECIFIED. Printed issue precedes printed event for all eight; authoritative kickoff chronology and pregame execution are not independently certified. NOT_LIVE_LABELLED; do not mix with explicit Baylor LIVE_IN_GAME. No outcome, sportsbook settlement, paid return, redemption, causal recommendation attribution or CLV is established. Historical tickets are not current available offers. Preserve all recommendation limits and original decisions; separate comparison remains pending.

Batch: 8 actual tickets / $36.00 stake / $32.65 printed maximum win / $68.65 printed maximum payout conditional on all eight winning. Prior24 / $87.50 plus8 / $36.00 =32 established actual wagers / $123.50 cumulative historical stake. This is an inventory count, not32 settled observations or complete lifetime history. User's recollection of eight last week versus nine distinct October17 tickets remains an unresolved count discrepancy; no existing tickets deleted or merged. No result assigned to the eight new tickets.

The same private record establishes the complete current pot $61.30 = $25.30 voucher funds + these $36.00 open stakes at cost at the user's baseline. That snapshot is posted separately in the money ledger, not another wager debit/deposit/return. Historic funding and result-derived returns are not added again. No model input, market, recommendation, frozen prediction, stake rule, allocation ceiling or schedule changed.

## Week 8 Friday established-wager final-score grades — October 24

**Cycle:** `CFB_MARKET_MONITOR_20261024T120126Z`

**Result source:** fresh complete CBS Week 8 response recovered by `2026-10-24T12:04:02Z`, retained at `evidence/operational/CFB_CBS_WEEK8_TEXT_TABLE_CAPTURE_20261024T120402Z.md`. The source page displayed final scores of Wyoming 28, Air Force 14 and Stanford 31, NC State 28.

**Scope:** deterministic full-game score grading for the two established October 23 Friday tickets only. This is not sportsbook settlement, adjudication, redemption, cash payment, current offer, CLV or recommendation attribution.

| Execution ID | Selection | Accepted spread / price | Final (selection first) | Signed spread result | Final-score grade | Printed result return | Result net |
|---|---|---|---|---:|---|---:|---:|
| CFB_OCT23-01 | Air Force | -5.5 / -110 | Air Force 14, Wyoming 28 | -19.5 | LOSS | $0.00 | -$5.00 |
| CFB_OCT23-02 | NC State | -7.5 / -107 | NC State 28, Stanford 31 | -10.5 | LOSS | $0.00 | -$3.00 |

Friday batch: `0 WIN / 2 LOSS / 0 PUSH`, `$8.00` graded stake, `$0.00` result return, `-$8.00` result net. Six October 23 Saturday tickets remain ungraded/open at this boundary (`$28.00` stake). The prior `$61.30` opening-pot snapshot is not recomputed here because sportsbook settlement/payment and the user's current voucher/cash balance remain unverified. Production versus `$20` sandbox allocation remains `UNASSIGNED`; no sandbox execution is inferred. Frozen predictions and original recommendation limits remain unchanged.

## Week 8 Saturday established-wager final-score grades — October 25

**Cycle:** `CFB_MARKET_MONITOR_20261025T120550Z`

**Result source:** fresh complete CBS Week 8 response at `evidence/operational/CFB_CBS_WEEK8_RESULTS_CAPTURE_20261025T120800Z.md` / Git blob `2aa53f5793bb511373eba9bbbf6e6249d3984836`. Official school result pages independently corroborate the six ticket finals.

**Scope:** deterministic full-game grading for the six established October 23 Saturday tickets. Printed ticket payouts are retained; this is not sportsbook adjudication, redemption, payment, available cash, CLV, or recommendation attribution.

| Execution ID | Selection | Accepted spread / price | Final (selection first) | Grade | Printed result return | Result net |
|---|---|---|---|---|---:|---:|
| CFB_OCT23-03 | Auburn | +7.5 / -110 | Auburn 17, LSU 38 | LOSS | $0.00 | -$5.00 |
| CFB_OCT23-04 | Cincinnati | +11.5 / -106 | Cincinnati 37, Texas Tech 24 | WIN | $9.70 | +$4.70 |
| CFB_OCT23-05 | West Virginia | +10.5 / -108 | West Virginia 24, TCU 20 | WIN | $9.65 | +$4.65 |
| CFB_OCT23-06 | Buffalo | -3 / -115 | Buffalo 31, Bowling Green 24 | WIN | $9.35 | +$4.35 |
| CFB_OCT23-07 | UCLA | -14.5 / -112 | UCLA 28, Michigan State 10 | WIN | $9.45 | +$4.45 |
| CFB_OCT23-08 | Texas | -3 / -115 | Texas 34, Ole Miss 27 | WIN | $5.60 | +$2.60 |

**Saturday batch:** `5 WIN / 1 LOSS / 0 PUSH`, `$28.00` graded stake, `$43.75` printed result return, `+$15.75` result net. **Complete October 23 Week 8 batch:** `5 WIN / 3 LOSS / 0 PUSH`, `$36.00` stake, `$43.75` printed result return, `+$7.75` result net. All eight are now final-score graded; sportsbook settlement/payment remains unverified. The `$61.30` prior pot snapshot is not recomputed without verified book payment/current voucher balance. Production versus `$20` sandbox remains `UNASSIGNED`; no sandbox execution is inferred. Frozen predictions and original recommendation limits remain unchanged.

