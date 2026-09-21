# Aula 19 — Offline MCP dependency for Kaggle

## Goal

Run Aula 19 with:

```text
Internet OFF
GPU OFF
MCP Python SDK pinned
```

## Strategy

Build a local wheelhouse and publish it as a Kaggle Dataset attached to the notebook.

```text
requirements/aula-19-mcp.txt
        ↓
pip download
        ↓
wheelhouse/
        ↓
Kaggle Dataset
        ↓
/kaggle/input/til-mcp-python-sdk-wheelhouse
        ↓
offline installation
```

## Build locally

```powershell
New-Item -ItemType Directory -Force .artifacts\aula-19-mcp-wheelhouse | Out-Null

python -m pip download `
  -r requirements\aula-19-mcp.txt `
  -d .artifacts\aula-19-mcp-wheelhouse
```

## Create Kaggle Dataset metadata

Inside the wheelhouse directory:

```powershell
kaggle datasets init -p .artifacts\aula-19-mcp-wheelhouse
```

Edit dataset-metadata.json with a stable id such as:

```json
{
  "title": "TIL MCP Python SDK Wheelhouse",
  "id": "pedrogentil/til-mcp-python-sdk-wheelhouse",
  "licenses": [{"name": "other"}]
}
```

Then publish:

```powershell
kaggle datasets create -p .artifacts\aula-19-mcp-wheelhouse
```

For future dependency updates:

```powershell
kaggle datasets version -p .artifacts\aula-19-mcp-wheelhouse -m "Update MCP wheelhouse"
```

## Kaggle runtime path

After attaching the dataset to the notebook, install without network access:

```text
python -m pip install --no-index --find-links /kaggle/input/til-mcp-python-sdk-wheelhouse "mcp[cli]==2.2.0"
```

The exact Kaggle mount directory should be confirmed after the dataset is attached.

## Reproducibility rule

The notebook should record:

- MCP package version;
- protocol baseline 2026-07-28;
- wheelhouse dataset source/version;
- Internet OFF.

The wheelhouse is an execution dependency, not course evidence.
