# Week12 Friday 07CT/13CT overdue recovery — authenticated GitHub write size boundary

STATUS: DIAGNOSTIC_EXECUTED; CANONICAL_PUBLICATION_BLOCKED; RUN_INCOMPLETE.

Authoritative head before diagnostic: `8781aec46c5e329fe07dcd5282e77d209285ed4c`. No source/compile/reconciliation stages repeated. Previously verified Week12 market delta 127,606 characters, blob `754856df54bfb5040f552e827f44d9cd8dd30afd`; 70 matched identities, latest 68 PASS and two expired Tuesday CONDITIONAL.

Bounded authenticated GitHub Git Data API `create_blob` differential, using unchanged canonical market text prefixes and existing market packet delta (Git blob objects only, not refs):
- 127,606-character existing market packet delta: PASS; returned exact existing blob SHA `754856df54bfb5040f552e827f44d9cd8dd30afd`.
- 1,048,576-character canonical prefix: PASS; blob `4b1ba1b02f10a8d0d2cc8981e92d870cc7ac1365`.
- 3,145,728-character canonical prefix: PASS; blob `2d599d8a9624d78c37c1fc915582f4943388aba6`.
- 5,242,880-character canonical prefix: FAIL `h2 protocol error: error reading a body from connection`.
- Previous 6,942,678-character complete canonical market append through `create_blob` and `update_file`: same HTTP/2 failure; immediate SHA readback unchanged.

Conclusion: observed size-sensitive authenticated connector transport failure. Exact threshold, cause (request size, gateway or timeout) and compression feasibility NOT VERIFIED. Blob objects created in diagnostic are not commits or canonical writes. Do not construct a tree pointing at a truncated blob, split governed logical observations, or bypass publication contract. A viable fix must deliver the exact complete Git blob under authenticated authorization and compare its SHA before SHA/HEAD-guarded tree/commit/ref promotion, with independent readback. Candidate routes for future bounded evaluation: supported authenticated streaming/multipart GitHub write interface; a pre-authorized trusted worker with scoped GitHub credentials; or a governed persistence contract change explicitly approved and independently tested. Do not move canonical branch until full-byte write and acceptance proof.

No sportsbook quote, prospective conditional review, Hot Sheet acceptance or Friday 13CT deadline compliance is implied. Four recurring task topology and v1 champion remain unchanged.
