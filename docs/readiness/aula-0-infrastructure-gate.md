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
- Kaggle 2.2.4 installation was observed on the permanent desktop;
- the earlier TLS issue was resolved safely with the system trust store.

### G5 — Kaggle CLI executable and authentication

Required evidence:

- `where.exe kaggle` resolves to the project virtual environment;
- `kaggle --version` succeeds;
- `kaggle auth login` succeeds.

Current status: **PARTIAL — AUTH PASS, PATH/VERSION EVIDENCE PENDING**

Evidence already obtained:

- interactive Kaggle authentication succeeded on the temporary desktop;
- subsequent Kaggle CLI query executed successfully.

Still required:

- capture `where.exe kaggle`;
- capture `kaggle --version`.

Blocking: **YES, evidence-only**

Tracked by:

- `INFRA-002 — Local Kaggle CLI Connectivity`

### G6 — Kaggle read-only connectivity

Required evidence:

- one non-destructive public query succeeds through Kaggle CLI.

Test executed:

`kaggle datasets list --search iris`

Current status: **PASS**

Evidence:

The query returned multiple public datasets, including `uciml/iris — Iris Species`.

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
G5 Kaggle CLI auth/path/version   PARTIAL
G6 Kaggle public read query       PASS
G7 Credential safety              PASS

O1 Codex → Kaggle MCP              PENDING
O2 ChatGPT web → Kaggle MCP       UNAVAILABLE
```

## Release Status

**AULA 0: NOT YET RELEASED — ONE EVIDENCE CHECK REMAINS**

The functional Kaggle path is already validated.

Only the following evidence must still be captured from the currently active temporary desktop environment:

```powershell
where.exe kaggle
kaggle --version
```

If both succeed and the executable resolves from the project `.venv`:

- mark G5 PASS;
- mark INFRA-002 PASS;
- update this document to `AULA 0: RELEASED`.

## Principle

Architect → Implement small → Execute → Observe → Evaluate → Correct → Version → Expand
