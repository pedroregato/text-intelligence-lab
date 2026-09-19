# Aula 15 — Retrieval, Semantic Search and Grounding

Status: `Draft`

Esta aula inaugura o bloco Retrieval and Grounding do TIL e mantém retrieval separado de generation antes da introdução de RAG.

## Escopo

- query, corpus, score e ranking;
- lexical retrieval com TF-IDF;
- cosine similarity;
- semantic search com vetores didáticos;
- top-k de retrieval;
- chunking;
- grounding;
- evidence pack;
- failure modes de retrieval.

## Fora de escopo

- RAG completo;
- LLM;
- vector database;
- agentes;
- APIs externas.

## Configuração

```text
Internet OFF
GPU OFF
```

## Gates antes de student-ready

- [x] Glossário Vivo atualizado;
- [x] PT-BR / EN / HTML regenerados;
- [x] execução headless integral;
- [x] warnings revisados;
- [ ] execução Kaggle;
- [x] revisão pedagógica final.

Especificação: `docs/curriculum/AULA-15-retrieval-semantic-search-grounding.md`.


## Headless validation — 2026-09-19

O notebook canônico da `main` foi executado integralmente com `nbconvert ExecutePreprocessor`.

Resultado:

```text
34 células
→ COMPLETE
→ 0 erros
→ 0 warnings do notebook
```

A execução confirmou:

- lexical retrieval com TF-IDF;
- cosine similarity;
- ranking e top-k;
- semantic search com vetores didáticos;
- chunking;
- evidence pack;
- grounding determinístico;
- soluções executáveis dos exercícios.

## Pedagogical review — PASS

A revisão em perspectiva de aluno confirmou:

- ponte clara entre Aula 14 e retrieval;
- retrieval separado de generation;
- distinção explícita entre lexical search e semantic search;
- vetores semânticos identificados como proxies didáticos;
- top-k de retrieval diferenciado de top-k de geração;
- chunking introduzido antes de RAG;
- grounding demonstrado sem LLM;
- failure modes discutidos;
- exercícios coerentes e progressivos;
- Glossário Vivo integrado;
- seção de reprodutibilidade;
- ponte explícita para a futura Aula 16 — RAG.

A aula permanece `Draft` até a execução oficial no Kaggle.
