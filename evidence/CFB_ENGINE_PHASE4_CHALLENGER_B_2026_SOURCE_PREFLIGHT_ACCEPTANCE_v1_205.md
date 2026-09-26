# CFB Engine — Challenger B 2026 Source Preflight Acceptance v1.205

Status: **PASS WITH LOCALIZED PBP INCOMPLETENESS / SOURCE FRONTIER FROZEN**
Parent: v1.204
Run: **36215880651**
Artifact: **10897001956**
Artifact digest: `sha256:4dc70419b9aa3afdfa2570861490598da69b2bccfed878e438dc17b69a9a7ea8`

Frozen execution cutoff: **2026-09-26T03:47:37.497112+00:00**

Source identities:
- schedule SHA-256: `5b2ff52996862b06b67309f1ebc27742e55c279ff4785c7a942915cdf820f1b1`
- PBP SHA-256: `81e38e7e874d249300bb108de0029a8ffb0b19c31cfea6e7aafab5507115e5da`

Population at cutoff:
- raw 2026 schedule rows: 3,679
- qualified relevant-FBS rows: 888
- at/before cutoff (spent, not prospective): 266
- future prospective target projection: **622**
- future FBS-vs-FBS: 599
- future FBS-vs-nonFBS: 23
- frozen membership: 138

Prior-source completeness:
- completed spent relevant-FBS games: 262
- completed spent games absent from current PBP: **2**
- missing PBP game IDs: **401862779, 401869941**

## Fail-closed disposition
The two missing PBP games do not invalidate unrelated future targets. Prediction construction must propagate prior-history completeness by team:
- if either side's strictly prior qualified history contains a game whose required PBP is absent, that side is history-incomplete;
- any target requiring a history-incomplete side is excluded from the prospective prediction artifact;
- unaffected targets remain eligible if every other frozen feature/model invariant passes;
- no zero fill, imputation, or silent omission of the missing prior game is permitted.

The producer must preserve the exact v1.204 future target key and report all exclusions. A later source refresh may create a new prospective freeze for then-future games, but may never overwrite or backfill this cutoff's evidence.

No model prediction, market join, target-outcome projection, refit, recalibration or redesign occurred in v1.204.
