# CFB Engine Core Execution Controls — v1.133

Status: ACTIVE CORE RULES
Scope: CFB Engine rebuild and operating routine
Authority effect: mandatory procedural controls; no change to frozen scientific/model/data contracts
Date: 2026-09-25
Companion authority: CFB_ENGINE_CORE_LEARNING_ENFORCEMENT_RULE_v1_132.md

## 1. Dependency-transition trigger

Whenever a material blocker closes, a new blocker appears, evidence changes a dependency, or a meaningful checkpoint completes:

1. Reconsider the global dependency order before continuing the prior next-step plan.
2. Identify the current highest-value executable work from authoritative state.
3. Do not continue an obsolete sequence merely because it was previously next.
4. Preserve frozen gates and dependency ordering.
5. Record material reordering when it affects the audit trail.

## 2. Completion-proof trigger

Before claiming DONE, PERSISTED, FIXED, ACCEPTED, PASS, FROZEN, or equivalent completion:

1. Identify the proof required for that claim.
2. Verify the actual persisted object/output rather than relying on a write response, filename, prose, or intended state.
3. Perform readback/hash verification where applicable.
4. Verify ancestry/supersession where authority depends on lineage.
5. Verify acceptance criteria separately from persistence.
6. If proof is incomplete, use a bounded status such as BUILT, EXECUTING, PARTIAL, or ACCEPTANCE PENDING instead of a completion claim.

Persistence proof and substantive acceptance proof remain distinct.

## 3. Repeated-friction escalation trigger

When substantially the same class of failure, correction, reminder, or workaround occurs twice:

1. Stop treating the event as an isolated patching problem.
2. Classify the recurring failure mode.
3. Investigate at least one causal layer deeper: workflow, trigger, contract, authority handling, serialization, tooling, dependency design, or other relevant system mechanism.
4. Prefer the smallest structural correction that prevents recurrence.
5. Install an enforceable trigger when the lesson generalizes.
6. Demonstrate the structural correction during later real work before marking the lesson LEARNED under v1.132.

This is the operational form of the project's systematic decomposition / onion-layer / Rubik's-Cube principle: repeated symptoms require examination of the system producing them.

## Compact core behavior

WAIT -> SWEEP.
CHANGE -> RECONSIDER DEPENDENCIES.
CLAIM COMPLETION -> PROVE IT.
REPEATED FAILURE -> INVESTIGATE THE SYSTEM.
LESSON -> INSTALL TRIGGER -> DEMONSTRATE IT.

## Stop/response enforcement

Before yielding, check whether any of these triggers fired during the cycle. If one fired, confirm its required action occurred. A response that skips an applicable core trigger is procedurally incomplete.

## Governance

These controls are effective immediately alongside production routine v5 and core learning-enforcement rule v1.132. Candidate routine v6 must incorporate and demonstrate them, but candidate status does not delay their applicability.

They do not authorize fitting, tuning, source/model promotion, production promotion, destructive cleanup, or 2025 TEST exposure. Existing fail-closed, authority, champion/challenger, persistence/readback, and explicit-authorization requirements remain intact.
