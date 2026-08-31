# TIL Documentation

This directory contains engineering documentation for the Text Intelligence Lab.

## Structure

- `decisions/` — Architecture Decision Records (ADRs): why an architectural or engineering choice was made.
- `experiments/` — Infrastructure and technical experiments: what was tested, how it was tested, evidence, and result.
- `runbooks/` — Repeatable operational procedures.
- `templates/` — Reusable documentation templates.

## Conventions

### ADR

Use an ADR when a durable architectural or engineering decision is made.

Recommended sections:

- Status
- Context
- Decision
- Alternatives Considered
- Consequences

### INFRA

Use an INFRA document when validating an integration, environment, tool, or operational assumption.

Recommended sections:

- Objective
- Hypothesis
- Environment
- Procedure
- Evidence
- Result
- Conclusion

## Current Infrastructure Experiments

- `INFRA-001` — OpenAI/Codex ↔ Kaggle MCP connectivity
- `INFRA-001B` — Local Codex ↔ Kaggle MCP connectivity
- `INFRA-002` — Local Kaggle CLI connectivity

## Principle

Architect → Implement small → Execute → Observe → Evaluate → Correct → Version → Expand
