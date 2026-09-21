# Aula 18 — Deterministic Workflows

## Status

Draft

## Role in the TIL

A Aula 18 é a segunda unidade do **Bloco C — Tools and Workflows**.

Progressão:

```text
Aula 17 — Tool Use, Function Calling and Contracts
→ Aula 18 — Deterministic Workflows
→ Aula 19 — Model Context Protocol (MCP)
→ Bloco D — Agentic Systems
```

A Aula 17 ensinou uma tool isolada. A Aula 18 ensina como **compor tools sob uma ordem explícita, estado controlado e políticas previsíveis** antes de introduzir autonomia ampla.

## Central Question

> **Como combinar múltiplas tools em um fluxo confiável, observável e recuperável sem depender de um agente autônomo?**

## Governing Principle

Um workflow determinístico deve tornar explícitos:

```text
ordem
+ estado
+ regras
+ erros
+ retries
+ checkpoints
+ approval gates
+ observabilidade
```

A sequência de execução é definida pelo sistema, não improvisada por um agente.

## Learning Objectives

Ao final da aula, o aluno deverá ser capaz de:

1. distinguir tool isolada de workflow;
2. distinguir workflow determinístico de agent loop;
3. representar etapas e dependências explícitas;
4. manter e inspecionar estado de execução;
5. implementar retries controlados;
6. explicar idempotência;
7. usar checkpoints para retomada;
8. aplicar approval gates antes de efeitos externos;
9. localizar falhas por etapa;
10. comparar execução linear simples com workflow estruturado;
11. reconhecer quando um workflow é suficiente e quando autonomia adicional ainda não se justifica;
12. preparar a base conceitual para MCP.

## Scope

### 1. Tool vs workflow

```text
tool
→ uma capacidade

workflow
→ composição ordenada de capacidades
```

### 2. Deterministic orchestration

A ordem do fluxo é conhecida de antemão.

Exemplo:

```text
validate_request
→ lookup_lesson
→ calculate_discount
→ build_message
→ approval_gate
→ send_message
```

### 3. State

O workflow deve carregar um estado explícito, por exemplo:

```text
request_id
current_step
inputs
outputs
attempts
status
errors
approved
```

### 4. Retry

Retry não significa repetir indefinidamente.

Devem ser explícitos:

- quais erros são retryable;
- quantidade máxima;
- condição de parada;
- registro de tentativas.

### 5. Idempotency

Executar novamente a mesma operação não deve produzir efeitos duplicados quando a operação for desenhada como idempotente.

### 6. Checkpoints

Registrar progresso para permitir:

```text
falha
→ inspeção
→ correção
→ retomada
```

em vez de reiniciar tudo cegamente.

### 7. Approval gates

Ações state-changing ou high-impact devem poder pausar antes da execução.

### 8. Failure taxonomy

Separar:

- step failure;
- validation failure;
- retry exhaustion;
- duplicate execution risk;
- state inconsistency;
- approval rejection;
- downstream dependency failure.

### 9. Observability

Registrar:

```text
workflow_id
step_name
step_status
attempt
started_at
latency_ms
input_summary
output_summary
error_type
checkpoint
approval_status
```

## Student Lab

Construir um **TIL Lesson Release Workflow** didático.

Fluxo:

```text
validate_release_request
→ get_lesson_status
→ build_release_note
→ approval_gate
→ publish_release_note
```

A etapa final será simulada localmente, sem side effect externo real.

O laboratório deverá incluir:

- execução feliz;
- falha transitória simulada;
- retry;
- checkpoint;
- retomada;
- prevenção de duplicidade;
- aprovação negada;
- log completo de execução.

## Architecture Decision Lab

Comparar:

```text
funções chamadas manualmente
vs
workflow determinístico
vs
agente autônomo
```

Pergunta central:

> A variabilidade do problema exige autonomia, ou um fluxo explícito já resolve com menor risco?

## MCP Bridge

A Aula 18 não implementa MCP.

Ela prepara a próxima transição:

```text
local tool registry
→ deterministic workflow
→ standardized capability exposure
→ MCP
```

Na Aula 19, tools e outros recursos poderão ser expostos por um protocolo padronizado sem alterar o princípio de que execução e governança devem permanecer observáveis.

## What the Lesson Must Not Do

- não introduzir frameworks agentes;
- não usar LLM para decidir livremente a sequência;
- não depender de API proprietária;
- não exigir internet;
- não executar side effects reais;
- não tratar retry como loop infinito;
- não confundir checkpoint com memória de longo prazo;
- não confundir workflow com agente.

## Notebook Design

```text
course/18-deterministic-workflows/
└── 18-til-deterministic-workflows.ipynb
```

Kaggle slug proposto:

```text
til-18-deterministic-workflows
```

Configuração:

```text
Internet OFF
GPU OFF
sem API externa
sem side effects reais
```

## Suggested Lesson Flow

```text
1. Objetivos
2. Tool vs workflow
3. Workflow determinístico
4. Estado explícito
5. Workflow runner
6. Happy path
7. Falha por etapa
8. Retry
9. Idempotência
10. Checkpoints
11. Approval gate
12. Observabilidade
13. Recovery lab
14. Architecture decision lab
15. Exercícios
16. Reprodutibilidade
17. Síntese
18. Ponte para MCP
```

## Evidence Strategy

Modo inicial: **STUDENT**.

O laboratório é local, determinístico e controlado.

Comparações futuras entre workflow determinístico e agente autônomo deverão ser tratadas em AUTHOR / EVIDENCE.

## Acceptance Criteria

Student-ready somente quando:

1. objetivos explícitos;
2. workflow separado de tool isolada;
3. estado explícito;
4. retries controlados;
5. idempotência demonstrada;
6. checkpoints demonstrados;
7. approval gate executável;
8. failure taxonomy;
9. observabilidade por etapa;
10. recovery lab;
11. architecture decision lab;
12. Glossário Vivo integrado contextualmente;
13. navegação anterior/home/próxima;
14. Internet OFF;
15. execução headless completa;
16. warnings revisados;
17. execução Kaggle concluída;
18. revisão pedagógica final.

## Exit Condition

A aula estará completa quando o aluno conseguir explicar:

> **Um workflow determinístico coordena capacidades sob uma sequência explícita, estado observável e políticas de execução previsíveis. Ele deve ser preferido a maior autonomia quando já resolve o problema com menor risco e complexidade.**
