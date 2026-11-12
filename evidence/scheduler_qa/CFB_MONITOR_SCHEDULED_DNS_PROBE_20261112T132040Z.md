# Scheduled CFB QA Git DNS probe

- Verdict: **SUCCESS — Git ref matches independently authenticated connector main**
- Trigger: NATURAL_ONE_TIME_SCHEDULED; first actual UTC: 2026-11-12 13:20:40 UTC; observed via clock__curr_time.
- Task ID: 6aeb87dd781481919f9f190e69cb5422; invocation: 35ce64b6-3a6c-8330-b582-17331b2980ce; scheduled_for: 2026-11-12T13:19:50Z; recorded_started_at: 2026-11-12T13:20:25.732208Z. Older latest_result 09ef50be-bce8-8327-9870-7319fbb85a21 was not attributed to this run.
- Shell: documented tools.exec_command through functions.exec; actually executed the probe with Python timing/capture wrapper. Default permissions only.
- OS: Debian GNU/Linux 13 (trixie); kernel Linux 6.18.57; x86_64. Stable worker/provisioning identity: UNKNOWN (not exposed). Task environment selection inherited, environments null; neither identifies the worker or proves parity.
- Effective network policy: UNKNOWN beyond exposed configuration and this observation. Context advertises restricted network and an allowlist (chatgpt.com, git.chatgpt-team.site, oaisdmntpr*.blob.core.windows.net, oaisdmntpr*aws.s3.*.amazonaws.com, oaisdsorpr*.blob.core.windows.net, sdmntpr*.oaiusercontent.com); actual Git HTTPS reached github.com successfully. This does not establish the enforced policy, resolver configuration, or which hosts other workers can reach.
- Unattended network-only permission: no such mode documented for the exposed shell. Generic escalation is not a network-only mode. Retry NOT_APPLICABLE because baseline succeeded.

## Exactly one baseline

```sh
GIT_TERMINAL_PROMPT=0 GCM_INTERACTIVE=never timeout 10 git ls-remote https://github.com/munchie50/cfb-acquisition-bridge.git refs/heads/main
```

- Probe start/end UTC: 2026-11-12T13:21:12.511047+00:00 / 2026-11-12T13:21:17.266412+00:00.
- Exit: 0; elapsed: 4.755349 s; sanitized stderr: (empty).
- Returned refs/heads/main: `9a8c68625695950b29d956c40f96ca26e7126ce5`.
- Independent authenticated GitHub connector git/ref/heads/main: `9a8c68625695950b29d956c40f96ca26e7126ce5`, exact match: true.
- Classification: SUCCESS; missing shell, DNS failure, timeout, and other failure not observed in this probe. No clone, credentials, DNS/configuration change, approval, production task changes or reschedule.

## Comparison and limits

- Production terminal candidate `evidence/run_receipts/CFB_MARKET_MONITOR_20261112T130402809Z_TERMINAL_CANDIDATE.md` @ 7f59e473708ecb8d2d5035e58541d6f34ea0d8e1: scheduled Monitor Git probe exited 128, could not resolve github.com; no clone. Offline bundle was separately inapplicable. Its RUN_INCOMPLETE remains unchanged.
- Work Mode diagnostic `evidence/scheduler_qa/CFB_MONITOR_WORK_MODE_CHECKOUT_DIAGNOSTIC_20261112T130650Z.md` @ e25b7caeeb1d1cc4aa1c229110a721c210f27ea2: direct HTTPS probe and clone succeeded there against its then-current pin. This scheduled QA worker also passed a direct probe, with its own current pin; no clone attempted here.
- The production DNS failure did not reproduce in this scheduled QA worker. Production worker parity, cause of the different result, continued reliability, and production completion remain unproved.
- Receipt observation completed 2026-11-12 13:21:50 UTC. One-time normal expiry; no lifecycle mutation.
