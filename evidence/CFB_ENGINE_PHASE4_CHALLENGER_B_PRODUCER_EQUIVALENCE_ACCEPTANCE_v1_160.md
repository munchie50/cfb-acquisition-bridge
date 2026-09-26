# CFB Engine — Challenger B Producer Equivalence Acceptance v1.160

Status: PASS / FROZEN PRODUCER SEMANTICS REPRODUCED
Run: 36208558029
Head: eb7286615a47e94d837efe5c1ab370ef4f5ff61a
Artifact: 10894822205
Artifact digest: sha256:d22b113440f185a6ca7797b9e3252ade42c65892b9daf3e90beb9df394cf3511

Fresh execution of the frozen v1.109/v1.115 producers on the original v1.108 schedule reproduced all four accepted artifacts:
- mechanical features: 12,718 vs 12,718, identical key set, zero column mismatches;
- mechanical primitives: 12,718 vs 12,718, identical key set, zero column mismatches;
- derived features: 12,718 vs 12,718, identical key set, zero column mismatches;
- derived primitives: 12,718 vs 12,718, identical key set, zero column mismatches.

Comparison tolerance was 1e-12 for numeric serialization/runtime representation. No 2025 accessed. No fit or score performed.

Consequence: frozen feature formulas are reproducible. Challenger-B correction may proceed as a population/input/chronology extension under v1.159-v1.161; feature redesign is neither required nor authorized.
