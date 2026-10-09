# Test Routine v6 — large payload update isolation

Status: MANUAL DIAGNOSTIC PASS. Production scheduled write blocker remains OPEN.

Isolated fixture: evidence/scheduler_qa/CFB_SCHEDULER_V6_UPDATE_PAYLOAD_SIZE_FIXTURE_2026-10-08.md.
Baseline create commit f1d11bccc861792b94ee663cd94b9e86909b9e7b, blob 28adb44dfca2ed63ad5879c0922550c660e0c7ae; independently read back.
SHA-guarded update replaced baseline with 63,044-character synthetic QA content (520 records).
Update commit d6708136621f00df571c66e3a70471a382ce6694, blob 254186242ef594f58479102a99bb608066824fe8.
Independent exact-content readback: PASS.

The production market-state surface was independently read at 28,865 characters and SHA c8616b340917e5db2674ec6c16581dd0d09275a5. Its October 8 morning scheduled update was rejected twice by connector safety checks. This experiment demonstrates manual SHA-guarded replacement of a larger synthetic payload works; it does not prove that the production payload, production path, or scheduled execution context would work. Payload size alone is not a demonstrated universal blocker.

Next isolation: test representative benign market-shaped content in the same isolated fixture, then compare request differences without writing to canonical operational surfaces. Preserve four production tasks, frozen model and all historical evidence.
