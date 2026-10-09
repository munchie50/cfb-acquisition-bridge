# Scheduler v6 task-state regression

Status: OPEN, read-only observation.

ChatGPT task state: CFB Evening Availability id 6ab4296f9fec8191a8d35056b70d17cb is_enabled=false, updated_at 2026-10-09T01:16:48.170842Z, last_run_time 2026-10-09T01:15:43.475970Z. Schedule still Wednesday/Thursday/Friday 19:30 America/Chicago.
Other three production tasks are enabled. Thus only three of four expected production tasks are currently enabled. Temporary Scheduler Canary remains disabled.

Prior task inspection on October 8 showed Evening Availability enabled. Actor and reason for the later state change are unverified. No automatic repair attempted during isolated scheduler QA because changing production task state requires governance/coverage verification.

Current exhaustive evidence/run_receipts/ listing (53 entries) has no October 8 evening-specific terminal receipt. This does not rule out other naming or persistence locations. Next safe action: inspect task invocation/termination and governance controls, then authorize and verify a minimal enabled-state restoration with four-task ownership/readback checks.

No production task or canonical repository mutation in this observation.
