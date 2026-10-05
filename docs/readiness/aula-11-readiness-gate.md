# Aula 11 — Readiness Gate

## Status

REVIEW CANDIDATE — reengineered v2, not yet student-ready.

## Central question

How can we change a fine-tuning experiment in a way that makes the observed behavior interpretable?

## Gates

### G1 — Pretraining vs fine-tuning

**PASS**

The lesson clearly separates pretrained encoder knowledge from task-specific classification-head adaptation.

### G2 — Deterministic initialization

**PASS — IMPLEMENTED**

Seeds are set before each newly initialized classification head.

### G3 — One-factor-at-a-time comparison

**PASS — IMPLEMENTED**

The lesson now separates:

```text
A vs B
→ more data, same epochs and learning rate

B vs C
→ more epochs, same data and learning rate
```

### G4 — No confounded learning-rate change

**PASS — IMPLEMENTED**

The previous simultaneous change in data size, epochs and learning rate was removed from the controlled comparison.

### G5 — Diagnostic-set hygiene

**PASS — IMPLEMENTED**

Diagnostic examples are checked to ensure they are not exact duplicates of training examples.

### G6 — No fixed execution claims

**PASS — IMPLEMENTED**

The lesson no longer pre-claims that the improved experiment must produce specific probability ranges or necessarily outperform the previous one.

### G7 — Confidence interpretation

**PASS**

Softmax probabilities and top-1/top-2 margin are treated as relative model outputs, not certainty.

### G8 — Exercise quality

**PASS — IMPLEMENTED**

The exercise compares two model artifacts for which only one experimental factor changed.

### G9 — Reproducibility

**PASS — BY DESIGN**

Internet OFF, versioned Kaggle Model, local_files_only=True, explicit seeds and documented experiment matrix.

### G10 — Kaggle Run All

**PASS — CURRENT REVISION**

The current revision completed successfully on Kaggle after the glossary-aligned notebook update.

### G11 — Pedagogical inspection

**PENDING**

Verify that the student can explain:

1. why a new classification head requires controlled initialization;
2. why changing several factors at once weakens causal interpretation;
3. what A vs B isolates;
4. what B vs C isolates;
5. why diagnostic examples must not be treated as a metric;
6. why softmax confidence is not calibrated certainty.

## Promotion rule

Promote only after G10 and G11 pass.

## Governing principle

> A better experiment changes as few causal factors as necessary and lets observed behavior—not expectation—drive the interpretation.
