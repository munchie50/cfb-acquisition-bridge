# Cloud preparation work — continuation checkpoint

State: QA IMPLEMENTATION / LOCAL BOUNDARY TESTS PASSED / CLOUD MEASUREMENT PENDING.
Repository: munchie50/cfb-acquisition-bridge.
Work branch: qa/cloud-source-preparation-20261030.
Starting accepted main: fc1a87133a2acfe81f8b348a76838cb43bc4a4cf.
Production recovery index blob: c82beea44dcd7300728a965a6cfe423467701ced.

## User goal and operating boundary

The user authorized reusable cloud source preparation and faster validation, with easy continuation across chats. First measure usefulness in QA, then compare alongside the current producer before production reliance. Keep exactly four ChatGPT production tasks and their schedules. Friday's grouped three-game decisions are AFTER the existing 13:00CT run; its explicit timing correction on main remains authoritative. This branch does not change that review, recommend bets, extend UCF's old expiry, publish canonical state or promote a model.

Estimate remains approximately1–2focused working days for the proposed first two areas, then natural-run proof. No measured whole-Monitor time savings yet. The long production CI seen tonight was roughly8minutes, but this branch has NOT optimized those checks. Do not promise that collector speedup becomes equivalent end-to-end savings.

## Implemented first milestone

- scripts/cfb_cloud_source_prepare.py accepts an explicit hash-pinned manifest with game identities, source links, source kinds and approved HTTPS hosts. It does not guess source URLs, auto-discover current authority or certify source text.
- Up to4parallel workers,64sources,4MiB/source,20second network timeout, no immediate retries; complete observed clocks and raw-response hashes retained. Explicit public-host checks also apply to redirects. Ordinary publicHTTP only, noFirecrawlpaidcalls.
- Each completed response saves a checkpoint atomically. A nonblocking output-directory lock rejects competing writers. Reusing another input in the same directory is rejected.
- Resume requires matching URL, exact raw-file hash/size, original aware acquisition clock and bounded age(default900seconds, maximum3600). Future/stale/corrupt/missing responses are fetched again; cache reuse never refreshes acquisition time. max-age0forces reacquisition.
- All fetched/reused responses remain UNREVIEWED. Failures are UNAVAILABLE_NOT_A_PASS; HTTP200/linked game coverage is not semantic completeness or market qualification. Output cannot write repository canonical files by itself.
-13local boundary tests passed. Includes partial checkpoint, failed-source retry, corrupt-file isolation, stale/future clocks, input mismatch, coverage gaps, duplicate identities/URLs, redirects, size/status failures and lock/bounds.
- scripts/cfb_cloud_source_benchmark.py compares serial/four-worker/resumed collection and reports status comparability. The explicit4URL/56declared-game fixture links a CBSboard to all56 and3retained official pages to2games; it is deliberately NOT full-slate football coverage or dynamic weekly discovery. Fresh QA reads must never be spliced into production decisions or training.
- .github/workflows/cfb_cloud_source_preparation_qa.yml runs only the work-branch workflow-file push or manualdispatch. No cron/newChatGPTtask. Read-onlyrepositorypermissions,10minutejoblimit,30dayartifacts. Network failures remain in manifests even if harness execution succeeds; a greenjob is not allsourcesavailable/footballproof.

## Exact resume procedure in a new chat

1. Read this file and the draftPR on the branch. Re-read accepted main recovery authority and user timing constraints; branch work is QA, not a replacement system of record.
2. Enumerate commits/files and ensure the branch still contains these complete files. Use a clean worktree; preserve unrelated changes. Never infer completion from this filename or workflow color.
3. Recover the latest CFB Cloud Source Preparation QA workflow run **for this branch and exact commit** via repository Actions. Read jobsteps/logs and download its artifact. Inspect benchmark.json plus all per-source manifest records. Record actual run/job/artifact identifiers and source failures before claiming a live demonstration.
4. If run fails, diagnose that exact stage and make the smallest repair. Existing valid checkpoints may be reused only under input hash and age bounds. Do not repeat successful production/model work.
5. To resume a recovered checkpoint manually: materialize the artifact, verify approved inputSHA, then invoke the worker against the recovered parallel/output directory. This code supports cross-process checkpoint reuse; automatic artifact restore across separate Actions runs is NOT wired yet.

Local checks:

```bash
python -m unittest discover -s scripts -p test_cfb_cloud_source_prepare.py -v
python scripts/cfb_cloud_source_prepare.py --input evidence/scheduler_qa/CFB_CLOUD_SOURCE_QA_INPUT_20261030.json --expected-sha256 f96b129bfafd019607c54d48614aabc6dcd0feaa1d17d4736f0ea78fc2fefd73 --output /tmp/cfb-source-prep-resume
```

The second command makes live requests. Use a recovered directory instead of /tmp only after checking its exact manifest and files. Outputs are QA raw evidence only.

## Next dependent work; do not skip to production

1. Independently recover cloud measurement and summarize collector-only savings and failures. Complete true kill/restart proof in an actual cloud run; local tests alone are bounded evidence.
2. Add controlled artifact restore for a subsequent run, preserving input identity/TTL/partial failures and validating a killed invocation. No unattended worker has yet demonstrated cross-run recovery.
3. Build the manifest adapter from CURRENT accepted full-slate population and explicit source references. Verify source-role coverage separately: a full-board URL linked to allgames is not complete football research. Old fixture URLs are not automatic current-week sources.
4. Connect as a read-only/shadow preparation producer. Reconcile full coverage, source ages, availability, runtime, source cost and duplicated requests with the existing Monitor. The Monitor continues actual football/number+price analysis and sole serialized publication/readback/closure.
5. Only after that proof, propose limited production use within existing tasks. Preserve the current path until accepted; no unrequested rollout.
6. Faster validation is a SEPARATE unfinished phase: inspect dependency order in existing45stepworkflow, parallelize only independent suites and cache immutable artifacts by verified digest. Benchmark identical checks/results first; never remove protection to reduce time. Current9suiteancestry stage and current-publication check are potential measurement targets, not already implemented savings.

## Continuation reporting

Always state BUILT / EXECUTED / VERIFIED separately. Update this checkpoint on this branch after real new evidence, preserve historical failures and link exact results. Keep a short root-level main continuation pointer/draftPR so a fresh chat can find the branch without rebuilding from memory. No new tracking framework is needed. A user asking whether the work is worthwhile has not cancelled the authorized QA work; answer briefly and continue useful independent work.


## Superseding verified milestone — 2026-10-30T01:53:56Z

State: BUILT / EXECUTED IN GITHUB CLOUD / BOUNDED READBACK VERIFIED. Still QA, not production/shadow-ready. DraftPR16: https://github.com/munchie50/cfb-acquisition-bridge/pull/16.

Run40988321126/job123844437594 at commitd15d6ab98ecdcc8edf74ca2ddbd46d6929bd0dd2 completed9exposedsteps successfully.13boundarytests passed in cloud. Decoded logs independently read. Artifact12948370503 ZIP SHA256055a35b825f1b401be06bc00533d7c04f801d70d880972682ef02144f8e40281 downloaded independently and verified; all4parallel raw-response hashes/sizes matched. Source manifests preserve actual clocks, URLs, HTTPstatuses and bytes. Durable result: evidence/scheduler_qa/CFB_CLOUD_PREPARATION_QA_RESULTS_20261030.json blob7cb887ccc90398fc1599d4c60ce12cbf96d26069.

Observed collector times: serial3.589348s, parallel0.354945s, same-runresume0.005753s;4/4sources fetched in both initialpasses,0failures. Downloaded artifact then resumed in a separate local process at01:52:50.053402Z:0newfetches/4reused/0failures,0.005574s. Original acquisition clocks retained. This is real cloud-to-local artifact recovery, NOT an interruptedcloudinvocation or automatically restored secondActionsrun. The rawresponses are unreviewedQAevidence; no model/canonicaldecisioningestion.

Interpretation: source-stage sample saves about3.23seconds versus that serialsample. One sequentialserialthenparallelmeasurement is confounded by endpointwarming/networkvariability; the observed10.112ratio is NOT a causalparallelismestimate or fullMonitorforecast. No demonstrated minutes saved in wholeproduction. Current measured benefit is correct checkpointreuse and bounded collector efficiency. Largerrepresentativeshadowtiming and analyticalcost remain to be measured. No productionpromotion, schedulechange or accelerated45stepvalidation implemented.

NEXT EXACT STEP: wire controlled artifactrestore into a second isolatedActionsrun and demonstrate a genuine interruptedcloudcheckpoint restart. Then build current-authority manifestadapter/fullsource-role coverage, shadowcompare usefulness and repeated sourcecost, before any productionproposal. Fastervalidation remains separate unfinishedphase. Do NOT rerun this completedfourURLbenchmark merely to manufacture moregreenproof. Recover these exact existingresults first; checkpoint/sourceage gates must still run on later reuse.
