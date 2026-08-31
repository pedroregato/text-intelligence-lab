# ADR-007 — Kaggle MCP/API Strategy

## Status

Accepted

## Context

The Text Intelligence Lab (TIL) uses Kaggle as its primary educational and experimental execution environment and GitHub as the source of truth for code, documentation, and engineering history.

Kaggle currently exposes several integration mechanisms with overlapping but distinct purposes: Kaggle MCP, Kaggle CLI/API, kagglehub, and the Kaggle web interface.

## Decision

Use each mechanism according to its natural role:

- GitHub remains the source of truth for code, documentation, version history, and engineering decisions.
- Kaggle UI is used for interactive inspection, notebook operation, and educational workflows.
- Kaggle CLI/API is used for explicit, reproducible platform operations.
- kagglehub is used from Python for programmatic access to Kaggle datasets, models, competitions, and notebook outputs.
- Kaggle MCP is used as an optional agentic integration for Codex and other MCP-compatible clients.

The TIL core workflow must not depend on Kaggle MCP being available.

## Alternatives Considered

- Use Kaggle MCP for all Kaggle operations.
- Use only Kaggle CLI/API.
- Use only the Kaggle UI.
- Build a custom Kaggle REST integration.

## Consequences

- The architecture remains simple and resilient.
- MCP can increase agent productivity without becoming a single point of failure.
- Platform operations remain possible through CLI/API and UI when MCP is unavailable.
- Multiple Kaggle interfaces are retained, but each has a clearly defined responsibility.
