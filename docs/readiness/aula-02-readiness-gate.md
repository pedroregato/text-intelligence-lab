# Aula 2 — Readiness Gate

## Status

REVIEW CANDIDATE — reengineered v2, not yet student-ready.

## Central question

Which normalization choices reduce superficial variation without destroying information needed by the task?

## Gates

### G1 — Tokenization and normalization

**PASS — IMPLEMENTED**

The lesson distinguishes tokenization from normalization and keeps transformations incremental.

### G2 — Accent collision

**PASS — IMPLEMENTED**

The notebook demonstrates that removing accents can collapse distinct forms such as `avó` and `avô` into the same normalized token.

### G3 — Negation preservation

**PASS — IMPLEMENTED**

The notebook demonstrates that removing `não` can collapse `não gostei` and `gostei` into the same token sequence.

### G4 — Trade-off framing

**PASS — IMPLEMENTED**

No transformation is presented as universally correct; each is connected to information preserved or lost.

### G5 — Exercise quality

**PASS — IMPLEMENTED**

The exercise requires preserving negation and reasoning about optional accent removal.

### G6 — Reproducibility

**PASS — BY DESIGN**

Internet OFF, CPU, Python standard library only, deterministic examples.

### G7 — Kaggle Run All

**PASS**

The current reengineered revision completed successfully on Kaggle with `KernelWorkerStatus.COMPLETE`.

### G8 — Pedagogical inspection

**PENDING**

Verify that the student can explain:

1. tokenization vs normalization;
2. why lowercasing often reduces superficial variation;
3. why removing accents can create lexical collisions;
4. why removing negation can destroy task-relevant information;
5. why preprocessing must be justified by the downstream objective.

## Promotion rule

Promote only after G7 and G8 pass.

## Governing principle

> Preprocessing should reduce nuisance variation without silently erasing distinctions that matter.
