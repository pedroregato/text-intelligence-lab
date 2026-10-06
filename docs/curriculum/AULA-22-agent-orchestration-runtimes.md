# Aula 22 — Agent Orchestration Runtimes

## Status

Proposed

## Role in the TIL

A Aula 22 é uma unidade proposta para o **Bloco D — Agentic Systems**.

Progressão prevista:

```text
Aula 20 — Agentic Systems Foundations
→ Aula 21 — Planning and Goal Decomposition
→ Aula 22 — Agent Orchestration Runtimes
```

A Aula 20 introduz agentic loop e Agent Harness.

A Aula 21 introduz planning, dependencies, plan validation e replanning.

A Aula 22 deve mostrar como esses mecanismos passam a ser executados por um runtime de orquestração com estado, transições, persistência e controle explícitos.

## Central Question

> **Quando um loop agente simples deixa de ser suficiente e passa a valer a pena usar um runtime de orquestração?**

## Governing Principle

> **Orchestration runtime só se justifica quando estado, persistência, branching, recovery, human-in-the-loop ou execução durável exigirem uma camada de coordenação mais explícita do que código procedural simples.**

O TIL não assume:

```text
framework > código simples
graph > workflow
LangGraph > outras alternativas
orchestration runtime > harness
```

## Core Distinction

```text
Decision Provider
→ propõe próxima ação

Agent Harness
→ controla runtime do comportamento agente

Planner
→ representa plano e dependências

Orchestration Runtime
→ coordena estado, nós, transições, persistência e retomada de execução
```

Essas responsabilidades podem coexistir na mesma implementação, mas não devem ser tratadas como sinônimos.

## Learning Objectives

Ao final da aula, o aluno deverá conseguir:

1. distinguir harness de orchestration runtime;
2. modelar execução como grafo de estado;
3. identificar nodes, edges e conditional routing;
4. tornar estado compartilhado explícito;
5. implementar checkpoints;
6. explicar durable execution;
7. implementar interrupt / human-in-the-loop;
8. distinguir retry, resume e recovery;
9. comparar implementação procedural com graph runtime;
10. medir overhead e utility da orquestração;
11. reconhecer quando um framework não é necessário;
12. ler LangGraph como implementação de referência, não como definição do conceito.

## Vendor-neutral architecture

```text
Input / Goal
↓
Shared State
↓
Node
↓
Transition Policy
↓
Next Node
↓
Checkpoint
↓
Continue / Interrupt / Resume / Stop
```

## Minimal Concepts

- state graph;
- node;
- edge;
- conditional edge;
- shared state;
- checkpoint;
- interrupt;
- resume;
- durable execution;
- retry;
- recovery;
- human-in-the-loop;
- execution trace.

## Comparative Evidence Lab

Comparar duas implementações da mesma tarefa:

### A — Procedural orchestrator

```text
Python
+ explicit state
+ functions
+ if/while
```

### B — Graph runtime

```text
state graph
+ nodes
+ conditional transitions
+ checkpoint
+ resume
```

Cenários:

1. fluxo simples e linear;
2. branching por estado;
3. interrupção para aprovação humana;
4. falha transitória com resume;
5. estado persistido e retomada posterior.

Comparar:

- task success;
- code complexity;
- state visibility;
- recovery capability;
- restart cost;
- number of transitions;
- persistence overhead;
- human intervention;
- cost proxy;
- latency proxy.

## Architecture Decision Lab

Pergunta:

> **Quando um graph runtime conquistou sua complexidade?**

Critérios:

- número de estados;
- branching;
- necessidade de persistência;
- necessidade de retomada;
- human-in-the-loop;
- duração do processo;
- reversibilidade;
- observabilidade;
- custo operacional;
- risco.

## LangGraph as Reference Implementation

LangGraph pode aparecer como **estudo de caso de implementação**.

O TIL deve ensinar primeiro os conceitos:

```text
state
nodes
edges
routing
checkpoint
interrupt
resume
```

e somente depois mapear:

```text
conceito TIL
→ primitiva LangGraph
```

A aula não deve depender de LangGraph para ensinar os fundamentos.

## Relationship with Agent Harness

Uma distinção pedagógica recomendada:

```text
Agent Harness
→ camada de runtime e controle ao redor da decisão

Orchestration Runtime
→ mecanismo que coordena estados e transições da execução
```

Em uma implementação concreta, um orchestration runtime pode ser parte do harness.

## Relationship with MCP

```text
MCP
→ como descobrir/acessar capabilities

Orchestration Runtime
→ quando e em qual sequência executar capabilities
```

## Relationship with Planning

```text
Planner
→ produz ou revisa um plano

Orchestration Runtime
→ executa e acompanha o plano
```

## Relationship with CASE-AI-BANKING-001

O case de AI Banking / Machine Customer oferece um cenário aplicado para discutir:

- orchestration em ambientes regulados;
- human approval;
- durable execution;
- audit trail;
- customer agent vs institutional agent;
- integração futura entre múltiplos agentes.

## What the Lesson Must Not Do

- não começar por LangGraph;
- não ensinar framework como sinônimo de conceito;
- não afirmar que graph é superior a código procedural;
- não esconder estado;
- não depender de API externa para o laboratório principal;
- não introduzir multi-agent antes de consolidar single-agent orchestration;
- não confundir planner, harness e orchestrator.

## Reproducibility Target

```text
Internet OFF
GPU OFF
sem API externa
sem side effects reais
runtime local/determinístico no laboratório base
```

Uma extensão opcional pode usar LangGraph se a dependência estiver previamente disponível no ambiente.

## Acceptance Criteria

A aula só deve ser promovida quando:

1. procedural vs graph estiver explicitamente comparado;
2. shared state for observável;
3. conditional routing executável;
4. checkpoint executável;
5. interrupt/resume executável;
6. recovery demonstrado;
7. human-in-the-loop demonstrado;
8. overhead de runtime medido;
9. Architecture Decision Lab concluído;
10. LangGraph permanecer opcional;
11. Glossário Vivo integrado;
12. headless PASS;
13. Kaggle COMPLETE;
14. inspeção pedagógica final.

## Exit Condition

O aluno deve conseguir explicar:

> **Um orchestration runtime não torna um sistema automaticamente melhor ou mais agente. Ele se justifica quando coordenação de estado, branching, persistência, retomada e supervisão se tornam complexas o suficiente para exigir uma camada explícita de execução.**
