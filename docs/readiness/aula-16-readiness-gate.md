# Aula 16 — Readiness Gate

## Status

REVIEW CANDIDATE — reengineered v2, not yet student-ready.

## Gates

### G1 — RAG decomposition

**PASS**

Retrieval, evidence pack, context, generation, attribution and evaluation remain separately observable.

### G2 — Fair generation-only baseline

**PASS — IMPLEMENTED**

Generation-only and RAG use the same didactic autoregressive generator. The comparison no longer forces generation-only to abstain.

### G3 — Evidence-conditioned generation

**PASS — IMPLEMENTED**

Retrieved evidence changes the logits used at the fact-bearing generation step. A token-by-token trace makes the conditioning observable.

### G4 — Counterfactual evidence test

**PASS — IMPLEMENTED**

The same question and generator are executed with deliberately stale/wrong evidence, showing that groundedness does not imply factual correctness.

### G5 — Failure localization

**PASS**

Retrieval, context, generation, attribution and factuality/governance failures remain separately diagnosed.

### G6 — Governance

**PASS**

The lesson distinguishes semantic relevance from authority, status and effective evidence.

### G7 — Reproducibility

**PASS — BY DESIGN**

Internet OFF, GPU OFF, no external API and deterministic local generation.

### G8 — Kaggle Run All

**PENDING**

Fresh execution required after generator reengineering.

### G9 — Pedagogical inspection

**PENDING**

Verify that the student can explain the causal difference between generation-only, RAG with correct evidence, and RAG with wrong evidence.

## Promotion rule

Promote only after G8 and G9 pass.

## Governing principle

> RAG should demonstrate that retrieved evidence changes generation; it should not win because the baseline was programmed to fail.
