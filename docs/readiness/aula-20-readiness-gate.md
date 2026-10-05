# Aula 20 — Readiness Gate

## Status

REVIEW CANDIDATE — initial agentic systems foundation.

## Scope

Aula 20 — Agentic Systems Foundations

Execution contract:

```text
Internet = OFF
GPU = OFF
External API = none
External side effects = none
Decision provider = deterministic/local
```

## Gates

### G1 — Workflow vs agentic loop distinction

**PASS — IMPLEMENTED**

The lesson explicitly distinguishes:

```text
workflow
→ transitions defined by execution policy

agentic loop
→ next action selected from observed state
```

Branching alone is not presented as sufficient evidence of agency.

### G2 — Explicit state and action space

**PASS — IMPLEMENTED**

The notebook defines:

- explicit `AgentState`;
- closed action allow-list;
- deterministic local capabilities;
- observable state transitions.

### G3 — Decision / authorization / execution separation

**PASS — IMPLEMENTED**

The architecture separates:

```text
choose_next_action
→ governance_gate
→ execute_action
```

The lesson preserves the TIL principle that a decision does not authorize itself.

### G4 — Termination and step budget

**PASS — IMPLEMENTED**

The loop includes:

- terminal success;
- safe stop;
- human escalation;
- step budget;
- explicit termination reasons.

A broken-provider lab demonstrates `step_budget_exceeded`.

### G5 — Human escalation

**PASS — IMPLEMENTED**

Ambiguous requests and missing approval can terminate in a controlled human escalation rather than speculative execution.

### G6 — Comparative evidence

**PASS — IMPLEMENTED**

The same scenarios are executed by:

- deterministic workflow;
- minimal agentic loop.

The comparison records:

- success;
- steps;
- decision count;
- tool calls;
- human intervention;
- termination reason;
- cost proxy;
- latency proxy.

### G7 — Failure taxonomy

**PASS — IMPLEMENTED**

The curriculum specification distinguishes:

- goal interpretation failure;
- next-action selection failure;
- invalid action;
- authorization failure;
- tool execution failure;
- observation/state failure;
- loop/termination failure;
- human escalation failure.

### G8 — Architecture decision lab

**PASS — IMPLEMENTED**

The student must choose among:

```text
direct_function
deterministic_workflow
agentic_loop
```

using variability, predictability, reversibility, cost, risk and supervision.

### G9 — Living Glossary

**PARTIAL**

Canonical entries were added for:

- Agentic Loop;
- Autonomy;
- Step Budget;
- Termination Condition;
- Human Escalation.

Generated PT-BR/EN/HTML glossary views must still be regenerated and validated.

### G10 — Headless execution

**PASS — CURRENT REVISION**

The current fairness-corrected revision completed end-to-end with `jupyter nbconvert --execute` on Windows. Workflow and agentic loop now start with the same information and both obtain `lesson_status` through the same capability.

Observed runtime warnings were environmental rather than lesson failures:

- Tornado/ZMQ registered a selector thread because the Windows Proactor event loop does not implement the required `add_reader` family;
- the temporary local Jupyter kernel reported unencrypted TCP transport.

The notebook produced the executed artifact successfully. Comparative evidence and failure-lab outputs remain subject to pedagogical inspection under G12.

### G11 — Kaggle Run All

**PENDING**

The current revision must complete on Kaggle with Internet OFF and GPU OFF.

### G12 — Pedagogical inspection

**PENDING**

Verify that a student can explain:

1. why branching does not automatically imply agency;
2. where next-action autonomy appears;
3. why decision and authorization remain separate;
4. why a step budget is architecturally necessary;
5. when human escalation is a successful outcome;
6. at least one scenario where a workflow is preferable;
7. whether the measured benefit of autonomy justifies its added complexity.

## Promotion rule

Promote only after G9–G12 pass.

## Governing principle

> **Autonomy is a measurable architectural property. It should be retained only when its utility justifies the additional cost, risk and loss of predictability.**
