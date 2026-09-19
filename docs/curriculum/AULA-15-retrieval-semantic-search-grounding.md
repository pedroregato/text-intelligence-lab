# Aula 15 — Retrieval, Semantic Search and Grounding

## Status

Draft

## Role in the TIL

A Aula 15 é a primeira unidade do bloco **Retrieval and Grounding**.

Ela parte da Aula 14, em que o aluno aprendeu como modelos generativos produzem texto, e introduz a pergunta seguinte:

> **Como localizar informação relevante antes de gerar uma resposta?**

A aula não ensina RAG ainda.

Sequência:

```text
14 — LLM Foundations
        ↓
15 — Retrieval, Semantic Search and Grounding
        ↓
16 — RAG
        ↓
Tools and Workflows
        ↓
Agentic Systems
```

## Central Principle

Retrieval e generation são capacidades diferentes.

```text
retrieval
→ localizar evidência

generation
→ produzir saída
```

RAG só deve aparecer depois que o aluno compreender cada componente separadamente.

## Learning Objectives

Ao final da aula, o aluno deverá ser capaz de:

1. explicar o que é retrieval;
2. distinguir busca lexical de busca semântica;
3. calcular similaridade cosseno entre consulta e documentos;
4. interpretar um ranking de resultados;
5. explicar o papel de embeddings em semantic search;
6. distinguir top-k de geração do top-k de retrieval;
7. explicar chunking em nível introdutório;
8. construir um conjunto pequeno de evidências recuperadas;
9. explicar grounding como vinculação da resposta à evidência disponível;
10. identificar situações em que retrieval falha mesmo sem geração;
11. reconhecer que recuperar informação relevante não garante resposta correta;
12. justificar quando retrieval acrescenta valor ao sistema.

## Prerequisites

- texto como dado;
- TF-IDF;
- embeddings;
- similaridade cosseno;
- métricas;
- LLM Foundations;
- custo, latência e utility.

## Scope

### 1. Retrieval

Retrieval é o processo de localizar itens relevantes para uma consulta dentro de uma coleção.

```text
query
→ representação
→ comparação com documentos
→ score
→ ranking
→ top-k resultados
```

### 2. Lexical Search

A primeira referência será TF-IDF + cosine similarity.

Objetivo: mostrar que termos compartilhados podem ser suficientes para várias tarefas.

### 3. Semantic Search

A aula deve mostrar que uma consulta e um documento podem ser semanticamente próximos mesmo sem compartilhar exatamente as mesmas palavras.

Para manter Internet OFF, a primeira versão utilizará **embeddings densos didáticos pré-computados**, explicitamente marcados como proxies pedagógicos e não como embeddings de um modelo real.

### 4. Ranking

O aluno deve observar:

- score;
- posição;
- top-k;
- resultados relevantes e irrelevantes;
- efeito da consulta sobre o ranking.

### 5. Chunking

Introdução conceitual:

- documento inteiro;
- segmentos menores;
- perda de contexto;
- excesso de contexto;
- overlap;
- custo do índice.

Não haverá ainda pipeline de RAG.

### 6. Grounding

Grounding será definido como o vínculo explícito entre uma resposta ou decisão e evidência recuperada.

Nesta aula, grounding será demonstrado **sem LLM**:

```text
query
→ retrieve
→ evidence pack
→ resposta determinística baseada apenas na evidência
```

Isso separa grounding de geração.

### 7. Failure Modes

A aula deve discutir pelo menos:

- consulta mal formulada;
- vocabulário incompatível;
- embedding inadequado;
- chunk incorreto;
- documento relevante ausente;
- ranking ruim;
- top-k insuficiente;
- top-k excessivo;
- evidência contraditória.

## Student Experiments

### Experiment A — Lexical retrieval

Coleção pequena de documentos.

- TF-IDF;
- cosine similarity;
- ranking;
- top-k.

### Experiment B — Semantic retrieval

Usar vetores densos didáticos pré-computados para mostrar proximidade semântica entre expressões lexicalmente diferentes.

O notebook deve declarar claramente:

> Os vetores são didáticos e não constituem benchmark de um embedding model real.

### Experiment C — Chunking

Comparar recuperação em:

- documento inteiro;
- chunks curtos.

Observar como granularidade muda o resultado.

### Experiment D — Grounded evidence pack

Selecionar os trechos mais relevantes e construir um pequeno pacote de evidência.

Não gerar uma resposta livre com LLM. O objetivo é compreender a interface entre retrieval e geração futura.

## Evidence Strategy

Primeira versão: **STUDENT MODE**.

São permitidos:

- corpus pequeno embutido no notebook;
- TF-IDF real;
- cosine similarity real;
- embeddings semânticos sintéticos explicitamente didáticos.

Não são permitidos como evidência real:

- scores sintéticos apresentados como benchmark;
- comparações entre embedding models que não tenham sido executadas;
- claims de superioridade de semantic search sem medição adequada.

Uma comparação futura entre métodos reais deverá nascer em experimento AUTHOR / EVIDENCE separado.

## What the Lesson Must Not Do

A Aula 15 não deve:

- ensinar geração autoregressiva novamente;
- construir pipeline RAG completo;
- chamar API de LLM;
- depender de vector database;
- depender de framework de agentes;
- confundir retrieval top-k com sampling top-k;
- apresentar embedding sintético como saída de modelo real;
- tratar cosine similarity como garantia de relevância;
- tratar grounding como garantia de factualidade.

## Glossary Gate

Antes de student-ready, registrar no Glossário Vivo:

- retrieval;
- information retrieval;
- query;
- lexical search;
- semantic search;
- ranking;
- retrieval score;
- top-k retrieval;
- chunk;
- chunking;
- overlap;
- grounding;
- evidence pack.

Reutilizar termos existentes:

- document;
- corpus;
- TF-IDF;
- embedding;
- cosine similarity;
- evidence.

## Notebook Design

Caminho:

```text
course/15-retrieval-semantic-search-grounding/
└── 15-til-retrieval-semantic-search-grounding.ipynb
```

Kaggle slug:

```text
til-15-retrieval-semantic-search-grounding
```

Configuração:

```text
Internet OFF
GPU OFF
sem API externa
```

## Suggested Lesson Flow

```text
1. Objetivos e ponte com a Aula 14
2. O que retrieval resolve
3. Query, corpus, score e ranking
4. Lexical retrieval com TF-IDF
5. Semantic search com vetores didáticos
6. Top-k de retrieval
7. Chunking
8. Grounding e evidence pack
9. Failure modes
10. Exercícios
11. Reprodutibilidade
12. Síntese
13. Ponte para RAG
```

## Exercises

### Exercise 1 — Rank documents

Dada uma consulta, calcular ranking TF-IDF e identificar os dois documentos mais relevantes.

Padrão:

```text
answer cell
→ hint
→ executable solution
```

### Exercise 2 — Lexical vs semantic

Comparar uma consulta com dois documentos e explicar por que lexical e semantic retrieval podem ordenar resultados de maneira diferente.

### Exercise 3 — Chunking

Dividir um texto em chunks por sentenças e observar qual chunk recebe maior score.

### Exercise 4 — Grounding

Dado um evidence pack, responder apenas com informação suportada pelos trechos recuperados e indicar qual trecho sustenta a resposta.

## Acceptance Criteria

Student-ready somente quando:

1. objectives explícitos;
2. retrieval separado conceitualmente de generation;
3. lexical retrieval executável;
4. semantic search demonstrado com proxy claramente identificado;
5. ranking e top-k observáveis;
6. chunking demonstrado;
7. grounding demonstrado sem LLM;
8. failure modes discutidos;
9. exercícios de código em answer → hint → solution;
10. Glossário Vivo atualizado;
11. Internet OFF;
12. execução headless completa;
13. execução Kaggle bem-sucedida;
14. warnings revisados;
15. revisão pedagógica concluída.

## Exit Condition

A aula estará completa quando o aluno conseguir explicar:

> **Retrieval encontra evidência; generation produz uma resposta. RAG combina essas capacidades, mas não deve esconder como cada uma funciona isoladamente.**

Essa compreensão é o gate para a Aula 16 — RAG.
