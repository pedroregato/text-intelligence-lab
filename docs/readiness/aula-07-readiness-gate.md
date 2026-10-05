# Aula 7 — Readiness Gate

## Status

REVIEW CANDIDATE — reengineered v2, not yet student-ready.

## Central question

How can hyperparameters be selected without turning final evaluation data into part of the decision process?

## Gates

### G1 — Model-selection roles

**PASS — IMPLEMENTED**

The lesson separates development data, CV folds, selection holdout and final test by role.

### G2 — Cross-validation mechanism

**PASS — IMPLEMENTED**

Stratified cross-validation is used to select hyperparameters within development data.

### G3 — Variance interpretation

**PASS — IMPLEMENTED**

Students inspect mean and standard deviation across folds instead of reading only the top-ranked configuration.

### G4 — Leakage anti-pattern

**PASS — IMPLEMENTED**

A controlled anti-pattern repeatedly evaluates candidates on the same holdout and selects the winner from that holdout.

### G5 — Procedural evidence

**PASS — IMPLEMENTED**

The lesson explicitly demonstrates that a holdout becomes selection/validation data as soon as its score influences model choice. The conclusion does not depend on a forced score gap.

### G6 — Independent final test

**PASS — IMPLEMENTED**

The final test is isolated before tuning and used only after decisions are frozen.

### G7 — Exercise quality

**PASS — IMPLEMENTED**

Exercises require leakage diagnosis, grid sensitivity analysis and design of a correct evaluation flow.

### G8 — Reproducibility

**PASS — BY DESIGN**

Internet OFF, CPU, deterministic stratified splits and CV, no fixed numerical result in markdown.

### G9 — Kaggle Run All

**PENDING**

Fresh execution required after reengineering.

### G10 — Pedagogical inspection

**PENDING**

Verify that the student can explain:

1. parameter vs hyperparameter;
2. validation vs final test;
3. why a repeatedly inspected holdout is no longer a final test;
4. why leakage is a procedural problem even when the observed score gap is small;
5. why more candidate configurations increase selection risk.

## Promotion rule

Promote only after G9 and G10 pass.

## Governing principle

> A dataset is not a final test because of its filename; it is a final test only while it remains outside the decision process.
