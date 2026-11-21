# Original Week12 selector QA contradiction — read-only source audit

Status: SOURCE-LEVEL DETERMINISTIC BLOCKER IDENTIFIED / NOT EXECUTED / NO CANONICAL MUTATION.
Read on current main:
- qa/cfb_week12_original_selector_integration_qa.py blob dc7764ca7827c3460c737ecfa37af90ce1ba4cc7
- scripts/cfb_hot_sheet_current_decision_binding_gate.py blob 8a6022e3aeea0d5c5fc0e9d455a9b56b4f1eb581
- qa/cfb_actual_canonical_selector_readback_qa.py blob a116848b9f050967a8d1fd166b634ec286de0667

## Exact deterministic contradiction
The original Week12 integration QA sets PREVIEW to evidence/operational/CFB_WEEK12_20261120_MANUAL_RENDERED_HOT_SHEET_PREVIEW_NOT_ACCEPTED.md and executes audit(sheet,ledger) expecting a positive verdict. That preview begins with **NONCANONICAL MANUAL RECOVERY PREVIEW — NOT ACCEPTED PRODUCTION / NO ACTIONABLE WAGERS**. The current original audit() explicitly rejects any sheet containing NONCANONICAL, NOT ACCEPTED, or NO ACTIONABLE WAGERS before evaluating the decision SHA. Thus this QA's positive branch cannot pass using its declared current preview and original gate, even when the exact base/delta blobs are staged. A failed execution at this first boundary would not prove a bad reconstructed ledger.

## Governed next action
Do NOT remove the fail-closed provisional rejection or strip labels to manufacture acceptance. Split QA into (a) explicit expected-negative provisional-preview test, and (b) a separate positive original-module test using a properly authorized candidate-only fixture that does not purport to be accepted production; its PASS is limited to supplied binding and cannot authorize canonical publication. Independently execute actual-canonical readback against a single pinned main snapshot, separately from virtual QA. Obtain original governance approval and full acceptance before any canonical pointer mutation. No current venue-qualified offers or wagers established.

## Drift warning
Earlier instructions to stage 3.6MB base+delta and simply run the unchanged Week12 integration QA omitted this deterministic positive-branch contradiction. Do not spend runtime transfer effort expecting this unchanged QA to pass. Source-level finding only, not an executed regression result.
