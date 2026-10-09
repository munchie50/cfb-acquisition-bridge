# Original frozen clock source-path audit — October 9

Status: VERIFIED_STATIC_DATAFLOW_AND_METADATA_BOUNDARY; ORIGINAL_RAW_CLOCK_CAUSE_OPEN
Run: CFB_FROZEN_CLOCK_ORIGIN_QA_20261009T225151Z
Scope: original2026schedule path only, no model execution or new current-source acquisition.

Original preflight run36215880651 head d4e928b303e23a91338f01fdedcdc62d5d68f3f2 independently recovered. Its existing artifact10897001956 is listed unexpired with digest4dc70419b9aa3afdfa2570861490598da69b2bccfed878e438dc17b69a9a7ea8. Original producer run36216090860 head6b825c471915f053fa2b4c84240d8a7759cbca42 anchored by acceptedv1.208.

| Stage | Pinned reference | Proven clock operation |
|---|---|---|
| Raw source acquisition | original preflight workflow blob4ad801b30f22b41c44ac67dca99def38f2e12c12 at d4e928b | sportsdataverse/cfbfastR-cfb-data 2026schedule parquet; original scheduleSHA2565b2ff52996862b06b67309f1ebc27742e55c279ff4785c7a942915cdf820f1b1 recorded by acceptedv1.205 |
| Preflight | scripts/phase4_challenger_b_2026_source_preflight_v1_204.py blob329569538667ba98fbc45f58d864fdfef8ef6f17 at d4e928b | Read parquet; pandas to_datetime(start_date,utc=True); future projection uses seven columns, including start_date |
| Producer input | scripts/phase4_challenger_b_2026_predict_v1_206.py blob6364966e6eeb031019218ce94596240c1e29f308 at6b825c4 | Read original projected CSV; parse start_date UTC; target ledger writes S; prediction references use original target start_date |
| Authenticated output | artifact10897612260 archiveSHA256772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf | original targetCSV622rows, memberSHA2561873e2aaca5d9644e7583e3d9211fd38fc25a4b0a9fcbbef5157701c05604fe0 matched its original manifest |

Seven projected/output fields: season, game_id, start_date, home_team, away_team, neutral_site, population_class. No exact-time-known/TBD/status field is carried into the original target ledger. Therefore a consumer cannot certify exact kickoff maturity from those seven fields alone. This does NOT prove the raw source had a particular status flag, that such a flag was true for31games, or that00:00Eastern/04:00UTC is universally a placeholder.

Bounded code evidence shows no explicit04:00UTC replacement or Friday-date synthesis in the traced producer/preflight steps. Both use UTC normalization. The original raw timestamp datatype/timezone and status values are not inspected, so timezone interpretation, provider convention, later schedule changes or upstream causation are NOT ruled out. Static path evidence is not original runtime row-by-row preflight/raw-byte replay.

Artifact recovery result: GitHub artifact-download connector returned a ZIP file reference; scratch retrieval of that reference returned HTTP403. ZIP bytes not obtained, digest not computed for that failed retrieval, no original projected CSV readback. Separate artifact metadata/accepted digest remain references, not authenticated local bytes. Do not call this a canonical write rejection, expired-artifact proof, scheduler failure or fixed transport cause. No retry or alternate destination used.

Executed checks: pinned scripts independently read at historical heads and their Git blobs recomputed; Python AST parse successful; exact UTC parse/projection/input/output statement checks passed; accepted producer archive digest and target-member manifest digest reproduced; target cardinality622 and exact seven-column schema verified. No old producer execution,2025TEST, raw PBP or future outcomes opened. Original2026manifest and targetCSV only read from accepted archive during this origin audit.

Integration disposition: existing active kickoff contract already separates frozen snapshot timestamps from qualified operational schedule/deadline authority; no additional rule or source/model rewrite is warranted from unproved raw flags. Prior49row audit18exact/31different and38SaturdayID/time matches remains unchanged. Next safe research: acquire permitted original source/preflight bytes with expected digest and preserve original timezone/status columns before assigning a narrower cause; future snapshots need separately reviewed source-status retention, not edits to accepted frozen artifacts. Natural operational enforcement remains pending.

scientific_effect: NONE
champion_effect: NONE
