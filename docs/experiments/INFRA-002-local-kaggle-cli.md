# INFRA-002 — Local Kaggle CLI Connectivity

## Objective

Validate the local PyCharm/Python environment for authenticated Kaggle CLI access and a non-destructive public Kaggle query.

## Hypothesis

The TIL local Python 3.11 virtual environment can install and run the official Kaggle CLI and query Kaggle successfully.

## Environment

- Windows PowerShell
- Project: `D:\PythonProjects\text-intelligence-lab`
- Virtual environment: `.venv`
- Python: 3.11.9
- pip: 24.0
- Kaggle package installed: 2.2.4

## Procedure and Evidence

### 1. Python environment validation

Validated:

- `python --version` → Python 3.11.9
- `python -m pip --version` → pip 24.0 from the project `.venv`
- `where.exe python` → project virtual environment is first in PATH
- `where.exe pip` → project virtual environment is first in PATH

**Result: PASS**

### 2. pip configuration validation

`python -m pip config debug` showed no active global, user, or virtual-environment pip configuration files.

**Result: PASS**

### 3. Kaggle CLI installation

Initial installation with:

`python -m pip install kaggle`

failed with:

`SSLCertVerificationError: self-signed certificate in certificate chain`

The installation was retried with the Windows/system trust store enabled:

`python -m pip install kaggle --use-feature=truststore`

Kaggle 2.2.4 and its dependencies were installed successfully.

**Result: PASS**

### 4. Kaggle executable validation

Pending:

- `where.exe kaggle`
- `kaggle --version`

**Result: PENDING**

### 5. Kaggle authentication

Pending:

- `kaggle auth login`

**Result: PENDING**

### 6. Non-destructive Kaggle query

Pending:

- `kaggle datasets list --search iris`

**Result: PENDING**

## Result

**IN PROGRESS**

The local Python environment and Kaggle CLI installation are validated.

The initial TLS issue was resolved without disabling certificate verification by enabling the system trust store.

Authentication and live Kaggle connectivity remain to be tested.

## Conclusion

INFRA-002 is no longer blocked.

The experiment will be complete after validating the Kaggle executable, authentication, and one public read-only query.
