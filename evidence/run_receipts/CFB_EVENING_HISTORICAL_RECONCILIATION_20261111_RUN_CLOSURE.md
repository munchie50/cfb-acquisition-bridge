# Evening Availability historical receipt reconciliation

Recorded 2026-11-11T02:29:48.496Z. RUN_PASS for the retained receipt census and recovery integration.

evidence/scheduler_qa/CFB_EVENING_RECEIPT_RECONCILIATION_20261111.json blob a4c6f5f27bfb2c355341e79ceb74705de88044ef records 34 retained files and 12 exact closure-to-candidate links across 14 Wed/Thu/Fri slots from October 8 through November 6 CT. Five original closures report RUN_PASS and seven report RUN_INCOMPLETE. The October 15 candidate uses a legacy filename and the closure binds its exact blob. Standard startup files for October 14 and 15 remain absent. November 4–6 each records GitHub DNS resolution failure after startup.

October 8 and October 30 natural closures remain unrecovered. The October 30 historical producer replay remains an incomplete replay. Broader scheduler-event and Health coverage remain open.

Recovery v1.283 blob 5a030e90df65f0261140e36920e3c89d3b0490dc passed the 472-reference preflight and exact repository readback. CI 42945584580 succeeded at 7372acec4549e55b265df99b32f16462851dcea3. Next production Monitor slot is Wednesday, November 11 at 07:00 CT.
