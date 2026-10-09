# Test Routine v6 — Evening health coverage and October 9 afternoon reconciliation

Scope: user-directed operational QA continuation. Production Routine v5 and Champion v1.193 unchanged.

## Trigger and recovered authority
Evening Availability's October 8 invocation has no recovered durable evening terminal receipt. Its response-derived write failure and self-disabling are preserved in the active persistence procedure and October 9 lifecycle repair record. Live task readback shows it restored/enabled. Health explicitly audited Market Monitor receipts but did not explicitly audit evening-cycle closure. Recovery doorway v1.245 still described natural afternoon proof as pending after new afternoon evidence became available.
Recovered v1.133 core controls, candidate Routine v6, active persistence procedure and October 5 terminal closure contract before mutation.

## Independent afternoon reconciliation
Natural scheduled cycle CFB_MARKET_MONITOR_20261009T180108Z was read independently, with closure at commit f57e511cbe24276169241f1f069d81395d635a60.
Exact read-back blobs:
- STARTED 562f2eb6b16f66ef7879303c74c217c49a0ae73a.
- terminal candidate 36f0782dd840114aa22ef109a6054d60ded77fd4.
- separate closure 0aef35d8204a5c48c142ca8724cf33c0401c297a, ending RUN_PASS.
- market bbc222ec291ba1faff3f083f6da132d8e8214cae.
- decision fcbdc7f48e8518dc6826d0d39c06d864da1a12e9.
- Hot Sheet 0d99c7c2aa1cebbce35e726992c38fa7e6c43083.
- execution unchanged b2ecc4f277ce97bea8caf204a406b8073e3d6e9a.
- scorecard unchanged 6ae881224fa18b65a4408fa807a2582aebccf6fd.
Executed structural reconciliation: 49 rows, 49 unique displayed game identities, section counts 1/2/3/5/7/17/14, Friday and Saturday morning PASS, 31 later Saturday INCONCLUSIVE, Nebraska separately unmodeled. Six assertions passed. This corroborates structural/output and closure evidence for this single real producer cycle; it does not independently qualify every source quote, certify scientific decision quality, identify the opaque earlier rejection, or prove sustained reliability.

## Installed correction
Appended EVENING AVAILABILITY COMPLETION AUDIT to existing Dual Engine Health task 6ab4296b60608191a7ebb238d4fa70bd. It now checks due evening cycles after their allowed flexible window, separates metadata/runtime reports from durable closure, verifies applicable outputs, checks enabled/cadence/downstream ownership and records exceptions in the existing health receipt. No new lifecycle-mutation authority is granted. Existing Market Monitor restoration instruction remains unchanged.
Independent fresh task readback passed 68 assertions: same 11-task inventory; exactly four enabled tasks; every title/schedule/timing mode/timezone/enabled state unchanged; all 10 other prompts unchanged; health prompt equals its complete old bytes plus the intended suffix. Disabled temporary/retired tasks remain disabled. No fifth active task, new schedule, run-now, canonical operational write or model change.

## Demonstration record and debt
Trigger: missing evening durable closure plus asymmetrical receipt monitoring.
Expected: existing health producer detects an elapsed evening cycle lacking conforming closure, without treating a future cycle as missed or replaying it.
Actual: control appended and exact prompt independently read back; evening historical gap remains visible; afternoon structural/closure evidence independently reconciled.
Classification: HEALTH_CONTROL_INSTALLED_AND_READ_BACK; NATURAL_HEALTH_AUDIT_DEMONSTRATION_PENDING. This is not a completed health run.
Next natural triggers: today's 16:30 CT flexible Health cycle can inspect last night's elapsed evening cycle; tonight's 19:30 CT flexible Evening Availability supplies its own corrected producer proof; subsequent Health can reconcile tonight's closure.
Afternoon classification: SINGLE_NATURAL_SCHEDULED_OUTPUT_AND_CLOSURE_RECONCILED. Earlier morning STARTED-only and October 8 evening incomplete evidence remain unrepaired historical gaps.
Still OPEN: opaque real write-rejection cause, repeated production reliability, natural evening end-to-end demonstration, natural failure-report envelope demonstration, optional formatter/metadata runtime integration. Successful afternoon execution does not prove the failure guard's rejection branch.
No equivalent canary was repeated because existing real evidence plus the next natural runs are the appropriate proof classes.
Scientific/Champion effect: NONE. Routine promotion: NONE.


## Continued test routing — time-window and unresolved-cycle replay

Trigger: the new evening audit used a moving prior-health boundary. A still-unresolved October 8 evening gap would fall outside a later newly-due-only scan after today's health invocation. That is an audit coverage loss, not evidence of completion.

Correction: appended UNRESOLVED CYCLE CARRY-FORWARD to the same Health task. Every audit now recovers unresolved cycle identities from the last persisted health audit, combines them with newly due cycles and records coverage/evidence/blocker/next action. Missing prior audit cannot silently advance coverage. A gap can only resolve through genuine contemporaneous evidence or a governed disposition retaining historical incompleteness. No task-lifecycle authority or new schedule was added.

Executed deterministic replay: ten cases passed. These are manual QA classifications using recovered evidence, not a scheduled Health execution. Synthetic mutations are explicitly labelled and never written as operational run evidence. Evening schedule uses its existing 19:30 CT flexible window; the harness waits through 20:30 inclusive before classifying absence. This is a dispatch-window boundary, not a promised completion deadline. STARTED-without-closure indicates missing proof, never that the invocation is still active.

Pinned evidence: repository tree 7fcab355289b566d65ec9d1d0464d27178347de1; recovered October 8 evening observation blob e3fa5e4036c6e6342b7073d7a2c107d01b87fd8a; morning response/STARTED reconciliation blob 3aea990e8fbd940386c210b7dab0ff9e2bbe6422; afternoon exact surface blobs listed above and closure commit persisted at 2026-10-09T18:05:40Z. Current live task metadata is observation evidence, not a historical task snapshot. No synthetic future condition asserts that tonight will fail.

Replay cases and results:
```json
[
  {
    "label": "Tonight before window",
    "start": "2026-10-09T19:30:00-05:00",
    "windowEnd": "2026-10-09T20:30:00-05:00",
    "asof": "2026-10-09T15:04:44-05:00",
    "expected": "NOT_DUE",
    "actual": "NOT_DUE"
  },
  {
    "label": "Tonight window opening",
    "start": "2026-10-09T19:30:00-05:00",
    "windowEnd": "2026-10-09T20:30:00-05:00",
    "asof": "2026-10-09T19:30:00-05:00",
    "expected": "WINDOW_OPEN_NO_COMPLETION_CLAIM",
    "actual": "WINDOW_OPEN_NO_COMPLETION_CLAIM"
  },
  {
    "label": "Tonight window end inclusive",
    "start": "2026-10-09T19:30:00-05:00",
    "windowEnd": "2026-10-09T20:30:00-05:00",
    "asof": "2026-10-09T20:30:00-05:00",
    "expected": "WINDOW_OPEN_NO_COMPLETION_CLAIM",
    "actual": "WINDOW_OPEN_NO_COMPLETION_CLAIM"
  },
  {
    "label": "Synthetic absent future dispatch after window",
    "start": "2026-10-09T19:30:00-05:00",
    "windowEnd": "2026-10-09T20:30:00-05:00",
    "asof": "2026-10-09T20:30:01-05:00",
    "expected": "DISPATCH_NOT_EVIDENCED",
    "synthetic": true,
    "actual": "DISPATCH_NOT_EVIDENCED"
  },
  {
    "label": "Authentic October 8 evening gap at current audit",
    "start": "2026-10-08T19:30:00-05:00",
    "windowEnd": "2026-10-08T20:30:00-05:00",
    "asof": "2026-10-09T15:04:44-05:00",
    "dispatched": true,
    "expected": "DISPATCH_REPORTED_NO_VERIFIED_CLOSURE",
    "actual": "DISPATCH_REPORTED_NO_VERIFIED_CLOSURE"
  },
  {
    "label": "Authentic morning start-only at current audit",
    "start": "2026-10-09T07:00:00-05:00",
    "windowEnd": "2026-10-09T07:00:00-05:00",
    "asof": "2026-10-09T15:04:44-05:00",
    "started": true,
    "dispatched": true,
    "expected": "STARTED_WITHOUT_VERIFIED_CLOSURE",
    "actual": "STARTED_WITHOUT_VERIFIED_CLOSURE"
  },
  {
    "label": "Authentic afternoon persisted closure",
    "start": "2026-10-09T13:00:00-05:00",
    "windowEnd": "2026-10-09T13:00:00-05:00",
    "asof": "2026-10-09T15:04:44-05:00",
    "started": true,
    "candidate": true,
    "closure": true,
    "outputs": true,
    "closureAt": "2026-10-09T18:05:40Z",
    "expected": "VERIFIED_PASS",
    "actual": "VERIFIED_PASS"
  },
  {
    "label": "Afternoon closure time-hidden before persistence",
    "start": "2026-10-09T13:00:00-05:00",
    "windowEnd": "2026-10-09T13:00:00-05:00",
    "asof": "2026-10-09T13:04:00-05:00",
    "started": true,
    "candidate": true,
    "closure": true,
    "outputs": true,
    "closureAt": "2026-10-09T18:05:40Z",
    "expected": "STARTED_WITHOUT_VERIFIED_CLOSURE",
    "synthetic": true,
    "actual": "STARTED_WITHOUT_VERIFIED_CLOSURE"
  },
  {
    "label": "Synthetic candidate alone cannot pass",
    "start": "2026-10-09T19:30:00-05:00",
    "windowEnd": "2026-10-09T20:30:00-05:00",
    "asof": "2026-10-09T20:31:00-05:00",
    "started": true,
    "candidate": true,
    "outputs": true,
    "expected": "STARTED_WITHOUT_VERIFIED_CLOSURE",
    "synthetic": true,
    "actual": "STARTED_WITHOUT_VERIFIED_CLOSURE"
  },
  {
    "label": "Synthetic closure without outputs cannot pass",
    "start": "2026-10-09T19:30:00-05:00",
    "windowEnd": "2026-10-09T20:30:00-05:00",
    "asof": "2026-10-09T20:31:00-05:00",
    "started": true,
    "candidate": true,
    "closure": true,
    "closureAt": "2026-10-10T01:00:00Z",
    "expected": "STARTED_WITHOUT_VERIFIED_CLOSURE",
    "synthetic": true,
    "actual": "STARTED_WITHOUT_VERIFIED_CLOSURE"
  }
]
```
Executed reference classifier (manual harness only; no production runtime integration claim):
```javascript
function classify({asof,start,windowEnd,started=false,dispatched=false,candidate=false,closure=false,outputs=false,closureAt=null}){
 if(Date.parse(asof)<Date.parse(start))return "NOT_DUE";
 if(candidate&&closure&&outputs&&closureAt&&Date.parse(closureAt)<=Date.parse(asof))return "VERIFIED_PASS";
 if(Date.parse(asof)<=Date.parse(windowEnd))return "WINDOW_OPEN_NO_COMPLETION_CLAIM";
 return started?"STARTED_WITHOUT_VERIFIED_CLOSURE":dispatched?"DISPATCH_REPORTED_NO_VERIFIED_CLOSURE":"DISPATCH_NOT_EVIDENCED";
}
```
Carry-forward demonstration: simulated next health newly-due filter yields zero October 8 rows, but recovered outstanding identity union retains CFB_EVENING_AVAILABILITY_2026-10-08. This uses the authentic unresolved identity and a labelled simulated future audit boundary; it does not fabricate a future health receipt.
```json
{
  "priorAudit": "2026-10-09T16:30:00-05:00",
  "naiveNewDue": [],
  "combined": [
    "CFB_EVENING_AVAILABILITY_2026-10-08"
  ]
}
```
Independent live readback after correction passed 68 preservation assertions: same inventory, four enabled, all schedules/timing modes/timezones/titles/enabled states unchanged, other prompts unchanged, Health old prompt plus exact suffix verified.

Result: MANUAL_REPLAY_DEMONSTRATED for classification and carry-forward rule; HEALTH_CONTROL_INSTALLED_AND_READ_BACK. Natural Health enforcement, evening end-to-end proof and root-cause closure remain pending. No historical receipt, model, operational market/decision/Hot Sheet or wager was changed. No extra run dispatched.
