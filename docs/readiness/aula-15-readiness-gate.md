# Aula 15 — Readiness Gate

## Status

REVIEW CANDIDATE — reengineered v2, not yet student-ready.

## Gates

### G1 — Retrieval mechanism

**PASS — IMPLEMENTED**

Lexical and semantic retrieval both execute real ranking pipelines.

### G2 — Real semantic representation

**PASS — IMPLEMENTED**

Semantic vectors are produced by the versioned multilingual DistilBERT encoder. No manually positioned 2D semantic vectors remain in the core experiment.

### G3 — Lexical failure / semantic comparison

**PASS — IMPLEMENTED**

The same low-overlap query is executed through TF-IDF and the contextual encoder. The lesson does not assume semantic search must win.

### G4 — Retrieval metrics

**PASS — IMPLEMENTED**

Labeled didactic queries are evaluated with Recall@1, Recall@2 and Recall@3.

### G5 — Top-k interpretation

**PASS — IMPLEMENTED**

Top-k is connected to measured retrieval recall rather than only list length.

### G6 — Grounding boundary

**PASS**

Retrieval, evidence pack and deterministic grounding remain separate from generation.

### G7 — Reproducibility

**PASS — BY DESIGN**

Internet OFF, CPU, versioned Kaggle Model, local_files_only=True.

### G8 — Kaggle Run All

**PASS — CURRENT REVISION**

The current reengineered revision completed successfully on Kaggle.

### G9 — Pedagogical inspection

**PENDING**

Verify that the student can explain why a dense encoder is not automatically a strong retriever, why Recall@k is needed, and why observed ranking outranks intuition.

## Promotion rule

Promote only after G8 and G9 pass.

## Governing principle

> Retrieval quality must be measured against relevant evidence, not inferred from a visually plausible embedding space.
