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
