# Aula 18 — Deterministic Workflows

Status: `Draft`

A Aula 18 é a segunda unidade do Bloco C — **Tools and Workflows**.

## Escopo

- tool vs workflow;
- deterministic orchestration;
- explicit workflow state;
- retries;
- retryable errors;
- idempotency;
- checkpoints;
- approval gates;
- recovery;
- workflow observability;
- workflow vs agent architecture decision.

## Laboratório

`TIL Lesson Release Workflow`:

```text
validate_release_request
→ get_lesson_status
→ build_release_note
→ approval_gate
→ publish_release_note
```

Inclui:

- happy path;
- falha transitória;
- retry;
- checkpoint;
- retomada;
- prevenção de duplicidade;
- aprovação negada;
- logs por etapa.

## Fora de escopo

- MCP operacional;
- frameworks agentes;
- LLM decidindo sequência livremente;
- APIs externas;
- side effects reais.

## Configuração

```text
Internet OFF
GPU OFF
sem API externa
sem side effects reais
```

## Gates antes de student-ready

- [x] especificação curricular;
- [x] notebook Draft;
- [x] novos conceitos no Glossário Vivo;
- [x] integração contextual do Glossário;
- [x] navegação anterior/home/próxima;
- [ ] PT-BR / EN / HTML regenerados;
- [ ] execução headless integral;
- [ ] warnings revisados;
- [ ] execução Kaggle;
- [ ] revisão pedagógica final.

Especificação: `docs/curriculum/AULA-18-deterministic-workflows.md`.
