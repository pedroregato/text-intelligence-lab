# TIL Documentation

This directory contains the engineering, pedagogical, experimental, and reference documentation for the Text Intelligence Lab.

## Structure

- `decisions/` — Architecture Decision Records (ADRs): why an architectural or engineering choice was made.
- `experiments/` — Infrastructure and educational experiments: what was tested, how it was tested, evidence, and result.
- `glossary/` — Living Glossary sources and generated PT-BR/EN/web views.
- `references/` — Living Reference Library and editorial policy.
- `case-studies/` — external and internal cases used as teaching evidence.
- `readiness/` — lesson readiness and release checks.
- `runbooks/` — repeatable operational procedures.
- `templates/` — reusable documentation templates.
- `ENGINEERING.md` — execution architecture and engineering policies.
- `ROADMAP.md` — curriculum state and next learning blocks.
- `TIL-COURSE-DESIGN-CONTRACT.md` — minimum pedagogical and operational standards.

## Conventions

### ADR

Use an ADR when a durable architectural, engineering, or course-design decision is made.

Recommended sections:

- Status
- Context
- Decision
- Alternatives Considered
- Consequences

The headless-first rule for interactive notebooks is recorded in `decisions/ADR-009-headless-first-interactive-notebooks.md`.

### Experiment

Use an experiment document when validating an integration, environment, model, metric, or operational assumption.

Recommended sections:

- Objective
- Hypothesis
- Environment
- Procedure
- Evidence
- Result
- Conclusion

Measured model evidence consumed by Aula 13C must keep its full provenance here and expose only the comparable summary in `data/model-evidence/til-model-evidence.csv`.

## Current Infrastructure Experiments

- `INFRA-001` — OpenAI/Codex ↔ Kaggle MCP connectivity
- `INFRA-001B` — Local Codex ↔ Kaggle MCP connectivity
- `INFRA-002` — Local Kaggle CLI connectivity
- `EDU-INFRA-001` — first TIL Kaggle notebook execution
- `EDU-INFRA-002` — Kaggle model resource validation

## Current Engineering Principle

```text
Architect
→ Implement small
→ Execute headless
→ Execute on Kaggle
→ Observe
→ Evaluate
→ Correct
→ Version
→ Expand
```

Interactivity is an optional learning layer; it must not be required for a notebook to finish `Run All`.
