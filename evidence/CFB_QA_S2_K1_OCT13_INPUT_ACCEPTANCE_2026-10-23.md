# S2_K1 October13 companion acceptance — October23 QA

Run: CFB_BACKLOG_20261023T231844Z
Acceptance recorded at observed UTC: 2026-10-23T23:26:32Z (October23 CT).
Status: ACCEPTED_EXACT_SOURCE_CONTEXT_AND_TARGET_BASELINE_INPUTS; S2_K1 STUDY-ONLY.
Actual acceptance is today, not October13. No pre-event availability or prediction freeze is backdated.

## Immutable boundary

Existing natural Tuesday run38420115839, artifact11825867738, ZIP SHA-256 dc68cff62a3f61aaea3707710905fe893b9ae00d7c7d91a41064709283e001e3.
Cutoff 2026-10-13T15:13:13.866672+00:00; 440 targets/880 sides.
Parent accepted S0: evidence/CFB_QA_WEEKLY_REFRESH_ACCEPTANCE_2026-10-16_OCT13.md.
Canonical accepted-source pointer independently recovered unchanged: accepted October13 S0 boundary; schedule SHA-2565335a2776ab6425e304bd6c05aeed7ad408ae351f1c8547a1b54e08f34f92176; PBP SHA-2568620a553c03c377638895e97eefc1aa8278a1176ee6615dcc124d8c3e604e0bc.
Exact downloaded ZIP and all17 package-listed file hashes reproduced. No source reacquisition or new weekly workflow.

## Independent source-context acceptance

Existing September29 independent reconciliation script adapted only for scratch paths, October13 cutoff and manifest/cardinality boundary. Reproduction: extract the exact artifact into cfb-work/oct13; recover exact scripts into cfb-work/repo/scripts; execute evidence/audits/cfb_qa_oct13_context_reconciliation_2026_10_23.py from scratch root. Requires pandas/numpy/pyarrow/pyreadr. Raw schedule/PBP are retained October13 2026 bytes, not current or target outcomes.
Replay Git blob 4738c02f09142d37893c4f207f56abbf9ff86e9c.
Result evidence/audits/CFB_OCT13_CONTEXT_ACCEPTANCE_20261023.json at 17f01661633c16eacbb9621fcde660f9fade5da7, independently saved/read back.

Verified: 4,878 context rows; 896 mechanical and896 derived primitive rows; all880 target sides, including3 zero-history sides, matched exact schedule identities and prior-source sets/counts. Zero duplicate/leaking identities. Opponent identities, source cutoffs, strict-prior histories and calendar-day pooled baselines reproduced. Each of48,780 raw values,48,780 baselines and48,780 feature flags matched at absolute tolerance1e-12, including matching unavailable values. Completion flags reproduced; actual v1.172 schedule-filtered PBP primitive builder matched numerical fields exactly. 1,205 zero-history opponent rows; no incomplete mechanical/derived context rows in this real sample. Real sample does not prove unavailable-history edge cases by itself.

Source producer abc843e7f86779b3f55f16bd3c75bbc4e450e094 / SHA-2568500b5365ccc374105156106501f2335be80de4bde7d97bb82fe3c47cc92c1f0 matches the package. Membership filter byte-identical to accepted S0 producer ae48cf05dde9647646c8ae2a71f90a2d97bf4cc2. MAP/components match frozen historical generator40447984a58dbc530cbe942bc1176f0c5bcbe9b2; primitive ancestry37c05aba201d3c2935b5d2b646437552949766fd. Primitive CSVs retain unused prior-game winner/rank metadata; those fields must never enter the consumer. This is not a claim that source primitive files contain no source-outcome fields.

## Independent target-baseline acceptance

Unchanged auditor scripts/cfb_qa_s2_k1_target_baseline_acceptance_v1_2026_09_30.py at de4a8f16cdc22a2cbb395b226dba6c20baa58b42 executed on the same exact S0/context/baseline files and cutoff.
Result evidence/audits/CFB_OCT13_TARGET_BASELINE_ACCEPTANCE_20261023.json at b485decdac510dbb88205f148e516129b4f738f1, independently saved/read back.
880 rows/17 features; target identity/count/cutoff reconciled; pooled baseline values independently recomputed within1e-12, UTC-day strict-prior restriction and same-team/same-season rest-day intervals preserved. Target rows never used as population baselines.
Candidate target-baseline SHA-2564047014eccd739c8caaee7691cbdd4b5cea4951572162b57516bf9f4ca353f5f.

## Consumer defect discovered after input acceptance checks

The existing QA consumer required finite opponent raw features even when opponent history count was0. The frozen rules require a finite baseline and residual0 for those cases. The retained valid contexts contain1,120 such rows per mapped feature, across847 target-side context sets. These counts are input evidence, not predictions or measured outcome improvement.
Corrected only the QA consumer residual helper: count finite/nonnegative/integer, baseline finite; positive history still requires finite raw values, zero history contributes exact0, positive-history equation unchanged.
Updated consumer45effd3f15033d831c5ede6a13eba95762e7653b; static guard52c59fc0a577a93b2b8d95e498ba4258df7ff16d; seven synthetic regression examples2cd2c28ec6f4575e0068bb65d5db8cf94f713345. All7 examples and existing consumer/spec static gates passed. Retained-context helper replay verified all valid residuals for all10 mapped features, preserving positive-history results; report evidence/audits/CFB_S2_K1_ZERO_HISTORY_REPLAY_20261023.json at fc128a1d3bfb2d9adcc99c5c7952b080c977c6f8.
No full consumer/model execution, coefficients opened, predictions, target outcome scoring or scientific-effect claim. Correction is BUILT/EXECUTED_IN_ISOLATED_HELPER/VERIFIED, not an accepted prospective prediction set or natural scheduled demonstration.

## Advancement and limits

These exact October13 input-companion dependencies are now independently ACCEPTED; earlier pending descriptions are superseded only for these retained bytes. Original candidate manifests remain immutable EXECUTED_NOT_ACCEPTED.
Next stage: complete the consumer/freeze-readiness audit using the accepted inputs, frozen config and existing contracts. Prove S0 eligibility, field allowlist, input/output lineage, chronology and a genuine pre-outcome future-game freeze before claiming prospective S2 predictions. Do not run the entire old population now or backfill games already played. A later weekly source cutoff needs its own same-cutoff input acceptance.
No S2 predictions generated or accepted, no protected2025 TEST, no outcome/market/wager/decision join to the QA path, no fit/recalibration/k-grid change, no Champion or production rule change, no promotion or new task. Separate contemporaneous accounting work uses separate files and is not a QA model input.
