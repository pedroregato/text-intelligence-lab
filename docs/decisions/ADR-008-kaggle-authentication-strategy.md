# ADR-008 — Kaggle Authentication Strategy

## Status

Accepted

## Context

The TIL requires secure authentication for local Kaggle CLI usage and may require authentication for Codex/Kaggle MCP integration.

Kaggle currently supports OAuth-based authentication, access tokens, and legacy kaggle.json credentials.

## Decision

- Prefer OAuth for interactive local Kaggle CLI usage.
- Prefer OAuth for Kaggle MCP when the client supports it reliably.
- Use a Kaggle access token only when OAuth is unsuitable, such as non-interactive automation or MCP compatibility requirements.
- Do not use legacy kaggle.json credentials as the default TIL authentication mechanism.
- Never commit Kaggle credentials, tokens, secrets, or local authentication files to GitHub.

## Alternatives Considered

- Use kaggle.json as the default mechanism.
- Use access tokens for every environment.
- Store credentials in project configuration files.

## Consequences

- Authentication remains separated from source code and version control.
- Interactive environments require an initial login or authorization.
- Future automated environments may require independently managed secrets.
- Authentication choices can vary by client without changing the TIL architecture.
