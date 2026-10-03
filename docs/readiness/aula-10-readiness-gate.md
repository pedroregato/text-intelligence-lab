# Aula 10 — Readiness Gate

## Status

REVIEW CANDIDATE — reengineered v2, not yet student-ready

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

**PENDING EXECUTION**

Required:

- Internet OFF;
- CPU;
- versioned Kaggle Model;
- `local_files_only=True`;
- successful Run All;
- no hard-coded execution results in markdown.

### G11 — Kaggle execution

**PENDING**

The reengineered notebook must complete a fresh Kaggle Run All.

### G12 — Pedagogical review

**PENDING**

Review should verify that the student can explain:

1. why a static lexical representation does not adapt itself to context;
2. how Q, K and V produce self-attention;
3. why a single cosine is insufficient evidence;
4. why grouped controls are stronger evidence;
5. how contextual separation changes across layers;
6. why attention weights are not equivalent to explanation;
7. how contextual embeddings support a downstream decision.

## Promotion rule

Promote to:

```text
Available / student-ready
```

only after G10, G11 and G12 pass.

## Governing principle

> Contextualization must be observed in the representation, not merely asserted in explanatory text.
