# Aula 20 — Agentic Systems Foundations

## Status

AVAILABLE / STUDENT-READY — pedagogically revised; current notebook revision awaiting final re-execution.

## Role in the TIL

A Aula 20 abre o **Bloco D — Agentic Systems**.

Progressão:

```text
Aula 17 — Tool Use, Function Calling and Contracts
→ Aula 18 — Deterministic Workflows
→ Aula 19 — Model Context Protocol (MCP)
→ Aula 20 — Agentic Systems Foundations
```

As aulas anteriores separaram capacidade, execução controlada e integração padronizada. A Aula 20 introduz uma nova variável arquitetural: **autonomia na escolha da próxima ação**.

## Central Question

> **Quando um sistema deixa de apenas seguir uma política de execução previamente definida e passa a participar da decisão sobre o que fazer a seguir?**

## Governing Principle

> **Autonomia deve ser tratada como propriedade mensurável, não como rótulo de marketing.**

O TIL não assume:

```text
agent > workflow
autonomia > determinismo
mais passos > mais inteligência
```

A pergunta é:

> Que capacidade adicional apareceu, qual evidência mostra valor e quais novos custos e riscos surgiram?

## Core Distinction

```text
Tool
→ executa uma capacidade

Workflow
→ coordena capacidades sob política explícita

MCP
→ padroniza exposição e discovery

Agentic loop
→ observa estado
→ escolhe próxima ação
→ executa sob controles
→ observa resultado
→ repete ou encerra
```

Um workflow pode ter branches, retries e regras complexas. Isso, por si só, não o transforma em agente.

A diferença pedagógica desta aula é o **locus da decisão de próxima ação**.

## Reference Architecture

```text
Goal / Request
      ↓
Observed State
      ↓
Decision Provider
      ↓
Proposed Action
      ↓
Governance Gate
(validation + authorization + policy)
      ↓
Tool / Capability Execution
      ↓
Observation
      ↓
State Update
      ↺
Termination / Human Escalation
```

Separações obrigatórias:

```text
decision ≠ authorization
decision ≠ execution
observation ≠ memory
agent loop ≠ unlimited loop
```

## Agent Harness

A arquitetura da Aula 20 também introduz o conceito de **Agent Harness** como camada executável ao redor do decision provider.

Definição operacional no TIL:

> **Agent Harness é a camada de runtime que conecta estado explícito, action space, governance, capabilities, observação, atualização de estado, limites, terminação, escalonamento humano e observabilidade.**

Abstração didática:

```text
Decision Provider
+
Agent Harness
=
execução agentic controlada
```

Essa expressão não é uma definição universal de agente. Ela serve para destacar que o comportamento do sistema não depende apenas do modelo ou decision provider.

Distinções:

```text
MCP
→ padroniza integração de capabilities

Workflow
→ coordena transições ou sequências

Agent Harness
→ controla o runtime do comportamento agente

Orchestrator
→ coordena múltiplos componentes, fluxos ou agentes
```

## Learning Objectives

Ao final da aula, o aluno deverá conseguir:

1. distinguir workflow determinístico de agentic loop;
2. identificar onde a autonomia aparece em uma arquitetura;
3. representar estado, ação, observação e condição de término;
4. explicar por que branching não é sinônimo de agência;
5. implementar um loop agente mínimo e observável;
6. separar decisão, validação, autorização e execução;
7. explicar o papel do agent harness como camada de runtime e controle;
8. aplicar step budget e termination conditions;
9. reconhecer quando escalar para supervisão humana;
10. comparar workflow e agentic loop sob a mesma tarefa;
11. avaliar sucesso, custo proxy, latência proxy, decisões, tool calls e intervenção humana;
12. localizar falhas em decision, policy, tool, observation e termination;
13. justificar quando a autonomia adicional não compensa.

## Student Lab

Problema didático: **TIL Lesson Release Decision**.

O mesmo objetivo será executado por duas arquiteturas.

### A — Deterministic Workflow

```text
validate_request
→ inspect_lesson_status
→ build_release_note
→ approval_gate
→ publish_simulated
```

### B — Minimal Agentic Loop

A cada passo:

```text
state
→ choose_next_action(state)
→ governance_gate(action)
→ execute(action)
→ observe(result)
→ update_state
→ stop / continue / escalate
```

O decision provider inicial será **determinístico e local**. Não usaremos LLM ou API proprietária na primeira versão.

Isso permite isolar o conceito de agência sem misturá-lo com qualidade de modelo.

## Action Space

- `inspect_request`
- `get_lesson_status`
- `build_release_note`
- `request_approval`
- `publish_simulated`
- `ask_human`
- `stop`

O agente não pode inventar novas tools.

## State Contract

```text
goal
request_valid
lesson_status
release_note
approval
published
needs_human
done
step_count
history
```

## Governance Boundary

A decisão produz uma **proposta de ação**.

Antes da execução:

```text
proposed action
→ schema validation
→ allow-list
→ authorization / approval policy
→ step budget
→ execution
```

A regra permanece:

> **decisão do modelo não é autorização.**

## Termination

O loop termina por:

- objetivo concluído;
- estado terminal seguro;
- necessidade de supervisão humana;
- step budget excedido;
- erro não recuperável.

Nunca usar loop aberto.

## Failure Taxonomy

- goal interpretation failure;
- next-action selection failure;
- invalid action;
- authorization failure;
- tool execution failure;
- observation/state update failure;
- loop/termination failure;
- human escalation failure.

## Observability

Registrar por passo:

```text
run_id
step
state_before
proposed_action
decision_reason
governance_outcome
tool_result
state_after
cost_proxy
latency_proxy
human_intervention
termination_reason
```

## Comparative Evidence Lab

Executar workflow e agentic loop sobre os mesmos cenários:

1. aula pronta e aprovação disponível;
2. aula não pronta;
3. solicitação ambígua;
4. aprovação ausente.

Comparar:

- task success;
- steps executed;
- decision count;
- tool calls;
- unnecessary actions;
- human intervention;
- policy violations;
- termination reason;
- cost proxy;
- latency proxy.

Pergunta de evidência:

> **A autonomia resolveu variabilidade real suficiente para justificar novos pontos de falha e governança?**

## Architecture Decision Lab

Escolher entre:

```text
direct function
deterministic workflow
agentic loop
```

Justificar por variabilidade, previsibilidade, risco, reversibilidade, custo e supervisão.

## What the Lesson Must Not Do

- não usar framework agente como conceito;
- não depender de LLM externo;
- não tratar chain-of-thought como observabilidade;
- não permitir side effects reais;
- não permitir ação fora da allow-list;
- não usar loop ilimitado;
- não chamar qualquer sistema com tools de “agente”;
- não afirmar que agente é superior a workflow;
- não introduzir multi-agent systems nesta aula.

## Reproducibility

```text
Internet OFF
GPU OFF
sem API externa
sem side effects reais
decision provider determinístico
```

## Notebook Design

```text
course/20-agentic-systems-foundations/
└── 20-til-agentic-systems-foundations.ipynb
```

Kaggle slug proposto:

```text
til-20-agentic-systems-foundations
```

## Evidence Strategy

Modo inicial: **STUDENT**.

A primeira versão deve tornar observáveis:

```text
mesmo objetivo
+ mesmas capabilities
+ mesmos cenários
→ workflow fixo vs agentic loop
→ evidência comparável
```

O objetivo não é provar superioridade do agente, mas localizar **onde a autonomia acrescenta valor e onde apenas acrescenta custo/risco**.

## Acceptance Criteria

Student-ready somente quando:

1. workflow e agentic loop estiverem claramente separados;
2. estado explícito;
3. action space explícito;
4. decision provider observável;
5. governance gate observável;
6. step budget;
7. termination reasons;
8. human escalation;
9. comparative evidence lab;
10. failure taxonomy;
11. architecture decision lab;
12. Glossário Vivo integrado;
13. Internet OFF;
14. execução headless completa;
15. execução Kaggle completa;
16. revisão pedagógica final.

## Exit Condition

A aula está completa quando o aluno consegue explicar:

> **Um sistema agente não é definido por possuir tools, MCP ou branches. O ponto central é a autonomia controlada na escolha da próxima ação a partir do estado observado — e essa autonomia só se justifica quando sua utility supera o custo, o risco e a perda de previsibilidade introduzidos.**
