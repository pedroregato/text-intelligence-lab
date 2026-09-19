# TIL-AIE-001 — Agentic Intelligence Evolution

## Status

Proposed

## Purpose

Definir a evolução curricular do **Text Intelligence Lab (TIL)** de um curso centrado em Text Intelligence para uma trilha de engenharia de sistemas inteligentes e agentes, preservando os fundamentos de NLP, Machine Learning clássico, Transformers, experimentação e avaliação.

## Governing Principle

> **Complexidade arquitetural precisa ser conquistada por evidência.**

O TIL não assume, por princípio, que:

```text
Transformer > ML clássico
LLM > Transformer
agente > LLM
```

Cada aumento de complexidade deve ser justificado por ganho demonstrável de utility no contexto da tarefa.

Uma forma inicial de pensar utility é:

```text
utility = f(qualidade, custo, latência, risco, autonomia)
```

A função exata depende do problema. O objetivo pedagógico não é produzir um ranking universal, mas ensinar o aluno a medir trade-offs e justificar decisões.

## Macroarchitecture

A evolução curricular passa a ser organizada em quatro macrocamadas.

### I — Text Intelligence

Fundamentos para transformar texto em representação, features, sinais e tarefas mensuráveis.

Inclui:

- texto como dado;
- tokenização e normalização;
- Bag-of-Words e TF-IDF;
- classificação;
- métricas;
- tarefas de NLP;
- embeddings.

### II — Model Engineering

Construção, comparação e avaliação de modelos sob condições explícitas.

Inclui:

- baselines clássicos fortes;
- Transformers;
- treinamento e fine-tuning;
- seleção de modelos;
- tuning;
- avaliação;
- custo e latência;
- evidência experimental;
- reprodutibilidade.

### III — Intelligent Orchestration

Decisões sobre **quando, por que e como combinar capacidades**.

Inclui:

- model routing;
- reasoning routing;
- tool routing;
- execution routing;
- agent routing;
- quality gates;
- cascades;
- utility;
- políticas de escalonamento;
- sistemas compostos.

A **Aula 13C — Model Routing, Orchestration e Utility** é o ponto formal de transição entre Model Engineering e sistemas mais autônomos.

### IV — Agentic Systems

Sistemas capazes de planejar, usar ferramentas, agir sobre ambientes e executar fluxos com graus explícitos de autonomia.

Inclui:

- tool use;
- structured outputs;
- planning;
- state e memory operacional;
- workflows;
- RAG como componente de sistemas;
- computer use;
- agentes especializados;
- multi-agent systems quando justificados;
- avaliação de agentes;
- human oversight;
- segurança e governança.

## Cross-cutting Concerns

As seguintes dimensões atravessam todas as macrocamadas e não devem ser tratadas apenas como módulo final:

```text
Observability
Safety
Governance
Reproducibility
Cost
Latency
Evaluation
Human oversight
```

Quanto maior a autonomia do sistema, maior deve ser a exigência de observabilidade, controle e evidência.

## Evidence Architecture

O TIL mantém a separação:

```text
AUTHOR / EVIDENCE
→ experimentos treinam, executam e medem
→ produzem artefatos versionados

STUDENT
→ aulas consomem evidência pronta
→ executam rapidamente
→ interpretam
→ comparam
→ tomam decisões
```

Princípio:

> **Experimentos produzem evidência; aulas consomem evidência.**

Essa separação deve continuar válida para LLMs e agentes. A introdução de novas capacidades não justifica transformar notebooks educacionais em pipelines longos, caros ou difíceis de reproduzir.

## Transition Logic

A progressão conceitual recomendada é:

```text
Text
→ Features
→ Models
→ Evaluation
→ Model Selection
→ Routing
→ Orchestration
→ Tools
→ Execution
→ Agents
→ Agentic Systems
```

O aluno deve conseguir responder, em cada transição:

1. qual limitação da camada anterior está sendo atacada;
2. qual capacidade nova foi adicionada;
3. qual custo ou risco novo apareceu;
4. qual evidência justifica manter a complexidade adicional.

## Routing Taxonomy

A partir da Aula 13C, routing deixa de significar apenas escolha entre modelos.

### Model Routing
Escolher qual modelo deve processar uma entrada.

### Reasoning Routing
Escolher quanto raciocínio ou qual estratégia de raciocínio deve ser aplicada.

### Tool Routing
Escolher se e qual ferramenta externa deve ser acionada.

### Execution Routing
Escolher entre responder, consultar, executar, escalar ou solicitar supervisão.

### Agent Routing
Escolher qual agente, papel ou workflow deve assumir a próxima etapa.

Essa taxonomia cria a ponte entre classificação tradicional e sistemas agentes.

## Proposed Next Learning Sequence

A sequência abaixo é arquitetural e pode ser refinada antes da criação dos notebooks.

### Bloco A — LLM Foundations

Primeira unidade: **Aula 14 — LLM Foundations: da classificação à geração** (`Proposed`).

Especificação: `docs/curriculum/AULA-14-llm-foundations.md`.

Objetivo: entender o que muda quando o sistema passa de modelos discriminativos/encoders para modelos generativos.

Tópicos candidatos:

- modelos autoregressivos;
- tokens, contexto e geração;
- prompting;
- structured outputs;
- sampling;
- limitações e failure modes;
- custo e latência de geração.

### Bloco B — Retrieval and Grounding

Objetivo: separar conhecimento paramétrico, recuperação e geração.

Tópicos candidatos:

- embeddings de sentença;
- semantic search;
- retrieval;
- chunking;
- RAG;
- grounding;
- avaliação de recuperação e resposta.

### Bloco C — Tools and Workflows

Objetivo: introduzir ação externa antes de introduzir autonomia ampla.

Tópicos candidatos:

- function/tool calling;
- contratos de ferramenta;
- validação de argumentos;
- workflows determinísticos;
- estado;
- retries;
- idempotência;
- observabilidade.

### Bloco D — Agentic Systems

Objetivo: estudar autonomia como propriedade mensurável do sistema.

Tópicos candidatos:

- planning;
- agent loop;
- memory operacional;
- execution policies;
- human-in-the-loop;
- computer use;
- agentes especializados;
- multi-agent systems;
- avaliação de agentes.

## Evidence Gates for Complexity

Uma nova camada arquitetural só deve ser promovida quando o aluno conseguir comparar a solução mais simples com a solução mais complexa.

Exemplos:

```text
baseline clássico
vs
Transformer
```

```text
single model
vs
routing/cascade
```

```text
LLM sem retrieval
vs
RAG
```

```text
workflow determinístico
vs
agente autônomo
```

A comparação deve considerar, quando aplicável:

- qualidade;
- custo;
- latência;
- robustez;
- taxa de falha;
- necessidade de intervenção humana;
- risco;
- autonomia;
- reprodutibilidade.

## Relationship with Aula 13C

A Aula 13C permanece como laboratório de transição.

Ela ensina que o problema deixa de ser apenas:

> Qual modelo tem melhor métrica?

e passa a incluir:

> Qual sistema deve executar esta entrada, com qual capacidade, sob quais limites de custo, latência, risco e autonomia?

Por isso, a 13C é a fronteira pedagógica entre **Model Engineering** e **Intelligent Orchestration**, além de preparar a entrada em **Agentic Systems**.

## Non-goals

Esta especificação não:

- declara agentes superiores a workflows;
- obriga uso de frameworks específicos;
- define LangGraph, CrewAI ou qualquer biblioteca como padrão do curso;
- assume LLM-as-judge como verdade de referência;
- define uma função universal de utility;
- substitui experimentação por arquitetura conceitual.

## Decision Rule

Quando duas arquiteturas atingirem resultado pedagógico e operacional semelhante, preferir a mais simples.

```text
capacidade adicional
→ evidência adicional
→ complexidade justificada
```

Sem evidência suficiente:

```text
manter arquitetura mais simples
```
