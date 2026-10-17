# Aula 22 — Readiness Gate

## Status

REVIEW CANDIDATE v2 — technical and pedagogical gates passed; Living Glossary regeneration remains before promotion.

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
**PARTIAL — CANONICAL ENTRIES PRESENT; GENERATED VIEWS PENDING**

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
**PASS — CURRENT v2**

Fresh local execution of the hardened v2 completed successfully with `jupyter nbconvert --execute` and produced:

```text
course/22-agent-orchestration-runtimes/
└── 22-til-agent-orchestration-runtimes.executed.ipynb
```

Observed warnings remained environmental rather than lesson failures:

- Tornado/ZMQ registered an additional selector thread because the Windows Proactor event loop does not implement the required `add_reader` family;
- the temporary local Jupyter kernel reported unencrypted TCP transport.

The current v2 therefore passes the local deterministic execution gate.

### G14 — Kaggle Run All
**PASS — CURRENT v2**

The hardened v2 was pushed to Kaggle after the final local headless run and completed successfully. This satisfies the current-revision Kaggle execution gate.

### G15 — Pedagogical inspection
**PASS — CURRENT v2 LOCAL EVIDENCE REVIEW**

Fresh executed outputs were inspected and confirmed:

- resume is controlled by the runtime rather than by manual node mutation;
- invalid runtime state ends as `failed / invalid_node`;
- `node_executions` is comparable across architectures and graph transitions are reported separately;
- utility profiles use explicit, architecture-neutral formulas;
- transient failure shows no artificial graph advantage;
- human interrupt and durable resume are behaviorally distinct;
- durable resume is the only current scenario where the graph runtime achieves lower burden under both declared utility profiles;
- the Decision Provider bridge accepts a valid `prepare` proposal and rejects an unsafe direct `publish` proposal;
- the saved local outputs are consistent with the written interpretation.

Observed evidence summary:

```text
linear              → procedural lower burden
branching           → procedural lower burden
human_interrupt     → procedural lower burden
transient_failure   → procedural lower burden
durable_resume      → graph runtime lower burden
```

This is the intended evidence pattern: graph orchestration earns its complexity only when durable state and recovery materially reduce reconstruction work.

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
