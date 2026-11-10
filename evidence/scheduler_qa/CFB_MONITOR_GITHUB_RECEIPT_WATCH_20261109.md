# GitHub receipt watch for the production Market Monitor

This is a read-only Monitor evidence check inside the existing 16:30 America/Chicago Engine Health run. Save findings within the normal GitHub Health audit and closure. The disabled Receipt Watch supplied the detection pattern. The Monitor remains the sole producer and Health does not dispatch recovery or publish.

For each due 07:00 and 13:00 CT Monitor slot, correlate the scheduler run ID and scheduled_for when available with GitHub startup, checkout stage trace, terminal candidate and separate closure. Bind records by exact invocation ID where captured, otherwise use explicit same-cycle correlation and distinguish ambiguous records. A run may start early. Manual and test receipts do not prove a scheduled production slot. Record expected slot, actual run ID or UNKNOWN, matched receipt paths and exact blobs, last proved stage, first failed or unproved boundary, sanitized reason and next action. Keep earlier unresolved coverage in the existing queue.

Use these distinctions:
- STARTUP_UNPROVEN: No matching verified RUN_STARTED. GitHub cannot say whether dispatch failed or startup logging failed. Capture scheduler status separately if available.
- STARTED_CLOSURE_UNPROVEN: Startup exists but the terminal chain is missing or incomplete. Record the last verified stage and any ambiguity.
- CLOSED_INCOMPLETE: Verified same-cycle RUN_INCOMPLETE or RUN_FAIL closure. Preserve the actual first failing stage.
- PUBLICATION_UNVERIFIED: A reported success lacks verified selected Hot Sheet, readback, required CI or closure binding. A saved prior sheet does not count for this run.
- VERIFIED_DELIVERY: Same-cycle accepted publication, independent readback, required selected CI and closure verified.

Record probe, clone, pinned head, immutable review verification and publication separately when the current Monitor emits those stages. Do not infer a stage result from configuration, CI in a different worker or a green automation status. Keep monitoring within the existing Health schedule. The existing GitHub Actions runtime smoke tests GitHub's runner and can be used as a comparator; it cannot observe private scheduler-worker DNS or dispatch telemetry. No extra job, slot, source retrieval, or producer is needed for this watcher.

Baseline check: November 9 Monitor closures aa81fcf8ac0430134f1c651ad624d8b70d65b031 and 7fdc64d09f88aaf4528cd77020232c42d73ceb9c are CLOSED_INCOMPLETE at helper transport, with no verified Week 11 publication. The November 8 shadow success and November 9 manual checkout are separate evidence.
