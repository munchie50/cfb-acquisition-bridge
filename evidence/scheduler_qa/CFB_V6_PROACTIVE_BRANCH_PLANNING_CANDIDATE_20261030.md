# CFB Routine v6 — proactive branch planning control — 2026-10-30
Status: TEST ROUTINE v6 ADDITIVE QA CANDIDATE; not an accepted v5 production amendment and not v6 core reset.

## Purpose
Make thinking ahead an everyday execution behavior, not a one-off incident checklist. Fold into existing v6 Verify State -> Global Dependency Reconsideration -> Select Work -> Verify Executable Readiness and expected-actual/WAIT sweep stages; do not create a separate routine stage, task, or long document for each action.

## Minimal behavior
For every material work unit, before executing or waiting, state the expected successful result, two or three materially plausible failure/partial-success classes, the observable evidence that distinguishes them, the immediate safe next action per branch, and the stop/rollback/deadline boundary. Keep this in the existing work receipt/checkpoint; routine trivial steps need only an implicit branch, not ceremony.
After execution, match observed evidence to one branch, execute the next safe step or mark a specific blocked dependency. When evidence is inconclusive, preserve uncertainty and pursue independent work rather than claiming completion. Revisit branches after material new evidence. Never invent future results, automatically retry unknown-side-effect work, or turn QA branch planning into authority for production mutation.

## Application
Scheduler: PASS/NO_UPDATE/STARTED-no-terminal/persistence/partial PASS; distinguish dispatch from missing receipts.
Model and Challenger: acceptance, mixed performance, leakage/regression, insufficient prospective sample; advance, revise, hold with trigger or retire.
Source/market: fresh source, qualified fallback, missing/unverified quote, expired cutoff; avoid retroactive betting decisions.
Routine promotion: evidence complete, targeted gap, failed regression; accept only independently authorized controls, isolate rollback.
WAIT: trigger independent debt sweep and plan post-trigger continuation before idle.

## Demonstration and acceptance
Historical Oct30 13CT precommitted branch plan is an authored example, not proof that the natural task executed. Test against at least one successful natural cycle, one early NO_UPDATE, and one started canonical write rejection; verify it changes time-to-next-action without extra tasks, spurious retries, false closure or materially increased burden. Compare v5 baseline and classify measured value. Promote selectively only after accepted QA and explicit minor-version registration. Keep four production tasks unchanged.
