# CFB Market Monitor audit — 2026-10-27 12:59 CT

- Cycle: `CFB_MARKET_MONITOR_20261027T175928Z`
- Authority: accepted recovery index `evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md` (`ddeca11cea78e0df52aeade13cf5b5c56c97d850`) with active v1.247 football-week cadence and the later accepted Week9 publication profile.
- RUN_STARTED: persisted and independently read back at `evidence/run_receipts/CFB_MARKET_MONITOR_20261027T175928Z_RUN_STARTED.md`; blob `cbd1f18aa56ffc7b0892bd23d29793ef13223cc5`.

## Provider budget

The Firecrawl account reported 1,000 credits remaining for the billing interval 2026-10-27T17:16:35.203Z through 2026-11-27T17:16:35.203Z. For the 31-day interval and cycle-day bucket 1, the governed cumulative release is `floor(1000 * 1 / 31) = 32` credits. Observed cycle consumption was 0 and no unsettled acquisition was known. No chargeable request was made in this run; direct public retrieval was sufficient and the decision cutoff had elapsed.

## Tuesday candidate boundary

GitHub Actions run `40532875540` completed successfully from commit `a6f49df4913aa6bb31bc2fa8b92a1ebbde172499`. Artifact `12746278820` (`cfb-weekly-tuesday-candidate-boundary`) had ZIP SHA-256 `29adfe868698d7368627d75ed42f3f2aead825266f3363e697677750b3d1975f`. Its manifest records 322 future targets at the 2026-10-27T15:38:14.731739Z cutoff and status `WEEKLY_CANDIDATE_BOUNDARY_NOT_ACCEPTED`; scientific acceptance, S2 production, market joins, and target-outcome joins are all false. The frozen Champion is unchanged.

## Fresh full-board capture

The public CBS Week9 board was recovered by 2026-10-27T18:01:32.658Z and normalized with the repository Week9 profile. The saved response contains 56 governed games and 112 team rows, all matched, with zero missing games. Kickoff section counts remain Tuesday 2, Wednesday 2, Thursday 2, Friday 3, Saturday morning 11, Saturday afternoon 22, Saturday evening/night 14, unresolved 0; total 56 with no duplicate identity. The capture is a mixed-book field-level fallback. Multi-book consensus is unavailable, Caesars is unverified, execution is unverified, sportsbook update clocks are unknown, and displayed Final/Open columns are quarantined.

Saved source: `evidence/operational/CFB_CBS_WEEK9_CURRENT_RESPONSE_20261027T180123Z.md`; source blob `c5f7b84cb1a6c70c389010e952d7a8a778c3e507`; normalized-source SHA-256 `3e8169995e475094e219a127a0de0184aa3a6a1a1511218fcb4c844be5078897`.

## Decision and publication disposition

The four saved partial CONDITIONAL reviews from the morning cycle expired at their immutable 2026-10-27T18:00:00Z evidence-validity cutoff. They were never appended to the canonical decision history, so the compiler cannot later present them as retained closed conditionals without inventing a prior canonical state.

- Middle Tennessee moneyline: post-cutoff FanDuel `-138`, numerically inside the original `-140 or better` threshold, but observed after cutoff. Closed; no resurrection or execution claim.
- Florida Atlantic `+13.5 -108` DraftKings: threshold still met post-cutoff, but closed; no execution claim.
- Cincinnati `+6.5 -105` DraftKings: threshold still met post-cutoff, but closed; no execution claim.
- Arizona `+3.5 -111` MGM: fails the original `+4.5 or better` threshold and is closed.

The canonical readiness audit at 2026-10-27T18:01:32Z still identifies 56 open games, 56 overdue decisions, and 56 review-required games. Forty-five original predictions remain not certified in the live publication packet and 11 are governed exclusions. The retained evidence batch has 23 open prediction games, 31 fetched-but-unreviewed sources, and one unavailable source; it is not a completed full-slate analytical review. No qualified fresh decision packet exists for all spreads, both moneylines, totals, alternates/team totals, or plausible parlays. Missing research is retained as debt, not converted to PASS.

Accordingly, no new current Hot Sheet was selected. `evidence/operational/CFB_WEEK9_HOT_SHEET_2026-10-26_0707CT.md` remains the last selected view, but it is stale and not certified as current for this cycle. Its frozen model content was not changed. The current recovery consumer preflight passed 243 navigation bindings only and does not cure the semantic or operational blockers.

Nebraska is present in the full-board capture: Nebraska `-7.5 -112` DraftKings, moneyline `-310` DraftKings, with `under 49.5 -108` MGM; Washington is `+8 -111` MGM, moneyline `+255` FanDuel, with `over 49.5 -110` DraftKings. These are post-cutoff mixed-book fallback observations, not a recommendation or verified Caesars execution offer.

## Ledgers, settlement, and blocker

Canonical market, decision, execution, and FIRST_FROZEN scorecard surfaces were read back at blobs `02df1f08c249bc859760e13de38b0c160f0759a8`, `5df8464b0b2372134939cf81d576e155d641113b`, `1a938f42e9f03e723bd50348f8a78dbd8b7098e9`, and `1e8e0a9c3cd34c163c32f6782cdfccf30b9e13d8`. No established Week9 execution, ticket, or authoritative final was found, so no execution, settlement, scorecard, production-bankroll, or separate $20 sandbox mutation was earned.

Exact blocker: the only richer reviews are expired and absent from canonical history, while the remaining analytical review is incomplete and all 56 canonical decisions are overdue. Publishing a current full-slate sheet would require fabricating history, downgrading richer evidence, or treating missing research as PASS.

Next safe action: retain this historical gap. At the next prospective Monitor cycle, use genuinely new immutable source/material reviews and game-specific remaining windows. Do not extend or revive the four expired cutoffs. A full Week9 publication also requires a governed disposition for preserving the expired noncanonical reviews without pretending that they previously entered the canonical stream.

Verdict: `RUN_INCOMPLETE`.
