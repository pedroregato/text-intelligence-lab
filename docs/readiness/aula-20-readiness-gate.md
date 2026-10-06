# Aula 20 — Readiness Gate

## Status

AVAILABLE / STUDENT-READY — previous validated revision; current pedagogical revision requires fresh execution.

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

### G3B — Agent Harness

**PASS — IMPLEMENTED**

The lesson now explicitly identifies the runtime layer around the decision provider as an Agent Harness and distinguishes its responsibilities from the model/decision provider, MCP, workflows and orchestration.

The notebook makes the following components visible inside the harness boundary:

- explicit state;
- action space;
- governance gate;
- capability execution;
- observation and state update;
- step budget;
- termination;
- human escalation;
- observability.

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

**PASS — CURRENT REVISION**

Canonical entries are present for:

- Agentic Loop;
- Autonomy;
- Step Budget;
- Termination Condition;
- Human Escalation;
- Agent Harness.

The PT-BR, EN and HTML glossary views were regenerated after the Agent Harness entry was added.

### G10 — Headless execution

**RECHECK REQUIRED — PEDAGOGICAL REVISION UPDATED NOTEBOOK**

The current fairness-corrected revision completed end-to-end with `jupyter nbconvert --execute` on Windows. Workflow and agentic loop now start with the same information and both obtain `lesson_status` through the same capability.

Observed runtime warnings were environmental rather than lesson failures:

- Tornado/ZMQ registered a selector thread because the Windows Proactor event loop does not implement the required `add_reader` family;
- the temporary local Jupyter kernel reported unencrypted TCP transport.

The notebook produced the executed artifact successfully. Comparative evidence and failure-lab outputs remain subject to pedagogical inspection under G12.

### G11 — Kaggle Run All

**RECHECK REQUIRED — PEDAGOGICAL REVISION UPDATED NOTEBOOK**

Kaggle version 2 completed successfully for `pedrogentil/til-20-agentic-systems-foundations` with the lesson's execution contract preserved.

### G12 — Pedagogical inspection

**PASS — CURRENT REVISION**

Observed comparative evidence is intentionally non-triumphal:

- ready_approved:
  - workflow: success, 5 steps, cost proxy 5.0;
  - agentic loop: success, 5 steps, 5 decisions, cost proxy 7.5;
- not_ready:
  - workflow stops after 2 steps, cost proxy 2.0;
  - agentic loop reaches the same terminal result after 3 steps, cost proxy 4.5;
- ambiguous:
  - both escalate safely to a human;
  - workflow does so without executing a step, while agentic loop spends one decision step and cost proxy 1.5;
- approval_missing:
  - both escalate safely to a human;
  - workflow uses 4 steps / cost proxy 4.0, while agentic loop uses 5 steps / cost proxy 7.5.

Therefore, in the measured scenarios, autonomy did not produce additional task utility. It introduced decision overhead without improving success or escalation outcomes.

The failure lab also produced:

```text
inspect_request
inspect_request
inspect_request
Termination: step_budget_exceeded
```

This makes the new governance surface directly observable: an agentic loop can fail to make progress and therefore requires explicit termination controls.

Pedagogical conclusion:

> In this task, the deterministic workflow remains the preferred architecture. The agentic loop is useful as a mechanism study, but its additional complexity has not yet been justified by observed utility.

## Promotion rule

Pedagogical criteria are satisfied. Final promotion of the current notebook revision requires regenerated glossary views, fresh headless execution and a fresh Kaggle Run All.

## Governing principle

> **Autonomy is a measurable architectural property. It should be retained only when its utility justifies the additional cost, risk and loss of predictability.**
