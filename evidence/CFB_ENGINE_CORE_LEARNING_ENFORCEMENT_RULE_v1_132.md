# CFB Engine Core Learning-Enforcement Rule — v1.132

Status: ACTIVE CORE RULE
Scope: CFB Engine rebuild and its operating routine
Authority effect: mandatory procedural control; does not alter frozen model/data/scientific contracts
Date: 2026-09-25

## Core principle

A lesson is not considered learned merely because it was noticed, explained, or documented. It must be converted into an enforceable trigger and subsequently demonstrated in real work.

Required lifecycle:

OBSERVED -> DOCUMENTED -> INSTALLED -> DEMONSTRATED -> LEARNED

A repeated failure reopens the lesson and requires correction of the enforcement mechanism.

## Mandatory learning-enforcement loop

After every meaningful mistake, correction, or newly discovered better practice:

1. Capture — state what failed or improved and why.
2. Generalize — classify whether the lesson is one-off or reusable.
3. Install — for reusable lessons, define the concrete trigger that must fire automatically.
4. Demonstrate — verify the trigger fires correctly during later applicable work.
5. Audit — if the same operational lesson requires another user reminder, treat that as evidence the enforcement mechanism failed and reopen it.

## Mandatory wait-state / independent-work trigger

Whenever the critical path becomes WAITING, QUEUED, RUNNING-EXTERNALLY, BLOCKED, or otherwise dependent on an external result:

1. Immediately perform an independent-work sweep.
2. Enumerate safe work that is genuinely independent of the pending dependency.
3. Execute the highest-value safe independent work before idling or yielding.
4. Do not manufacture parallel work.
5. Do not parallelize shared-authority mutation, dependency-ordered integration, fitting/tuning behind an uncleared gate, or work that could contaminate protected evidence.
6. Record why any obvious independent candidate was rejected when rejection matters to the audit trail.
7. Reconcile independent results with the completed dependency before authoritative downstream mutation.

Waiting is valid only when the sweep finds no safe work with material value or when tool/execution limits prevent it.

## Stop/response enforcement

Before yielding to the user, the routine must ask:

- Is anything currently waiting or externally running?
- If yes, was the independent-work sweep performed?
- Was safe material work available?
- If available, was it executed?
- If not executed, is the reason explicit and valid?
- Did any new lesson from this cycle receive an installed trigger rather than documentation alone?

A response checkpoint that skips this test is procedurally incomplete.

## Governance

This rule is core and applies immediately. It strengthens execution discipline without relaxing any existing authority, fail-closed, persistence/readback, champion/challenger, 2025 TEST-protection, or explicit-authorization gates.

Existing production routine v5 remains the stable routine baseline; this core rule is mandatory alongside it. Candidate routine v6 should incorporate and demonstrate this rule, but candidate status does not delay its core applicability.

No scientific/modeling decision is changed by this checkpoint.
