# Security Policy

## Secrets and Credentials

The Text Intelligence Lab repository must not contain:

- Kaggle access tokens
- Kaggle API credentials
- `kaggle.json`
- local access-token files
- OAuth secrets
- GitHub personal access tokens
- passwords
- private keys
- environment files containing secrets

## Local Storage

Authentication material should remain outside the repository and use the authentication mechanism recommended by the relevant client.

Interactive OAuth is preferred where practical.

Environment variables or operating-system credential stores may be used when automation requires secrets.

## Git Hygiene

Before committing infrastructure changes:

```powershell
git status
git diff --staged
```

If a credential is accidentally committed, removing the file in a later commit is not sufficient. The credential must be revoked or rotated and repository history may require remediation.

## Documentation

Experiment evidence may include commands, versions, paths, and error messages, but must never include secret values.
