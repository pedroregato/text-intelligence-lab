# TIL Infrastructure Readiness Gate — Aula 0

## Purpose

Define the minimum infrastructure conditions that must be satisfied before starting Aula 0.

The gate exists to prevent educational work from beginning on top of an unverified execution and integration foundation.

## Decision Rule

Aula 0 is **RELEASED** only when all mandatory criteria are PASS.

Optional criteria may remain pending if they do not block the core TIL workflow.

## Mandatory Criteria

### G1 — Local repository and Git workflow

Required evidence:

- project repository exists locally;
- Git repository is initialized;
- commit succeeds;
- push to GitHub succeeds.

Current status: **PASS**

Evidence:

- local project path: `D:\PythonProjects\text-intelligence-lab`
- branch: `main`
- commit and push successfully executed.

### G2 — GitHub as source of truth

Required evidence:

- repository is accessible;
- documentation and project files are readable from GitHub;
- write-capable integration exists for controlled updates.

Current status: **PASS**

Evidence:

- repository: `pedroregato/text-intelligence-lab`
- README and ADR documents were read successfully through the connected GitHub integration;
- repository permissions include pull and push capability.

### G3 — Python execution environment

Required evidence:

- Python 3.11 is active;
- project virtual environment is first in PATH;
- pip resolves from the virtual environment.

Current status: **PASS**

Evidence:

- Python 3.11.9
- project `.venv`
- pip 24.0 from the project virtual environment.

### G4 — Kaggle CLI installation

Required evidence:

- official Kaggle package installs successfully in the project virtual environment.

Current status: **PASS**

Evidence:

- Kaggle 2.2.4 installed successfully;
- TLS certificate issue resolved using the system trust store.

### G5 — Kaggle CLI executable and authentication

Required evidence:

- `where.exe kaggle` resolves to the project virtual environment;
- `kaggle --version` succeeds;
- `kaggle auth login` succeeds.

Current status: **PENDING**

Blocking: **YES**

Tracked by:

- `INFRA-002 — Local Kaggle CLI Connectivity`

### G6 — Kaggle read-only connectivity

Required evidence:

- one non-destructive public query succeeds through Kaggle CLI.

Minimum accepted test:

`kaggle datasets list --search iris`

Current status: **PENDING**

Blocking: **YES**

Tracked by:

- `INFRA-002 — Local Kaggle CLI Connectivity`

### G7 — Credential safety

Required evidence:

- no Kaggle token, API credential, access file, or secret is committed;
- authentication material remains outside the repository;
- project security policy is documented.

Current status: **PASS**

Evidence:

- `SECURITY.md`
- `.env` and virtual environments are excluded from version control;
- Kaggle credentials are explicitly prohibited from the repository.

## Optional Criteria

### O1 — Local Codex ↔ Kaggle MCP

Desired evidence:

- Codex registers the official Kaggle MCP endpoint;
- authentication succeeds;
- Kaggle MCP tools are discovered;
- one read-only public query succeeds.

Current status: **PENDING**

Blocking: **NO**

Tracked by:

- `INFRA-001B — Local Codex ↔ Kaggle MCP Connectivity`

Rationale:

Kaggle MCP is an agentic productivity layer, not a core dependency. The TIL remains operational through GitHub, Kaggle CLI/API, kagglehub, and Kaggle UI if MCP is unavailable.

### O2 — ChatGPT web ↔ Kaggle MCP

Current status: **UNAVAILABLE IN CURRENT SESSION**

Blocking: **NO**

Tracked by:

- `INFRA-001 — OpenAI/Codex ↔ Kaggle MCP Connectivity`

Rationale:

This limitation applies to the current ChatGPT surface and does not affect the local TIL workflow.

## Current Gate Status

```text
G1 Local Git workflow              PASS
G2 GitHub source of truth          PASS
G3 Python 3.11 / .venv            PASS
G4 Kaggle CLI installed           PASS
G5 Kaggle CLI auth                PENDING
G6 Kaggle public read query       PENDING
G7 Credential safety              PASS

O1 Codex → Kaggle MCP              PENDING
O2 ChatGPT web → Kaggle MCP       UNAVAILABLE
```

## Release Status

**AULA 0: NOT YET RELEASED**

Reason:

Mandatory criteria G5 and G6 remain pending.

## Minimum Remaining Desktop Work

From the activated project virtual environment:

```powershell
where.exe kaggle
kaggle --version
kaggle auth login
kaggle datasets list --search iris
```

If all four validations succeed and no credential-safety issue is detected:

- mark G5 PASS;
- mark G6 PASS;
- complete INFRA-002 as PASS;
- update this document to `AULA 0: RELEASED`.

## Principle

Architect → Implement small → Execute → Observe → Evaluate → Correct → Version → Expand
