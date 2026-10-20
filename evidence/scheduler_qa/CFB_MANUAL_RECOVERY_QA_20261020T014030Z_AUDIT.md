# CFB manual recovery QA — October19 CT

Run: CFB_MANUAL_RECOVERY_QA_20261020T014030Z
Scope: Test Routine v6 candidate; Production v5 and Champion unchanged.

## Trigger and expected behavior

Sunday weekly QA appended untagged recovery notes after the last structured checkpoint. Current recovery consumer preflight and two Sunday CI runs failed. Expected: preserve all historical bytes/failures, recover complete dependencies, qualify the current weekly selector without weakening historical semantics, run the actual consumer and complete existing CI, persist/read back independently, and sweep blocked dependencies through accepted ancestry.

## Executed corrections and demonstration

1. Reproduced uncheckpointed-tail failure on base a96e53d43211d388deb997ce65926d433ba992eb. Preserved Sunday notes; appended complete structured navigation. Exactly one October18 current weekly selector; October11 R2 remains an independently checked historical correction. Scorecard selector advanced to actual complete Week7 bytes. Unknown/stale/ambiguous successors remain rejected.
2. Existing full workflow uncovered a second defect after recovery passed: current scorecard bytes were used to rerender Saturday's historical sheet. Added explicit saved-source recovery through exact Git path/blob history, complete historical render equality, and separate current-readiness reporting. No current ledger or saved sheet is rewritten. Six saved-audit tests include authentic current-scorecard advancement and malformed binding rejection. Existing live gate stays strict.
3. 28 weekly,20 navigation,8 consumer and6 saved-audit tests passed (62 affected tests). Three weekly acceptance/no-op/fallback static gates passed. Wednesday static gate's event token was missing r[...] and falsely rejected the existing correct bounded scheduler; fixed the assertion, not the schedule.
4. Full existing GitHub Hot Sheet workflow39355186169 at eac4910dd24bb905ed0c1775f587e3c5b38f9d5e passed; full final navigation run39355315537 is separately checked for terminal closure. Wednesday fallback validation39355190919 passed.
5. Every modified code/control/evidence file was independently read back exactly. Large index transfer initially used truncated shell output (commit1c1e933); detected via independent Git diff, restored complete prior bytes plus tested append at f630af0 / blob2bca8206d06285bb8b30c49465fb8663c3b7b435, and installed exact length/hash transport protection. Intermediate failed commits/CI retained. Final index9800858 / blob88947ef6e0b5482e19322addb2dbed31bd69d6a5 is785225 characters;40 declared pointer bindings pass prewrite validation.

## Ancestry sweep — material correction to prior status

Original accepted archive10897612260 was independently downloaded and authenticated at ZIP SHA256772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf. All manifest output hashes checked; original622target/526prediction/96exclusion partition and immutable cutoff verified by existing archive gate.

All56 directed identities in retained Monday CBS Week8 capture d4491d759b0ed0e8954344d2fa77a58682c35da4 match original accepted targets:49 predictions,7 exclusions,147 existing numeric fields. Four explicit CBS abbreviations were resolved to exact directed archive identities; unknown/duplicate/unmatched identities reject. Diagnostic JSON337a23b03a10617ff87d9ba8c1c224cd3ebe1d9c and executable9267282972d636a399ebc2106f387019e6b24191 persisted/read back. This is identity/accepted-number recovery only; retained source rows are not fresh markets, current kickoff authority, earned decisions, recommendation or publication acceptance.

Therefore earlier blanket no-Week8-FIRST_FROZEN/prediction claims are overbroad. The actual blocker is Week7-specific normalizer/profile/schema/renderer/history bootstrap. Tuesday10CT scheduled REFRESH generation and independent acceptance are separate, not the existence test for original accepted predictions. Do not recompute or replace original numbers/exclusions merely to publish a new week.

## Reconciliation / protected boundaries

Current selected Week7 sheet unchanged:62 identities57PASS5CONDITIONAL, expired windows; no new actionable pick. Current saved integrity can pass while40 quote identities are elapsed; current readiness is not certified. Current market87d735251e328226087daa9aa1519c22c702a762, decision65b87247a18060069402d9814692ab57ce97dcf3, execution75caee4052e02ea7d2453d1d37fd3866e13ecc07, scorecard7a6defc4b93ff5c1752890130ff9bdaf50deb2e5 and original Week7 lineage d80e26c398de48e7a386ad9a627fe44f4111ac45 unchanged. No fitting, promotion, source refresh, market/outcome join, decision, wager, settlement, money, automation prompt/cadence/enabled mutation. BigNine paused.

## Learning, debt and next work

Benefit: restored recoverability and removed a false missing-model dependency. Cost: exact weekly-selector qualification and historical source recovery require maintained consumers. Net positive at bounded manual/CI scope; no betting-edge or natural delivery consistency claim. TestRoutinev6 ancestry check prevented unnecessary freeze/recomputation; whole-path demonstration exposed a second consumer failure beyond the first repair. Natural weekly producer prewrite compliance remains DEMONSTRATION_PENDING.

Next highest-value work: qualify a Week8 bootstrap/profile from recovered original49+7 lineage, actual kickoff/source and independently earned per-game decisions; retain closed Week7 and all histories. A later new weekly candidate is independently audited without replacing FIRST_FROZEN. Saturday21final-window coverage remains OPEN; existing four-task roles unchanged. Historical incomplete cycles are not replayed/upgraded. Do not manufacture a schedule or fifth task to close the gap. Future current publication still requires genuine fresh source/review/limits and full consumer/closure proof.
