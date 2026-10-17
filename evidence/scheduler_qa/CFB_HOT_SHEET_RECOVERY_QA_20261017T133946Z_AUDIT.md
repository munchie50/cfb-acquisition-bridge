# Hot Sheet recovery consumer reconciliation — Test Routine v6

Run: CFB_HOT_SHEET_RECOVERY_QA_20261017T133946Z
Scope: user-directed static integration QA, not a new Market Monitor or market observation.
Baseline main: 14bbbc407afb75cbe019baaf7ef979b9c9102f3c.

## Trigger and reproduced failure

Morning scheduled cycle CFB_MARKET_MONITOR_20261017T120424Z persisted RUN_PASS, while existing full Hot Sheet CI39031845936/job117393704557 failed at money-ledger selection. Independently decoded logs identify `missing/ambiguous/stale current money selector`; later whole-publication checks were skipped. Original scheduled closure, checkpoint and failed CI remain historical evidence, unchanged. Operational completion and independent integrated CI are separate claims.

The newest checkpoint had nine pointers and omitted four dependencies required by current consumers: money ledger, R2 weekly learning review, original Week7 lineage census and the October11 historical Health source required by that exact review. Existing earlier complete checkpoint and current exact repository bytes establish these references; no filename/version guessing or automatic reader inheritance. New bounded preflight reproduced all four omissions before correction.

## Correction and prevention

Appended a prospectively complete checkpoint; original history retained. New read-only scripts/cfb_recovery_consumer_preflight.py checks every declared pointer hash plus existing money/weekly/current-publication consumer bindings. Eight regression methods exercise complete boundary, each missing dependency, later-checkpoint omission despite valid historical pointer, stale hash, missing roles, duplicate role, optional stale pointer and internally stale sheet decision binding. No generic reader/schema weakening.

Active persistence procedure requires proposed-index preflight BEFORE navigation write and independent readback/recheck afterward. Existing Hot Sheet workflow runs the new regressions and preflight before the unchanged money/weekly checks. Bounded current Week7/October11 review qualification is explicit; a future weekly consumer requires separate qualification. No new workflow dispatch, task, schedule, feed account or purchase.

## Executed evidence

108 affected local tests PASS:8 new preflight,28 money,25 carry-forward,20 navigation,27 current-publication. Real money/review/source guards pass on exact bytes; original +$20 funding remains one unassigned transaction. Whole saved-publication audit at observed2026-10-17T13:42:12Z PASS:62 games, no elapsed-current-quote or overdue-open-decision exceptions. An earlier manually supplied13:43Z audit argument was a prospective diagnostic, not actual-clock proof; the observed-clock repeat above governs current exception reporting.

Code7931f6b609c7ec00cc0ded5ba03118ad8893b624/test521486c2f4e571c31344b90e7341b36328373150/procedurea58839b8551554a4514afad5dbbf8ff34889115e/indexf9f893309149a199af88f1984162c68bc1083367/workflowddcd47a978fa0ed7d29a3e142c759edf9dae900d independently fetched and exact-content matched after serial Contents writes. Existing CI39037623741 at739b4ae86db6f8071360530a7cb78c76c6a394de had passed new preflight, money, weekly review, selected publication binding and accepted archive retrieval at this audit boundary; remaining CI/terminal proof belongs in the separate terminal candidate and closure.

## Expected versus actual and remaining debt

Expected: restore complete dependency boundary, reject omissions before write, keep source/decision/scientific/capital bytes unchanged, independently verify full current sheet. Actual bounded local and persisted/readback behavior matches; full independent CI completion pending at this document boundary.

Hot Sheet unchanged atb8a3b3627201a99fe13d7f758045dd48a0d66e3a:41PASS21INCONCLUSIVE,zero actionable recommendations,62exact-once. Market210e16209b064f7acadc9bb86772de845668e324;decision8eba1865589019028888297766f5f3482da76134;execution75caee4052e02ea7d2453d1d37fd3866e13ecc07;money3aebcbdcc535479c29c31f18073cba09f59aab01 unchanged. Original51predictions11exclusions/153numbers remain frozen. Caesars is not a recommendation prerequisite; identified qualified market data, material review, earned rule/limits remain separate unresolved readiness requirements. Source-access choice remains under existing control; no provider silently selected. Productionv5 active/v6candidate,Champion unchanged.

Status: CORRECTED/PERSISTED/READ_BACK/LOCAL_DEMONSTRATED; independent full CI and two-phase closure pending here. Natural future producer use of this additional prewrite control remains DEMONSTRATION_PENDING; next ordinary scheduled navigation update is the trigger. Earlier gaps/failures are not retrospectively upgraded.
