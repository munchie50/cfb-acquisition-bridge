# CFB Engine — Challenger B 2026 First-Freeze PBP Exclusion Diagnosis v1.212

Status: **PASS — PBP EXCLUSIONS FULLY EXPLAINED BY KNOWN v1.204 SOURCE GAPS**
Parent: v1.211
Run: **36216368448**
Artifact: **10897022432**
Digest: `sha256:05b0da3e6d48b4e179444e8fd2048d6945ddc62fe0120f466cbb42645a126441`
Cutoff: **2026-09-26T03:47:37.497112+00:00**

Results:
- prior-PBP-missing affected team-sides: **33**
- unique affected targets: **33**
- unique responsible prior games: **2**
- responsible game IDs: **401862779, 401869941**
- all 33 propagated dependencies point to completed games
- exact match to the two PBP gaps already frozen by v1.204
- no additional hidden PBP gap detected
- predictions changed: false

Interpretation: the PBP-related exclusions in the accepted v1.208 first live-shadow freeze are expected propagation from the two already-known source-lag games. They are not evidence of an additional producer or source-completeness defect.

The accepted first-freeze predictions/exclusions remain immutable. A later prospective freeze may benefit from a later PBP snapshot only for games still future at that later cutoff; it may not backfill v1.208.

No model, prediction, calibration, population, market rule, or production status changed.
