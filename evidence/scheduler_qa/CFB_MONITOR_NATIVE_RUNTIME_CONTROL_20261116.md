# Market Monitor native runtime control — November 16 CT

Work Mode control near 13:10 CT. Benchmark for the temporary hourly Canary, not a scheduled-worker success. Pin 35abd7be234eeec92b54b29609b7a8ad1236e6fd matched both Git main and connected GitHub fetch_commit(main).

| Layer | Verified Work Mode observation |
|---|---|
| Native shell | Python process executed under normal task permissions. |
| Connector-to-binary transfer | Exact complete GitHub base64 response passed into shell/Python in the same orchestration cell; strict decode, binary write and on-disk readback verified 3,780 bytes and Git blob b13930cb714eb87c8dce6136ffab6fbceeb44898. |
| Native HTTPS | Read-only Git main ref and immutable REST blob requests failed with DNS under a child environment with all standard proxy keys stripped. Both succeeded with only the inherited uppercase HTTPS_PROXY present and separately with only the inherited lowercase https_proxy present. Both succeeded with the normal inherited setting. Only key names were examined or recorded. No proxy values, endpoints or credentials were copied or exposed. No global configuration changes. |
| Checkout | Unchanged helper executed once at the exact pin and independently checked HEAD. Returned SUPPORTED_GIT_RUNTIME_VERIFIED with 60 retained immutable reviews. |
| Current downstream code | Week 12 compiler and CBS collector both imported from the verified worktree and selected the same active Week 12 profile. No fresh CBS request, decision run or publication. |

Historical boundary: the October 29 natural task receipt identifies the exact same helper blob but does not preserve how it reached the Python file or how Git traffic was routed. November 8 one-time scheduled QA proved the equivalent exact-byte handoff and normal HTTPS checkout, but does not identify the Oct 29 worker. The November 16 recurring producer verified connector reads but reports the handoff unavailable and a failed REST fallback. The minimum observed working path is therefore a callable native runtime, one documented exact-byte route, and functioning provisioned HTTPS. The result does not establish which proxy setting or other runtime condition is present on the recurring worker. A GitHub origin/slate/code regression does not explain the pre-helper stop.

Use this control to compare the first actual hourly Canary and the existing recurring worker by linked receipts. If Canary passes, identify which tool or transport is present there and absent/unusable in the recurring worker, and recover supported environment assignment options before calling it restoration. If Canary fails, isolate whether it lost execution exposure, transport or Git connectivity. No GitHub Actions route or task changes in this control.
