# INFRA-002 — Local Kaggle CLI Connectivity

## Objective

Validate the local Python environment for authenticated Kaggle CLI access and a non-destructive public Kaggle query.

## Hypothesis

A TIL Python 3.11 virtual environment can install and run the official Kaggle CLI, authenticate successfully, and query Kaggle.

## Environments

### Permanent desktop

- Windows PowerShell
- Project: `D:\PythonProjects\text-intelligence-lab`
- Virtual environment: `.venv`
- Python: 3.11.9
- pip: 24.0
- Kaggle package installed: 2.2.4

### Temporary desktop

- Windows PowerShell
- Project: `F:\text-intelligence-lab`
- Project synchronized from GitHub
- Project-local `.venv` created and activated
- Kaggle authentication completed successfully

## Procedure and Evidence

### 1. Python environment validation — permanent desktop

Validated:

- `python --version` → Python 3.11.9
- `python -m pip --version` → pip 24.0 from the project `.venv`
- `where.exe python` → project virtual environment is first in PATH
- `where.exe pip` → project virtual environment is first in PATH

**Result: PASS**

### 2. pip configuration validation — permanent desktop

`python -m pip config debug` showed no active global, user, or virtual-environment pip configuration files.

**Result: PASS**

### 3. Kaggle CLI installation — permanent desktop

Initial installation with:

`python -m pip install kaggle`

failed with:

`SSLCertVerificationError: self-signed certificate in certificate chain`

The installation was retried with the Windows/system trust store enabled:

`python -m pip install kaggle --use-feature=truststore`

Kaggle 2.2.4 and its dependencies were installed successfully.

**Result: PASS**

### 4. Kaggle executable provenance/version — temporary desktop

Still to record:

- `where.exe kaggle`
- `kaggle --version`

The successful authenticated query proves the command is executable, but the exact executable path and reported CLI version have not yet been captured as evidence on the temporary desktop.

**Result: PENDING EVIDENCE**

### 5. Kaggle authentication — temporary desktop

Interactive Kaggle authentication completed successfully and returned:

`Authentication Successful!`

**Result: PASS**

### 6. Non-destructive Kaggle query — temporary desktop

Command:

`kaggle datasets list --search iris`

The command returned public Kaggle dataset results successfully, including:

- `uciml/iris` — Iris Species
- `himanshunakrani/iris-dataset` — Iris dataset
- `arshid/iris-flower-dataset` — Iris Flower Dataset

No persistent Kaggle resource was created or modified.

**Result: PASS**

## Result

**PASS WITH ONE EVIDENCE ITEM PENDING**

The important functional hypothesis is validated:

- Kaggle CLI is callable;
- interactive authentication succeeds;
- authenticated/public Kaggle connectivity works;
- a read-only dataset search returns real Kaggle resources.

The only remaining evidence item is to capture the executable path and CLI version on the temporary desktop.

## Conclusion

INFRA-002 has functionally succeeded.

For strict completion of the readiness gate, record:

```powershell
where.exe kaggle
kaggle --version
```

No further Kaggle authentication or public-query test is required unless the environment changes.
