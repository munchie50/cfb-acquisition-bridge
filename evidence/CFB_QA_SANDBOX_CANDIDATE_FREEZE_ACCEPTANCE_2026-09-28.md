# CFB QA Sandbox — Outcome-Blind Candidate Freeze Acceptance — 2026-09-28

Status: PASS — CANDIDATE PREDICTIONS FROZEN / NOT SCORED
Production effect: NONE
Champion effect: NONE
Outcome access: NONE
2025 protected TEST access: NONE

## Execution authority
Authoritative freeze run: 36421939025
Head: a3318105c4e32c1f505bedbc5bd6939254190b83
Job: 108926522033
Artifact: 10970862853
Artifact name: cfb-qa-sandbox-candidate-freeze-2026-09-27
Artifact ZIP digest: sha256:8955c64f72ea8068279aed3b4ac1f062200394fbc1eb278cb1864de4da9fe5c9

Corrected generator:
- Git blob: 40447984a58dbc530cbe942bc1176f0c5bcbe9b2
- SHA-256: ed089fc928b3ef51d59f97c578491c21e122cc1b51b00e7ad8af0bf1885d1497
- bounded correction commit: 2f8aad0963d6a09ae9b8eb749163f3ff65d3566a

## Runner gates
All passed:
1. exact immutable v1.172/v1.179/v1.183 artifact ZIP hashes;
2. all seven frozen child input hashes;
3. exact corrected generator SHA-256 and Git blob identity;
4. generator compile;
5. outcome-blind candidate generation;
6. independent frozen-output gate;
7. artifact upload.

Runner independent gate reported:
- total rows: 55,834
- S0: 6,246
- S1_K1/K2/K4/K8: 6,204 each
- S2_K1/K2/K4/K8: 6,193 each

Runner output hashes:
- sandbox_candidate_predictions.csv: ed858f1bd72decd93d02aec4de507c3217470b8d01294c2cf677a2d79ed78ee3
- manifest.json: 270de37c5fa523e333799a2325f8baa4488cfa0eb114970886d43702fc2211e7

## Independent post-run artifact acceptance
The uploaded artifact was independently downloaded after workflow completion and inspected outside the producing runner.

Reproduced:
- ZIP SHA-256: 8955c64f72ea8068279aed3b4ac1f062200394fbc1eb278cb1864de4da9fe5c9
- prediction CSV SHA-256: ed858f1bd72decd93d02aec4de507c3217470b8d01294c2cf677a2d79ed78ee3
- manifest SHA-256: 270de37c5fa523e333799a2325f8baa4488cfa0eb114970886d43702fc2211e7
- prediction rows: 55,834
- exact family counts: S0 6,246; each S1 6,204; each S2 6,193
- season range: 2016–2024 only
- forbidden outcome/market/spread/odds/wager/stake/closing columns: none
- manifest status: PREDICTIONS_FROZEN_NOT_SCORED
- 2025_accessed: false
- outcomes_joined: false
- manifest generator SHA-256 matches the pinned corrected generator.

Independent omission reconstruction from the artifact:
- S1 omitted games: exactly 42 and exactly equal the frozen expected S1 omission set.
- S2 omitted games: exactly 53 and exactly equal the frozen expected S2 omission set.

## Classification
PASS. The candidate freeze is accepted as outcome-blind frozen QA Sandbox evidence.

This acceptance demonstrates that the bounded S2 exception-handler correction restored the already-frozen completion-safe semantics and that the implementation-only performance optimization remains compatible with the frozen cardinality/omission contract.

It does NOT establish that S1 or S2 improves predictive performance. No outcomes were joined or scored. It does not authorize outcome access, candidate selection, k selection, model refit, Champion mutation, production promotion, or 2025 TEST access.

## Next gate
The construction/freeze phase is closed. Any outcome-scoring/evaluation phase is a separate governed authorization boundary. Before such a phase, recover this acceptance record and the current QA checkpoint; preserve this artifact and hashes immutably.
