# Runbook — TIL Kaggle Notebook Workflow

## Purpose

Keep GitHub as the source of truth while using Kaggle as the primary educational and experimental execution environment.

## Canonical flow

```text
Edit locally
→ review Git diff
→ commit/push to GitHub
→ push notebook to Kaggle
→ observe Kaggle status
→ inspect outputs/logs
→ correct locally
→ version in GitHub
```

## Responsibilities

- **GitHub** — canonical source, history, documentation, decisions.
- **Local repository** — preferred editing and review workspace.
- **Kaggle** — execution environment and execution-version record.
- **Kaggle UI** — execution inspection and educational interaction.
- **Kaggle CLI** — reproducible transfer, status, output, and pull operations.

## Push and execute

From the repository root:

```powershell
kaggle kernels push -p .\course\00-til-environment-validation
```

Check status:

```powershell
kaggle kernels status pedrogentil/til-00-environment-validation
```

## Download outputs

```powershell
New-Item -ItemType Directory -Force .\experiments\EDU-INFRA-001\kaggle-output | Out-Null

kaggle kernels output pedrogentil/til-00-environment-validation `
  -p .\experiments\EDU-INFRA-001\kaggle-output
```

## Editing policy

Prefer **source-first**:

1. Edit locally.
2. Commit to GitHub.
3. Push to Kaggle.
4. Treat Kaggle as execution environment, not a second source repository.

If a useful change is made in the Kaggle UI, pull it back before continuing local edits:

```powershell
kaggle kernels pull pedrogentil/til-00-environment-validation `
  -p .\course\00-til-environment-validation `
  -m

git status
git diff
```

Accept the change only after reviewing the diff and committing it to GitHub.

## Environment note

The project local baseline is Python 3.11, but EDU-INFRA-001 observed Kaggle running Python 3.12.13 on 2026-08-31.

Therefore, future notebooks must not assume exact Python minor-version parity between local and Kaggle environments unless a lesson explicitly requires it.

## Completion criteria

A notebook execution is considered validated when:

- Kaggle reports the run as complete;
- expected output artifacts can be downloaded;
- the output is inspected rather than inferred;
- relevant warnings/errors are evaluated;
- accepted source changes are present in GitHub.
