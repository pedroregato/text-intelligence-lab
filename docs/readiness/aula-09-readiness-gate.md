# Aula 9 — Readiness Gate

## Status

REVIEW CANDIDATE — reengineered v2, not yet student-ready.

## Central question

What can a static word embedding represent, and what evidence shows its limitations?

## Gates

### G1 — Distributed representation

**PASS — IMPLEMENTED**

The lesson introduces dense lexical vectors and cosine similarity without treating dimensions as directly interpretable semantic features.

### G2 — Controlled Word2Vec experiment

**PASS — IMPLEMENTED**

The notebook trains Skip-gram Word2Vec on a transparent synthetic corpus with deliberately repeated context patterns.

### G3 — Neighbor interpretation discipline

**PASS — IMPLEMENTED**

Nearest neighbors are treated as observations from the learned geometry, not as proof of human-like understanding.

### G4 — Stability Lab

**PASS — IMPLEMENTED**

The same corpus and hyperparameters are trained under multiple seeds. Top-5 neighborhoods and pairwise Jaccard overlap are compared to make small-data instability observable.

### G5 — Static embedding limitation

**PASS — IMPLEMENTED**

The corpus contains `banco` in financial and seat contexts, and the notebook directly demonstrates that `model.wv["banco"]` returns one stored lexical vector regardless of occurrence context.

### G6 — Polysemy interpretation

**PASS — IMPLEMENTED**

The lesson distinguishes:

```text
one lexical vector
from
one contextual representation per occurrence
```

The bridge to Aula 10 does not claim that Transformer input embeddings are equivalent to Word2Vec.

### G7 — Corpus sensitivity

**PASS — IMPLEMENTED**

An exercise requires changing the distribution of contexts for `banco` and observing how geometry changes while the representation remains static by token.

### G8 — Exercise quality

**PASS — IMPLEMENTED**

Exercises require stability analysis, structural explanation of static embeddings, and corpus modification. Hint/solution access is opt-in.

### G9 — Reproducibility

**PASS — BY DESIGN**

Internet OFF, CPU, workers=1, explicit seeds, synthetic corpus, and no fixed numerical outcomes in markdown.

### G10 — Kaggle Run All

**PENDING**

The reengineered notebook requires a fresh Kaggle execution.

### G11 — Pedagogical inspection

**PENDING**

Verify that the student can explain:

1. what Word2Vec learns from co-occurrence;
2. why cosine similarity is representation-dependent evidence, not semantic truth;
3. why a small corpus can produce unstable neighborhoods;
4. what changing the seed tests;
5. why `banco` has only one stored vector in Word2Vec;
6. how that limitation motivates contextual representations in Aula 10.

## Promotion rule

Promote only after G10 and G11 pass.

## Governing principle

> The limitation of static embeddings should be observed in the representation itself, not merely asserted in markdown.
