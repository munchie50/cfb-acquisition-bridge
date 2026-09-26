# CFB Engine — Challenger B 2016 Membership Resolution v1.155

Status: PROSPECTIVE SAME-PROVIDER RESOLUTION / MEMBERSHIP GATE CLOSED FOR 2016
Parent: v1.154
No fitting or scoring.

## Problem
Recovered CBS historical season maps begin at 2017. Challenger B requires TRAIN coverage beginning in 2016.

## Same-provider evidence
Fresh historical CBS evidence was checked before constructing the rule:
- CBS published a 2016 all-128-FBS-team surface/list, establishing 128 active FBS teams for the 2016 season.
- CBS's Coastal Carolina transition report states Coastal Carolina's gridiron FBS debut would be in 2017 and, with UAB returning to the field in 2017, those changes would bring FBS to 130 teams.
- The exact recovered qualified 2017 CBS season map contains 130 teams.

Therefore the deterministic 2016 active-FBS membership map is:
**recovered qualified 2017 CBS map minus Coastal Carolina minus UAB = 128 teams.**

This is a prospective same-provider derivation, not a claim that an original 2016 serialized map was recovered.

## Controls
- Idaho remains FBS in 2016 and 2017.
- Liberty is not added until its 2018 transition.
- UAB is excluded from the active 2016 game universe because its football program did not field a 2016 team; it returns in 2017.
- Coastal Carolina is excluded from 2016 FBS membership; its FBS football transition begins in 2017.
- Resulting identity count must equal CBS's 2016 128-team invariant.
- Any schedule participant alias must still resolve deterministically to the canonical 128 identities; unresolved identities fail closed.

## Classification
2016 no longer requires provider-division substitution. Membership can be constructed from exact recovered 2017 CBS authority plus CBS-documented 2017 additions/return and the CBS 2016 128-team invariant.

This closes membership identity for 2016 prospectively while preserving the distinction that the original 2016 historical serialized membership artifact was not recovered.

## Next
Build the 2016-2025 season membership artifact and corrected relevant-FBS schedule population, then run the v1.153 class-conformance audit. 2025 projection remains outcome-blind.

Locks unchanged.
