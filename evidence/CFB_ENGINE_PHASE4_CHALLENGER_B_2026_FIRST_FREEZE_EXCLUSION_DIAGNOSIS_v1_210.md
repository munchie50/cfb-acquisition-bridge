# CFB Engine — Challenger B 2026 First-Freeze Exclusion Diagnosis v1.210

Status: **PASS — MISSING-POINT EXCLUSIONS EXPLAINED BY UNFINISHED PRIOR GAMES**
Parent: v1.209
Diagnostic run: **36216293734**
Artifact: **10897546711**
Digest: `sha256:cfe621e460b726b3619134bb9e77bacc449ce37042e8aefc49b515cb16ce26d0`
Frozen cutoff: **2026-09-26T03:47:37.497112+00:00**

The accepted v1.208 first live-shadow freeze contained 96 excluded targets. v1.209 traced the `prior_points_missing` component without modifying any prediction.

Results:
- affected team-sides: **58**
- unique affected targets: **56**
- missing-prior trace rows: 58
- unique responsible prior games: **4**
- responsible prior games marked completed at cutoff: **0**
- responsible prior games incomplete/not-completed at cutoff: **4** (58 propagated team-side dependencies)

## Interpretation
The missing-points exclusions are expected fail-closed temporal behavior, not evidence of completed-game score corruption.

At the frozen cutoff, these four earlier-started games did not yet have completed results. Because v1.206 freezes all feature information to what was available at the cutoff, it may not:
- use their eventual outcomes,
- silently omit them from a team's chronology,
- impute their scores/features, or
- backfill the affected v1.208 predictions later.

Accordingly, the 56 affected targets remain valid exclusions under the first freeze.

A later prospective freeze may use those games only after they are completed/available at that later cutoff, and only for targets still strictly in the future. It must create new evidence rather than overwrite v1.208.

No prediction, model, threshold, calibration, population rule, market rule, or production status changed.
