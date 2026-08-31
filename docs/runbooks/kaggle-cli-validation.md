# Runbook — Validate Local Kaggle CLI

## Purpose

Complete INFRA-002 by validating the installed Kaggle CLI, authentication, and one non-destructive public query.

## Preconditions

- Project virtual environment activated.
- Kaggle package already installed in `.venv`.
- No Kaggle credentials stored in the repository.

## Procedure

From the project root:

```powershell
where.exe kaggle
kaggle --version
```

Confirm that the executable resolves to the project virtual environment.

Authenticate:

```powershell
kaggle auth login
```

Complete the interactive authorization flow.

Run one public, read-only query:

```powershell
kaggle datasets list --search iris
```

## Evidence to Record

Update `docs/experiments/INFRA-002-local-kaggle-cli.md` with:

- Kaggle executable path
- Kaggle CLI version
- authentication result
- public query result
- errors, if any

## Success Criteria

INFRA-002 is PASS when:

- the executable resolves from the TIL virtual environment;
- the CLI reports a valid version;
- authentication succeeds;
- a public read-only query returns Kaggle resources.

## Failure Handling

Do not disable TLS verification.

If certificate errors return, prefer the Windows/system trust store approach already validated for this environment.

Do not commit tokens, access files, or authentication output containing secrets.
