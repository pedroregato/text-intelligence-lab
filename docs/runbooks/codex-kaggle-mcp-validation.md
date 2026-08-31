# Runbook — Validate Codex ↔ Kaggle MCP

## Purpose

Execute INFRA-001B and validate direct local Codex connectivity with the official Kaggle MCP server.

## Preconditions

- Local Codex CLI installed.
- Codex authenticated.
- Network access to the official Kaggle MCP endpoint.
- No Kaggle credentials stored in the repository.

## Procedure

Record the installed Codex version:

```powershell
codex --version
```

Register the official Kaggle MCP endpoint:

```powershell
codex mcp add kaggle --url https://www.kaggle.com/mcp
```

Inspect the registration:

```powershell
codex mcp list --json
```

Attempt OAuth authentication:

```powershell
codex mcp login kaggle
```

After successful authentication, start a fresh Codex session.

Use a read-only prompt such as:

> Use the Kaggle MCP server to search for public datasets matching "iris". Return only resource identifiers/titles and do not create, modify, download, submit, or delete anything.

## Evidence to Record

Update `docs/experiments/INFRA-001B-local-codex-kaggle-mcp.md` with:

- Codex CLI version
- MCP registration result
- authentication result
- available Kaggle MCP tools
- tool invoked
- returned public metadata
- errors, if any

## Success Criteria

INFRA-001B is PASS when Codex can:

- register the official Kaggle MCP server;
- authenticate successfully;
- discover Kaggle MCP tools;
- complete one non-destructive public resource query.

## Fallback

If OAuth fails because of an MCP client limitation, do not weaken TLS and do not embed a Kaggle token directly in repository files.

Use an environment-variable-backed bearer token only after confirming the supported configuration fields of the installed Codex version.
