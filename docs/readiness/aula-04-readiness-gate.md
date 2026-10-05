# Aula 4 — Readiness Gate

## Status

REVIEW CANDIDATE — reengineered v2, not yet student-ready.

## Central question

How does a concrete TF-IDF value arise from term counts, document frequency, IDF smoothing and vector normalization?

## Gates

### G1 — TF/DF/IDF mechanism

**PASS — IMPLEMENTED**

The lesson separates term frequency, document frequency and inverse document frequency.

### G2 — Manual IDF

**PASS — IMPLEMENTED**

Students compute the scikit-learn default smoothed IDF:

```text
log((1 + n) / (1 + df)) + 1
```

### G3 — Raw TF-IDF

**PASS — IMPLEMENTED**

A raw TF × IDF weight is calculated manually before using TfidfVectorizer.

### G4 — L2 normalization

**PASS — IMPLEMENTED**

The default L2 normalization step is made explicit and computed manually.

### G5 — Manual × sklearn reconciliation

**PASS — IMPLEMENTED**

The manually reconstructed first document vector is compared against the TfidfVectorizer output with numerical equality checking.

### G6 — Variant awareness

**PASS — IMPLEMENTED**

The lesson states that TF-IDF has implementation variants and identifies the relevant sklearn defaults.

### G7 — Exercise quality

**PASS — IMPLEMENTED**

The exercise asks the student to reconstruct a weight and explain the difference between raw and normalized TF-IDF.

### G8 — Reproducibility

**PASS — BY DESIGN**

Internet OFF, CPU, notebook-defined corpus, no fixed numerical outputs in markdown.

### G9 — Kaggle Run All

**PENDING**

Fresh execution required after reengineering.

### G10 — Pedagogical inspection

**PENDING**

Verify that the student can explain:

1. TF vs DF;
2. why rare terms get higher IDF;
3. what smooth_idf changes;
4. why raw TF-IDF differs from the default sklearn output;
5. what L2 normalization does;
6. why TF-IDF is lexical/statistical rather than semantic.

## Promotion rule

Promote only after G9 and G10 pass.

## Governing principle

> A TF-IDF weight should be reconstructible from the stated formula and normalization choices.
