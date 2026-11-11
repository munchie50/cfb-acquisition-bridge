# Controlled production stage trace
correlation_id: CFB_MARKET_MONITOR_20261111T130218Z_AUTO11
timestamp_utc: 2026-11-11T13:02:18Z
trigger: NATURAL_SCHEDULED
startup: PASS; receipt blob 92ae8caff95fed7ff3717a1508a3f29b65798bc4
main_authenticated_at_start: e4449126423299f4db0f2adcf69cd327aad60b2d
pin: 97f7fb74451f8548f7a188f4594f13da3d683dc6
compare: ahead 2, only rollout evidence and startup receipt; no material canonical drift
workflow_blob: 8633ff69c5fb710ebf9079a5cd3b896744ebfe57 VERIFIED
request_commit: 796ddc4bd187e9cc2d624ae38c357d3f5974cb94
request_blob: e099daa63c92d4ed7d65c20568238d59893af4fb VERIFIED
result_blob: 9c8a0007988271a9c8d59170a2f032e035d31d05
actions_run_id: 43025582572
result: PASS_PRODUCTION_CANDIDATE
source_at_utc: 2026-11-11T13:02:56.682383+00:00
source_blob: ede082c6311b79d5357a4744296372147995b544 VERIFIED
candidate_sheet_blob: 00f74860987660ccb2f00934fdb474a8eeb8e84c
presentation_audit: PASS_CONDITIONAL_CANONICAL_PRESENTATION_ONLY 67 games
decision_scope: retained only; no new material review
git_probe: FAILED; command git ls-remote refs/heads/main, exit 128, fatal Could not resolve host github.com
network_only_permission: UNAVAILABLE on documented container command tool
checkout: BLOCKED DNS_RESOLUTION; no clone attempted, no retry
compiler_new_decisions: NOT_EXECUTED
live_publication: NOT_EXECUTED; staged Actions sheet is not canonical
live_sheet_readback: NOT_EXECUTED
independent_sweep: verified Week11 accepted prediction pointer 15b8572f331daa18f6779e460ea52e15cf648bff, current CBS source, Friday delivery handoff; no new decision qualified
classifier_execution: NOT_RUN
next_action: capable sole-publisher Monitor must revalidate material/price/original cutoff and run canonical compiler, publication, live sheet readback
