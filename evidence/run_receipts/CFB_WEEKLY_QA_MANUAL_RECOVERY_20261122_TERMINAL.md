# CFB Weekly QA manual recovery — terminal candidate

Status: RUN_INCOMPLETE / BOUNDED QA EXECUTED. Trigger: user requested immediate execution of existing Weekly QA task; inline run, not separate scheduled invocation.

STARTUP PASS: evidence/run_receipts/CFB_WEEKLY_QA_MANUAL_RECOVERY_20261122_START.md blob 9f5159a9b9cc520a0217ee4b97d42d1288ec84e5, independent readback.

READBACK PASS: Sunday natural Market Monitor candidate blob 87b66167429e9f7e309ea9bbb1ad2dc8be53718c; display release blob 359357d1b42074ff09eb11245aa4cc492e7457a8; current binding gate script blob 8a6022e3aeea0d5c5fc0e9d455a9b56b4f1eb581; Sunday QA R1 blob 16e74b2cbf8ff6cf80c520b856763fecb19de0b5; postgame scorecard blob 8e158d780b29f529cc029daf9383c19a68819157.

Findings: Nov22 07CT Monitor recorded display PASS, 70 historical games, 68 historical PASS/2 closed conditionals, zero executable wagers; current named-book offers BLOCKED, fresh decisions NOT_ATTEMPTED, canonical publication BLOCKED due to Nov20 reconstructed decision not bound to accepted current canonical pointer. This is not a regression in binding gate: its code rejects provisional publications by design. Week11 scorecard has qualified 67/67; current postgame scorecard contains no accepted Week12 final cohort. Week12 13 real-money tickets/$75 remain UNGRADED, actual settlements unverified. Existing Sunday QA R1 and closure independently corroborate. Do not infer wins, bankroll or actionable plays.

Due scope unresolved: official Week12 70-game final ID qualification NOT_EXECUTED, independent current CBS acquisition NOT_EXECUTED, ticket grades BLOCKED by official finals, Evening consumer display NOT_VERIFIED, exact large-ledger byte verification NOT_EXECUTED, original runtime NOT_EXECUTED. Current task does not become a second Hot Sheet publisher. No mutation to Champion, frozen projections, canonical pointers, wager or money ledgers, or four schedules.

First operational next step: existing Market Monitor's 13CT natural run must perform governed current source/outcome capture, report exact game-ID final provenance, and separately verify market/decision binding without promoting historical provisional offers. Existing Health 16:30CT run reconciles failures. QA to score only independently verified official outcomes. No fifth task or expired cutoff renewal.
