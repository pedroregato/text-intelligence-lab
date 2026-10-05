# Aula 15 — Readiness Gate

## Status

AVAILABLE / STUDENT-READY — current revision validated.

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

**PASS — CURRENT REVISION**

Observed semantic retrieval evidence supports the lesson's intended interpretation:

- Semantic Recall@1 mean: 0.625
- Semantic Recall@2 mean: 0.75
- Semantic Recall@3 mean: 1.0

The results make top-k sensitivity directly observable: increasing k improves evidence coverage in this measured didactic set. This supports the lesson's core point that retrieval quality should be evaluated against labeled relevance rather than inferred from plausible-looking similarity scores alone.

The ranking inspection also showed that semantic scores were relatively close across documents, reinforcing that a generic dense encoder is not automatically a strong retriever and that Recall@k is needed to evaluate whether relevant evidence is actually recovered.

## Promotion rule

Promotion criteria satisfied: G8 and G9 pass on the current revision.

## Governing principle

> Retrieval quality must be measured against relevant evidence, not inferred from a visually plausible embedding space.
