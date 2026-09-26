# CFB Engine — Challenger B 2025 Prospective Prediction Acceptance v1.194

Status: **PASS — FAIR 2025 PREDICTIONS FROZEN AND INDEPENDENTLY ACCEPTED / OUTCOMES REMAIN SEALED**
Parents: v1.191, v1.193
Producer: v1.188
Independent auditor: v1.189

## Canonical producer evidence

Canonical producer run: **36214793786**
Head: `bf03b5d0f629b87a3ff204ffcdada84a1fdca01a`
Artifact: **10896494289**
Artifact ZIP digest: `sha256:386facc0452a2a8a4914d178cac6dc0c75db4bc30ff8f023c212f8eaac678038`

The producer completed successfully:
- target games: **934**
- eligible frozen fair predictions: **793**
- explicit fail-closed exclusions: **141**
- target accounting: 793 + 141 = 934
- team-side feature/eligibility ledger: **1,868 rows**
- fit/optimization performed: **false**
- market joined: **false**
- target outcomes joined: **false**
- chronology: strictly earlier kickoff only
- own target game excluded from source history.

The producer cryptographically bound prediction to the v1.193 frozen fit files:
- selected coefficients SHA-256: `bf15ce41180bfb4e250d311df279e98c13b65432756ae07f7a30264cbae0e221`
- TRAIN scaling SHA-256: `68fb5193ccb8828ac8d34dfe820101181c2bde078a04a6d5afd4c08bcf0cab45`
- lambdas: margin **0.1**, total **0.1**, win **0.01**.

## Independent acceptance

Audit run: **36214895984**
Head: `6d3d58ef36beaee0e3cba5f8ca9ce856b249c3e1`
Audit artifact: **10896728908**
Audit artifact digest: `sha256:db2b248558d3bb7bacf5d7806d7ea64e052a4c510151e04d18f5a1d3992d9230`

The independent v1.189 audit PASS reproduced:
- exact 934-game target key;
- 808 FBS-vs-FBS + 126 FBS-vs-nonFBS;
- 879 regular + 9 conference championship + 46 postseason;
- 64 neutral-site targets;
- exact 793 prediction / 141 exclusion accounting;
- 1,868-row team-side ledger;
- strict chronology and own-game exclusion;
- 108 frozen model coefficient terms and 34 scaling features;
- exact fit coefficient/scaling hashes;
- all producer-manifest file hashes;
- every prediction independently recomputed from frozen scaling + coefficients to tolerance;
- 2025 outcomes opened: **false**;
- 2025 outcomes scored: **false**.

## Digest-hardened workflow corroboration

Run **36214884353** subsequently passed after the workflow itself was hardened to verify the complete accepted v1.183 fit ZIP digest before extraction. It reproduced the same substantive accounting: 934 targets, 793 predictions, 141 exclusions, no market join, no target-outcome join.

This later run is corroborative only. The canonical frozen prediction artifact remains 10896494289 because it is the exact artifact independently audited by v1.189. No evidence path is silently switched.

## Gate effect

The fair prospective 2025 prediction freeze is now accepted.

**STOP BOUNDARY:** 2025 outcomes remain sealed. Joining or scoring 2025 outcomes requires separate explicit user authorization under the frozen governance contract.

No market join, refit, recalibration, redesign, promotion, or champion replacement is authorized by this acceptance. Production v1 remains champion/fallback.
