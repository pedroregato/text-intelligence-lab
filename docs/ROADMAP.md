# TIL Curriculum Roadmap

## Estado atual

### Macrocamada I — Text Intelligence

Fundamentos para transformar texto em dados, representações, features e tarefas mensuráveis.

- Aula 0 — Como o TIL funciona
- Aula 1 — Texto como dado
- Aula 2 — Tokenização e normalização
- Aula 3 — Bag-of-Words
- Aula 4 — TF-IDF
- Aula 5 — Primeiro classificador de textos
- Aula 6 — Avaliação de classificadores
- Aula 7 — Seleção de modelos e tuning
- Aula 8 — N-grams e engenharia de features textuais
- Aula 9 — Word Embeddings

### Macrocamada II — Model Engineering

Construção, comparação e avaliação de modelos sob condições explícitas.

- Aula 10 — Embeddings contextuais e Transformers
- Aula 11 — BERT para classificação de texto
- Aula 12 — Baselines fortes: Naive Bayes, Logistic Regression e LinearSVC
- Aula 13 — Métricas e Indicadores: da fórmula à decisão
- Aula 13B — Metric Scenario Lab: cenários, thresholds e custos de erro

Evidência disponível:

```text
EDU-ORCH-001
→ TF-IDF + MultinomialNB
vs
DistilBERT multilingual
→ quality + latency + runtime proxy
→ data/model-evidence/til-model-evidence.csv
```

### Macrocamada III — Intelligent Orchestration

- Aula 13C — Model Routing, Orchestration e Utility: sistemas compostos de IA

A Aula 13C é o ponto formal de transição entre **Model Engineering** e sistemas com maior capacidade de orquestração.

Ela já consome duas camadas de evidência:

```text
EDU-ORCH-001
→ modelos isolados medidos
→ til-model-evidence.csv

EDU-ORCH-002
→ routing/cascade medido
→ til-routing-evidence.csv
→ evidence_status = measured-recovered
```

O fallback `DEMO` permanece apenas para manter a aula executável quando os artefatos não estiverem disponíveis. Ele não substitui nem reclassifica evidência medida.

Arquitetura pedagógica adotada:

```text
AUTHOR / EVIDENCE
→ experimentos treinam e medem
→ produzem evidência

STUDENT
→ aulas consomem evidência pronta
→ execução rápida
→ interpretação e decisão
```

Princípio:

> **Experimentos produzem evidência; aulas consomem evidência.**

## Próximo movimento curricular

O próximo passo não é adicionar complexidade por sequência tecnológica. É avançar para novas capacidades somente quando houver uma pergunta pedagógica e uma evidência que justifiquem a transição.

A especificação arquitetural está em:

`docs/architecture/TIL-AIE-001-agentic-intelligence-evolution.md`

Princípio central:

> **Complexidade arquitetural precisa ser conquistada por evidência.**

O TIL não assume que:

```text
Transformer > ML clássico
LLM > Transformer
agente > LLM
```

A progressão passa a seguir:

```text
Text Intelligence
→ Model Engineering
→ Intelligent Orchestration
→ Agentic Systems
```

com observabilidade, segurança, governança, avaliação, custo, latência e supervisão humana atravessando todas as etapas.

## Sequência arquitetural proposta

A numeração das próximas aulas será definida quando cada unidade estiver suficientemente especificada. A ordem conceitual proposta é:

### Bloco A — LLM Foundations

**Próxima unidade oficial: Aula 14 — LLM Foundations: da classificação à geração**  
Status: `Available`  
Especificação: `docs/curriculum/AULA-14-llm-foundations.md`

Objetivo: entender o que muda quando o sistema passa de modelos discriminativos/encoders para modelos generativos, sem assumir que a capacidade generativa substitui automaticamente soluções mais simples.

A Aula 14 deve cobrir:

- modelos autoregressivos;
- next-token prediction;
- tokens, contexto e janela de contexto;
- logits e probabilidades em nível conceitual;
- greedy decoding e sampling;
- temperature, top-k e top-p;
- structured outputs;
- failure modes;
- custo, latência e utility da geração.

O núcleo da primeira versão deve ser executável com `Internet OFF` e sem API proprietária. Retrieval, RAG, tools e agentes ficam explicitamente para blocos posteriores.

### Bloco B — Retrieval and Grounding

**Próxima unidade oficial: Aula 15 — Retrieval, Semantic Search and Grounding**  
Status: `Available`  
Especificação: `docs/curriculum/AULA-15-retrieval-semantic-search-grounding.md`

Objetivo: separar retrieval de generation antes de construir RAG.

A Aula 15 cobre:

- query, corpus, score e ranking;
- lexical retrieval com TF-IDF;
- semantic search;
- cosine similarity;
- top-k de retrieval;
- chunking;
- grounding;
- evidence pack;
- failure modes de retrieval.

A primeira versão usa `Internet OFF`, TF-IDF real e vetores semânticos didáticos explicitamente marcados como proxies.

### Aula 16 — Retrieval-Augmented Generation (RAG)

Status: `Proposed`  
Especificação: `docs/curriculum/AULA-16-rag.md`

A Aula 16 combinará as capacidades estudadas separadamente nas Aulas 14 e 15:

```text
generation
+
retrieval + grounding
=
RAG
```

O foco será tornar observáveis retrieval, evidence pack, context construction, grounded answer, attribution e failure localization, sem depender inicialmente de API externa ou framework de RAG.

### Bloco C — Tools and Workflows

Objetivo: introduzir ação externa antes de autonomia ampla.

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

Objetivo: tratar autonomia como propriedade mensurável.

Tópicos candidatos:

- planning;
- agent loop;
- memory operacional;
- execution policies;
- human-in-the-loop;
- computer use;
- agentes especializados;
- multi-agent systems quando justificados;
- avaliação de agentes.

## Taxonomia de Routing

A partir da Aula 13C, routing deixa de significar apenas escolha entre modelos.

```text
Model Routing
→ qual modelo?

Reasoning Routing
→ quanto/qual raciocínio?

Tool Routing
→ qual ferramenta?

Execution Routing
→ responder, consultar, executar ou escalar?

Agent Routing
→ qual agente ou workflow?
```

Essa taxonomia é a ponte curricular entre classificação tradicional, sistemas compostos e sistemas agentes.

## Evidence Gates

Cada aumento de complexidade deve permitir uma comparação explícita com uma alternativa mais simples.

Exemplos futuros:

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

As comparações devem considerar, quando aplicável:

- qualidade;
- custo;
- latência;
- robustez;
- taxa de falha;
- necessidade de intervenção humana;
- risco;
- autonomia;
- reprodutibilidade.

## Trilhas aplicadas

Os seguintes tópicos continuam planejados e serão encaixados na macroarquitetura conforme seus pré-requisitos pedagógicos:

### Tarefas aplicadas de NLP

- NER
- topic modeling
- similaridade textual
- recuperação de informação
- sumarização
- QA
- multilabel classification

### Sequências históricas e fundamentos

- RNN
- LSTM / GRU
- limitações de processamento sequencial
- por que atenção e Transformers mudaram o cenário

Esses tópicos não precisam necessariamente preceder toda a trilha moderna, mas devem aparecer quando ajudarem o aluno a compreender a evolução arquitetural.

### Engenharia transversal

- serving
- APIs
- batching
- custo e latência
- observabilidade
- drift
- experiment tracking
- governança
- segurança

### Avaliação generativa

- BLEU / ROUGE em contexto
- avaliação humana
- rubricas
- LLM-as-judge com cautela
- testes de regressão

### Capstone Kaggle

- competição ou problema real
- baseline
- experimentação
- leaderboard
- relatório final
- post-mortem técnico

## Regra de decisão

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
