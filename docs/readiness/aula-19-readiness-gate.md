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

**PENDING REVALIDATION — v2 REENGINEERING**

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

### G2A — Protocol visibility

**PENDING EXECUTION REVIEW**

The reengineered notebook now includes:

- N×M integration-cost lab;
- protocol X-ray with MCP/JSON-RPC representation;
- readable discovered JSON Schema;
- discovery-driven invocation;
- explicit deterministic ToyHost;
- composed tool → prompt → human-review flow;
- trust/poisoning demo separated from authorization;
- predict → observe → explain failure lab;
- ambiguous architecture case;
- final conceptual check independent of Python SDK syntax.

These items become PASS only after execution and pedagogical inspection.

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

**PENDING — v2 REENGINEERING**

The previous notebook version executed headlessly. The reengineered v2 must be executed again because its laboratory structure changed materially.

### G5 — Kaggle execution

**PENDING — v2 REENGINEERING**

The previous notebook version was validated on Kaggle. The reengineered v2 requires a new complete Kaggle Run All with the offline MCP dependency attached.

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

**PASS**

The generated glossary views were rebuilt and committed:

```text
docs/glossary/glossary.pt-BR.md
docs/glossary/glossary.en.md
docs/glossary/web/index.html
```

Evidence:

```text
0aeb568 — glossary: regenerate views for Aula 19 MCP
```

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

only after G8 passes.

## Governing principle

> MCP should be introduced only where standardized capability exposure and discovery create enough utility to justify the additional integration layer.
