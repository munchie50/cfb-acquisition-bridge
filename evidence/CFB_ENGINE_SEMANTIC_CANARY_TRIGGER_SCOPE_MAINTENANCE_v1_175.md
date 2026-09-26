# CFB Engine — Semantic Canary Trigger Scope Maintenance v1.175

Status: **PASS — WORKFLOW NOISE DEBT REDUCED / SEMANTIC AUDIT CAPABILITY PRESERVED**
Parent recovery authority: v1.174

## Change
`.github/workflows/Main.yml` previously launched the full 2016–2025 semantic canary on nearly every push to `main`, excluding only giveaway workflow files. This caused evidence-only, narrow diagnostic, and recovery commits to each launch a redundant full-season audit.

The automatic trigger is now scoped to:
- pushes to `main` that change `.github/workflows/Main.yml` itself.

The existing `workflow_dispatch` trigger is preserved for deliberate full-season semantic audits.

Change commit: 125656614a100253941ac1f3d177623d5ffcd004
Workflow content SHA after readback: 1b1e5f4dca89d57fbabbbf1512f597f2e35efa07

## Why this is safe
The semantic-canary implementation is self-contained in Main.yml and downloads its public 2016–2025 PBP inputs at runtime. It does not execute repository producer scripts or consume repository evidence files. Therefore unrelated repository commits cannot alter its computation. Automatic execution on Main.yml changes directly covers changes to the canary implementation, while workflow_dispatch preserves intentional reruns against current upstream PBP.

The scope change does not alter semantic formulas, evidence acceptance, production/challenger locks, or model authorization.

## Expected transition behavior
The trigger-change commit itself legitimately launches one final push-triggered semantic-canary run because Main.yml changed. Previously queued/in-progress runs from earlier pushes may continue. New unrelated pushes after this commit should not launch additional Main.yml runs.

Locks unchanged: production v1 champion; no Challenger-B fitting/scoring authorization; 2025 protected; no market join; no promotion.
