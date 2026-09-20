# Aula 16 — Retrieval-Augmented Generation (RAG)

Status: `Draft`

Esta aula combina as capacidades estudadas separadamente nas Aulas 14 e 15:

```text
generation
+
retrieval + grounding
=
RAG
```

## Escopo

- generation-only baseline;
- retrieval;
- evidence pack;
- context construction;
- grounded answer;
- source attribution;
- top-k sensitivity;
- insufficient evidence;
- retrieval/context/generation/attribution failures;
- laboratório de diagnóstico por estágio com logs de retrieval, contexto, resposta e fonte;
- factuality versus groundedness;
- governança da evidência, freshness e authority level;
- utility e trade-offs.

## Fora de escopo

- APIs externas;
- vector databases;
- LangChain / LlamaIndex;
- agentes;
- LLM-as-judge.

## Configuração

```text
Internet OFF
GPU OFF
```

## Gates antes de student-ready

- [x] especificação curricular;
- [x] notebook Draft;
- [x] Glossário Vivo atualizado;
- [x] PT-BR / EN / HTML regenerados;
- [x] navegação anterior/home/próxima incluída;
- [ ] execução headless integral;
- [ ] warnings revisados;
- [ ] execução Kaggle;
- [ ] revisão pedagógica final.

Especificação: `docs/curriculum/AULA-16-rag.md`.


## Logic validation — 2026-09-20

Os componentes determinísticos centrais foram executados em sequência fora da interface do notebook.

Resultado:

```text
status: PASS
retrieval top-1: C1
grounded answer source: C1
grounded answer: true
missing-evidence source: None
missing-evidence grounded: false
```

A validação também detectou e corrigiu um caso de attribution inadequada: uma evidência irrelevante recuperada não deve ser apresentada como fonte de uma resposta sem suporte.

Essa validação lógica não substitui o gate de execução headless integral do `.ipynb` nem a execução oficial no Kaggle.


## Failure diagnosis lab — 2026-09-20

A Aula 16 foi enriquecida com cenários concretos e um mini laboratório de diagnóstico.

Novos elementos:

```text
retrieval log
→ context log
→ answer
→ source
→ failure diagnosis
```

Casos cobertos:

- retrieval encontra os itens errados;
- retrieval encontra C1, mas C1 desaparece na construção do contexto;
- contexto contém C1, mas a geração contradiz C1;
- resposta está correta, mas não preserva attribution.

Validação lógica:

```text
A → retrieval failure   PASS
B → context failure     PASS
C → generation failure  PASS
D → attribution failure PASS
```

A versão anterior da Aula 16 já havia executado com sucesso no Kaggle. Como o notebook foi enriquecido depois dessa execução, a versão atualizada deve passar por um novo `Run All` antes de ser promovida para `Available`.


## Factuality and evidence governance — 2026-09-20

A Aula 16 agora explicita que:

```text
groundedness != factuality
```

Novo cenário diagnóstico:

```text
retrieval      = OK
context        = OK
generation     = OK
attribution    = OK
factuality     = FAIL
governance     = FAIL
```

O caso usa uma política antiga `POL-2024` com `status = superseded` e uma política vigente `POL-2026` com `status = active` e `authority_level = official`.

Metadados introduzidos:

- `source_owner`;
- `version`;
- `effective_date`;
- `last_reviewed_at`;
- `authority_level`;
- `status`.

O laboratório de diagnóstico passa a ter cinco casos:

```text
A → retrieval failure
B → context failure
C → generation failure
D → attribution failure
E → factuality failure
```

Como essa melhoria altera o notebook após a última execução Kaggle, a versão atualizada precisa de novo `Run All` antes da promoção para `Available`.
