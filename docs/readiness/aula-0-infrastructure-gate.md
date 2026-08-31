# TIL Infrastructure Readiness Gate — Aula 0

## Purpose

Define the minimum infrastructure conditions that must be satisfied before starting Aula 0.

The gate exists to prevent educational work from beginning on top of an unverified execution and integration foundation.

## Decision Rule

Aula 0 is **RELEASED** only when all mandatory criteria are PASS.

Optional criteria may remain pending if they do not block the core TIL workflow.

## Mandatory Criteria

### G1 — Local repository and Git workflow

Current status: **PASS**

Evidence:

- project repository exists locally;
- Git workflow validated;
- commit and push to GitHub succeeded.

### G2 — GitHub as source of truth

Current status: **PASS**

Evidence:

- repository `pedroregato/text-intelligence-lab` is accessible;
- README and project documentation are readable through the connected GitHub integration;
- controlled write operations to the repository have succeeded.

### G3 — Python execution environment

Current status: **PASS**

Evidence:

- Python 3.11 baseline validated;
- project-local `.venv` validated;
- pip resolved from the virtual environment.

### G4 — Kaggle CLI installation

Current status: **PASS**

Evidence:

- official Kaggle package installed successfully;
- Kaggle 2.2.4 installation validated;
- earlier TLS issue was resolved safely with the system trust store.

### G5 — Kaggle CLI executable and authentication

Current status: **PASS**

Evidence:

- `where.exe kaggle` → `F:\text-intelligence-lab\.venv\Scripts\kaggle.exe`
- `kaggle --version` → `Kaggle CLI 2.2.4`
- interactive Kaggle authentication succeeded.

Tracked by:

- `INFRA-002 — Local Kaggle CLI Connectivity`

### G6 — Kaggle read-only connectivity

Current status: **PASS**

Evidence:

- `kaggle datasets list --search iris` returned multiple public datasets;
- `uciml/iris — Iris Species` was among the returned resources.

Tracked by:

- `INFRA-002 — Local Kaggle CLI Connectivity`

### G7 — Credential safety

Current status: **PASS**

Evidence:

- `SECURITY.md`;
- environment files and virtual environments excluded from version control;
- Kaggle credentials explicitly prohibited from the repository.

## Optional Criteria

### O1 — Local Codex ↔ Kaggle MCP

Current status: **PENDING**

Blocking: **NO**

Tracked by:

- `INFRA-001B — Local Codex ↔ Kaggle MCP Connectivity`

Rationale:

Kaggle MCP is an agentic productivity layer, not a core dependency.

### O2 — ChatGPT web ↔ Kaggle MCP

Current status: **UNAVAILABLE IN CURRENT SESSION**

Blocking: **NO**

Tracked by:

- `INFRA-001 — OpenAI/Codex ↔ Kaggle MCP Connectivity`

## Current Gate Status

```text
G1 Local Git workflow              PASS
G2 GitHub source of truth          PASS
G3 Python 3.11 / .venv            PASS
G4 Kaggle CLI installed           PASS
G5 Kaggle CLI auth/path/version   PASS
G6 Kaggle public read query       PASS
G7 Credential safety              PASS

O1 Codex → Kaggle MCP              PENDING
O2 ChatGPT web → Kaggle MCP       UNAVAILABLE
```

## Release Status

**AULA 0: RELEASED**

All mandatory infrastructure criteria are PASS.

Optional MCP validation may continue independently and does not block the educational phase.

## Principle

Architect → Implement small → Execute → Observe → Evaluate → Correct → Version → Expand
