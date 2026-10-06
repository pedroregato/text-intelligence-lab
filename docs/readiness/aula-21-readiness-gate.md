# Aula 21 — Readiness Gate

## Status

REVIEW CANDIDATE — initial planning foundation.

## Scope

Aula 21 — Planning and Goal Decomposition

Execution contract:

```text
Internet = OFF
GPU = OFF
External API = none
External side effects = none
Planner = deterministic/local
```

## Gates

### G1 — Reactive vs planning distinction
**PASS — IMPLEMENTED**

### G2 — Goal decomposition + explicit plan contract
**PASS — IMPLEMENTED**

The lesson now makes the chain explicit:

```text
goal
→ subgoals
→ plan steps
→ execution
```

Plan steps expose `subgoal`, `depends_on`, `preconditions`, `status` and `reason`.

### G3 — Plan validation
**PASS — IMPLEMENTED**

Validation now detects not only missing/future dependencies and disallowed actions, but also the safety ordering rule that approval must precede publication.

### G4 — Plan generation vs execution separation
**PASS — IMPLEMENTED**

### G5 — Replanning
**PASS — IMPLEMENTED**

When external state invalidates the original plan, the lesson now creates an explicit recovery plan v2, validates it and records both versions in `plan_history`.

### G6 — Comparative evidence lab
**PASS — IMPLEMENTED**

Reactive and plan-based architectures now receive the same external environment dynamics. The comparison includes `plan_versions` so replanning is observable and avoids privileged information on either side.

### G7 — Failure lab
**PASS — IMPLEMENTED**

### G8 — Architecture decision lab
**PASS — IMPLEMENTED**

### G9 — Living Glossary
**PASS — CURRENT REVISION**

Canonical entries for Planning, Goal Decomposition, Replanning and Plan Validation are present in the generated PT-BR and EN glossary views.

### G10 — Headless execution
**PASS — CURRENT REVISION**

Observed local nbconvert execution on 2026-10-06 completed successfully and produced:

```text
course/21-planning-and-goal-decomposition/21-til-planning-and-goal-decomposition.executed.ipynb
```

Observed evidence:

- valid plan → `Plan errors: []`;
- invalid plan → `('s3', 'approval_must_precede_publish')`;
- `simple_ready`: both architectures succeed; plan-based has higher `cost_proxy` (7.5 vs 6.0);
- `not_ready`: both safely refuse publication; plan-based has higher `cost_proxy` (5.5 vs 3.0);
- `state_changes`: both avoid publication; plan-based records `plan_versions = 2` and `replans = 1`, with higher `cost_proxy` (10.0 vs 6.0).

### G11 — Kaggle Run All
**PENDING**

### G12 — Pedagogical inspection
**PASS — CURRENT REVISION**

The observed run supports the intended claims:

1. goal decomposition and plan structure are explicit;
2. plan validation rejects an unsafe approval ordering before execution;
3. planning does not improve task success in the measured scenarios;
4. the reactive baseline remains cheaper in all measured scenarios;
5. replanning is observable as a second plan artifact, not only as a trace label;
6. the `state_changes` scenario shows that a reactive architecture can also stop safely when it revalidates critical state;
7. therefore the evidence does not justify planning by task success alone.

Pedagogical conclusion:

> **In this lab, explicit planning earns value mainly through inspectability, pre-execution validation and observable plan revision — not through higher task success. If those properties are not required, the simpler reactive architecture remains preferable.**

Inspect at least:

1. valid plan returns no validation errors;
2. invalid plan reports `approval_must_precede_publish`;
3. simple stable scenario reveals planning overhead when outcome is unchanged;
4. state-change scenario produces `plan_versions = 2` and `replans = 1`;
5. both architectures observe the same external state change;
6. student can explain goal decomposition vs planning, dependency vs precondition, and planning vs execution;
7. student can justify whether the measured planning benefit earns its complexity.

Verify that the student can explain:

1. reactive next-action vs explicit planning;
2. why a plan is an observable artifact rather than private reasoning;
3. why validation occurs before execution;
4. when replanning is justified;
5. when planning is only overhead;
6. how stale plans create risk;
7. why deterministic workflow may remain preferable.

## Promotion rule

Promote only after G9–G12 pass.

Current remaining blocker:

- G11 — Kaggle Run All / COMPLETE for the current revision.

## Governing principle

> **Planning is justified only when explicit decomposition, dependencies and revision create enough utility to offset planning overhead and stale-plan risk.**
