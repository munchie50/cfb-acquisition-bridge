# CFB QA — Generic Weekly REFRESH_SNAPSHOT Acceptance Readiness — 2026-09-30

Status: GENERIC INDEPENDENT ACCEPTANCE EXECUTABLE CONSTRUCTED / STATIC READBACK PENDING / NO WEEKLY CANDIDATE ACCEPTED
Scope: next-cycle acceptance plumbing only.

## Routine finding
The recurring Tuesday workflow can now create a complete v1.246 weekly candidate package, but the existing v1.207 independent 2026 acceptance executable is frozen to FIRST_FROZEN:
- exact 622-target population;
- v1.206 filenames;
- first-freeze artifact IDs/hashes;
- first-freeze fixed counts.

It cannot independently accept a normal v1.246 REFRESH_SNAPSHOT. Without a generic refresh acceptance executable, the next weekly candidate would reach a governance gap after generation: workflow green remains NOT_ACCEPTED and the accepted-source pointer could not legitimately advance.

## Constructed executable
Added `scripts/cfb_qa_weekly_refresh_acceptance.py`.

The audit is candidate-agnostic but fail-closed. It requires the complete v1.246 S0 directory retained by the Tuesday package and independently verifies:
- REFRESH_SNAPSHOT/v1.216 lineage and one immutable cutoff;
- exact target uniqueness and prediction+exclusion population accounting;
- two side-ledger rows per target;
- every target strictly future at cutoff;
- own-game exclusion and strict chronology;
- all prior kickoffs before both target and cutoff;
- finite prediction values and win-probability bounds;
- frozen coefficient/scaling byte identities;
- 108 coefficient terms, 34 scaling features and frozen lambdas;
- independent recomputation of margin/total/win predictions to 1e-12;
- every manifest-listed output byte hash;
- retained raw schedule/PBP existence and exact SHA-256 identities for later accepted-source pointer advancement.

The report explicitly records target outcomes unopened, market unjoined, and no fit/optimization.

## Deliberate non-automation
This executable is NOT wired to self-accept a Tuesday artifact. Candidate generation remains NOT_ACCEPTED. A future weekly package must be independently recovered, its exact artifact/ZIP identity frozen, this audit executed against those bytes, and the acceptance evidence persisted/read back before:
1. the weekly S0 boundary becomes accepted prospective REFRESH_SNAPSHOT evidence;
2. the accepted prediction source-state pointer advances;
3. any exact S2_K1 prediction consumer executes against that boundary.

## Scientific boundary
No candidate was generated or accepted during this construction. No source was reacquired, no target outcomes/market/wager data joined, no protected 2025 TEST accessed, no S2 prediction generated, and no Champion/model authority changed.

Frontier remains CADENCE WAIT.
