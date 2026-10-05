# Aula 12 — Readiness Gate

## Status

REVIEW CANDIDATE — reengineered v2, not yet student-ready.

## Central question

When does a more complex architecture earn its place over a strong classical baseline?

## Gates

### G1 — Fair classical comparison

**PASS — IMPLEMENTED**

MultinomialNB, LogisticRegression and LinearSVC use the same TF-IDF representation, folds and metric.

### G2 — Variability visible

**PASS — IMPLEMENTED**

The lesson compares mean F1 macro and fold-to-fold variability instead of ranking models only by mean.

### G3 — No fixed execution claims

**PASS — IMPLEMENTED**

Previously hard-coded F1 values and feature lists were removed from explanatory markdown.

### G4 — Dynamic evidence reading

**PASS — IMPLEMENTED**

Observed ranking, gap and variability are derived from the actual execution output.

### G5 — Feature interpretation discipline

**PASS — IMPLEMENTED**

Coefficient inspection is treated as corpus-specific evidence rather than a predetermined or causal explanation.

### G6 — Transformer comparison boundary

**PASS — IMPLEMENTED**

The lesson distinguishes conceptual trade-offs from a controlled empirical Baseline-vs-Transformer comparison.

### G7 — Utility framing

**PASS — IMPLEMENTED**

The lesson connects quality, cost, latency, interpretability, maintenance and risk without declaring a universal winner.

### G8 — Exercise quality

**PASS — IMPLEMENTED**

The exercise requires comparing observed mean and variability and judging whether evidence is strong enough for a superiority claim.

### G9 — Reproducibility

**PASS — BY DESIGN**

Internet OFF, CPU, explicit seed, same folds and metric, no fixed numerical results in markdown.

### G10 — Kaggle Run All

**PASS**

The current reengineered revision completed successfully on Kaggle with `KernelWorkerStatus.COMPLETE`.

### G11 — Pedagogical inspection

**PENDING**

Verify that the student can explain:

1. why representation and folds must be controlled in a model comparison;
2. why rank 1 is not equivalent to robust superiority;
3. why fold variability matters;
4. why coefficients are corpus-specific associations;
5. why this lesson does not itself prove classical models beat or lose to Transformers;
6. how utility extends beyond quality alone.

## Promotion rule

Promote only after G10 and G11 pass.

## Governing principle

> Complexity should be justified by measured utility, not by model class or marketing hierarchy.
