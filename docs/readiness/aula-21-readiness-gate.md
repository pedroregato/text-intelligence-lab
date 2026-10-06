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

### G2 — Explicit plan contract
**PASS — IMPLEMENTED**

### G3 — Plan validation
**PASS — IMPLEMENTED**

### G4 — Plan generation vs execution separation
**PASS — IMPLEMENTED**

### G5 — Replanning
**PASS — IMPLEMENTED**

### G6 — Comparative evidence lab
**PASS — IMPLEMENTED**

### G7 — Failure lab
**PASS — IMPLEMENTED**

### G8 — Architecture decision lab
**PASS — IMPLEMENTED**

### G9 — Living Glossary
**PARTIAL**

Canonical entries were added for Planning, Goal Decomposition, Replanning and Plan Validation. Generated views still need regeneration and validation.

### G10 — Headless execution
**PENDING**

### G11 — Kaggle Run All
**PENDING**

### G12 — Pedagogical inspection
**PENDING**

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

## Governing principle

> **Planning is justified only when explicit decomposition, dependencies and revision create enough utility to offset planning overhead and stale-plan risk.**
