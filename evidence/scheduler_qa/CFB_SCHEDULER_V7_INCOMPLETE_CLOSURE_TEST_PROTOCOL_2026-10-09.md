# Scheduler diagnostic V7 — incomplete-result closure and topology preservation

Authority: user-authorized ongoing temporary scheduler QA; active manual fast-loop protocol; Test Routine v6 remains candidate. Existing temporary canary id 6ac4e807aaac8191b3255fae8ab82577 is reused for at most one new one-time invocation; no new recurring task.

## Distinct hypothesis
A source-independent minimal diagnostic terminal can record an operationally incomplete result and separate read-back closure while preserving four production task states. Prior V6 proved successful-update closure, not this controlled failure branch.

This is explicitly simulated: set failed_stage=SIMULATED_OPERATIONAL_BLOCK and reason_code=QA_CONTROLLED_BLOCK. Do not make a deliberately forbidden/rejected connector request, mutate a canonical file or claim actual rejection reproduction. The simulation's incomplete workload result and the test harness verdict are separate.

## Permitted operations
Read authority, current task metadata and diagnostic receipts. Create unique timestamped STARTED, terminal CANDIDATE and separate CLOSURE under evidence/scheduler_qa/ only; independently fetch each. No existing-file mutation is needed. No external research, sportsbook quotes, credentials/browser/sign-in, production task mutations, additional task or rerun.

## Required sequence and minimal envelope
1. Record actual invocation time, execution_class (MANUAL_FAST_LOOP or NATURAL_ONE_TIME_SCHEDULED), test_id, the four production task ids/enabled states and current authority.
2. Create/read STARTED.
3. Apply only the declared synthetic control block; no actual market/decision/Hot Sheet work.
4. Create a small terminal CANDIDATE containing test_id, actual start/boundary, workload_status=DIAGNOSTIC_INCOMPLETE, failed_stage=SIMULATED_OPERATIONAL_BLOCK, reason_code=QA_CONTROLLED_BLOCK, applicable_surfaces=NONE_PRODUCTION, STARTED blob, terminal_readback=PENDING, scientific_effect=NONE and production_effect=ZERO. Do not include external-source bodies or raw attempted production payloads.
5. Independently fetch CANDIDATE; compare exact bytes and blob.
6. Only then create/read CLOSURE citing the candidate path/blob and preserving workload_status=DIAGNOSTIC_INCOMPLETE. Re-read production task metadata; assert the same four tasks remain enabled with unchanged prompts/cadences.
7. test_verdict=PASS is allowed only after STARTED, CANDIDATE and separate CLOSURE readbacks and topology reconciliation. PASS refers to controlled failure handling, never production workload success or opaque rejection closure.

If permitted receipt persistence fails, report TEST_INCOMPLETE / TERMINAL_PERSISTENCE_UNAVAILABLE with observed safe classification and last proven stage. Do not bypass restrictions, retry canonical surfaces or mutate production tasks. One-time scheduler lifecycle completion may auto-disable the temporary canary; the invocation must not issue automation-management mutations.

## Acceptance limits
Manual demonstration is prerequisite to the one-time scheduled comparison; natural canary proof remains distinct from actual production failure, source safety and representative Market Monitor acceptance. Scheduled test may execute early/late relative to requested DTSTART; record requested and observed times without inventing scheduler precision.
No equivalent repetition unless a failed stage requires the smallest justified correction. Natural 13:00 production gate remains separate.
