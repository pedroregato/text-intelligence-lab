# Aula 22 — Readiness Gate

## Status

REVIEW CANDIDATE — notebook implemented; execution and pedagogical validation pending.

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
- vendor-neutral nodes and transition policy;
- conditional routing;
- in-memory checkpoint store;
- interrupt / resume;
- durable-resume simulation;
- retry / recovery distinction;
- procedural baseline;
- comparative evidence table;
- checkpoint failure lab;
- Architecture Decision Lab;
- LangGraph mapping only after mechanism-first instruction.

### G13 — Headless execution
**PASS — CURRENT REVISION**

Observed local execution on Windows with `jupyter nbconvert --execute` completed successfully and produced:

```text
course/22-agent-orchestration-runtimes/
└── 22-til-agent-orchestration-runtimes.executed.ipynb
```

The observed warnings were environmental rather than lesson failures:

- Tornado/ZMQ registered an additional selector thread because the Windows Proactor event loop does not implement the required `add_reader` family;
- the temporary local Jupyter kernel reported unencrypted TCP transport.

The notebook executed to completion under the target local deterministic contract.

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
