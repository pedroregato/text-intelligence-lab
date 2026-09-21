# Aula 19 — Model Context Protocol (MCP)

## Status

Draft specification

## Protocol Baseline

Esta aula deve usar como referência principal a especificação MCP **2026-07-28** e o **Python SDK v2**, linha estável compatível com essa revisão.

Fontes canônicas:

- https://modelcontextprotocol.io/
- https://modelcontextprotocol.io/specification/
- https://blog.modelcontextprotocol.io/posts/2026-07-28/

A versão deve ser explicitada no notebook porque o protocolo evolui e exemplos antigos podem refletir semântica de versões anteriores.

## Role in the TIL

A Aula 19 é a terceira unidade do **Bloco C — Tools and Workflows**.

Progressão:

```text
Aula 17 — Tool Use, Function Calling and Contracts
→ Aula 18 — Deterministic Workflows
→ Aula 19 — Model Context Protocol (MCP)
→ Bloco D — Agentic Systems
```

A Aula 17 ensinou o contrato de uma tool.

A Aula 18 ensinou como coordenar tools sob estado, políticas, retries, checkpoints e approval gates.

A Aula 19 deve responder:

> **Como expor e descobrir capacidades de forma padronizada sem confundir protocolo de integração com autonomia agente?**

## Governing Principle

MCP deve ser ensinado como **protocolo de integração e exposição de capacidades**, não como sinônimo de agente, workflow ou framework de orquestração.

```text
capability
→ contract
→ MCP exposure
→ discovery
→ invocation
→ controlled execution
```

A governança aprendida nas Aulas 17 e 18 continua válida.

## Learning Objectives

Ao final da aula, o aluno deverá conseguir:

1. explicar qual problema de integração o MCP resolve;
2. distinguir host, client e server;
3. distinguir tool, resource e prompt;
4. explicar capability discovery;
5. reconhecer version negotiation e compatibilidade;
6. comparar stdio e HTTP como formas de transporte;
7. explicar por que autorização não é responsabilidade do modelo;
8. relacionar MCP com contracts, validation e observability;
9. identificar riscos de segurança na exposição de capacidades;
10. distinguir MCP de workflow e de agente;
11. implementar um servidor MCP mínimo e um cliente didático;
12. justificar quando MCP adiciona utility e quando uma integração direta é suficiente.

## Modern MCP Architecture

A especificação 2026-07-28 adota um núcleo stateless.

A abstração pedagógica deve começar por:

```text
Host
  ↓
MCP Client
  ↓
transport
  ↓
MCP Server
  ↓
tools / resources / prompts
```

O aluno deve compreender que o servidor expõe capacidades e que o host/client decide como consumi-las.

## Core Concepts

### 1. Host, Client and Server

- **Host**: aplicação que coordena a experiência e contém ou gerencia clientes MCP.
- **Client**: componente que comunica com um servidor MCP.
- **Server**: expõe capacidades por meio do protocolo.

### 2. Tools

Tools representam ações ou operações invocáveis.

Conectar explicitamente com a Aula 17:

```text
tool contract
→ input schema
→ validation
→ execution
→ result
```

MCP padroniza a exposição e descoberta; não elimina a necessidade desses controles.

### 3. Resources

Resources representam dados ou conteúdo que podem ser lidos pelo cliente.

A aula deve diferenciar:

```text
tool
→ ação

resource
→ conteúdo / contexto
```

### 4. Prompts

Prompts são templates ou capacidades de prompt expostas pelo servidor.

Não devem ser apresentados como equivalente a system prompt ou como mecanismo de segurança.

### 5. Discovery

A versão moderna do protocolo permite discovery das capacidades e também requests auto-descritivos.

O laboratório deve tornar visível:

```text
discover
→ inspect capabilities
→ select capability
→ invoke
→ observe result
```

### 6. Versioning

A aula deve apresentar explicitamente:

```text
protocol version
→ negotiation / compatibility
→ supported capability
```

O objetivo não é decorar versões, mas entender que protocolos evoluem e integrações precisam tratar compatibilidade.

### 7. Transport

Cobrir conceitualmente:

- conexão in-process para testes e ensino;
- stdio;
- Streamable HTTP.

A versão 2026-07-28 remove o `initialize/initialized` e o `Mcp-Session-Id` do wire protocol moderno. Cada request carrega sua versão e metadados necessários; `server/discover` pode ser usado para obter capacidades antecipadamente.

No núcleo do notebook, cliente e servidor devem se conectar **in-process**, sem subprocesso, porta ou infraestrutura remota. Depois de o aluno compreender o protocolo, stdio e HTTP aparecem como alternativas reais de transporte.

Isso preserva:

```text
Internet OFF
+ execução headless
+ sem porta local
+ sem dependência de processo externo
```


### 8. Authorization and Security

A aula deve separar:

```text
model decision
≠
authorization decision
```

Tópicos:

- autenticação e autorização;
- princípio do menor privilégio;
- validação de origem/issuer quando aplicável;
- exposição mínima de capabilities;
- secrets fora do prompt;
- approval gates para ações relevantes;
- auditabilidade.

### 9. Multi Round-Trip Requests (MRTR)

A revisão 2026-07-28 substitui o antigo padrão de requests iniciados livremente pelo servidor por um fluxo controlado de múltiplas idas e voltas.

Modelo conceitual:

```text
client request
→ server precisa de informação adicional
→ input_required
→ client coleta resposta
→ repete a request original com inputResponses
→ server continua
```

O tema deve aparecer **conceitualmente** na primeira versão da aula, especialmente como ponte para approval/elicitation, mas não precisa dominar o laboratório básico.

### 10. Deprecated Features and Historical Context

A aula deve alertar explicitamente que materiais MCP anteriores podem ensinar padrões que mudaram.

Na revisão 2026-07-28:

- `sampling` foi depreciado;
- `roots` foi depreciado;
- `initialize/initialized` deixou de fazer parte do fluxo moderno;
- `Mcp-Session-Id` foi removido do protocolo moderno.

O objetivo não é ensinar migração completa, mas desenvolver uma disciplina importante:

> **Protocolos versionados precisam ser estudados junto com a versão da especificação.**

### 11. Observability

Registrar, quando aplicável:

```text
protocol_version
server
method
capability_name
latency_ms
status
error_type
authorization_outcome
trace_context
```

A especificação moderna também documenta propagação de contexto OpenTelemetry via metadados.

## Student Lab

Construir um **TIL Lesson MCP Server** mínimo com o Python SDK v2.

No caminho principal do notebook:

```text
MCPServer
↕ in-process
Client
```

Essa forma de conexão existe oficialmente no SDK para testes e permite observar discovery, capabilities e invocação sem abrir portas ou lançar subprocessos.

Somente depois do caminho principal, a aula apresenta conceitualmente:

```text
mesmo servidor
→ stdio
ou
→ Streamable HTTP
```


Capacidades propostas:

### Resource

`til://lessons/status`

Retorna estado didático das aulas em dados simulados.

### Tool

`get_lesson_status`

Entrada:

```text
lesson_id
```

Saída estruturada:

```text
lesson_id
status
```

### Tool

`build_release_note`

Entrada:

```text
lesson_id
status
```

Saída:

```text
release_note
```

### Prompt

`review_release`

Template simples para revisar uma release note.

Nenhuma capability deve produzir side effect externo real.

## Protocol Introspection Lab

Antes do Architecture Lab, o aluno deve inspecionar pelo cliente:

```text
protocol_version
server_capabilities
tools
resources
prompts
```

Objetivo:

> **Não apenas chamar uma capability, mas observar o contrato e as capacidades que o protocolo torna descobríveis.**

Essa etapa cria a ponte entre:

```text
Aula 17 → contrato
Aula 18 → política de execução
Aula 19 → descoberta e exposição padronizadas
```

## Architecture Lab

Comparar três alternativas:

```text
A — função Python direta
B — tool local estruturada
C — capability exposta via MCP
```

Pergunta:

> **Que problema adicional o MCP resolve que a função ou tool local não resolvem?**

O aluno deve considerar:

- interoperabilidade;
- discovery;
- padronização;
- isolamento;
- custo operacional;
- segurança;
- observabilidade;
- necessidade real de múltiplos consumidores.

## Evidence Gate

A introdução do MCP precisa respeitar o princípio central do TIL:

> **Complexidade arquitetural precisa ser conquistada por evidência.**

O laboratório deve mostrar ao menos um cenário em que integração direta é suficiente e outro em que exposição padronizada traz benefício observável.

Não assumir:

```text
MCP > direct API
MCP > function call
MCP = agent
```

## Failure Taxonomy

Cobrir:

- protocol/version mismatch;
- capability not found;
- invalid arguments;
- transport failure;
- authorization failure;
- server execution failure;
- malformed structured result;
- timeout;
- unavailable dependency.

## What the Lesson Must Not Do

- não tratar MCP como agente;
- não introduzir multi-agent systems;
- não depender de API proprietária;
- não esconder contratos atrás de framework;
- não usar autorização baseada em confiança do modelo;
- não exigir internet para o núcleo do notebook;
- não introduzir side effects reais;
- não ensinar sintaxe de SDK sem explicar o protocolo.

## Notebook Design

Proposta:

```text
course/19-model-context-protocol/
└── 19-til-model-context-protocol.ipynb
```

Kaggle slug:

```text
til-19-model-context-protocol
```

Configuração inicial:

```text
Internet OFF
GPU OFF
sem API proprietária
sem side effects reais
```

## Suggested Lesson Flow

```text
1. Objetivos
2. O problema que MCP resolve
3. MCP ≠ agent
4. Host / Client / Server
5. Tools / Resources / Prompts
6. Discovery
7. Protocol version and compatibility
8. Transport: stdio vs HTTP
9. Authorization and security
10. Observability
11. Minimal MCP server
12. Minimal client
13. Failure lab
14. Architecture decision lab
15. Reproducibility
16. Summary
17. Bridge to Agentic Systems
```

## Glossary Candidates

PT-BR / EN:

- Protocolo de Contexto de Modelo / Model Context Protocol
- Host MCP / MCP host
- Cliente MCP / MCP client
- Servidor MCP / MCP server
- Descoberta de capacidades / Capability discovery
- Recurso MCP / MCP resource
- Prompt MCP / MCP prompt
- Negociação de versão / Version negotiation
- Transporte stdio / stdio transport
- Autorização / Authorization
- Capability exposure / Exposição de capacidades

## Acceptance Criteria

Student-ready somente quando:

1. referência de versão MCP explicitada;
2. host/client/server explicados;
3. tools/resources/prompts diferenciados;
4. discovery demonstrado;
5. versioning demonstrado;
6. conexão in-process demonstrada;
7. stdio e Streamable HTTP explicados;
8. MRTR explicado conceitualmente;
9. features depreciadas identificadas;
10. segurança e autorização abordadas;
11. observabilidade demonstrada;
12. servidor mínimo executável;
13. cliente mínimo executável;
14. protocol introspection lab;
15. failure taxonomy demonstrada;
16. architecture decision lab;
17. Glossário Vivo integrado;
18. Internet OFF no núcleo;
19. execução headless completa;
20. execução Kaggle validada;
21. revisão pedagógica final.

## Exit Condition

A aula estará completa quando o aluno conseguir explicar:

> **MCP padroniza como capacidades e contexto são expostos, descobertos e invocados. Ele não substitui contratos, workflows, autorização ou governança, e não transforma por si só um sistema em agente.**
