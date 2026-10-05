# CFB Terminal Run Receipt Closure Contract — 2026-10-05

Status: ACTIVE OPERATIONAL CONTROL
Scope: CFB scheduled and manual production-operation receipts.
Scientific effect: NONE.
Champion effect: NONE.
Parents: CFB_ENGINE_CORE_EXECUTION_CONTROLS_v1_133.md; evidence/run_receipts/README.md; demonstrated closure pattern CFB_RUN_CLOSURE_2026-09-29_2020CT_MARKET_MONITOR_RESET.md.

## Problem proved
A historical 2026-09-27 Sunday Market receipt declared RUN_PASS while its own persistence/readback section still marked the Sunday Early Board and terminal receipt readback as pending. A terminal state therefore cannot be certified in the same logical step that still depends on proving its own persistence.

## Required two-phase closure
1. RUN_STARTED may be persisted prospectively before operational mutation.
2. Perform the governed work.
3. Persist/read back every applicable canonical/output surface.
4. Persist a terminal receipt candidate containing the factual run result and the surfaces expected to close.
5. Independently fetch/read back that terminal receipt candidate.
6. Only after steps 3 and 5 succeed, persist a separate RUN_CLOSURE record that certifies the final terminal classification.

## Terminal semantics
- RUN_PASS requires all applicable governed surfaces plus terminal receipt candidate to exist and independently read back before RUN_CLOSURE is issued.
- RUN_INCOMPLETE is required when useful work occurred but a required surface/readback/closure dependency remains unresolved.
- RUN_FAIL is required when the governed run cannot safely continue or its required integrity checks fail.
- RUN_STARTED alone is never completion evidence.
- Scheduler last-run metadata is never completion evidence.
- A terminal receipt that says its own proof is pending is not sufficient to establish RUN_PASS; absent a later conforming closure record, treat the historical run as completion-ambiguous for audit purposes.
- Historical receipts are append-only and are never rewritten to improve their status.

## Closure record minimum fields
- run identity/type and prospective boundary;
- final terminal state;
- exact applicable surfaces;
- independent readback identifiers/digests where available;
- explicit statement that closure was issued only after terminal-receipt readback;
- unresolved items, if terminal state is RUN_INCOMPLETE or RUN_FAIL;
- statement of scientific/Champion effect.

## Compatibility
This contract formalizes the already-demonstrated 2026-09-29 closure/finalization pattern. It does not create a new scheduler, alter task count/cadence, change Champion/model state, or authorize retrospective reconstruction.

## Demonstration requirement
Structural control is active immediately. LEARNED closure requires a future natural scheduled production cycle to use this two-phase pattern successfully. Until then, terminal-receipt semantics are CORRECTED / PROSPECTIVE DEMONSTRATION PENDING.
