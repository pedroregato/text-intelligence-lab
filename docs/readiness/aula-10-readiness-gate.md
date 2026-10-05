# Aula 10 — Readiness Gate

## Status

AVAILABLE / STUDENT-READY — current revision validated.

## Scope

Aula 10 — Embeddings contextuais e Transformers

Execution baseline:

```text
Model = goddiao/distilbert-base-multilingual-cased
Framework = PyTorch
Variation = default
Version = 1
Internet = OFF
GPU = OFF
```

## Gates

### G1 — Conceptual progression

**PASS**

The lesson now follows:

```text
static representation
→ manual self-attention
→ real contextual encoder
→ controlled semantic evidence
→ layer-wise analysis
→ downstream disambiguation
```

### G2 — Attention mechanism is observable

**PASS — IMPLEMENTED**

The notebook computes scaled dot-product self-attention explicitly with NumPy and shows that the same base representation for `banco` can produce a different contextualized output when neighboring tokens change.

### G3 — Model dependency is explicit

**PASS — IMPLEMENTED**

The Kaggle kernel metadata declares the versioned model source and the notebook fails early if the expected local model path is absent.

### G4 — Real subword tokenization

**PASS — IMPLEMENTED**

The notebook queries the attached tokenizer for real segmentations instead of presenting an invented tokenization.

### G5 — Controlled contextualization experiment

**PASS — IMPLEMENTED**

The notebook compares six Portuguese sentences containing `banco`, grouped into financial and seat senses, and computes:

- full pairwise cosine matrix;
- mean within-sense similarity;
- mean between-sense similarity;
- observed gap;
- lexical controls.

No fixed numerical result is written into the lesson.

### G6 — Layer-wise contextualization

**PASS — IMPLEMENTED**

The notebook requests hidden states and measures within-sense versus between-sense similarity across layers.

### G7 — Downstream mini-application

**PASS — IMPLEMENTED**

The notebook builds centroids for the two senses and uses contextual token embeddings for deterministic nearest-centroid disambiguation.

### G8 — Attention interpretation caution

**PASS — IMPLEMENTED**

The notebook inspects real attention heads and treats attention weights as observable mechanism evidence, not as automatic causal explanation.

### G9 — Exercise quality

**PASS — IMPLEMENTED**

Exercises require:

- predict → observe → explain with `manga`;
- finding and interpreting an ambiguous or failing `banco` example;
- use of the TIL hint/solution interaction pattern.

### G10 — Reproducibility

**PASS**

Required:

- Internet OFF;
- CPU;
- versioned Kaggle Model;
- `local_files_only=True`;
- successful Run All;
- no hard-coded execution results in markdown.

### G11 — Kaggle execution

**PASS**

The reengineered v2 completed successfully on Kaggle with the required versioned DistilBERT model attached, Internet OFF and CPU execution.

### G12 — Pedagogical review

**PASS — CURRENT REVISION**

Observed evidence supports the intended claims:

- the six "banco" examples produced higher mean cosine within the same sense (0.889) than across different senses (0.833), for an observed gap of 0.056;
- lexical controls showed that absolute cosine values are not sufficient on their own, supporting the need for grouped comparisons;
- layer-wise gaps were not monotonic: layers 0 and 1 were slightly negative (-0.003, -0.006), then became positive from layer 2 onward, reaching 0.056 at layer 6;
- centroid disambiguation correctly separated a financial case ("o banco recusou meu financiamento") and a seat case ("pintei o banco que fica na varanda");
- the intentionally ambiguous case ("fui ao banco") produced close scores (0.890 vs 0.907), making uncertainty observable instead of hiding it;
- attention heads showed clearly different token-weight patterns, supporting the distinction between attention as mechanism evidence and attention as causal explanation.

The lesson therefore demonstrates contextualization through measured representation changes, group-level evidence, layer-wise dynamics, downstream use and attention-pattern diversity.

## Promotion rule

Promote to:

```text
Available / student-ready
```

only after G10, G11 and G12 pass. All three gates now pass on the current revision.

## Governing principle

> Contextualization must be observed in the representation, not merely asserted in explanatory text.
