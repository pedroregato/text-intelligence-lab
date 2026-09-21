# Aula 19 — MCP Notebook Blueprint

## Status

Design blueprint — pre-implementation

## Purpose

Definir a sequência pedagógica, a responsabilidade de cada célula e a evidência observável da **Aula 19 — Model Context Protocol (MCP)** antes da implementação do notebook.

Baseline:

- MCP specification: `2026-07-28`;
- Python SDK: v2 stable;
- núcleo do notebook: `Internet OFF`, `GPU OFF`, sem API proprietária e sem side effects reais.

## Design Principle

A aula não deve começar com sintaxe do SDK.

A progressão pedagógica deve ser:

```text
problema de integração
→ abstração MCP
→ capabilities
→ servidor mínimo
→ cliente
→ discovery / introspection
→ invocation
→ segurança / observabilidade
→ decisão arquitetural
```

A pergunta central permanece:

> **Quando a exposição padronizada de capacidades compra utility suficiente para justificar a complexidade adicional?**

---

## Cell-by-cell Blueprint

### Célula 1 — Título

**Tipo:** Markdown

Título:

`# Aula 19 — Model Context Protocol (MCP)`

Mensagem inicial:

```text
Aula 17 → estruturamos uma tool
Aula 18 → coordenamos tools em workflows
Aula 19 → padronizamos como capacidades são expostas e descobertas
```

Pergunta central da aula.

---

### Célula 2 — Objetivos

**Tipo:** Markdown

Objetivos resumidos:

- explicar o problema de integração resolvido pelo MCP;
- distinguir host, client e server;
- distinguir tools, resources e prompts;
- observar discovery e protocol version;
- invocar capabilities por um cliente;
- discutir transportes, autorização e observabilidade;
- decidir quando MCP é ou não necessário.

---

### Célula 3 — Glossário Vivo

**Tipo:** Markdown

Links contextuais para os termos da Aula 19.

Candidatos:

- Model Context Protocol;
- MCP host;
- MCP client;
- MCP server;
- capability discovery;
- MCP tool;
- MCP resource;
- MCP prompt;
- protocol version;
- transport;
- authorization.

**Gate:** termos devem existir no Glossário antes da promoção student-ready.

---

### Célula 4 — Antes do MCP: qual é o problema?

**Tipo:** Markdown

Mostrar:

```text
App A ── integração própria ── Serviço X
App B ── integração própria ── Serviço X
App C ── integração própria ── Serviço X
```

Pergunta:

> O problema aqui é inteligência do modelo ou padronização da integração?

Resultado esperado:

`integration problem ≠ reasoning problem`.

---

### Célula 5 — O que MCP adiciona?

**Tipo:** Markdown

Diagrama:

```text
AI Application / Host
        ↓
MCP Client
        ↓
standardized protocol
        ↓
MCP Server
        ↓
tools / resources / prompts
```

Explicar que MCP padroniza exposição, discovery e invocation.

---

### Célula 6 — MCP não é agente

**Tipo:** Markdown

Quadro:

```text
MCP          → protocolo de integração
workflow     → política/sequência de execução
agent        → grau de autonomia para decidir e agir
```

Conectar explicitamente à Aula 18.

---

### Célula 7 — Version discipline

**Tipo:** Markdown

Registrar:

```text
MCP specification = 2026-07-28
Python SDK         = v2
```

Explicar por que a aula declara a revisão do protocolo.

Nota sobre materiais legados.

---

### Célula 8 — Ambiente e dependência

**Tipo:** Code

Responsabilidades:

- importar `mcp`;
- obter versão instalada do pacote;
- emitir mensagem clara;
- falhar cedo se a dependência não existir.

Não instalar pacotes em tempo de execução.

A dependência deve ser preparada previamente no ambiente Kaggle.

---

### Célula 9 — Imports

**Tipo:** Code

Imports mínimos previstos:

```python
from mcp import Client
from mcp.server import MCPServer
...
```

Adicionar apenas tipos realmente usados.

Evitar low-level `Server` na primeira versão.

---

### Célula 10 — Dados simulados do laboratório

**Tipo:** Code

Criar algo como:

```python
SIMULATED_LESSON_STATUS = {
    "17": "Available",
    "18": "Available",
    "19": "Draft",
}
```

Observação pedagógica:

> estado simulado do laboratório ≠ estado real do TIL.

Mesma disciplina aprendida na Aula 18.

---

### Célula 11 — Criando o MCP Server

**Tipo:** Markdown

Antes do código:

```text
Python function
    ↓
registered capability
    ↓
MCPServer
```

Explicar que o SDK deriva parte dos contratos da assinatura e documentação das funções.

---

### Célula 12 — Instância do servidor

**Tipo:** Code

Criar:

```python
mcp = MCPServer(
    "TIL Lesson Server",
    instructions="..."
)
```

Sem transport ainda.

---

### Célula 13 — Resource: lesson status

**Tipo:** Markdown

Conceito:

```text
resource
→ conteúdo que a aplicação lê

tool
→ operação que pode ser chamada
```

URI sugerida:

`til://lessons/status`

---

### Célula 14 — Implementando o resource

**Tipo:** Code

Registrar recurso que serialize os estados simulados.

Resultado deve ser determinístico.

---

### Célula 15 — Tool: get_lesson_status

**Tipo:** Markdown

Conectar à Aula 17:

```text
name
description
input
validation
result
```

---

### Célula 16 — Implementando get_lesson_status

**Tipo:** Code

Entrada:

`lesson_id: str`

Saída estruturada contendo:

- `lesson_id`;
- `status`.

Erro controlado para aula inexistente.

---

### Célula 17 — Tool: build_release_note

**Tipo:** Code

Receber:

- lesson_id;
- status.

Retornar release note sem side effect.

Essa tool reaproveita conceitualmente o domínio da Aula 18 sem duplicar o workflow inteiro.

---

### Célula 18 — Prompt: review_release

**Tipo:** Markdown

Explicar:

```text
prompt
→ template que o usuário/host escolhe e renderiza

prompt ≠ tool
prompt ≠ security policy
```

---

### Célula 19 — Implementando o prompt

**Tipo:** Code

Registrar `review_release`.

Parâmetro sugerido:

`release_note: str`

Retornar mensagem de revisão.

---

### Célula 20 — O cliente MCP

**Tipo:** Markdown

Introduzir:

```text
Client(mcp)
```

Explicar:

- conexão in-process;
- sem subprocesso;
- sem porta;
- ideal para testes e ensino;
- mesmas operações de cliente utilizadas com transportes reais;
- não demonstra framing de rede.

---

### Célula 21 — Protocol Introspection Lab

**Tipo:** Code

Dentro de:

```python
async with Client(mcp) as client:
    ...
```

Exibir:

- `client.protocol_version`;
- `client.server_info`;
- `client.server_capabilities`;
- `client.instructions`.

Objetivo:

> observar o protocolo antes de chamar qualquer capability.

---

### Célula 22 — Discovery: tools

**Tipo:** Code

Executar:

`await client.list_tools()`

Exibir DataFrame didático com:

- name;
- title;
- description;
- input_schema.

Pergunta:

> O que o cliente consegue descobrir sem conhecer o código Python do servidor?

---

### Célula 23 — Discovery: resources e prompts

**Tipo:** Code

Executar:

- `list_resources()`;
- `list_resource_templates()`;
- `list_prompts()`.

Mostrar listas de maneira compacta.

---

### Célula 24 — Chamando uma tool

**Tipo:** Code

Executar:

`call_tool("get_lesson_status", {"lesson_id": "18"})`

Mostrar:

- conteúdo retornado;
- conteúdo estruturado, se aplicável;
- `is_error`.

---

### Célula 25 — Lendo um resource

**Tipo:** Code

Executar:

`read_resource("til://lessons/status")`

Interpretar o conteúdo.

Conectar:

```text
resource address
→ URI
```

---

### Célula 26 — Renderizando um prompt

**Tipo:** Code

Executar:

`get_prompt("review_release", {...})`

Mostrar roles e conteúdo renderizado.

Reforçar:

> MCP entrega mensagens; ele não precisa executar um LLM neste laboratório.

---

### Célula 27 — Três primitives, três papéis

**Tipo:** Markdown

Tabela:

| Primitive | Papel pedagógico | Quem decide usar? |
|---|---|---|
| Tool | operação | modelo/host sob política |
| Resource | conteúdo/contexto | aplicação/host |
| Prompt | template selecionável | usuário/host |

Usar a formulação da documentação atual do SDK para evitar confusão conceitual.

---

### Célula 28 — Discovery vs hard-coded integration

**Tipo:** Markdown

Comparar:

```text
hard-coded call
→ cliente precisa conhecer endpoint/assinatura

MCP discovery
→ cliente pode inspecionar capabilities e contratos
```

Não declarar que discovery elimina integração ou governança.

---

### Célula 29 — Protocol version e compatibilidade

**Tipo:** Markdown + pequena Code cell opcional

Mostrar `client.protocol_version`.

Explicar modo `auto` conceitualmente:

```text
modern server
→ server/discover
→ 2026-07-28

older server
→ fallback legado
```

Não implementar servidor legado na primeira versão.

---

### Célula 30 — Transportes

**Tipo:** Markdown

Diagrama:

```text
mesmas capabilities

in-process
stdio
Streamable HTTP
```

Separar:

```text
capability semantics
≠
transport
```

O núcleo do notebook usa in-process.

---

### Célula 31 — Segurança e autorização

**Tipo:** Markdown

Princípios:

```text
model confidence
≠
authorization

capability exists
≠
caller is authorized
```

Conectar approval gates da Aula 18.

Cobrir least privilege e secrets fora do prompt.

---

### Célula 32 — MRTR: quando o servidor precisa de mais informação

**Tipo:** Markdown

Fluxo conceitual:

```text
client request
→ server returns input_required
→ client obtains required input
→ repeats original request with inputResponses
→ server continues
```

Não implementar na versão inicial do lab.

Objetivo: mostrar evolução moderna do protocolo sem aumentar demais a carga do primeiro notebook.

---

### Célula 33 — O que mudou em 2026

**Tipo:** Markdown

Caixa de atenção:

```text
sampling             → deprecated
roots                → deprecated
initialize/initialized → legacy path
Mcp-Session-Id       → absent from modern 2026 path
```

Mensagem:

> tutoriais MCP precisam ser lidos junto com a versão que ensinam.

---

### Célula 34 — Observabilidade do cliente

**Tipo:** Markdown

Campos conceituais:

```text
protocol_version
capability
operation
latency_ms
status
error_type
```

Conectar à observabilidade das Aulas 17 e 18.

---

### Célula 35 — Wrapper observável

**Tipo:** Code

Criar helper simples para medir chamadas do cliente usadas no lab.

Não construir framework.

Produzir lista de eventos.

---

### Célula 36 — Tabela de eventos MCP

**Tipo:** Code

Mostrar DataFrame dos eventos capturados.

Objetivo:

> transformar invocation em evidência observável.

---

### Célula 37 — Failure Lab

**Tipo:** Markdown

Casos:

A. tool inexistente;  
B. lesson_id inexistente;  
C. argumentos inválidos;  
D. resource inexistente.

Aluno deve classificar:

- capability not found;
- invalid arguments;
- server execution failure;
- resource not found.

---

### Célula 38 — Exercício executável

**Tipo:** Code

Espaço para aluno executar pelo menos dois failure cases e registrar resultado.

---

### Célula 39 — Dica

**Tipo:** Markdown

Sugerir:

- `client.call_tool(...)`;
- `client.read_resource(...)`;
- observar `is_error` e exceções/resultados tipados.

---

### Célula 40 — Solução de referência

**Tipo:** Code

Implementar solução curta e legível.

Sem esconder comportamento com helpers sofisticados.

---

### Célula 41 — Architecture Decision Lab

**Tipo:** Markdown

Comparar:

```text
A — função direta
B — tool estruturada local
C — capability via MCP
```

Critérios:

- número de consumidores;
- necessidade de discovery;
- interoperabilidade;
- isolamento;
- segurança;
- observabilidade;
- custo operacional.

---

### Célula 42 — Casos de decisão

**Tipo:** Code

DataFrame com cenários, por exemplo:

- função usada dentro de um único módulo;
- tool chamada por um único workflow local;
- capabilities consumidas por hosts diferentes;
- servidor compartilhado entre aplicações.

---

### Célula 43 — Sua decisão

**Tipo:** Markdown

Aluno escolhe:

- `direct_function`;
- `structured_tool`;
- `mcp_capability`.

Regra:

> escolher a arquitetura mínima suficiente.

---

### Célula 44 — Referência de interpretação

**Tipo:** Code/Markdown

Fornecer escolhas de referência acompanhadas de justificativa, não apenas rótulos.

---

### Célula 45 — Síntese arquitetural

**Tipo:** Markdown

```text
Aula 17
capability contract
      ↓
Aula 18
controlled execution
      ↓
Aula 19
standardized exposure + discovery
```

Princípio:

> MCP resolve um problema de integração. Ele não cria autonomia por si só.

---

### Célula 46 — Ponte para Agentic Systems

**Tipo:** Markdown

Mostrar:

```text
MCP capabilities
+ workflow / execution policy
+ model decisions
+ state
+ oversight
→ possible agentic system
```

Evitar:

`MCP → agent`

---

### Célula 47 — Reprodutibilidade

**Tipo:** Markdown

Registrar:

```text
Internet OFF
GPU OFF
in-process client/server
no external API
no external side effects
MCP version pinned/documented
```

---

### Célula 48 — Navegação

**Tipo:** Markdown

Anterior:

Aula 18 — Deterministic Workflows.

Home:

TIL Course Home.

Próxima:

Bloco D / próxima unidade Agentic Systems ainda em preparação.

---

## Headless Execution Path

O `Run All` deve funcionar sem intervenção:

```text
imports
→ simulated state
→ register capabilities
→ connect in-process
→ introspection
→ discovery
→ tool call
→ resource read
→ prompt render
→ observability
→ failure examples
→ architecture lab
→ complete
```

Nenhuma célula obrigatória deve:

- esperar input humano;
- iniciar servidor persistente;
- abrir porta;
- lançar subprocesso;
- acessar Internet;
- exigir LLM externo.

---

## Cognitive Load Strategy

A aula deve usar quatro camadas visuais:

1. diagramas textuais antes de código;
2. código mínimo;
3. saída observável;
4. interpretação imediatamente após a execução.

Padrão:

```text
conceito
→ diagrama
→ código
→ resultado
→ interpretação
```

O objetivo é evitar que MCP seja aprendido como uma coleção de decorators.

---

## Explicit Non-goals for v1

Não incluir na primeira versão executável:

- servidor remoto real;
- OAuth real;
- multi-agent;
- LLM externo;
- MRTR implementado ponta a ponta;
- extensions customizadas;
- subscriptions avançadas;
- low-level `Server`;
- framework agente;
- deploy HTTP.

Esses temas podem aparecer como leitura, extensão ou AUTHOR lab posterior.

---

## Student-ready Gate

Antes da promoção:

```text
[ ] MCP version explicit
[ ] Python SDK version explicit
[ ] glossary integrated
[ ] host/client/server clear
[ ] tool/resource/prompt clear
[ ] discovery executable
[ ] protocol introspection executable
[ ] tool call executable
[ ] resource read executable
[ ] prompt rendering executable
[ ] failure lab executable
[ ] observability visible
[ ] authorization concept clear
[ ] modern vs legacy distinction clear
[ ] architecture decision lab complete
[ ] Internet OFF
[ ] headless PASS
[ ] Kaggle COMPLETE
[ ] pedagogical review complete
```
