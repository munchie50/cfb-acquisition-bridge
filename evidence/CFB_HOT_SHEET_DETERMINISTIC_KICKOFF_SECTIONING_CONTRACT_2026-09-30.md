# CFB Hot Sheet — Deterministic Kickoff Sectioning Contract — 2026-09-30

Status: ACTIVE OPERATIONAL PRESENTATION CONTROL
Scope: Hot Sheet construction only. No Champion/model/market/decision/execution/outcome authority changes.

## Purpose
Prevent placeholder NEXT UP sections, omitted games, duplicate games, and timezone-driven misclassification.

## Governing time
All kickoff classification is normalized to America/Chicago before section assignment. Source kickoff times must be authoritative schedule data. Do not infer an unknown kickoff.

## Required mutually exclusive sections
1. NEXT UP — THURSDAY: every governed Thursday game.
2. NEXT UP — FRIDAY: every governed Friday game.
3. NEXT UP — SATURDAY MORNING: every governed Saturday game with CT kickoff before 12:00.
4. NEXT UP — SATURDAY AFTERNOON: every governed Saturday game with CT kickoff at or after 12:00 and before 17:00.
5. NEXT UP — SATURDAY EVENING/NIGHT: every governed Saturday game with CT kickoff at or after 17:00.
6. UNRESOLVED KICKOFF: governed game whose authoritative kickoff cannot be established. Never guess a bucket.

## Exactly-once invariant
Every governed relevant-FBS game must appear in exactly one kickoff section. No duplicate membership. Sum of section membership counts, including UNRESOLVED KICKOFF, must equal governed-slate cardinality.

A Hot Sheet may not claim conforming completion when the invariant fails.

## Render requirements
Each populated section must show actual game rows, not a placeholder such as “games remain on the canonical full-slate view.”
Each row should carry, when already governed/available: kickoff CT, game, Frozen Engine, current market, total, and current decision state.
If a section truly has zero governed games, state “No governed [section] games.”
Priority/watchlist views may follow the chronological sections but never substitute for them.

## Contamination boundary
Sectioning consumes existing governed identities, kickoff data, frozen predictions, market observations, and decision states. It must not create/recompute a prediction, market observation, threshold, decision, execution, or outcome.

## Validation
Before persistence:
- normalize kickoff to America/Chicago;
- assign exactly one section;
- assert no duplicate game identity;
- assert union equals governed slate;
- assert section count sum equals governed-slate count;
- fail closed to UNRESOLVED KICKOFF when schedule authority is missing;
- persist and independently read back the Hot Sheet.

## 2026 Week 5 correction note
CBS Week 5 schedule authority establishes Thursday Oct. 1 games Western Kentucky at New Mexico State (8:00 PM ET = 7:00 PM CT) and North Texas at Tulsa (9:00 PM ET = 8:00 PM CT). Friday Oct. 2 establishes Liberty at Delaware and Pittsburgh at Virginia Tech at 7:00 PM ET = 6:00 PM CT, plus Penn State at Northwestern at 8:00 PM ET = 7:00 PM CT. These must render as actual Thursday/Friday rows rather than placeholders.

Installed under Production Routine v5 after the 2026-09-30 Hot Sheet presentation defect was observed.


## 2026-10-04 prospective football-week day coverage correction
Trigger: the Sunday 2026-10-04 07:05 CT Market Monitor recovered authoritative Week 6 Tuesday and Wednesday modeled kickoffs. The prior six-bucket contract could not classify those known kickoffs without omission or false relabeling and correctly failed closed.

This section prospectively supersedes **Required mutually exclusive sections** above for all future Hot Sheets. Historical Hot Sheets and historical RUN_INCOMPLETE receipts are not rewritten.

### Required mutually exclusive sections — superseding set
1. NEXT UP — TUESDAY: every governed Tuesday game.
2. NEXT UP — WEDNESDAY: every governed Wednesday game.
3. NEXT UP — THURSDAY: every governed Thursday game.
4. NEXT UP — FRIDAY: every governed Friday game.
5. NEXT UP — SATURDAY MORNING: every governed Saturday game with CT kickoff before 12:00.
6. NEXT UP — SATURDAY AFTERNOON: every governed Saturday game with CT kickoff at or after 12:00 and before 17:00.
7. NEXT UP — SATURDAY EVENING/NIGHT: every governed Saturday game with CT kickoff at or after 17:00.
8. UNRESOLVED KICKOFF: governed game whose authoritative kickoff cannot be established. Never guess a bucket.

Exactly-once validation now applies across all eight buckets. Known Tuesday/Wednesday kickoffs may not be placed in UNRESOLVED KICKOFF or relabeled into Thursday-Saturday. If a future governed football-week schedule contains a known kickoff on a day not covered by this superseding set, fail closed and amend the presentation authority prospectively rather than omit or misclassify the game.

Decision cadence follows the same principle: Tuesday/Wednesday games require a realistic pre-kickoff reconciliation deadline and final practical execution cutoff based on their actual kickoff window. Do not inherit a Thursday-Saturday deadline mechanically.

Scientific/Champion effect: NONE. Presentation/operational control only.


## 2026-10-08 exact-time source-conflict QA clarification
Trigger: independent primary-source recovery for Iowa at Washington found the official schedule/UW preview at 20:00 CT but Iowa game-week notes at 20:05 CT. Research evidence: `evidence/operational/CFB_WEEK6_OCT08_FRIDAY_PRIMARY_SOURCE_CONTEXT_QA.md`, independently read-back blob 6833796673dfd7a063342ec7d14f43aef744c9d3.

Before treating multiple sources as kickoff-time corroboration:
1. Normalize every observation's explicit date, time and timezone to America/Chicago.
2. Compare exact timestamps, not merely weekday or section labels. Two times in the same section can still conflict.
3. If primary sources conflict, preserve each source/time and mark exact-time qualification unresolved. Do not silently round, average, select the later time or claim an exact match.
4. Where all observations establish the same section, that section may remain established while the exact minute is unresolved. Do not falsely discard known day/section information.
5. Preserve immutable frozen timestamps. Any later operational presentation change requires separately qualified schedule evidence.
6. Do not extend an already-governed practical cutoff based solely on a conflicting later timestamp. No missing cutoff is invented by this control.
7. Sectioning/time QA is independent of final player availability, current market offer qualification and decision completion.

Bounded demonstration: actual Friday source evidence was normalized using Python datetime/ZoneInfo. Five schedule times matched the retained research; the Iowa notes observation differed by exactly +5 minutes. This demonstrates source-conflict detection against this case, not resolution of the conflict or natural production execution.
Producer-consumer demonstration remains pending at the next real Hot Sheet source qualification. Champion/scientific/decision authority is unchanged.
