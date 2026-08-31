# EDU-INFRA-001 — First TIL Kaggle Notebook Execution

## Status

PASS

## Objective

Prove that the first TIL course notebook can be versioned in GitHub, uploaded to Kaggle, executed there, and produce downloadable evidence.

## Hypothesis

If the canonical TIL notebook and its Kaggle metadata are pushed through the authenticated Kaggle CLI, Kaggle will create/update the notebook, execute a new version, and persist `til_environment_evidence.json` as an output.

## Environment

- Repository: `pedroregato/text-intelligence-lab`
- GitHub owner: `pedroregato`
- Kaggle owner: `pedrogentil`
- Source of truth: GitHub
- Local baseline: Python 3.11 with project `.venv`
- Observed Kaggle runtime: Python 3.12.13 / CPython
- Kaggle OS: Linux 6.12.90+, glibc 2.35
- Working directory: `/kaggle/working`
- Accelerator: CPU
- Internet: disabled
- External datasets: none
- Notebook: `course/00-til-environment-validation/00-til-environment-validation.ipynb`
- Kaggle slug: `pedrogentil/til-00-environment-validation`

## Procedure

1. Push the notebook:
   `kaggle kernels push -p .\course\00-til-environment-validation`
2. Check status:
   `kaggle kernels status pedrogentil/til-00-environment-validation`
3. Download evidence:
   `kaggle kernels output pedrogentil/til-00-environment-validation -p .\experiments\EDU-INFRA-001\kaggle-output --file-pattern "til_environment_evidence.json"`
4. Inspect the downloaded JSON and Kaggle execution log.

## Evidence

Kaggle reported:

```text
Kernel version 1 successfully pushed.
pedrogentil/til-00-environment-validation has status "KernelWorkerStatus.COMPLETE"
```

Downloaded output:

```json
{
  "experiment_id": "EDU-INFRA-001",
  "notebook": "00-til-environment-validation.ipynb",
  "executed_at_utc": "2026-08-31T13:50:47.778639+00:00",
  "runtime": {
    "python_version": "3.12.13",
    "python_full_version": "3.12.13 (main, Mar  4 2026, 09:23:07) [GCC 11.4.0]",
    "platform": "Linux-6.12.90+-x86_64-with-glibc2.35",
    "implementation": "CPython",
    "working_directory": "/kaggle/working",
    "is_kaggle": true
  },
  "result": "PASS"
}
```

The Kaggle log also emitted an `nbformat` `MissingIDFieldWarning`. This did not affect execution, but the canonical notebook was corrected afterward to include cell IDs.

## Result

PASS

The notebook was created from the GitHub-controlled source, pushed through Kaggle CLI, executed successfully in Kaggle, and generated a downloadable evidence artifact.

## Conclusion

The core operational flow for TIL notebooks is validated:

```text
GitHub/local source
→ Kaggle CLI push
→ Kaggle execution
→ status observation
→ output download
→ evidence review
→ correction
→ GitHub versioning
```

Aula 0 operational readiness is confirmed.
