# Week12 profile activation and compiler gate — targeted current-main verification

Status: VERIFIED_WEEK12_WORKFLOW_COMPILER_SKIPPED_BY_DESIGN / SEPARATE_WEEK12_MODULE_EXISTS / CANONICAL_ACCEPTANCE_HOLD

## Exact current-main source evidence
- .github/workflows/cfb_monitor_collection.yml Git blob 27f6da1c220dcc029dd7c465c10cfbaba13b62e7: preflight source verification has continue-on-error true; WEEK12 path explicitly says 'Compiler preflight awaits a qualified Week 12 compiler.' Compile step if: steps.preflight_source.outcome == 'success' && steps.preflight_source.outputs.profile == 'WEEK11'; compile has continue-on-error true. Its Python reads evidence/audits/CFB_WEEK11_ORIGINAL_ANCESTRY_RECOVERY_20261109.json and uses Week11-specific compile. Therefore a successful Week12 collection workflow does not execute this compile or prove accepted Week12 publication.
- scripts/cfb_week12_publication.py Git blob 8656a3f8cc511715fc3a7a5905de1d5b2e3055bf: separate Week12 module DOES exist, profile WEEK12, original lineage SHA guard, compile(market,decision,source,lineage,cycle,as_of,decision_rows). It is not proven wired into the above GitHub workflow. Do not conflate 'module exists' with 'production executed', or claim Week12 compiler universally absent.
- Historical evidence/operational/CFB_WEEK12_NOV21_INTEGRITY_AUDIT_CONTINUATION_20261121.md already identified this exact workflow condition and eight collection runs where Week12 compile was skipped; this fresh-read independently confirms current source has not fixed the wiring.
- Nov21 original selector QA executed PASS in evidence/run_receipts/CFB_MARKET_MONITOR_20261121_13CT_MANUAL_CATCHUP_CONTINUATION.md. Selector QA is not a compiler/activation execution proof.
- Week12 original frozen archive identity is verified against accepted Week11 archive, but evidence/audits/CFB_WEEK12_CBS_ORIGINAL_LINEAGE_PREFLIGHT_20261115.json retains PROFILE_ACTIVATION_PENDING. Do not automatically supersede this from collection job success.

## Safe minimal repair frontier
1. Identify governing Week12 compiler admission contract and check the existing Week12 module's required arguments/side effects against it. Keep read-only candidate/test lane separate from production and preserve original frozen lineage.
2. Add a separately guarded Week12 read-only compiler preflight path only after original-module integration and deterministic negative tests (wrong lineage, incomplete source, stale/duplicate packet, mismatched decision pointer); never merely widen WEEK11 condition or swap import names.
3. Gate workflow reporting explicitly so 'collection success' cannot be represented as 'Week12 compile/publication success'. Do not mutate existing production workflow until governed acceptance and worker runtime are verified.
4. Independently qualify Week12 official finals for postgame canonical scorecard; do not confuse retrospective scorecard with prospective Hot Sheet activation. No late betting authorization.

No production workflow, four scheduled tasks, Champion, original predictions, canonical scorecard, market/decision, or money ledger changed in this read-only verification.
