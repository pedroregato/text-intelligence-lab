# Aula 17 — Tool Use, Function Calling and Contracts

Status: `Candidate — final validation pending`

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
- [x] revisão pedagógica final.

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


## Glossário Vivo integrado

A Aula 17 passou a usar o Glossário Vivo no próprio fluxo pedagógico, não apenas como lista de termos.

Integrações incluídas:

- barra inicial de conceitos com links clicáveis;
- links contextuais em Tool Contract;
- links contextuais em Input Schema;
- links em Side Effects e Approval Gate;
- link em Tool Observability;
- revisão de conceitos antes da ponte para MCP.

Isso mantém o glossário como recurso ativo de aprendizagem ao longo da aula.


## Validação técnica da versão candidata

Validação realizada em 2026-09-20:

- estrutura do notebook: PASS;
- IDs de células únicos: PASS;
- navegação no último bloco: PASS;
- outputs canônicos limpos: PASS;
- Tool Registry: PASS;
- argument validation: PASS;
- failure taxonomy paths: PASS;
- observability paths: PASS;
- architecture decision lab: PASS;
- Living Glossary contextual integration: PASS;
- caminhos de código executáveis: PASS.

Pendente antes de `Available / student-ready`:

- execução integral da versão candidata no Kaggle;
- execução headless integral do arquivo canônico em ambiente notebook;
- revisão final dos warnings de execução.


## Revisão pedagógica final

Status: PASS

Critérios revisados:

- progressão de resposta → tool request → validation → execution → result;
- separação entre tool result e assistant response;
- contratos e schemas apresentados antes de workflows/MCP;
- failure taxonomy explícita;
- distinção entre validação estrutural e erro semântico de argumentos;
- side effects e approval gates introduzidos antes de ações reais;
- observabilidade por estágio;
- exercício de decisão arquitetural com solução mínima suficiente;
- integração contextual com o Glossário Vivo;
- ponte para MCP sem confundir MCP com agente.

A aula está pedagogicamente pronta para promoção assim que os gates de execução final forem concluídos.
