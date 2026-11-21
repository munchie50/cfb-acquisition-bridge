# Original selector QA fixture — immutable blob staging, isolated commit

Status: FIXTURE_GIT_TREE_AND_COMMIT_CREATED_AND_READBACK_VERIFIED. PYTHON_TEST_NOT_EXECUTED. NOT_PRODUCTION.

At main head `a7a53299aded8f46b539dfa06200ab2bbffe7c3f`, GitHub created isolated fixture tree `855dd76e717a95e32a184d6b569bc5f070986c03` with original existing immutable blob objects at:
- `qa/fixtures/week12_selector_blobs/6862be6a1bd88a3290b1e90a49c33a7a87e92559` -> Git blob `6862be6a1bd88a3290b1e90a49c33a7a87e92559`
- `qa/fixtures/week12_selector_blobs/646bbe85edba726037e1b98125783ff2cd87a4e8` -> Git blob `646bbe85edba726037e1b98125783ff2cd87a4e8`

Recursive GitHub tree readback confirmed both paths and hashes. GitHub then created an **unreferenced** commit `9b2d3e0b5ce0e3c878270d3d3f8b173cfc8b86e8` with that tree and exact main parent `a7a53299aded8f46b539dfa06200ab2bbffe7c3f`; GitHub commit API readback confirmed tree and parent. No branch ref update. This stages fixture bytes without uploading them again and preserves existing main files, including the original QA source and unchanged preview.

For an authorized Python worker with actual access to this isolated commit, first verify checkout of exact commit and file SHA bytes, then run from repository root:

`python qa/cfb_week12_original_selector_integration_qa.py --repo . --blob-dir qa/fixtures/week12_selector_blobs`

Capture exact stdout/stderr/exit and verify original module imports and positive/negative results. An unreferenced commit is not necessarily fetchable by every git transport; check availability, do not infer worker execution from API readback. This does not prove production scheduler parity, current Hot Sheet publication, or betting authority. No fifth scheduled task or GitHub Actions scheduler was created.
