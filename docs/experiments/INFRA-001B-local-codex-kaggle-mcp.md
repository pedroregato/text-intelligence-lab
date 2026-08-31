# INFRA-001B — Local Codex ↔ Kaggle MCP Connectivity

## Objective

Validate direct connectivity between the local Codex CLI and the official Kaggle MCP server.

## Hypothesis

The local Codex CLI can register the official Kaggle remote MCP server, authenticate securely, discover its tools, and execute one non-destructive public Kaggle query.

## Preconditions

- Codex CLI installed and authenticated locally.
- Network access to `https://www.kaggle.com/mcp`.
- No Kaggle token committed to the repository.
- Kaggle CLI authentication is independent from this MCP test.

## Official MCP Endpoint

`https://www.kaggle.com/mcp`

## Procedure

### 1. Record Codex version

Run:

`codex --version`

Record the exact version in this document.

### 2. Register Kaggle MCP

Run:

`codex mcp add kaggle --url https://www.kaggle.com/mcp`

This should add a remote HTTP MCP server entry to the Codex configuration.

### 3. Inspect MCP registration

Run:

`codex mcp list --json`

Confirm that a server named `kaggle` is enabled and points to the official endpoint.

### 4. Preferred authentication test — OAuth

Run:

`codex mcp login kaggle`

Complete the browser authorization flow if prompted.

Do not paste access tokens into source files, shell history unnecessarily, notebooks, ADRs, or GitHub.

### 5. Restart or start a fresh Codex session

Start a new Codex session after authentication so the MCP tool inventory is refreshed.

### 6. Minimum non-destructive query

Ask Codex to use only the Kaggle MCP integration to perform one read-only operation, for example:

`Use the Kaggle MCP server to search for public datasets matching "iris". Return only resource identifiers/titles and do not create, modify, download, submit, or delete anything.`

Acceptable alternatives are reading public dataset metadata or querying a public notebook, provided no persistent resource is created.

### 7. Evidence to capture

Record:

- Codex CLI version
- MCP server registration output
- authentication result
- whether Kaggle tools became visible
- tool invoked
- query supplied
- returned public resource metadata
- any error message

## Expected Result

**PASS** if Codex can register the Kaggle MCP server, authenticate if required, discover Kaggle MCP tools, and complete one read-only public query.

## OAuth Fallback

If `codex mcp login kaggle` fails because of an MCP OAuth/client issue, do not weaken TLS or store a token in the repository.

Kaggle officially supports bearer-token authentication using a token beginning with `KGAT`.

Before configuring the fallback, inspect the installed Codex version's supported MCP configuration fields and use an environment-variable-backed bearer token rather than embedding the token directly in `config.toml`.

The fallback must be recorded separately from the OAuth attempt.

## Safety Constraints

During INFRA-001B:

- do not create notebooks;
- do not create datasets;
- do not create models;
- do not submit to competitions;
- do not start persistent Kaggle workloads;
- do not commit credentials;
- perform read-only discovery or metadata queries only.

## Status

**PENDING LOCAL EXECUTION**

## Conclusion

To be completed after the local desktop test.
