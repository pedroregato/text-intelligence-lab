# Aula 5 — Readiness Gate

## Status

REVIEW CANDIDATE — reengineered v2, not yet student-ready.

## Central question

How does a TF-IDF representation become a class decision inside Multinomial Naive Bayes?

## Gates

### G1 — Pipeline transparency

**PASS — IMPLEMENTED**

The lesson opens the trained Pipeline into its TF-IDF and classifier components.

### G2 — Probability visibility

**PASS — IMPLEMENTED**

`predict_proba` is displayed per example and explicitly treated as model output rather than certainty.

### G3 — Feature evidence

**PASS — IMPLEMENTED**

The lesson inspects non-zero TF-IDF features and the corresponding `feature_log_prob_` values by class.

### G4 — Manual log-score reconstruction

**PASS — IMPLEMENTED**

Class scores are reconstructed as:

```text
X @ feature_log_prob_.T + class_log_prior_
```

and checked against the class returned by `.predict()`.

### G5 — Probability reconciliation

**PASS — IMPLEMENTED**

Manual normalization of log-scores is numerically reconciled with `predict_proba`.

### G6 — Contribution decomposition

**PASS — IMPLEMENTED**

Per-feature score contributions are exposed without claiming causal explanation.

### G7 — Exercise quality

**PASS — IMPLEMENTED**

The exercise asks the student to explain one prediction from text through TF-IDF, log-scores and probabilities.

### G8 — Reproducibility

**PASS — BY DESIGN**

Internet OFF, CPU, notebook-defined data, deterministic split, no fixed scores/probabilities in markdown.

### G9 — Kaggle Run All

**PENDING**

Fresh execution required after reengineering.

### G10 — Pedagogical inspection

**PENDING**

Verify that the student can explain:

1. what TF-IDF contributes to the classifier;
2. what `feature_log_prob_` represents;
3. where the class prior enters;
4. how the winning class is chosen;
5. why `predict_proba` is not certainty;
6. why contribution decomposition is not causal explanation.

## Promotion rule

Promote only after G9 and G10 pass.

## Governing principle

> The first classifier should expose the path from features to class score, not only the final label.
