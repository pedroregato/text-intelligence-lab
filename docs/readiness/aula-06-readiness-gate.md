# Aula 6 — Readiness Gate

## Status

REVIEW CANDIDATE — reengineered v2, not yet student-ready.

## Central question

How do classification metrics arise from the actual error counts of a model?

## Gates

### G1 — Confusion matrix interpretation

**PASS — IMPLEMENTED**

The lesson starts from real/predicted labels and makes the confusion structure observable.

### G2 — Manual TP/FP/FN/TN derivation

**PASS — IMPLEMENTED**

For one class under a one-vs-rest view, TP, FP, FN and TN are calculated directly from label pairs.

### G3 — Manual metric derivation

**PASS — IMPLEMENTED**

Precision, recall and F1 are calculated from the counts before using scikit-learn.

### G4 — Independent verification

**PASS — IMPLEMENTED**

Manual results are checked against `precision_recall_fscore_support`.

### G5 — Same Accuracy Lab

**PASS — IMPLEMENTED**

Two synthetic classifiers with equal total accuracy expose different class-specific error profiles.

### G6 — Business interpretation

**PASS — IMPLEMENTED**

Metric choice is connected to false-positive and false-negative cost.

### G7 — Exercise quality

**PASS — IMPLEMENTED**

The exercise requires manual derivation before library verification.

### G8 — Reproducibility

**PASS — BY DESIGN**

Internet OFF, CPU, notebook-defined data and no fixed numerical results in explanatory markdown.

### G9 — Kaggle Run All

**PASS**

The current reengineered revision completed successfully on Kaggle with `KernelWorkerStatus.COMPLETE`.

### G10 — Pedagogical inspection

**PENDING**

Verify that the student can explain:

1. TP, FP, FN and TN for a selected class;
2. why precision reacts to false positives;
3. why recall reacts to false negatives;
4. why F1 depends on both;
5. why equal accuracy can hide different class behavior;
6. why metric choice depends on the cost of error.

## Promotion rule

Promote only after G9 and G10 pass.

## Governing principle

> Metrics should be derived from observable errors before being treated as library outputs.
