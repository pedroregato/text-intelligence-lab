# INFRA-003 — Public Kaggle Web Reachability

## Objective

Validate that public Kaggle resources and documentation are reachable independently of the local Kaggle CLI.

## Hypothesis

Kaggle public documentation and at least one public dataset resource can be reached successfully from the current environment.

## Environment

- ChatGPT web session
- Public web access
- No Kaggle authentication required
- No local desktop dependency

## Procedure

1. Open the current Kaggle API documentation.
2. Confirm that Kaggle documents the CLI and kagglehub as supported programmatic interfaces.
3. Access a known public dataset resource.
4. Record only read-only public metadata.

## Evidence

### Kaggle API documentation

The current Kaggle API documentation is reachable and documents:

- Kaggle CLI as a terminal/shell interface.
- kagglehub as a Python library for Kaggle resources.
- OAuth authentication via `kaggle auth login`.
- dynamic rate limiting.

### Public dataset

Public dataset reached successfully:

- Title: `Iris Species`
- Owner/organization: UCI Machine Learning
- Public resource page available
- Dataset description available
- Files listed publicly, including `Iris.csv`
- License shown as CC0 / Public Domain

## Result

**PASS**

Public Kaggle documentation and public dataset metadata are reachable.

## Interpretation

This experiment proves:

`current web environment → public Kaggle resources`

It does **not** prove:

- local `.venv` → Kaggle CLI;
- local Kaggle CLI authentication;
- local Kaggle CLI → Kaggle API;
- Codex → Kaggle MCP.

Therefore INFRA-003 does not replace G5 or G6 in the Aula 0 readiness gate.

## Conclusion

Kaggle itself is publicly reachable and the intended Iris read-only target exists.

The remaining uncertainty for G5/G6 is local CLI execution and authentication, not public Kaggle availability.
