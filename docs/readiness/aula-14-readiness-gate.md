# Aula 14 — Readiness Gate

## Status

REVIEW CANDIDATE — reengineered v2, not yet student-ready.

## Central question

What changes when the system stops selecting one label and starts generating a sequence token by token?

## Gates

### G1 — Conceptual scope

**PASS**

The lesson separates classifier, encoder and autoregressive generator.

### G2 — Autoregressive mechanism observable

**PASS — IMPLEMENTED**

A complete token-by-token generation loop is executed. Each step records:

- current context;
- next-token distribution;
- chosen token;
- updated context;
- stopping condition.

### G3 — Decoding policy separated from model

**PASS — IMPLEMENTED**

Greedy, sampling, temperature, top-k and top-p are implemented as decoding policies over the same model logits.

### G4 — Sequence-level comparison

**PASS — IMPLEMENTED**

Greedy and sampling configurations are compared across complete generated sequences, not only one token.

### G5 — Stopping / cost / latency

**PASS — IMPLEMENTED**

The lesson distinguishes EOS from max_new_tokens and connects generated-token count to didactic cost and latency models.

### G6 — Structured output boundary

**PASS — IMPLEMENTED**

Generation and validation remain separate concerns.

### G7 — Failure lab

**PASS — IMPLEMENTED**

The lesson distinguishes decoding, stopping, contract and factual failures. The first three are executable in the notebook; factual failure is explicitly deferred to retrieval/RAG evidence.

### G8 — Exercise quality

**PASS — IMPLEMENTED**

Exercises require prediction, modification, failure analysis and architecture choice. Hint/solution references are opt-in.

### G9 — Reproducibility

**PASS — BY DESIGN**

Internet OFF, GPU OFF, no external API, deterministic micro-model and seeded sampling.

### G10 — Kaggle Run All

**PASS**

The reengineered notebook requires a fresh Kaggle execution.

### G11 — Pedagogical inspection

**PENDING**

Verify that the student can explain:

1. where autoregression occurs;
2. the difference between model logits and decoding policy;
3. temperature as distribution shaping rather than intelligence;
4. EOS versus application-imposed limits;
5. why generated-token count matters operationally;
6. why generation and structured-output validation are separate.

## Promotion rule

Promote to student-ready only after G10 and G11 pass.

## Governing principle

> Autoregressive generation must be observed as a loop, not inferred from a single next-token distribution.
