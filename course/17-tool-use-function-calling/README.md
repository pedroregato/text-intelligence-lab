# Aula 17 — Tool Use, Function Calling and Contracts

Status: `Draft`

A Aula 17 inicia o Bloco C — **Tools and Workflows**.

## Escopo

- resposta textual vs tool call;
- tool contract;
- input schema;
- argument validation;
- deterministic execution;
- tool result vs assistant response;
- failure taxonomy;
- read-only vs state-changing;
- approval gates;
- tool observability;
- TIL Tool Registry;
- ponte para workflows e MCP.

## Laboratório

O notebook constrói um pequeno registro de ferramentas locais:

```text
lookup_glossary(term)
calculate_percentage(value, percent)
get_lesson_status(lesson_id)
```

Pipeline observável:

```text
tool request
→ selection
→ validation
→ execution
→ result
→ assistant response
```

Taxonomia de falhas:

```text
tool selection failure
argument generation failure
validation failure
execution failure
result interpretation failure
```

## Fora de escopo

- APIs proprietárias;
- frameworks agentes;
- MCP operacional;
- ações externas irreversíveis;
- side effects reais;
- LLM decidindo tool calls.

## Configuração

```text
Internet OFF
GPU OFF
sem API externa
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

Especificação: `docs/curriculum/AULA-17-tool-use-function-calling.md`.


## Architecture decision lab

O Exercício 5 foi ampliado para um laboratório de decisão arquitetural com oito cenários.

O aluno compara:

```text
direct_answer
direct_function
structured_tool
```

e justifica a escolha considerando:

- complexidade;
- determinismo;
- observabilidade;
- reutilização;
- risco;
- governança.

O objetivo é reforçar o princípio do TIL de escolher a arquitetura mínima suficiente e exigir evidência antes de adicionar complexidade.
