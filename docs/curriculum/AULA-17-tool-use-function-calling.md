# Aula 17 — Tool Use, Function Calling and Contracts

## Status

Available / student-ready

## Role in the TIL

A Aula 17 inicia formalmente o **Bloco C — Tools and Workflows**.

Progressão do bloco:

```text
Aula 17 — Tool Use, Function Calling and Contracts
→ Aula 18 — Deterministic Workflows
→ Aula 19 — Model Context Protocol (MCP)
→ Bloco D — Agentic Systems
```

A ordem é deliberada: primeiro entender o que é uma ferramenta e seu contrato; depois compor ferramentas em workflows; só então introduzir MCP como protocolo padronizado de integração.

## Central Question

> **Como um modelo deixa de apenas responder e passa a solicitar ações externas de forma estruturada, validável e observável?**

## Governing Principle

Tool use não deve ser tratado como “mágica do modelo”.

Uma tool deve ser entendida como um contrato explícito:

```text
name
+ description
+ input schema
+ validation
+ execution
+ result
+ error semantics
```

A complexidade adicional só se justifica quando a ação externa acrescenta capacidade necessária.

## Learning Objectives

Ao final da aula, o aluno deverá ser capaz de:

1. distinguir resposta textual de tool call;
2. explicar o papel de um contrato de ferramenta;
3. definir entradas estruturadas com schema;
4. validar argumentos antes da execução;
5. distinguir erro de decisão, validação e execução;
6. explicar efeitos colaterais e risco operacional;
7. implementar uma tool determinística simples;
8. observar chamada, argumentos, resultado e erro separadamente;
9. explicar quando uma função Python direta é suficiente;
10. preparar a base conceitual para workflows e MCP.

## Scope

### 1. From answer to action

Comparar resposta textual com solicitação estruturada de ação.

### 2. Tool contract

Introduzir:

- name;
- description;
- input schema;
- required fields;
- types;
- constraints;
- output contract;
- error contract.

### 3. Argument validation

Exemplos:

- campo ausente;
- tipo incorreto;
- valor fora do domínio;
- combinação inválida;
- argumento não permitido.

### 4. Deterministic execution

A primeira versão deve usar funções Python locais, pequenas e reproduzíveis, sem API externa obrigatória.

### 5. Tool result

Distinguir:

```text
tool request
→ tool execution
→ tool result
→ assistant response
```

### 6. Failure taxonomy

- tool selection failure;
- argument generation failure;
- validation failure;
- execution failure;
- result interpretation failure.

### 7. Side effects and safety

Distinguir:

```text
read-only
vs
state-changing
```

Introduzir approval gates sem ainda ensinar agentes.

### 8. Observability

Registrar, quando aplicável:

```text
tool_name
arguments
validation_status
execution_status
latency
result_summary
error_type
side_effect_class
```

## Student Lab

Construir um pequeno **TIL Tool Registry** com três ferramentas locais:

1. `lookup_glossary(term)`
2. `calculate_percentage(value, percent)`
3. `get_lesson_status(lesson_id)`

O aluno deverá inspecionar contratos, executar chamadas válidas, provocar chamadas inválidas e observar validação e erros.

## MCP Bridge

A Aula 17 **não ensina MCP ainda**, mas prepara explicitamente a ponte:

```text
função Python
→ tool estruturada
→ catálogo de tools
→ workflow
→ MCP server
```

Na Aula 19, tools, resources e prompts serão apresentados como primitivas expostas por um servidor MCP, dentro da arquitetura host/client/server e com atenção a discovery, authorization, segurança e governança.

## What the Lesson Must Not Do

A Aula 17 não deve:

- começar por frameworks agentes;
- introduzir MCP antes de tool contracts;
- depender de API proprietária;
- executar ações irreversíveis;
- esconder validação;
- confundir decisão do modelo com execução da ferramenta;
- tratar tool use como sinônimo de agentic system;
- exigir internet para o núcleo.

## Notebook Design

```text
course/17-tool-use-function-calling/
└── 17-til-tool-use-function-calling.ipynb
```

Kaggle slug:

```text
til-17-tool-use-function-calling-and-contracts
```

Configuração inicial:

```text
Internet OFF
GPU OFF
sem API externa
```

## Suggested Lesson Flow

```text
1. Objetivos
2. De resposta para ação
3. O que é uma tool
4. Tool contract
5. Input schema
6. Validation
7. Execution
8. Tool result
9. Failure taxonomy
10. Side effects e safety
11. Observability
12. TIL Tool Registry Lab
13. Exercícios
14. Reprodutibilidade
15. Síntese
16. Ponte para deterministic workflows
```

## Exercises

### Exercise 1 — Design a tool contract
Definir contrato para uma ferramenta de consulta.

### Exercise 2 — Break the schema
Produzir chamadas inválidas e explicar por que devem ser rejeitadas.

### Exercise 3 — Locate the failure
Dado um log de tool use, localizar seleção, argumento, validação, execução ou interpretação.

### Exercise 4 — Read-only or state-changing?
Classificar ferramentas por efeito e risco.

### Exercise 5 — Is a tool necessary?
Comparar resposta direta, função local e tool estruturada.

## Evidence Strategy

Modo inicial: **STUDENT**.

As tools serão locais, determinísticas e pequenas.

Experimentos futuros com modelos reais decidindo tool calls deverão seguir AUTHOR / EVIDENCE.

## Acceptance Criteria

Student-ready somente quando:

1. objetivos explícitos;
2. tool call separado de execução;
3. contratos observáveis;
4. validação executável;
5. erros por estágio demonstrados;
6. read-only vs state-changing discutido;
7. observabilidade incluída;
8. laboratório executável;
9. ponte para workflows explícita;
10. ponte para MCP explícita;
11. Glossário Vivo atualizado;
12. navegação anterior/home/próxima presente;
13. Internet OFF no núcleo;
14. execução headless completa;
15. warnings revisados;
16. execução Kaggle concluída;
17. revisão pedagógica concluída.

## Exit Condition

A aula estará completa quando o aluno conseguir explicar:

> **Uma tool não é apenas uma função chamada por um LLM. É uma capacidade externa exposta por um contrato, validada antes da execução, observada durante o uso e governada de acordo com seus efeitos e riscos.**

Essa compreensão prepara a Aula 18 — **Deterministic Workflows** e, posteriormente, a Aula 19 — **Model Context Protocol (MCP)**.
