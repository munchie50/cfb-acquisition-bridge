# Canary v2 immediate request — 2026-10-06
Status: IMMEDIATE_RUN_REQUEST_ACCEPTED / EXECUTION_PENDING.
User explicitly requested immediate execution at approximately 07:53 CT.
automations_run_now for existing task 6ac4e807aaac8191b3255fae8ab82577 returned success and Immediate run requested. Saved schedule unchanged.
This proves request acceptance only, not execution or delivery. Prior 08:27 CT arming record is preserved.
Manual run-now is a different trigger from the scheduled clock. Its success cannot prove natural scheduling repaired.
First subsequent task readback still showed original Stage 1 last_run_time; first repository enumeration showed no v2 STARTED/RESULT files.
Next: independently discover/fetch v2 artifacts, reconcile invocation and target SHA, then suppress the redundant 08:27 trigger once execution is confirmed.
No browser/sign-in use. No production changes. Original Stage 1 remains unobserved. Production defect OPEN.
