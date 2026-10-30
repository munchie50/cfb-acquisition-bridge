# Proactive branch planning — lifecycle follow-through and promotion routing
Date: 2026-10-30
Status: QA WORKFLOW CONTROL; NOT PRODUCTION PROMOTION.

## Precommitted decision flow
1. Recover the expedited acceptance contract and its G1-G4 results, using persisted evidence rather than re-running already-passed gates.
2. G1/G2 incomplete: execute next bounded replay against real pre-outcome evidence; record result, actual next action, defect and proof pointer. No invented outcome.
3. Any failed gate: identify smallest correction, revise only affected candidate, rerun failed case plus adjacent regression; preserve other valid passes. Repeat until PASS or evidence-backed RETIRE decision.
4. G1/G2 PASS and G3 waiting: label READY_PENDING_NATURAL_PROOF with exact event and next review. Continue unrelated work.
5. G1-G4 PASS: produce READY_FOR_USER_APPROVAL recommendation in same QA cycle with baseline delta, evidence links, v5 minor control ID, rollback trigger, and measured overhead. No silent production change.
6. After explicit approval: independently accept versioned amendment on authoritative branch, update recovery pointer, read back exact commit and active instructions, verify next natural production use. If rollout regresses, rollback only that control, preserve original v5.0 and all evidence.
7. Report each review as ADVANCED / CORRECTION_REQUIRED / WAIT_FOR_NATURAL_TRIGGER / READY_FOR_USER_APPROVAL / RETIRED, with next concrete action. Never leave generic HOLD without owner, gate and trigger.

## Efficiency and safety
No fifth task, no artificial observation weeks, no duplicate production run, no betting or Champion mutation, no premature completion. Existing Weekly Engine QA owns recurring review; ordinary work can collect G3 evidence. Production routine v5 remains governing until explicitly accepted. Use existing registry for selective version tracking.
