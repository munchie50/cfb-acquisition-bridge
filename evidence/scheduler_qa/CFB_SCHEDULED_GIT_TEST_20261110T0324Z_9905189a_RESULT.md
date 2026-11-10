# Scheduled Git checkout diagnostic — RESULT

correlation_id: CFB-GIT-20261110T0324Z-9905189a
scheduled_for_utc: 2026-11-10T03:24:00Z
invocation_id: 9905189a-f534-8331-b6db-bc255a828239
observed_start_utc: 2026-11-10T03:23:43Z
startup_receipt: evidence/scheduler_qa/CFB_SCHEDULED_GIT_TEST_20261110T0324Z_9905189a_STARTED.md
startup_receipt_readback_blob: e2c7274f28844488ebc2e13332aa07d97f73bc44
authenticated_main_checkpoint: 7bc760cc1760b405bff096b55117ab03d0a75cd9 (STARTED receipt commit to main; no claim of immutable tip at later clock)
helper_path: scripts/cfb_runtime_checkout.py
helper_blob: b13930cb714eb87c8dce6136ffab6fbceeb44898
helper_decoded_bytes: 3780
helper_base64_validation: PASS, complete 5040 base64 chars via authenticated GitHub connector
shell: /bin/bash, /usr/bin/git version 2.47.3, /usr/bin/timeout, python3, curl
transport: GitHub connector read PASS; complete connector-to-shell binary handoff NOT_EXPOSED through available tools; shell outbound DNS unavailable

## Stage results
probe:
  command: GIT_TERMINAL_PROMPT=0 GCM_INTERACTIVE=never timeout 10s git ls-remote https://github.com/munchie50/cfb-acquisition-bridge.git refs/heads/main
  rc: 128
  elapsed_ms: 135
  error: "fatal: unable to access GitHub: Could not resolve host: github.com"
  verdict: FAIL_DNS_RESOLUTION
transfer:
  command: authenticated connector fetch_file base64 for exact helper
  rc: 0 (connector); shell transfer NOT_AVAILABLE
  elapsed: NOT_MEASURED
  error: no complete binary handoff from connector result into shell is exposed
  verdict: CONNECTOR_READ_PASS_TRANSFER_UNPROVED
clone:
  command: NOT_RUN
  rc: NOT_RUN
  elapsed: 0
  verdict: BLOCKED_BY_PROBE; no clone attempted
pin:
  command: NOT_RUN
  rc: NOT_RUN
  elapsed: 0
  verdict: BLOCKED_BY_CHECKOUT
review_validation:
  command: NOT_RUN (unchanged load_review not executable without verified checkout)
  rc: NOT_RUN
  elapsed: 0
  verdict: BLOCKED_BY_CHECKOUT
immutable_api_fallback:
  command: python3 urllib.request.urlopen(https://api.github.com/repos/munchie50/cfb-acquisition-bridge/git/blobs/b13930cb714eb87c8dce6136ffab6fbceeb44898, timeout=10)
  rc: 1
  elapsed_s: 0.024
  error: URLError [Errno -3] Temporary failure in name resolution
  verdict: FAIL_DNS_RESOLUTION

final_verdict: TEST_INCOMPLETE
first_failing_boundary: ordinary scheduled-worker Git HTTPS DNS resolution
fallback_boundary: connector read succeeds but complete helper handoff to shell unproved; direct immutable API DNS fails
git_first_boundary_pass: NO
fallback_boundary_pass: NO
production_parity: NOT_CLAIMED
publication: NOT_RUN
task_changes: NONE
retries: NONE
next_safe_action: investigate scheduled-worker DNS/network and complete authenticated connector-to-shell transport; repeat only as a new authorized test after structural correction
