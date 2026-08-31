# Runbook — Temporary Windows Desktop Setup

## Purpose

Prepare a temporary Windows desktop for continuing TIL infrastructure validation without turning the temporary machine into a permanent project environment.

The setup should be minimal, secure, reproducible, and easy to remove.

## Target Architecture

```text
Temporary Windows desktop
    ├── Git
    ├── Python 3.11
    ├── TIL repository clone
    ├── project-local .venv
    ├── Kaggle CLI
    └── Codex CLI
```

## Principles

- GitHub remains the source of truth.
- Do not copy the permanent desktop virtual environment.
- Recreate `.venv` from Python 3.11.
- Prefer interactive OAuth for Kaggle and Codex.
- Do not store secrets in the repository.
- Do not create permanent Kaggle resources during infrastructure tests.
- Remove local credentials before giving up control of the temporary machine.

## Phase 1 — Inspect Existing Software

Open PowerShell and run:

```powershell
git --version
py --list
python --version
codex --version
```

Do not install anything that is already available and suitable.

## Phase 2 — Install Git If Required

Use the official Git for Windows installer or the Windows package manager available on the machine.

After installation:

```powershell
git --version
```

## Phase 3 — Install Python 3.11 If Required

The TIL baseline is Python 3.11.

After installation, validate:

```powershell
py -3.11 --version
```

Do not substitute Python 3.12, 3.13, or 3.14 for the TIL environment unless a later ADR changes the project baseline.

## Phase 4 — Clone the Repository

Choose a temporary working directory.

Example:

```powershell
mkdir C:\TIL
cd C:\TIL
git clone https://github.com/pedroregato/text-intelligence-lab.git
cd text-intelligence-lab
git status
```

Expected branch:

`main`

## Phase 5 — Create the Project Virtual Environment

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
python -m pip --version
```

Expected Python major/minor:

`3.11`

## Phase 6 — Install Kaggle CLI

First try:

```powershell
python -m pip install kaggle
```

If the same certificate-chain issue observed on the permanent desktop occurs, use the already validated safe alternative:

```powershell
python -m pip install kaggle --use-feature=truststore
```

Do not use `--trusted-host` merely to bypass certificate verification.

Validate:

```powershell
where.exe kaggle
kaggle --version
```

## Phase 7 — Authenticate Kaggle

Use the interactive OAuth flow:

```powershell
kaggle auth login
```

Then perform the read-only test:

```powershell
kaggle datasets list --search iris
```

Do not create datasets, notebooks, models, submissions, or other persistent resources.

## Phase 8 — Install Codex CLI If Required

Current official Windows installation method:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

Alternative supported method when Node/npm is already available:

```powershell
npm install -g @openai/codex
```

Validate:

```powershell
codex --version
```

Authenticate using the interactive ChatGPT sign-in flow.

## Phase 9 — Validate Kaggle MCP

Follow:

`docs/runbooks/codex-kaggle-mcp-validation.md`

Minimum commands:

```powershell
codex mcp add kaggle --url https://www.kaggle.com/mcp
codex mcp list --json
codex mcp login kaggle
```

Then perform only a read-only Kaggle MCP query.

## Phase 10 — Synchronization Discipline

Before making any project edit:

```powershell
git pull origin main
git status
```

If documentation is changed intentionally:

```powershell
git add <files>
git diff --staged
git commit -m "<message>"
git push origin main
```

Do not copy files manually between the permanent and temporary desktops. Use GitHub.

## Phase 11 — Cleanup Before Leaving the Temporary Desktop

Before relinquishing the machine:

1. Sign out of Codex/ChatGPT if the machine is not exclusively yours.
2. Sign out or revoke local Kaggle authentication if appropriate.
3. Remove any local token files or environment variables created during testing.
4. Delete the local repository if the machine is shared or untrusted.
5. Empty the recycle bin if sensitive local files were removed.
6. Do not remove or revoke credentials on the permanent desktop by mistake.

## What May Remain

On a trusted personal temporary machine, the following may remain if desired:

- Git
- Python 3.11
- Codex CLI

The TIL repository and authentication state should remain only if the machine is under the user's continuing control.

## Success Criteria

The temporary desktop is ready when:

- Git can clone/pull the TIL repository;
- Python 3.11 creates the TIL `.venv`;
- Kaggle CLI runs;
- Kaggle authentication succeeds;
- the Iris public query succeeds;
- Codex CLI runs;
- optionally, Codex reaches Kaggle MCP.

## Scope Boundary

This setup is for infrastructure validation only.

Do not start Aula 0, NLP experiments, teaching datasets, or persistent Kaggle workloads until the readiness gate is released.
