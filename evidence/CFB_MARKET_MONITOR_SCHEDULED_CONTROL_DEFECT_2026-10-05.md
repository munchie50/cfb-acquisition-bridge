# CFB Market Monitor Scheduled-Control Defect Classification — 2026-10-05

Status: OPEN / REPRODUCED / ENGINE-PERSISTENCE PATH EXONERATED FOR TESTED MANUAL PAYLOAD CLASS
Scope: Bug #2 from the incomplete 2026-10-04 QA continuation.
Champion effect: NONE.

## Evidence
Natural scheduled cycles:
- 2026-10-04 13:00 CT: RUN_STARTED persisted; no conforming terminal receipt exists.
- 2026-10-05 07:00 CT: RUN_STARTED persisted at 07:03 CT; no conforming terminal receipt exists as of this QA continuation.
Automation readback on 2026-10-05 confirms CFB Market Monitor is enabled and retains the governed 07:00/13:00 CT Sunday-Saturday exact schedule.

Contrasting manual evidence:
- 2026-10-04 08:40 CT manual prospective Market Monitor: RUN_PASS after representative canonical market update, decision update, full 49-row Week 6 Hot Sheet persistence, and readback.
- 2026-10-05 October-4 QA persistence recovery: create-file, exact-SHA update, complete 47-game scorecard payload, and recovered Weekly Beta Learning Review all persisted and independently read back.

## Classification
The repeated failure occurs after the scheduled task has enough execution to recover authority and persist RUN_STARTED, but before it persists any conforming terminal receipt. Because the same repository persistence primitives and representative/full production payloads pass outside the natural scheduled execution, current evidence does not support classifying GitHub persistence, Hot Sheet sectioning, Champion state, market logic, or decision logic as the root defect.

Current defect class: SCHEDULED EXECUTION / CONTROL-PLANE POST-START TERMINATION, exact terminating actor unobserved.

## Fail-closed implications
- Scheduler last_run_time is not engine completion evidence.
- Start-only cycles remain incomplete.
- Do not replay or hindsight-reconstruct their missing market/decision observations.
- Do not patch Champion, frozen predictions, Hot Sheet semantics, or repository persistence solely to make this defect disappear.
- Do not create a fifth recurring watchdog. Dual Engine Health retains completion-audit responsibility.

## Smallest safe correction
No engine/model mutation is justified. Preserve the enabled Market Monitor and its governed cadence. The next natural scheduled cycle is the next prospective proof boundary. Dual Engine Health must classify any start-only cycle as incomplete and may restore enabled state only if unexpectedly disabled under unchanged authority.

## Closure criterion
Close this defect only after a natural scheduled Market Monitor cycle produces and independently persists:
1. RUN_STARTED,
2. required canonical/Hot Sheet evidence for that cycle, and
3. a conforming terminal RUN_PASS/RUN_INCOMPLETE/RUN_FAIL receipt,
with readback proving the terminal artifact.

Until then: OPEN.

Scientific effect: NONE. Champion v1.193 unchanged.
