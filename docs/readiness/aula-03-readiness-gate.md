# Aula 3 — Readiness Gate

## Status

REVIEW CANDIDATE — reengineered v2, not yet student-ready.

## Central question

What information does Bag-of-Words preserve, and what does it discard?

## Gates

### G1 — Vocabulary and matrix

**PASS — IMPLEMENTED**

The lesson makes vocabulary, feature columns and document-term counts visible.

### G2 — Order-loss evidence

**PASS — IMPLEMENTED**

Two sentences with identical words/counts in different order are transformed and verified to produce identical Bag-of-Words vectors.

### G3 — Representation-collision interpretation

**PASS — IMPLEMENTED**

The lesson explains that order alone is discarded when lexical identity and frequency remain unchanged.

### G4 — Counterexample discipline

**PASS — IMPLEMENTED**

The notebook clarifies that Bag-of-Words does not make all different sentences identical; lexical composition changes still alter the vector.

### G5 — Exercise quality

**PASS — IMPLEMENTED**

The student must construct a representation collision and explain what information was lost.

### G6 — Reproducibility

**PASS — BY DESIGN**

Internet OFF, CPU, notebook-defined data and deterministic CountVectorizer behavior.

### G7 — Kaggle Run All

**PENDING**

Fresh execution required after reengineering.

### G8 — Pedagogical inspection

**PENDING**

Verify that the student can explain:

1. how words become features;
2. what each matrix axis means;
3. why sparse representation matters;
4. why two different word orders can produce the same vector;
5. what information is preserved versus discarded.

## Promotion rule

Promote only after G7 and G8 pass.

## Governing principle

> A representation limitation should be visible as a concrete collision, not only described in prose.
