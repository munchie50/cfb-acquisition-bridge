# CFB Engine — Challenger B 2025 Prospective Feature/Prediction Freeze Contract v1.187

Status: **FROZEN PROCEDURE / EXECUTION NOT YET ACCEPTED**
Parent: v1.186
Model identity: accepted v1.183/v1.184 Challenger B
Production v1 remains champion/fallback.

## Purpose
Construct the full 2025 Challenger-B fair-prediction artifact without exposing target-game outcomes to prediction construction, without refitting, and without market data.

## Frozen target population
Use the accepted v1.186 outcome-blind schedule projection from v1.157 artifact 10893997859:
- 880 qualified games;
- 770 FBS-vs-FBS;
- 110 FBS-vs-non-FBS;
- 839 regular;
- 10 conference championship;
- 31 postseason;
- 54 neutral.

The target key is exactly the 880 unique v1.186 game IDs. No target may be added or removed based on outcomes, model performance, market availability, or later inspection.

## Source isolation
Raw 2025 schedule/PBP bytes may contain outcomes and are quarantined source evidence only.

The prediction path may receive only:
- target identity/kickoff/venue/population fields from the accepted outcome-blind projection;
- prior-game information with source kickoff strictly earlier than target kickoff;
- frozen feature definitions from v1.159/v1.172;
- frozen v1.183 TRAIN scaling and coefficients.

For every target, its own PBP, own points/result, and all later-game PBP/results are forbidden inputs.

## Same-season feature construction
For each team-target pair:
1. order that team's qualified 2025 schedule strictly by kickoff;
2. identify prior games only where source kickoff < target kickoff;
3. compute mechanical and derived PBP aggregates using unchanged v1.172 semantics;
4. compute points-for/against only from prior completed games, shifted before the target row;
5. carry the same missing-PBP / primitive-completeness fail-closed logic used by v1.172;
6. never impute missing model predictors;
7. preserve opening-game and incomplete-history exclusions explicitly.

A raw source row may be read to construct a prior-game aggregate only after chronology has established that the source game precedes the target. Target outcome fields are never merged onto target prediction rows.

## Prediction construction
For eligible target games:
- construct the same 34 numeric side-specific predictors + venue state accepted by v1.180;
- use v1.183 TRAIN means/SDs exactly;
- use v1.183 coefficients exactly;
- selected lambdas remain margin 10, total 100, win 10;
- no refit, recalibration, coefficient change, feature change, or population change;
- output fair margin, fair total, and home-win probability only.

No market/external-rating fields may be read or joined.

## Required execution outputs
The producer must emit:
- 880-game target ledger;
- team-side feature/eligibility ledger;
- eligible fair-prediction table;
- exclusion ledger with deterministic reason(s);
- chronology/leakage audit;
- immutable manifest with source/artifact identities and SHA-256 for every output.

## Mandatory assertions
Execution must fail closed unless:
- target game IDs equal the accepted v1.186 880-game keyset exactly;
- target schedule contains no outcome or market fields;
- every source contribution satisfies source kickoff < target kickoff;
- no target's own game ID contributes to its features;
- no 2025 target outcome is present in prediction rows;
- all 34 numeric predictors for every scored row are finite;
- scaling/coefficient identities reproduce the accepted v1.183 artifact;
- prediction probabilities are finite and within [0,1];
- no market-like field is present;
- no fitting/optimization routine executes.

## Independent acceptance
A separate auditor must reproduce:
- target-key equality;
- population counts;
- chronology inequalities;
- own-game exclusion;
- model/scaling hashes;
- output hashes;
- prediction row/exclusion accounting.

The producer artifact is evidence, not acceptance.

## Outcome-opening gate
Even after producer and independent audit PASS, **2025 outcomes remain sealed**. Joining/scoring 2025 outcomes requires a separate explicit user authorization.

## Promotion boundary
No 2025 prediction or later TEST result automatically promotes Challenger B. Production v1 remains champion/fallback until a separately authorized promotion checkpoint.

## Immediate next action
Implement and run the v1.187 producer against pinned v1.157/v1.172/v1.183 artifacts, then independently audit it. Stop before any 2025 outcome join or scoring.
