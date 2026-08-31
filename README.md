# Text Intelligence Lab (TIL) with Kaggle

Laboratório educacional e experimental de Text Intelligence, NLP e Machine Learning, combinando fundamentos, experimentação científica, engenharia de IA e desenvolvimento assistido por agentes com Kaggle e GitHub.

## Engineering Principle

```text
Architect
   ↓
Implement small
   ↓
Execute
   ↓
Observe
   ↓
Evaluate
   ↓
Correct
   ↓
Version
   ↓
Expand
```

## Execution Architecture

```text
                 GitHub
            source of truth
                  ▲
                  │
              Git local
                  │
        ┌─────────┴─────────┐
        │                   │
     PyCharm              Codex
        │                   │
   Kaggle CLI          Kaggle MCP
        │                   │
   kagglehub                │
        └─────────┬─────────┘
                  ▼
               Kaggle
                  ▲
                  │
              Kaggle UI
```

## Responsibility Boundaries

- **GitHub** — source of truth for code, documentation, history, and engineering decisions.
- **Kaggle UI** — interactive notebook inspection and educational workflows.
- **Kaggle CLI/API** — explicit, reproducible Kaggle platform operations.
- **kagglehub** — programmatic Kaggle resource access from Python.
- **Kaggle MCP** — optional agentic integration for Codex and other MCP-compatible clients.

The project must remain operational even when Kaggle MCP is unavailable.

## Current Infrastructure Status

| Capability | Status |
| --- | --- |
| Local Git → GitHub | PASS |
| OpenAI session → GitHub | PASS |
| Python 3.11 virtual environment | PASS |
| Kaggle CLI installation | PASS |
| Kaggle CLI authentication | PENDING |
| Kaggle CLI public query | PENDING |
| ChatGPT web → Kaggle MCP | UNAVAILABLE IN CURRENT SESSION |
| Local Codex → Kaggle MCP | PENDING |

## Repository Structure

```text
text-intelligence-lab/
├── course/
├── data/
├── docs/
│   ├── decisions/
│   ├── experiments/
│   ├── runbooks/
│   └── templates/
├── experiments/
├── .gitignore
├── README.md
└── setup_structure.py
```

See `docs/README.md` for documentation conventions and experiment tracking.

## Current Phase

Infrastructure integration and validation only.

Educational NLP notebooks and course content have not started yet.
