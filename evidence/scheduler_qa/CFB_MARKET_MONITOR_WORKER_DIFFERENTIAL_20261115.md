# Market Monitor worker differential — November 15 CT

Objective: isolate the first differing stage between a real scheduled success and the current production failure, and retest an alternative whose checkout does not depend on worker GitHub DNS.

| Evidence | First material boundary |
|---|---|
| October 29 natural production RUN_PASS | Exact helper blob b13930cb714eb87c8dce6136ffab6fbceeb44898 materialized and ran; full live Git history validated with 28 retained reviews; fresh CBS, compiler, CI, and persisted closure followed. Stable worker identity and precise helper materialization route unavailable. |
| November 8 one-time scheduled capability proof | Same-cell connector-to-shell transfer worked when functions.exec and nested shell were available. The separate immutable API test also passed at its tested endpoint. Neither establishes recurring production worker parity. |
| November 12 scheduled production and same-morning QA probe | Production Git HTTPS failed resolving github.com. The scheduled QA worker ran the same Git command successfully against independently authenticated main. Production's offline bundle pin was also stale. Exposed inherited/null environment settings do not identify either runtime. |
| November 15 1 p.m. natural production | Scheduler and authenticated connector receipt operations worked. Same helper blob recovered by connector. No complete connector-to-shell transfer was exposed; immutable API helper transfer failed on api.github.com DNS. Helper, checkout, CBS, compiler and publication never ran. |
| November 15 Work Mode control | Direct Git HTTPS returned independently authenticated main 55f49e805ee00d316f09d1f85290bb35c2957071. Work Mode and a scheduled QA success do not demonstrate connectivity in the recurring producer. |

The provable boundary difference is runtime transport capability and network reachability. The exact infrastructure reason and the scheduled worker's stable provisioning identity are unavailable. Changing the source, betting logic, helper contents, or retrying an equivalent DNS route cannot address this observed failure. Week 12 profile integration is a separate producer dependency.

## Verified fresh-bundle QA experiment

- Updated only the existing isolated branch `qa/monitor-offline-bundle-20261111`, workflow commit `0b485399c051c82018a9997bafd51b77b749b3d1`. Pinned the connector-verified main above. Producer used read-only repository permissions and generated a fresh full-history bundle in [Actions run 43769045358](https://github.com/munchie50/cfb-acquisition-bridge/actions/runs/43769045358).
- Artifact 14183700677 was fetched through the authenticated GitHub connector. Verified complete ZIP: 12,273,187 bytes, SHA-256 `d48b63012bb98e4fcddc26c75598fba1f468f499a57ca2c687730b5b4fdd70e9`. Its sole bundle was 12,273,047 bytes, SHA-256 `775dcfeb4a02cdf65a8cc5350f939662d74fdf2e4cb6eacec51456ab0f1b7b0b`.
- In Work Mode, with Git restricted to file transport, restored exact pin, nonshallow ancestry, five required Week 11/governance scripts, unchanged helper identity and 60 retained immutable reviews using the unchanged review loader. A real older artifact 13862091095 resolved to dd4b33db02d28df7dcd3328a8fc63036bfc06064 and was rejected against the current pin.
- This proves a QA producer and DNS-independent Git checkout for that snapshot, not recurring worker artifact materialization or production publication. The QA artifact pin becomes historical when main advances and must not be reused for a later unqualified run.

## Correction and verification boundary

Test this transport in the actual recurring Monitor execution class, using a newly generated bundle tied to the connector-authenticated execution pin and independently verified artifact digest and exact checkout. Obtain and check the pin at the start of the run. Use fresh canonical-parent checks before changes; reject unexpected drift rather than accepting a reachable older commit. Separate connector download, binary handoff, file-only checkout and immutable review validation in the receipt. If the actual worker cannot materialize the artifact, move the Git-dependent stages to the connected Actions runner and pass back verified outputs for the existing Monitor to accept and publish under its authority. A successful artifact transport alone leaves Week 12 compiler, fresh acquisition/review and full scheduled publication unproved. No production schedule or task definition changes were made in this QA experiment.

Evidence: [October 29 candidate](../run_receipts/CFB_MARKET_MONITOR_20261029T180541Z_TERMINAL_CANDIDATE.md) · [November 12 comparison](CFB_MONITOR_SCHEDULED_DNS_PROBE_20261112T132040Z.md) · [November 15 candidate](../run_receipts/CFB_MARKET_MONITOR_20261115T185733Z_AUTO11-20261115T185733Z_TERMINAL_CANDIDATE.md).

## Reusable offline checkout probe and validation

The existing isolated branch `qa/monitor-offline-bundle-20261111` now contains [the stage-specific probe](https://github.com/munchie50/cfb-acquisition-bridge/blob/ad7331f64c7fb6361b4d76b45e7d0815e2cb2a23/qa/cfb_monitor_offline_bundle_probe.py) and [its workflow integration](https://github.com/munchie50/cfb-acquisition-bridge/commit/2a23cac7f6ac51b9560977b1629f5624aebfc7ae). The probe takes an already materialized artifact ZIP, trusted digest, independently authenticated expected commit, and requested weekly compiler. It emits the failing stage so archive integrity, binary extraction, exact pin, file-only clone, compiler presence, and immutable-review verification can be distinguished. Connector download and transfer to the local ZIP remain a separately observed outer step.

[Actions run 43769594749](https://github.com/munchie50/cfb-acquisition-bridge/actions/runs/43769594749) passed valid checkout, wrong expected pin rejection and wrong digest rejection. Independently downloaded actual uploaded artifact 14183428937 through the connector and ran the same probe in Work Mode. ZIP 12289341 bytes, digest `sha256:4666a8ec5c7ee0fc2057fc94f9e8a09fdb35affddba7c560e0a7f0e407ff7e35`; exact full checkout d792d0a95d4af36e6df7b5c352a74cd9deeea92b; 60 immutable reviews verified. The requested `cfb_week12_publication.py` was missing. This correctly reported `FILE_ONLY_CHECKOUT_VERIFIED` and `profile_ready: false`. A completed checkout is a prerequisite, and the Week 12 compiler remains a separate dependency.

Next proof: use a newly pinned artifact and this stage vocabulary in the actual recurring producer execution class. If connector download succeeds but its returned bytes cannot be materialized there, keep Git-dependent computation in Actions and test transfer of a compact, independently verifiable output. No production prompt or schedule change in this QA work.
