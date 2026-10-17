# Aula 23 — Readiness Gate

## Status

PROPOSED — specification drafted; notebook not implemented.

## Scope

Aula 23 — Model-Driven Decisions: LLM as Decision Provider

Target execution contract:

```text
Internet = OFF
GPU = OFF (T4 optional)
External API = none in the main lab
Model = qwen-lm/qwen2.5/transformers/0.5b-instruct/1 (Apache 2.0)
External side effects = none
Fallback = explicit replay mode
```

## Prerequisites

- Aula 20 consolidated: explanation of why the deterministic `choose_next_action` occupies a decision-provider slot, plus at least one scenario where the agentic loop wins on counted work;
- ADR-010 accepted;
- model handle validated on Kaggle (ADR-003 rule).

## Gates

### G1 — Same interface for all decision providers
**PENDING**

Classifier, free-generation LLM and constrained LLM return the same `{intent, lesson_id, confidence}` object.

### G2 — Harness unchanged from Aula 20
**PENDING**

`AgentState`, `ACTIONS`, `governance_gate` and `execute_action` are identical to Aula 20, except for one `goal` field (`publish` | `status`) with a status-only termination condition, applied to every decision provider.

### G3 — Fair comparison
**PENDING**

- evaluation set disjoint from training set, checked in code;
- LLM few-shot examples drawn only from the classifier training set.

### G4 — Contract failures measured
**PENDING**

Invalid outputs are counted and shown, never silently dropped.

### G5 — Constrain before vs validate after
**PENDING**

Both variants executable on the same requests.

### G6 — LLM as next-action provider
**PENDING**

LLM replaces `choose_next_action` in the Aula 20 loop; gate decisions logged per step.

### G7 — Injection Failure Lab
**PENDING**

Shows what the gate blocks and what it cannot detect (plausible but wrong arguments).

### G8 — Measured latency
**PENDING**

Wall time per decision and generated tokens, measured on Kaggle CPU.

### G9 — Replay mode
**PENDING**

Explicit banner; replay tables match live tables for the recorded run.

### G10 — Architecture Decision Lab
**PENDING**

### G11 — Living Glossary
**PENDING**

Candidate new entries:

- learned decision provider;
- constrained decoding / constrained choice;
- validate after generation;
- prompt injection;
- replay mode;
- open-weight model.

Reuse existing entries: structured output, hallucination, confidence-gated routing, agent harness, governance gate.

### G12 — Notebook implementation
**PENDING**

### G13 — Headless execution (replay mode)
**PENDING**

### G14 — Kaggle Run All (live mode, model attached)
**PENDING**

### G15 — Pedagogical inspection
**PENDING**

## Promotion rule

Do not promote until G1–G15 pass.

## Governing principle

> The model proposes; the policy decides. The harness contains forbidden actions, not plausible wrong decisions.
