# Nov. 25 Monitor first authenticated GitHub call

Reused Nov. 24 natural scheduled startup b12971c8ba921b2174a2bda5d075fe4cfbbb49aa and Nov. 24 manual publication 1a363d08c9d696f86b8ae24df09ad84e6eeec037. Reviewed shared CBS handoff and terminal closure contract. The Nov. 25 07 CT run reported tool discovery but no main call; underlying termination remains unknown.

Startup-only change: name github_fetch_commit with exact repo and main ref as first action after discovery, require actual returned SHA or exact failure/capability boundary, and preserve append-only receipt creation, 404/409 handling and readback. The rest of the prompt matched exactly. Verified live installed SHA-256 971a1a15d6e7c8476caf04789b6a694abd02be166999ba632d979e9179c07a46; verified rollback evidence/scheduler_qa/CFB_20261125_MONITOR_FIRST_GITHUB_CALL_ROLLBACK.json, blob 375761f9f996112b6af96947a389e5a39c961809. Existing task ID, schedule, ownership, enabled status, and environment settings matched. Next live slot 2026-11-25T13:00:00-06:00.

This is configuration and prompt readback proof. At the existing 13 CT natural slot, verify actual first read, startup receipt and readback, CBS capture, due decision review and separate closure using that invocation's evidence. If the worker exits before calling, raw platform invocation/termination evidence is still required. No inline replay or new scheduled task.
