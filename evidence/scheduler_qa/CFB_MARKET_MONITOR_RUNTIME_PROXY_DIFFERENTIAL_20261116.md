# Market Monitor runtime transport differential — November 16 CT

Status: controlled Work Mode differential verified. Exact October 29 worker provisioning and current recurring worker proxy disposition are unobserved. No task, cadence, runner configuration, helper, model, or canonical publication mutation.

## Layers reconciled

- Scheduler/task: October 29 morning and afternoon natural production receipts verify real helper execution and publication. The October 30 original prompt backup identifies task 6ab42966c2e081919f956c941e6e0fff. Its last retained November 1 diagnostic was no_update and it is paused. The enabled replacement is 6ae766e788d881919726d0eeb44450dd in a different conversation. Their currently exposed schedule and inherited/null environment descriptors match. That metadata does not identify a backing worker. Reactivating the old ID alone has no demonstrated benefit.
- Tool surface: November 8 one-time scheduled capability result actually executed tools.exec_command inside the same functions.exec cell as connector GitHub base64 fetch, verified all 3780 bytes/blob and ran the unchanged helper with full checkout and 51 reviews. Current recurring 13 CT receipt explicitly reports no exposed equivalent shell/payload handoff in connector orchestration. This difference exists before Git or the helper runs. The recurring worker did start and publish its receipt.
- Network: November 12 one-time scheduled QA reached Git HTTPS while the recurring worker failed resolving github.com. On November 16 the recurring worker's REST fallback failed resolving api.github.com. No helper execution occurred. Both November 16 failure receipts still stand.
- Runtime implementation: the exact helper b13930cb714eb87c8dce6136ffab6fbceeb44898 is the one the successful October 29 scheduled receipts used. No helper-code delta explains today's pre-execution failure.

## November 16 controlled Work Mode test

Against authenticated repository main b5c48e39ec1033198df7df22290432a8a43a555f, using normal permissions and bounded read-only probes:
- Raw socket getaddrinfo failed with EAI_AGAIN (-3) for both github.com and api.github.com.
- Git ls-remote succeeded with the installed environment. It still succeeded with system, global and environment-count Git config disabled. It failed DNS with only the HTTP(S)/ALL/NO_PROXY environment keys removed in its child process. Proxy values, endpoints and credentials were not read back or recorded.
- Python urllib's default opener recovered the public immutable GitHub REST helper blob. Decoded byte count 3780 and recomputed Git blob SHA-1 b13930cb714eb87c8dce6136ffab6fbceeb44898 matched. The same URL via an opener with ProxyHandler({}) reproduced gaierror -3.
- Interpretation: the working Work Mode route depends on its provisioned proxy despite local DNS failure. The no-proxy control reproduces the recurring worker's symptom. That does not prove that the recurring worker has no proxy; a different or ineffective routing policy could yield the same result. No proxy values were transplanted, and no runtime policy was changed.

## Restoration and proof

Restore the original capabilities, not merely the prompt: provision or assign this existing task a supported runtime exposing exact connector-to-Python transfer and a functioning sanctioned GitHub transport. Match successful scheduled QA capabilities, then prove them in the actual recurring task. The available automation update interface has no environment assignment or infrastructure fields. Both a restored documented handoff and the existing immutable REST fallback are viable only in an environment that actually supports them. A new prompt cannot provide either capability.

If that assignment cannot be restored, the tested alternatives are the exact pinned file-only bundle or existing Actions connector handoff. The November 12 external handoff QA proved source collection, retained decision compiler use and negative guards; it did not prove automatic current-worker consumption, current reviews or publication. Favor a compact connector-readable request/result when that worker cannot materialize a full bundle. The current production prompt still calls for native checkout and disallows the Actions bypass; a tested alternate production path would require an explicit, read-back transition rather than silently routing around it. Keep the existing schedule and sole Monitor publication authority. Natural end-to-end checkout, fresh data and accepted publication independently read back remain the acceptance proof.

References: [October 29 natural success](../run_receipts/CFB_MARKET_MONITOR_20261029T180541Z_TERMINAL_CANDIDATE.md) · [November 8 capability result](CFB_CAPABILITY_20261108T160501Z_lgb8ogo_RESULT.json) · [November 12 DNS comparison](CFB_MONITOR_SCHEDULED_DNS_PROBE_20261112T132040Z.md) · [November 16 13 CT closure](../run_receipts/CFB_MARKET_MONITOR_20261116T185552Z_299da847_RUN_CLOSURE.md) · [external handoff QA](CFB_MONITOR_EXTERNAL_DECISION_HANDOFF_20261112.md).
