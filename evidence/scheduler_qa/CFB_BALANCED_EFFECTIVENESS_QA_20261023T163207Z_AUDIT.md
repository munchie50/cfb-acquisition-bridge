# CFB balanced effectiveness and control-cost audit — October 23, 2026

Run: CFB_BALANCED_EFFECTIVENESS_QA_20261023T163207Z. Observed audit recording clock: 2026-10-23T16:44:40.998961+00:00. User-directed manual QA under v6 candidate; Production v5 and Champion v1.193 remain active. This is a bounded execution of the existing October17 stabilization agenda, not a new weekly learning review or model acceptance.

## Finding and correction

The most actionable defect was missed execution intake. Nine original issued tickets uploaded October17 CT were recoverable but absent from the current execution ledger. All nine were individually visually inspected; distinct printed identities were compared privately, and untouched image hashes retained in `evidence/operational/CFB_OCT17_ORIGINAL_TICKET_INTAKE_2026-10-23.json`. Every ticket is an actual real-money wager. No cashable identifier or raw image is saved in the repository.

Upload metadata ranges from 2026-10-18T01:38:22.280516Z through 01:40:13.438528Z, before the Sunday review's stated source run CFB_WEEKLY_QA_20261018T135505Z. The old review accurately described its then-empty canonical Week7 intake, but it did not complete the available-original-ticket reconciliation. It cannot now establish that the user placed no Week7 bets. This audit prospectively supersedes that missing-execution description only; the old review and its numbers remain unchanged. Exact writer omission cause is UNKNOWN. Demonstrated seam: reading the execution ledger alone is insufficient to discharge the existing wager-comparison duty when identified original uploads remain unprocessed.

Correction: append the nine executions and derived final-score grades to the existing canonical execution ledger; preserve the old 15-ticket/$53.45 history in full. New established total is 24 distinct actual wagers / $87.50 cumulative historical stake. Funding/allocation, paid cash, the separate $20 sandbox ceiling and all current-week recommendations remain separate.

## Week7 actual tickets and historical comparison

Finals are reused from the accepted scorecard at Git blob `d210d8c51106ef393a23a4fb69c6fcdb219e3f16`. The pre-event comparison is the immutable 40-game review at `35d11b59ee76d1876060c869efd0950313657fa9`, plus each referenced immutable recommendation JSON. Game ID/pair/date are reconciled, with Nebraska ticket's 'Oregon vs Nebraska' display order explicitly distinguished from accepted Nebraska @ Oregon orientation. These exact source references were selected without using outcomes.

| Execution | Actual ticket | Stake | Final away-home | Grade | Printed-payout result return | Comparison to final saved recommendation |
|---|---|---:|---|---|---:|---|
| CFB_OCT17-01 | North Carolina +3 (-110) | $5.00 | 24-20 | WIN | $9.55 | OUTSIDE_FINAL_FIVE_RECOMMENDATIONS |
| CFB_OCT17-02 | Penn State +6 (-110) | $5.00 | 18-21 | WIN | $9.55 | WITHIN_RECORDED_LIMITS |
| CFB_OCT17-03 | Tennessee +7.5 (-110) | $2.50 | 10-26 | WIN | $4.75 | OUTSIDE_FINAL_FIVE_RECOMMENDATIONS |
| CFB_OCT17-04 | Oklahoma -6.5 (-117) | $2.00 | 21-13 | LOSS | $0.00 | OUTSIDE_FINAL_FIVE_RECOMMENDATIONS |
| CFB_OCT17-05 | Nebraska +7.5 (-110) | $5.00 | 14-17 | WIN | $9.55 | WITHIN_RECORDED_LIMITS |
| CFB_OCT17-06 | Houston -4 (-112) | $5.00 | 32-35 | LOSS | $0.00 | OUTSIDE_RECORDED_PRICE_LIMIT |
| CFB_OCT17-07 | Virginia Tech -8.5 (-112) | $5.00 | 24-34 | WIN | $9.45 | OUTSIDE_RECORDED_PRICE_LIMIT |
| CFB_OCT17-08 | Air Force ML (+102) | $2.00 | 31-41 | WIN | $4.05 | WITHIN_RECORDED_LIMITS |
| CFB_OCT17-09 | Ole Miss -4 (-112) | $2.55 | 3-31 | WIN | $4.85 | OUTSIDE_FINAL_FIVE_RECOMMENDATIONS |

Nine tickets: 7 WIN / 2 LOSS / 0 PUSH; $34.05 staked; $51.75 printed-payout-based result return; +$17.70 result net. This is final-score arithmetic conditional on ordinary full-game settlement, NOT verified sportsbook adjudication, redemption/payment or bankroll cash. Printed maximum payouts are retained verbatim; Air Force, Tennessee and Ole Miss have cents differing from theoretical exact American-odds arithmetic, so they are not silently replaced with a different return.

Three tickets met the saved number AND price: Nebraska +7.5/-110, Penn State +6/-110, Air Force ML+102. Their $12 stake graded 3–0, printed-payout result net +$11.15. Two matched selected games but failed the original -110 price floor: Virginia Tech -8.5/-112 (WIN), Houston -4/-112 (LOSS). Better Houston points do not offset a worse price. Those two total $10 stake, result net -$0.55. The other four total $12.05 stake, grade3–1/result net+$7.10 and are outside the final five recommendations: North Carolina, Tennessee, Oklahoma, Ole Miss. These are exact numeric/card-membership comparisons, not proof the engine caused the wagers or that the final card was delivered before execution. Receipt timezone, actual kickoff/execution chronology, qualified closes/CLV and budget attribution remain UNVERIFIED/UNASSIGNED.

Frozen display context remains separate: North Carolina's +3 ticket is opposite the rounded Duke -2.5 favorite but still has a positive 0.5-point display cushion; Oklahoma's -6.5 has a positive model cushion but lost. Ole Miss -4 is beyond the rounded model's -2 yet won. These contrasting cases reject a simplistic 'winner proves edge' or 'model direction equals recommendation' explanation; no calibrated EV, new rule, or outcome-driven tune follows.

## Cross-week results with explicit populations

| Football week | Modeled scorecard population | SU direction | Margin MAE | Total MAE | Established tickets after this intake | Ticket grades | Recorded financial scope |
|---|---:|---:|---:|---:|---:|---|---|
| 4 | 53 FBS-vs-FBS | 36/53 | 14.781 | 11.071 | 6 / $18.05 | 4W–2L, includes Baylor live WIN | Grade-only; full return not booked |
| 5 | 47 modeled | 32/47 | 15.525 | 14.116 | 5 / $15.40 | 3W–2L | Grade-only; full return not booked |
| 6 | 49 modeled | 25/49 | 15.13 | 13.54 | 4 / $20.00 | 1W–2L–1P | $14.55 result return / -$5.45 net |
| 7 | 51 modeled | 32/51 corrected | 12.89 reported, unreconciled | 13.40 | 9 / $34.05 | 7W–2L | $51.75 printed-payout result return / +$17.70 net |

Source reviews: September27 v1.244; October4 RECOVERY_R1; October11 R2; October18 R1. Earlier-week metrics above are reproduced as reported, including their rounding. Week7 SU was independently reconciled from all51 unique existing rows:32 correct, not the31 asserted in the old summary. The daily slices also sum32. Existing flags and independent signed-margin comparisons agree32/51 (62.7%). The probability-threshold classifier is a distinct34/51 from rounded displays; it must not be relabelled margin direction. Rounded error rows imply marginMAE12.8431 versus published12.89; exact original archive recomputation is outside this audit and the full-precision discrepancy remains OPEN, not silently replaced with rounded numbers. Rounded totalMAE13.3980 supports reported13.40. Append the bounded SU correction to the scorecard without changing any original row or forecast. Cohorts differ by team/week/eligibility and are not a matched experiment. Week7 improved versus Week6 in SU/margin error, while total error was nearly flat; Week4 total error was lower. This does not establish monotonic improvement or that tighter controls improved predictions. Week4 excludes its live Baylor execution from any pregame analysis, leaving five not-live-labelled tickets (3W–2L), still without independent pregame timing certification.

Across all24 tickets:15W–8L–1P, one explicit live. A whole-history paid-cash profit is NOT computed because the original11 remain grade-only. The two later fully tabulated result samples (Weeks6–7) total13tickets/$54.05 stake/$66.30 result return/+$12.25 result net; small and heterogeneous, with causal recommendation attribution incomplete. Do not replace this with a production ROI claim. Week7's final five-recommendation shadow4–1 is a different population from the nine actual tickets7–2. Four Week5 tickets numerically matched the recorded five-card limits; Wisconsin was in the modeled board but outside its explicit five-entry execution card, while UMass was on the card without an established October2 ticket. No absence elsewhere is inferred.

## Operational effectiveness: demonstrated gaps, not an invented reliability rate

- Week4 market/decision/close history is incomplete. Later ticket recovery does not restore the missing pre-event recommendation history.
- Week5 required manual persistence/weekly-output recovery; manual success did not establish natural scheduler reliability.
- Week6 had five closed prior-INCONCLUSIVE early windows. They are process losses of review opportunity, not five demonstrated profitable missed bets.
- Week7 had 21 unserved final-review windows after the Saturday afternoon Monitor remained incomplete. Morning saved work and a later manual supported card do not close those windows. The apparent afternoon need for a richer renderer was narrowed by authentic existing-path renewal replay; a new state framework was unnecessary.
- Sunday Week8 publication rejection correctly prevented a Week7 identity/profile substitution, but the review's blanket 'no original Week8 boundary' was subsequently superseded by recovery of genuine September26 original lineage. This was an authority-recovery/adaptation problem; waiting for a new Tuesday candidate was unnecessary.
- October23 natural Monitor reported RUN_PASS while recovery bindings/CI were incomplete; bounded transfer and finishing corrections were manually demonstrated. That is continuing producer/integration debt, not evidence that today's current five recommendations lack research.

No all-schedule success percentage or total manual-hours estimate is published: a full deduplicated expected-invocation denominator and attributable worker-time trace have not been established here. This targeted audit uses the cited historical incidents, not an exhaustive scheduler census. Historical operational failures remain incomplete even after later repairs.

## Control benefit, cost and disposition

| Existing mechanism | Demonstrated benefit | Adverse cost / limitation | Net and disposition / next evidence |
|---|---|---|---|
| Frozen identities, exclusion and outcome separation | Kept original predictions/exclusions immutable through result joins | Requires source/companion recovery; partial recovery falsely suggested absent originals | HELPFUL; keep identity locks, correct recovery interpretation, do not wait for a fresh candidate when originals exist |
| Original number AND price limits | Three actual Week7 tickets qualify; two -112 tickets remain outside -110 floors regardless of results | Some excluded prices win, and no causal expected-value gain is proved | HELPFUL integrity; keep limits. Larger prospective price/number sample needed for economic claim |
| Recommendation/venue decoupling and honest fallback labels | Supported conditional cards can be delivered without verified Caesars or synthetic consensus | Misapplying benchmark/venue checks as universal recommendation prerequisites loses coverage | HELPFUL separation; keep existing October16/17 scope. No extra source prerequisite |
| Existing conditional renewal path | Replay and later real renewed reviews use the current renderer | Earlier blanket redesign diagnosis delayed delivery; real source/material renewal still costs work | HELPFUL; reuse existing path, no richer-state project absent a concrete unmet requirement |
| Exact bytes, hashes, consumer preflight and separate closure | Detected truncated transport, stale frontier and false integrated completion | Manual integration remains costly; green checks do not deliver football research | HELPFUL integrity, MIXED operational effect; keep bounded checks, require natural finishing proof, avoid duplicate equivalent canaries |
| PASS diagnostics and all-market review | Preserved prospective reconsideration; Week7 40-game/120-market review shows actual breadth | A PASS count combines exclusions, elapsed/process cases and researched no-bets; does not prove full fresh football coverage | MIXED; keep reasons/actual research clocks visible; no quotas or historical reopening |
| Sole producer/four-task ownership | Avoided conflicting canonical publishers | Saturday13CT last Monitor leaves later windows without assured review;21 unserved windows documented | MIXED; preserve ownership; prospective coverage adjustment remains open, no task change in this audit |
| Wager quarantine and capital separation | Tickets do not contaminate predictions, and funding isn't wager profit | Quarantine became incomplete intake: nine available tickets omitted from weekly comparison | ADJUST: complete downstream intake now; narrow existing weekly source-completeness clarification, natural demonstration pending |
| Repeated technical QA/manual refresh | Can prove exact bounded saved bytes | Equivalent repetitions cannot prove natural reliability, edge or future coverage; opportunity cost unmeasured | DEFER equivalent repeats; next independent evidence is scheduled producer behavior or genuinely changed inputs |

## Producer correction, baseline and next proof

Append a narrow clarification to the existing weekly review contract: before treating an empty canonical week's execution set as complete wager-comparison work, reconcile identified available original ticket uploads, deduplicate and intake them under current controls, or explicitly carry an intake backlog. Lack of a new ticket source remains unknown; no exhaustive general personal-history search is required. The source-completeness check belongs to existing weekly execution reconciliation; it must not become another prerequisite for forming current-week recommendations. Actual9-image correction plus six rejection mutations demonstrate this bounded case. Natural Weekly QA adoption remains DEMONSTRATION_PENDING.

Stable operational comparison reference is the current Production v5 / Champion v1.193, existing qualitative controlled-Beta path, original limits and four-task ownership, with exact-byte/current-frontier repairs already installed. This audit does not enact a new freeze, scheduler plan, routine promotion, betting rule or gate. Batch discretionary changes through existing weekly QA; genuine integrity or decision-delivery defects still warrant prompt correction. The previously proposed two-complete-week observation has NOT elapsed or proved profitability. In existing weekly records compare on-time actual analytical coverage, natural full-cycle completion/manual rescue, qualified recommendations versus process no-bets, integrity exceptions and separately attributed ticket results. Roll back a discretionary change only on demonstrated cost/false blocking with preserved integrity; do not remove a hash/freeze lock to improve a pick count.

The baseline/cost audit is EXECUTED for this retrospective scope. Financial advantage, full matched-population causal comparison, comprehensive control wall-time cost, natural producer reliability, Saturday late-window coverage, qualified closes and S2 same-cutoff semantic acceptance remain OPEN. Those limitations do not prevent this bounded audit from closing after saved readbacks/integration.

## Reproducibility and evidence

`python evidence/scheduler_qa/cfb_balanced_effectiveness_replay_20261023.py` reuses immutable Git blobs and emits the retained result JSON. It rejects duplicate execution IDs, duplicate images, wrong game identity, invented receipt timezone, invented sandbox allocation and missing tickets. It does not claim a numerical replay proves the visual extraction or source truth. Exact original source sizes/hashes and visual method are in the intake manifest; the nine originals remain private.

Authoritative source bindings at this audit boundary:
- `evidence/CFB_ENGINE_WEEKLY_BETA_LEARNING_REVIEW_2026-09-27_v1_244.md` — Git blob `a2be87b15d66775fde192af99c5f7e1b2b0b11df`.
- `evidence/CFB_ENGINE_WEEKLY_BETA_LEARNING_REVIEW_2026-10-04_RECOVERY_R1.md` — Git blob `daee098decf80e970a732b71dbd689eda3dfd921`.
- `evidence/CFB_ENGINE_WEEKLY_BETA_LEARNING_REVIEW_2026-10-11_R2.md` — Git blob `0dda6d5a92f12ce08512e0509a9ca457870f514b`.
- `evidence/CFB_ENGINE_WEEKLY_BETA_LEARNING_REVIEW_2026-10-18_R1.md` — Git blob `89d646b66ad845ef1f00985ae55ef88cabba92b6`.
- `evidence/operational/CFB_EXECUTION_LEDGER.md` — Git blob `75caee4052e02ea7d2453d1d37fd3866e13ecc07`.
- `evidence/operational/CFB_MONEY_LEDGER.md` — Git blob `3aebcbdcc535479c29c31f18073cba09f59aab01`.
- `evidence/operational/CFB_CLOSING_MARKET_LEDGER.md` — Git blob `29d5b67be99cefb477f3cf05192513379e6bb05f`.
- `evidence/operational/CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md` — Git blob `d210d8c51106ef393a23a4fb69c6fcdb219e3f16`.
- `evidence/operational/CFB_WEEK7_COMPLETE_MULTI_MARKET_REVIEW_20261017T155337Z.json` — Git blob `35d11b59ee76d1876060c869efd0950313657fa9`.
- `evidence/operational/CFB_ORIGINAL_WAGER_EXECUTION_CARD_LINEAGE_AUDIT_2026-10-09.json` — Git blob `ff6e1274c08ebc734e1ae3d822e49e49e4182535`.
- `evidence/scheduler_qa/CFB_ENGINE_HEALTH_20261017T214055Z_AUDIT.md` — Git blob `6e831c449dc11be56b2e841fdedac0cf4c371a93`.
- `evidence/scheduler_qa/CFB_HANDOFF_REPAIR_20261023T121755Z_AUDIT.md` — Git blob `e3c7c291468d0e55dead9c7bd603eaba42823fe7`.
- `evidence/scheduler_qa/CFB_PRODUCTION_RECONCILIATION_20261023T115133Z_AUDIT.md` — Git blob `40af98ab4523237592d0e931cf8350946d8b102b`.
- `evidence/operational/CFB_OCT17_ORIGINAL_TICKET_INTAKE_2026-10-23.json` — Git blob `ebddadf7b10d6b2e7a0442aa282185d872500517`.
- `evidence/scheduler_qa/CFB_BALANCED_EFFECTIVENESS_QA_20261023T163207Z_RESULTS.json` — Git blob `54efec0ee8aa57c85bcdc867902cc600aeedd5a2`.
- `evidence/scheduler_qa/cfb_balanced_effectiveness_replay_20261023.py` — Git blob `0f80fd6dc2909cb6e683b60a5d2ab8496bfa80e8`.

Saved execution append, register/contract changes and navigation identities are certified by this run's terminal candidate/closure after independent readback; this document does not self-certify its persistence. No source price, current decision, sheet, model or original scorecard-row mutation is performed; only a separately labelled scorecard summary reconciliation is appended.
