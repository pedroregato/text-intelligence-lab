# Aula 14 — LLM Foundations: da classificação à geração

## Status

Proposed

## Role in the TIL

A Aula 14 será a primeira unidade após a Aula 13C e inaugura o bloco **LLM Foundations** da arquitetura `TIL-AIE-001`.

Ela não começa por RAG, agentes ou frameworks. Seu objetivo é estabelecer a mudança conceitual mínima necessária para o aluno compreender sistemas generativos antes de adicionar retrieval, tools ou autonomia.

Sequência:

```text
Aula 13C
Model Routing / Orchestration / Utility
        ↓
Aula 14
LLM Foundations
        ↓
Retrieval and Grounding
        ↓
Tools and Workflows
        ↓
Agentic Systems
```

## Central Question

A pergunta da aula é:

> **O que muda quando deixamos de apenas classificar ou representar texto e passamos a gerar texto token a token?**

## Pedagogical Principle

A aula deve preservar o princípio:

> **Complexidade arquitetural precisa ser conquistada por evidência.**

Portanto, a Aula 14 não deve transmitir a ideia de que um LLM substitui automaticamente classificadores, encoders ou pipelines clássicos.

O aluno deve aprender a distinguir:

```text
capacidade nova
≠
substituição automática
```

## Learning Objectives

Ao final da aula, o aluno deverá ser capaz de:

1. explicar a diferença entre um modelo discriminativo e um modelo autoregressivo;
2. descrever geração como previsão sequencial do próximo token;
3. explicar o papel de tokens, contexto e janela de contexto;
4. distinguir logits, probabilidades e estratégia de sampling em nível conceitual;
5. explicar como temperature e top-k/top-p alteram comportamento de geração;
6. distinguir saída livre de saída estruturada;
7. identificar failure modes básicos de geração;
8. relacionar geração a custo, latência e risco;
9. justificar quando um modelo generativo acrescenta valor a uma tarefa;
10. reconhecer quando uma solução mais simples continua suficiente.

## Prerequisites

Conhecimentos esperados:

- tokenização;
- probabilidades básicas;
- classificação supervisionada;
- métricas;
- Transformers em nível introdutório;
- custo e latência;
- noção de utility;
- distinção entre modelo isolado e sistema composto.

Dependências curriculares principais:

```text
Aula 2
→ tokenização

Aulas 5–7
→ classificação e avaliação

Aulas 10–11
→ Transformers

Aulas 13–13C
→ métricas, custo, routing e utility
```

## Scope

### 1. Classificar não é gerar

Comparação conceitual:

```text
Classificador
entrada → representação → classe

Modelo autoregressivo
contexto → próximo token
        → novo contexto
        → próximo token
        → ...
```

A aula deve mostrar que ambos são modelos probabilísticos, mas respondem a problemas diferentes.

### 2. Next-token prediction

Introduzir:

- distribuição sobre o vocabulário;
- logits;
- softmax em nível conceitual;
- seleção do próximo token;
- repetição do processo.

Não é necessário derivar toda a matemática do Transformer novamente.

### 3. Tokens and Context

Explorar:

- token não é necessariamente palavra;
- prompt como parte do contexto;
- sequência acumulada;
- janela de contexto;
- efeito de contexto insuficiente ou excessivo.

### 4. Determinism and Sampling

Introduzir de forma visual e experimental:

- greedy decoding;
- temperature;
- top-k;
- top-p;
- seed quando suportada;
- determinismo vs diversidade.

A aula deve evitar apresentar parâmetros de geração como “botões mágicos”.

### 5. Structured Outputs

Mostrar a diferença entre:

```text
texto livre
vs
estrutura esperada
```

Exemplos possíveis:

- JSON;
- categorias tipadas;
- campos obrigatórios;
- validação pós-geração.

Este tópico prepara Tool Calling sem ainda introduzi-lo.

### 6. Failure Modes

Introduzir pelo menos:

- resposta plausível mas incorreta;
- instrução ambígua;
- perda de restrições;
- formato inválido;
- sensibilidade ao contexto;
- variabilidade de saída;
- custo excessivo;
- latência.

Evitar tratar “hallucination” como categoria única para todos os erros.

### 7. Utility of Generation

Retomar a função conceitual da Aula 13C:

```text
utility = f(qualidade, custo, latência, risco, autonomia)
```

Nesta aula, autonomia ainda deve permanecer baixa. O foco é **capacidade generativa**, não agente.

## Proposed Student Experiments

A aula deve preferir experimentos pequenos e observáveis.

### Experiment A — Próximo token

Apresentar uma distribuição pequena e didática de candidatos ao próximo token.

Objetivo:

- visualizar logits/probabilidades;
- escolher greedy;
- comparar com sampling.

Este experimento pode ser inteiramente local e determinístico.

### Experiment B — Temperature

Usar uma distribuição fixa e variar temperature.

O aluno observa:

- concentração da distribuição;
- diversidade;
- estabilidade.

Não é necessário chamar uma API externa.

### Experiment C — Structured output validation

Fornecer exemplos de saídas gerativas e um schema simples.

O aluno deve:

- identificar saída válida/inválida;
- validar estrutura;
- perceber que geração e validação são etapas diferentes.

### Experiment D — Task Fit

Comparar três tipos de problema:

1. classificação fechada;
2. extração estruturada;
3. geração aberta.

O aluno decide que tipo de capacidade é necessária e justifica a escolha.

Este exercício reforça que LLM não é escolha automática.

## Evidence Strategy

A Aula 14 deve iniciar em **STUDENT MODE**.

Não é necessário treinar um LLM.

A primeira versão pode utilizar:

- distribuições sintéticas explicitamente didáticas para sampling;
- exemplos estáticos para structured output;
- evidência versionada quando houver comparação real de custo/latência de geração.

Qualquer benchmark real futuro deve vir de experimento AUTHOR / EVIDENCE separado.

Regra:

```text
experimento autoral
→ mede comportamento/custo/latência
→ versiona evidência

Aula 14
→ consome evidência
→ interpreta
```

## What the Lesson Must Not Do

A Aula 14 não deve:

- ensinar RAG antes de explicar geração;
- introduzir agentes;
- ensinar frameworks de orquestração;
- depender de API proprietária para completar `Run All`;
- exigir internet para seu núcleo pedagógico;
- usar resultados de marketing como evidência técnica;
- sugerir que prompting elimina necessidade de avaliação;
- transformar temperature em sinônimo de “criatividade” sem ressalvas;
- comparar custos de modelos diferentes sem metodologia explícita.

## Glossary Gate

Antes de a aula ser marcada como student-ready, o Glossário Vivo deve conter, no mínimo:

- Large Language Model / LLM;
- autoregressive model;
- prompt;
- context;
- context window;
- logits;
- sampling;
- temperature;
- top-k;
- top-p;
- greedy decoding;
- structured output;
- generation;
- hallucination ou termo equivalente tratado com definição cuidadosa.

Termos já existentes devem ser reutilizados; não criar duplicatas semânticas.

Após atualizar `docs/glossary/glossary.yaml`, regenerar:

```text
glossary.pt-BR.md
glossary.en.md
docs/glossary/web/index.html
```

## Notebook Design

Nome canônico proposto:

```text
course/14-llm-foundations/
└── 14-til-llm-foundations.ipynb
```

Kaggle slug proposto:

```text
til-14-llm-foundations
```

Internet:

```text
OFF por padrão
```

A primeira versão deve ser executável sem API externa.

## Suggested Lesson Flow

```text
1. Objetivos
2. De classificação para geração
3. Próximo token
4. Tokens e contexto
5. Sampling e determinismo
6. Structured outputs
7. Failure modes
8. Custo, latência e utility
9. Exercícios
10. Reprodutibilidade
11. Síntese
12. Ponte para Retrieval and Grounding
```

## Exercise Ideas

### Exercise 1 — Greedy vs sampling

Dada uma distribuição de probabilidades, identificar:

- token greedy;
- candidatos possíveis sob top-k;
- impacto esperado de temperature.

### Exercise 2 — Context reasoning

Analisar dois prompts com diferentes quantidades de contexto e discutir:

- informação necessária;
- ruído;
- custo;
- risco de interpretação.

### Exercise 3 — Validate structured output

Implementar uma validação simples em Python para um objeto esperado.

Padrão obrigatório:

```text
answer cell
→ hint
→ executable solution
```

### Exercise 4 — Choose the simplest adequate architecture

Para diferentes tarefas, escolher entre:

- regra;
- classificador;
- encoder/Transformer;
- LLM generativo.

A resposta deve justificar a capacidade necessária, sem ranking universal.

## Acceptance Criteria

A Aula 14 só poderá ser marcada como student-ready quando:

1. objetivos estiverem explícitos;
2. a mudança discriminativo → autoregressivo estiver clara;
3. houver ao menos um experimento visual de distribuição/sampling;
4. structured output estiver separado de texto livre;
5. failure modes forem tratados;
6. custo e latência forem conectados à geração;
7. houver pelo menos um exercício de decisão arquitetural;
8. exercícios de código seguirem answer → hint → executable solution;
9. Glossário Vivo estiver atualizado;
10. notebook executar headless;
11. notebook executar com sucesso no Kaggle;
12. internet não for necessária para o núcleo da aula;
13. warnings forem revisados;
14. revisão pedagógica em perspectiva de aluno estiver concluída.

## Exit Condition

A Aula 14 estará pedagogicamente completa quando o aluno conseguir explicar:

> **Por que um LLM consegue fazer algo que um classificador não foi projetado para fazer — e por que isso não significa que devemos usar um LLM para tudo?**

Essa compreensão é o gate para avançar para **Retrieval and Grounding**.
