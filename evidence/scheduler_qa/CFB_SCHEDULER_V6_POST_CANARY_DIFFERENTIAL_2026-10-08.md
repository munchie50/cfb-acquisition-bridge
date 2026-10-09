# V6 scheduled versus production differential

Natural scheduled isolated update PASS: 2026-10-09T01:25:09.391Z. Exact readback and separate closure verified.
Production morning canonical update RUN_INCOMPLETE: two rejected updates; canonical blob unchanged.
Manual evening market recovery RUN_INCOMPLETE: CBS page showed inconsistent future event states; data not accepted.
Conclusion: scheduler and GitHub updates work on isolated test path; production market write and live source qualification remain open. No production mutations or historical reconstruction.
