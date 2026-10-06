# Aula 21 — Planning and Goal Decomposition

## Status

Draft / review candidate

## Role in the TIL

A Aula 21 é a segunda unidade do **Bloco D — Agentic Systems**.

Progressão:

```text
Aula 20 — Agentic Systems Foundations
→ Aula 21 — Planning and Goal Decomposition
```

A Aula 20 tornou observável a escolha iterativa da próxima ação. A Aula 21 adiciona uma nova capacidade:

> **representar explicitamente um plano de múltiplas etapas antes e durante a execução.**

## Central Question

> **Quando escolher apenas a próxima ação deixa de ser suficiente e passa a valer a pena construir, validar e revisar um plano explícito?**

## Governing Principle

> **Planejamento só se justifica quando reduz incerteza operacional ou melhora coordenação o suficiente para compensar seu custo e risco adicionais.**

O TIL não assume:

```text
plan > reactive loop
longer plan > better plan
replanning > stable execution
```

## Core Distinction

```text
Reactive next-action
→ observa estado
→ escolhe próxima ação
→ executa
→ repete

Explicit planning
→ interpreta objetivo
→ decompõe em subobjetivos
→ cria dependências
→ valida plano
→ executa
→ observa desvios
→ mantém / revisa / replaneja
```

## Learning Objectives

Ao final da aula, o aluno deverá conseguir:

1. distinguir seleção reativa de próxima ação de planejamento explícito;
2. decompor objetivo em subtarefas observáveis;
3. representar dependências entre etapas;
4. validar plano antes da execução;
5. distinguir plan generation de plan execution;
6. aplicar plan budget;
7. reconhecer planos inválidos, redundantes ou incompletos;
8. observar quando o estado invalida uma etapa futura;
9. executar replanning controlado;
10. medir plan quality e execution quality separadamente;
11. comparar reactive loop e plan-based execution;
12. justificar quando planejar não traz utility adicional.

## Student Lab

Problema didático: **TIL Lesson Publication with Conditional Dependencies**.

O objetivo continua sendo simulado e sem side effects externos.

### Architecture A — Reactive Agent

```text
state
→ choose_next_action
→ governance
→ execute
→ observe
→ repeat
```

### Architecture B — Plan-Based Agent

```text
goal
→ build_plan
→ validate_plan
→ execute_step
→ observe
→ check_plan_validity
→ continue / replan / escalate
```

## Planning Contract

Cada etapa do plano terá:

```text
step_id
action
preconditions
depends_on
status
reason
```

## Plan Quality Checks

Antes da execução:

- actions pertencem à allow-list;
- dependências existem;
- não há ciclos;
- pré-condições mínimas são coerentes;
- não há publicação antes de aprovação;
- step budget não é excedido.

## Replanning

Replanning só ocorre quando evidência observada invalida o plano atual.

Exemplos:

- status da aula mudou;
- aprovação foi negada;
- capability ficou indisponível;
- nova informação criou dependência ausente.

## Observability

Registrar:

```text
plan_id
plan_version
step_id
action
dependencies
preconditions
plan_validation
execution_result
state_change
replan_reason
cost_proxy
latency_proxy
termination_reason
```

## Comparative Evidence Lab

Executar reactive loop e plan-based execution sobre os mesmos cenários:

1. objetivo simples e estável;
2. objetivo com dependência explícita;
3. mudança de estado após criação do plano;
4. plano deliberadamente inválido.

Comparar:

- task success;
- actions executed;
- planning overhead;
- replans;
- invalid steps avoided;
- human intervention;
- cost proxy;
- latency proxy;
- termination reason.

## Failure Taxonomy

- goal decomposition failure;
- missing dependency;
- invalid ordering;
- cyclic plan;
- stale plan;
- unnecessary replanning;
- execution divergence;
- unsafe plan;
- plan budget exceeded.

## What the Lesson Must Not Do

- não usar LLM externo;
- não esconder plano em chain-of-thought;
- não tratar plano como raciocínio privado;
- não permitir side effects reais;
- não introduzir multi-agent;
- não confundir planning com workflow fixo;
- não tratar replanning como loop irrestrito;
- não assumir que planejar sempre melhora resultado.

## Reproducibility

```text
Internet OFF
GPU OFF
sem API externa
sem side effects reais
planner determinístico/local
```

## Notebook Design

```text
course/21-planning-and-goal-decomposition/
└── 21-til-planning-and-goal-decomposition.ipynb
```

Kaggle slug:

```text
til-21-planning-and-goal-decomposition
```

## Acceptance Criteria

Student-ready somente quando:

1. reactive loop vs planning estiver explícito;
2. plan contract executável;
3. dependencies observáveis;
4. plan validation executável;
5. plan execution separado de plan generation;
6. replanning controlado;
7. plan budget;
8. failure lab;
9. comparative evidence lab;
10. architecture decision lab;
11. Living Glossary integrado;
12. Internet OFF;
13. headless PASS;
14. Kaggle COMPLETE;
15. revisão pedagógica final.

## Exit Condition

A aula está completa quando o aluno consegue explicar:

> **Planejamento não é uma sequência maior de ações. É uma representação explícita de subobjetivos, dependências e condições que pode ser validada, executada e revisada sob evidência. Ele só deve ser usado quando essa estrutura acrescentar utility real.**
