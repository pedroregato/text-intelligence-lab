# Aula 22 — Readiness Gate

## Status

PROPOSED — architecture defined; implementation not started.

## Scope

Aula 22 — Agent Orchestration Runtimes

Target execution contract:

```text
Internet = OFF
GPU = OFF
External API = none
External side effects = none
Base lab = local / deterministic
LangGraph = optional reference implementation
```

## Gates

### G1 — Harness vs orchestration runtime distinction
**PASS — SPECIFIED**

### G2 — Procedural vs graph comparison
**PASS — SPECIFIED**

### G3 — Explicit shared state
**PASS — SPECIFIED**

### G4 — Conditional routing
**PASS — SPECIFIED**

### G5 — Checkpointing
**PASS — SPECIFIED**

### G6 — Interrupt / resume
**PASS — SPECIFIED**

### G7 — Durable execution
**PASS — SPECIFIED**

### G8 — Recovery
**PASS — SPECIFIED**

### G9 — Human-in-the-loop
**PASS — SPECIFIED**

### G10 — Architecture Decision Lab
**PASS — SPECIFIED**

### G11 — Living Glossary
**PARTIAL**

Canonical entries added for:

- Orchestration Runtime;
- Checkpoint;
- Durable Execution;
- Interrupt and Resume.

Generated glossary views still need regeneration.

### G12 — Notebook implementation
**PENDING**

### G13 — Headless execution
**PENDING**

### G14 — Kaggle Run All
**PENDING**

### G15 — Pedagogical inspection
**PENDING**

## LangGraph policy

LangGraph is a reference implementation, not the definition of orchestration.

The lesson must first teach:

```text
shared state
nodes
edges
conditional routing
checkpoint
interrupt
resume
recovery
```

and only then map those concepts to framework primitives.

## Promotion rule

Do not promote until G11–G15 pass.

## Governing principle

> **A graph runtime is justified only when coordination, persistence, recovery, or human intervention create enough value to offset the additional runtime and conceptual overhead.**
