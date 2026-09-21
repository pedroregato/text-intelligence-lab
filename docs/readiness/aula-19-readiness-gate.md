# Aula 19 — Readiness Gate

## Status

REVIEW CANDIDATE — not yet student-ready

## Scope

Aula 19 — Model Context Protocol (MCP)

Protocol baseline:

```text
MCP specification = 2026-07-28
Python SDK         = 2.2.0
```

## Gates

### G1 — Curriculum and conceptual scope

**PASS**

The lesson clearly separates:

```text
MCP      → integration protocol
workflow → execution policy / sequence
agent    → autonomy to decide and act
```

The transition from Lessons 17 and 18 is explicit.

### G2 — Executable MCP lab

**PASS**

The notebook implements:

- MCPServer;
- MCP Client in-process;
- tool;
- resource;
- prompt;
- protocol introspection;
- capability discovery;
- invocation;
- failure lab;
- observability;
- architecture decision lab.

### G3 — Reproducibility

**PASS**

Execution contract:

```text
Internet OFF
GPU OFF
MCP 2.2.0 pinned
offline Kaggle wheelhouse
no proprietary API
no external side effects
```

Dataset dependency:

```text
pedrogentil/til-mcp-python-sdk-wheelhouse
```

### G4 — Local headless execution

**PASS**

The notebook executed headlessly with all code cells processed and no recorded execution errors.

### G5 — Kaggle execution

**PASS**

The notebook was pushed and executed on Kaggle with the offline MCP dependency attached.

### G6 — Living Glossary source

**PASS**

Aula 19 concepts were added to:

```text
docs/glossary/glossary.extensions.yaml
```

Terms include:

- Model Context Protocol;
- MCP Host;
- MCP Client;
- MCP Server;
- Capability Discovery;
- MCP Tool;
- MCP Resource;
- MCP Prompt;
- Protocol Version;
- Transport;
- Authorization.

The notebook contains contextual links to those concepts.

### G7 — Generated glossary views

**PENDING**

Regenerate:

```text
docs/glossary/glossary.pt-BR.md
docs/glossary/glossary.en.md
docs/glossary/web/index.html
```

using:

```powershell
python docs/glossary/build_glossary.py
```

Commit the generated views before promotion.

### G8 — Pedagogical review

**PENDING**

The lesson still requires final human review of:

- explanation density;
- progression from concept to code;
- clarity of host/client/server;
- interpretation of discovery;
- failure lab;
- architecture decision lab;
- bridge to Agentic Systems.

## Promotion rule

Promote to:

```text
Available / student-ready
```

only after G7 and G8 pass.

## Governing principle

> MCP should be introduced only where standardized capability exposure and discovery create enough utility to justify the additional integration layer.
