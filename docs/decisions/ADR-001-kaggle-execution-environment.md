# ADR-001 — Kaggle as Primary Execution Environment

## Status

Accepted

## Context

The Text Intelligence Lab (TIL) requires a primary environment for running
educational notebooks, experiments, datasets, and later GPU-based workloads.

The project also uses GitHub as the source of truth for code, documentation,
history, and engineering decisions.

## Decision

Kaggle will be the primary environment for educational and experimental
execution.

GitHub will remain the source of truth for code, documentation, version history,
and engineering artifacts.

## Alternatives Considered

- Local execution as the primary environment
- GitHub Codespaces
- Google Colab
- A self-hosted Jupyter environment

## Consequences

Positive consequences:

- Reproducible cloud execution
- Native integration with Kaggle datasets and notebooks
- Access to CPU/GPU resources when needed
- Alignment with the educational goals of the project

Trade-offs:

- Some workflows will depend on Kaggle platform capabilities
- Synchronization between GitHub and Kaggle will need to be defined and tested
- Local execution will remain useful for engineering tasks and lightweight tests
