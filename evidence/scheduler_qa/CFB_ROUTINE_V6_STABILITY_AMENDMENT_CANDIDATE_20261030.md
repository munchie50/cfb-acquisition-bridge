# Test Routine v6 — stability and routine-selection amendment candidate — 2026-10-30
Status: QA CANDIDATE AMENDMENT / NOT PRODUCTION / NOT YET ACCEPTED. This is an additive candidate for the existing v6 back-half, not a v7 or a replacement routine.

## Selection at start of every CFB work unit
Read newest accepted constitution/contracts and recovery frontier. Declare in the work receipt: `PRODUCTION_GOVERNOR=Production Routine v5` (until independently accepted supersession), `TEST_METHOD=Test Routine v6 + this candidate amendment` when exercising QA, and `EVIDENCE_STATE=BUILT/EXECUTED/VERIFIED/ACCEPTED/PRODUCTION` as appropriate. Distinguish governing authority from diagnostic procedure. Do not claim the amendment accepted until tests and review. A new chat must recover this from the accepted repo, not from memory alone. When a newer accepted routine supersedes v5, update the declaration to that exact authority.

## Minimal additions mapped to existing v6 controls
A. Producer verification / monitoring: before attributing a scheduler failure to code, classify `NO_UPDATE` before RUN_STARTED, RUN_STARTED without terminal, canonical write rejection, terminal receipt rejection, or verified complete. Record invocation ID/time, scheduler metadata, receipt presence and observability limit. Absence of a receipt does not prove absence of dispatch. Distinguish manual from natural cycles.
B. Producer verification / closure debt: baseline task prompt hash or exact byte count, timing mode, schedule, enabled state, task count, accepted source/authority pointers and known supersessions. Compare to last independently accepted configuration; flag drift and contradictions, not speculative causation. Avoid additional unbounded prompt growth.
C. Demonstration / expected-actual: choose the smallest isolated failure-path test for changed controls, followed by independent readback and the next legitimate natural cycle. Do not run extra production jobs solely for proof. A green workflow, static replay or manual success cannot close natural-scheduler acceptance.
D. Reconcile / monitor / integration debt: if a natural startup fails, preserve diagnostic status and next natural recovery opportunity within existing four tasks; only retry automatically where a preaccepted bounded retry rule proves no duplicate side effects, no stale evidence, no user deadline violation and no excess cost. Otherwise fail closed, report and seek approval for the minimal change. No blanket self-restart.
E. Net impact: compare latency, coverage, decisions available before cutoff, reliability and resource use against baseline. Reject a guard that increases checks but harms the actual user objective without justified benefit.

## Required targeted QA demonstrations before this amendment is accepted
1. Oct30 NO_UPDATE with missing receipt: classify uncertainty correctly, do not fabricate root cause or terminal PASS.
2. Oct08 canonical update rejection with RUN_STARTED: distinguish from startup failure and use persistence-specific diagnostic path.
3. Normal completed natural Market Monitor: verify full-slate/receipt/Hot Sheet readback without adding redundant work.
4. Changed task configuration: detect drift without modifying live tasks; unchanged control must not false alarm.
5. Bounded recovery: duplicate-run and stale-source safety tests; if safe recovery cannot be proven, no automatic retry.
6. Routine selection: simulate new-chat recovery, show v5 governing and v6 testing without claiming promotion.

Acceptance requires expected-vs-actual matrix, independent QA readback, explicit unresolved debt, and user-facing readiness decision. Production v5, Champion, four task schedules, cloud branch, wager records and canonical Hot Sheet unchanged.
