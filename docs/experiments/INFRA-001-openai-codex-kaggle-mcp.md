# INFRA-001 — OpenAI/Codex ↔ Kaggle MCP Connectivity

## Objective

Validate whether the OpenAI/Codex environment can use the official Kaggle MCP server to query Kaggle resources.

## Hypothesis

An MCP-compatible OpenAI/Codex environment can connect to the official Kaggle MCP server and perform non-destructive public queries.

## Environment

- ChatGPT web session
- GitHub integration connected
- Repository: `pedroregato/text-intelligence-lab`
- Official Kaggle MCP endpoint confirmed from current Kaggle documentation
- Kaggle MCP not exposed as a tool in this ChatGPT session

## Procedure

1. Verify current Kaggle MCP documentation.
2. Confirm the official remote MCP endpoint and supported authentication mechanisms.
3. Inspect integrations actually exposed in the active OpenAI environment.
4. Validate read-only GitHub access to the TIL repository.
5. Attempt to identify a directly callable Kaggle MCP integration in the active session.

## Evidence

- GitHub repository discovery succeeded.
- `README.md` was read successfully.
- `docs/decisions/ADR-001-kaggle-execution-environment.md` was read successfully.
- The connected GitHub integration reports read/write-capable repository permissions.
- No Kaggle MCP tool/server is exposed in the active ChatGPT session.

## Result

**PARTIAL / ENVIRONMENT LIMITATION**

The official Kaggle MCP capability is documented, but it cannot be invoked directly from the current ChatGPT web session because that server is not exposed as an available integration here.

This does not demonstrate incompatibility between Codex and Kaggle MCP. It only establishes that this ChatGPT session cannot execute the required MCP call.

## Conclusion

INFRA-001 remains partially open.

The next test is:

`INFRA-001B — Local Codex ↔ Kaggle MCP connectivity`

The minimum follow-up test should configure the official Kaggle MCP server in the local Codex environment, authenticate securely, and perform one non-destructive public resource query.
