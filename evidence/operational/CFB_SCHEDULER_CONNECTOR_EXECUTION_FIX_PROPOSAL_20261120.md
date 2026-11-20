# CFB scheduler permanent fix proposal — 2026-11-20

STATUS: PROPOSED ONLY. NOT IMPLEMENTED, VERIFIED, ACCEPTED, OR PROMOTED.

## Observed failure
The 2026-11-20 07:00 and 13:00 CT Market Monitor runs did not produce an accepted Saturday Hot Sheet. Scheduled invocation and GitHub connector access worked, but direct Git HTTPS checkout/ls-remote from the worker failed DNS resolution of github.com. A scheduler 'completed' status is not production success. Do not repeat GitHub Actions scheduler experiments as the default remedy.

## Proposed alternative
Develop a connector-mediated, reproducible source-recovery and execution bundle, decoupling the scheduled worker from its broken Git HTTPS network route. Use authenticated GitHub connector to read pinned authoritative repository revision/tree and required source files, reconstruct a manifest with blob SHA checks, establish commit/ancestry integrity by independently verifiable GitHub API evidence or an approved equivalent, and run the existing v1 champion compiler in a controlled runtime with captured dependencies and reproducible inputs. Preserve immutable source snapshots, CBS provenance, market timestamps, and separate v2 shadow outputs. Write outputs and append-only receipts via connector, then fresh-read and independently verify the published Hot Sheet. Never equate connector file retrieval with complete authenticated checkout or bypass the current ancestry gate without an explicit approved replacement contract.

## Minimum bounded acceptance tests
1. Read current constitution/master contracts/status and confirm exact mandatory gates and executable dependencies.
2. Smallest test: pin one known revision, independently verify tree/manifest, recover one fixture and compare byte/hash identity to trusted baseline.
3. Execute a deterministic historical fixture with v1, compare result to accepted reference and verify clean provenance.
4. Test scheduled environment without Git HTTPS: connector source acquisition -> execution -> persisted receipt -> independent readback.
5. Failure injection for missing file, mismatched hash, stale source, connector permission loss, incomplete game coverage, and delayed schedule; fail closed with useful incomplete closure.
6. Only after accepted evidence, promote to all four existing production tasks with job-specific contracts, without creating a permanent fifth task.

## Operational priorities and constraints
First complete missed 07:00 and 13:00 CT production catch-up manually where governance allows. Friday 13:00 CT is Saturday slate placement deadline; do not retroactively assert it was met. Never invent plays, market prices, or full-slate coverage. Preserve v1 production champion and v2 challenger. Keep four regular production tasks and one open test slot. No unilateral acceptance gate relaxation. Use fresh-read -> smallest delta -> write -> readback, distinguish BUILT / EXECUTED / VERIFIED / ACCEPTED / PRODUCTION. Resolve authoritative evidence before design changes.

## Revisit trigger
When user authorizes permanent scheduler repair, start by checking latest persisted current state and this proposal, then design the smallest fixture test. This document is a backlog proposal, not authorization to modify production gates.
