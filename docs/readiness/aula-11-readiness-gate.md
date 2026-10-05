# Aula 11 — Readiness Gate

## Status

AVAILABLE / STUDENT-READY — current revision validated.

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

**PASS — CURRENT REVISION**

Observed evidence supports the lesson's intended interpretation:

- A_minimal: accuracy 0.3333, F1 macro 0.1667;
- B_more_data: accuracy 0.4444, F1 macro 0.3485;
- C_more_epochs: accuracy 0.4444, F1 macro 0.3333;
- diagnostic examples had no exact duplicates in training;
- top-1/top-2 margins were very small (0.002 to 0.017), with probabilities close to one third across classes.

The outputs make the controlled comparisons visible: A vs B isolates the effect of more data, while B vs C shows that more epochs did not improve the observed result. The diagnostic set also demonstrates that a top-1 prediction can be fragile even when a class is selected.

## Promotion rule

Promotion criteria satisfied: G10 and G11 pass on the current revision.

## Governing principle

> A better experiment changes as few causal factors as necessary and lets observed behavior—not expectation—drive the interpretation.
