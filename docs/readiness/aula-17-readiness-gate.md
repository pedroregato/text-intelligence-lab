# Aula 17 — Readiness Gate

## Status

REVIEW CANDIDATE — reengineered v2, not yet student-ready.

## Central question

Who or what decides whether a tool should be used, which tool to select, and how that decision differs from validation and execution?

## Gates

### G1 — Tool availability vs selection

**PASS — IMPLEMENTED**

The lesson explicitly distinguishes:

```text
tool availability
≠
tool selection
```

### G2 — Decision layer observable

**PASS — IMPLEMENTED**

A deterministic didactic selector converts user requests into one of:

- direct_answer;
- tool_request;
- abstain.

The selector emits a reason, tool name and arguments when applicable.

### G3 — End-to-end request flow

**PASS — IMPLEMENTED**

The notebook executes:

```text
user request
→ decision
→ tool request
→ validation
→ execution
→ result
→ assistant response
```

### G4 — Selection vs lookup

**PASS — IMPLEMENTED**

The execution layer now distinguishes a wrong semantic selection from a missing tool name in the registry.

### G5 — Semantic ambiguity

**PASS — IMPLEMENTED**

The lesson includes an ambiguity case showing that two tools may expose similar schemas while serving different intents.

### G6 — Failure taxonomy

**PASS — IMPLEMENTED**

The lesson separates:

- decision/tool selection failure;
- tool lookup failure;
- argument generation failure;
- validation failure;
- execution failure;
- result interpretation failure.

### G7 — Architecture minimality

**PASS**

The existing exercise on direct answer vs direct function vs structured tool remains and is now supported by an executable decision layer.

### G8 — Reproducibility

**PASS — BY DESIGN**

Internet OFF, GPU OFF, no external API, deterministic selector and local tools.

### G9 — Kaggle Run All

**PENDING**

Fresh execution required after reengineering.

### G10 — Pedagogical inspection

**PENDING**

Verify that the student can explain:

1. why a tool being available does not mean it should be used;
2. who/what may occupy the selection layer;
3. why schema validation cannot prove semantic correctness;
4. the difference between selecting the wrong tool and requesting a nonexistent tool;
5. why discovery does not eliminate semantic selection.

## Promotion rule

Promote only after G9 and G10 pass.

## Governing principle

> Tool use begins with a decision, not with an already-selected function call.
