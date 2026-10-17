# Aula 22 — Readiness Gate

## Status

REVIEW CANDIDATE v2 — runtime semantics, evidence design and pedagogy hardened; fresh execution and final inspection required.

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
**PASS — IMPLEMENTED**

The current notebook includes:

- explicit shared state;
- vendor-neutral nodes and governed transition policy;
- real conditional routing through a revision branch;
- in-memory checkpoint store with checkpoint counters persisted consistently;
- interrupt / resume controlled by the runtime rather than by manual node mutation;
- durable-resume simulation with explicit process-loss semantics;
- distinct terminal semantics for completed, interrupted, recoverable error and failed;
- retry / resume / recovery distinction;
- fair procedural baseline with real pause/resume behavior;
- reconstruction work measured after process loss instead of injected as an arbitrary restart constant;
- comparable raw metrics with node executions separated from graph transitions;
- contextual utility profiles using the same declared weights across architectures;
- Decision Provider bridge back to Aula 20 with governed agentic routing;
- invalid-checkpoint failure lab;
- Architecture Decision Lab;
- Coding Lab with checkpoint and compensation challenges;
- reference answers for the comprehension check;
- LangGraph mapping only after mechanism-first instruction.

### G13 — Headless execution
**PENDING — FRESH RUN REQUIRED FOR v2**

A prior revision passed local headless execution, but the current v2 changed:

- routing semantics;
- resume control;
- failure states;
- procedural baseline;
- evidence metrics;
- contextual utility analysis;
- agentic routing bridge;
- coding exercises.

Therefore the earlier PASS is retained only as historical evidence and does **not** promote the current revision.

### G14 — Kaggle Run All
**PENDING — CURRENT v2 NOT YET EXECUTED**

A previous revision reached Kaggle execution, but v2 must receive a fresh Run All after local headless validation.

### G15 — Pedagogical inspection
**PENDING — FINAL REVIEW AFTER EXECUTION**

Final inspection must confirm:

- no manual node jump during resume;
- invalid runtime state ends as failed;
- raw metrics compare compatible quantities;
- utility weights are explicit and architecture-neutral;
- transient failure narrative does not claim a graph advantage that the evidence does not show;
- human interrupt and durable resume remain semantically distinct;
- Decision Provider integration preserves runtime governance;
- saved outputs match the written interpretation.

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
