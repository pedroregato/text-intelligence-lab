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
- Kaggle CLI executable: `F:\text-intelligence-lab\.venv\Scripts\kaggle.exe`
- Kaggle CLI version: 2.2.4
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

Validated:

- `where.exe kaggle` → `F:\text-intelligence-lab\.venv\Scripts\kaggle.exe`
- `kaggle --version` → `Kaggle CLI 2.2.4`

**Result: PASS**

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

**PASS**

The hypothesis is validated:

- the Kaggle CLI is installed and resolved from the project virtual environment;
- the exact CLI version is recorded;
- interactive authentication succeeds;
- Kaggle connectivity works;
- a read-only public dataset query returns real resources.

## Conclusion

INFRA-002 is complete.

The TIL local/portable Windows workflow for Kaggle CLI access is validated.

No further Kaggle CLI validation is required unless the environment, authentication method, or project baseline changes.
