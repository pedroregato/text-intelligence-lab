# Aula 16 — Retrieval-Augmented Generation (RAG)

## Status

Draft

## Role in the TIL

A Aula 16 combina duas capacidades que já foram estudadas separadamente:

```text
Aula 14
→ generation

Aula 15
→ retrieval + grounding

Aula 16
→ Retrieval-Augmented Generation (RAG)
```

O objetivo não é apresentar RAG como um framework ou padrão mágico, mas como uma arquitetura composta cuja utilidade deve ser observada e medida.

## Central Question

> **Como combinar retrieval e generation sem perder rastreabilidade da evidência?**

## Governing Principle

RAG só acrescenta valor quando o componente de retrieval fornece contexto útil à geração.

Portanto:

```text
RAG
≠
LLM + vector database por definição

RAG
=
retrieval
+ evidence selection
+ context construction
+ generation
+ grounding / attribution
+ evaluation
```

A arquitetura deve permanecer alinhada ao princípio do TIL:

> **Complexidade arquitetural precisa ser conquistada por evidência.**

## Learning Objectives

Ao final da aula, o aluno deverá ser capaz de:

1. explicar a arquitetura básica de um pipeline RAG;
2. distinguir retrieval quality de generation quality;
3. montar um contexto a partir de evidências recuperadas;
4. explicar por que uma resposta pode falhar mesmo quando o retrieval funciona;
5. explicar por que retrieval ruim pode comprometer uma boa geração;
6. distinguir grounded answer de resposta apenas plausível;
7. identificar retrieval failure, context failure e generation failure;
8. observar o efeito de top-k e seleção de evidência sobre a resposta;
9. explicar a importância de citar ou rastrear a fonte usada;
10. justificar quando RAG é preferível a generation-only;
11. reconhecer quando RAG não é necessário;
12. relacionar RAG a custo, latência, risco e utility.

## Prerequisites

- Aula 14 — LLM Foundations;
- Aula 15 — Retrieval, Semantic Search and Grounding;
- TF-IDF;
- embeddings;
- cosine similarity;
- ranking;
- chunking;
- grounding;
- structured output;
- utility.

## Architecture

A forma mínima ensinada será:

```text
query
  ↓
retrieval
  ↓
ranked evidence
  ↓
context construction
  ↓
generator
  ↓
grounded answer
  ↓
evaluation
```

Cada etapa deverá ser observável separadamente.

## Scope

### 1. Generation-only baseline

Antes do RAG, a aula deve mostrar uma resposta produzida sem contexto recuperado.

O objetivo é estabelecer um baseline conceitual:

```text
query
→ generator
→ answer
```

### 2. Retrieval

Reutilizar o mecanismo da Aula 15:

- query;
- corpus;
- score;
- ranking;
- top-k;
- evidence pack.

### 3. Context Construction

Transformar evidências recuperadas em um contexto explícito.

Exemplo:

```text
SYSTEM / INSTRUCTION
Use apenas a evidência fornecida.

EVIDENCE
[C1] ...
[C2] ...

QUESTION
...
```

O contexto deve permanecer visível ao aluno.

### 4. Generator

A primeira versão da aula não precisa depender de API externa.

A abordagem preferida é usar um **gerador didático determinístico** ou um conjunto de respostas pré-definidas controladas para ensinar a arquitetura antes de introduzir um LLM real.

Se um modelo real for incorporado futuramente, deverá obedecer à política AUTHOR / EVIDENCE.

### 5. Grounded Answer

A resposta deve:

- usar apenas informação presente no evidence pack;
- manter referência ao trecho usado;
- sinalizar ausência de evidência quando necessário.

### 6. Failure Taxonomy

Separar falhas por estágio.

#### Retrieval failure

O documento correto não foi recuperado.

#### Context construction failure

A evidência correta foi recuperada, mas organizada de forma inadequada.

#### Generation failure

O contexto contém a resposta, mas a saída gerada ignora, distorce ou extrapola a evidência.

#### Attribution failure

A resposta pode estar correta, mas não há rastreabilidade da fonte usada.

Essa taxonomia é importante para observabilidade futura.

### 7. Generation-only vs RAG

A comparação deve perguntar:

```text
generation-only
vs
retrieval + grounding + generation
```

Não declarar RAG superior por princípio.

A comparação deve considerar:

- qualidade;
- cobertura da evidência;
- groundedness;
- custo;
- latência;
- risco;
- complexidade.

## Student Experiments

### Experiment A — Generation-only

Uma consulta cuja resposta depende de informação presente apenas no corpus didático.

O aluno observa que, sem evidência, o sistema não deveria afirmar informação específica.

### Experiment B — Retrieve then answer

Reutilizar lexical retrieval da Aula 15.

```text
query
→ top-k
→ evidence pack
→ grounded answer
```

### Experiment C — Top-k sensitivity

Comparar:

- top-k = 1;
- top-k = 2;
- top-k = 3.

Observar:

- contexto suficiente;
- contexto irrelevante;
- redundância;
- risco de conflito.

### Experiment D — Missing evidence

A consulta não possui resposta no corpus.

O comportamento esperado deve ser:

```text
evidence insufficient
→ abstain / sinalizar ausência
```

### Experiment E — Failure localization

Fornecer cenários observáveis por estágio:

1. trecho correto não recuperado;
2. trecho correto recuperado, mas removido na construção do contexto;
3. contexto correto, mas geração incompatível com a evidência;
4. resposta correta sem atribuição da fonte.

O aluno deve localizar **o primeiro estágio em que a evidência correta deixou de ser preservada**.

A aula deve incluir um mini laboratório com logs explícitos de:

- `retrieved_ids`;
- `context_ids`;
- resposta;
- fonte atribuída;
- diagnóstico esperado.

O objetivo é preparar o aluno para observabilidade de sistemas de IA, evitando o diagnóstico genérico “o RAG errou”.

## Evidence Strategy

A primeira versão será **STUDENT MODE**.

Permitido:

- corpus local pequeno;
- retrieval real com TF-IDF;
- cosine similarity real;
- gerador didático determinístico;
- resultados totalmente reproduzíveis.

Não permitido como evidência real:

- afirmar superioridade de RAG a partir de exemplos sintéticos;
- tratar respostas pré-definidas como benchmark de LLM;
- comparar fornecedores/modelos sem execução medida.

Experimentos futuros com LLM real devem seguir:

```text
AUTHOR / EVIDENCE
→ executar
→ medir
→ versionar evidência

STUDENT
→ consumir
→ interpretar
```

## What the Lesson Must Not Do

A Aula 16 não deve:

- começar por LangChain, LlamaIndex ou outro framework;
- exigir vector database;
- exigir API externa;
- esconder retrieval dentro de um helper opaco;
- tratar grounding como garantia de verdade;
- tratar top-k maior como automaticamente melhor;
- confundir ausência de evidência com erro do gerador;
- usar LLM-as-judge como referência absoluta;
- introduzir agentes.

## Glossary Gate

Antes de student-ready, o Glossário Vivo deve conter, quando ainda não existirem:

- Retrieval-Augmented Generation / RAG;
- generation-only;
- context construction;
- grounded answer;
- groundedness;
- attribution;
- citation / source attribution;
- retrieval failure;
- context failure;
- generation failure;
- abstention;
- insufficient evidence.

Reutilizar conceitos existentes:

- retrieval;
- query;
- ranking;
- top-k retrieval;
- chunking;
- grounding;
- evidence pack;
- generation;
- structured output;
- utility.

## Notebook Design

Caminho proposto:

```text
course/16-rag/
└── 16-til-retrieval-augmented-generation.ipynb
```

Kaggle slug:

```text
til-16-retrieval-augmented-generation
```

Configuração inicial:

```text
Internet OFF
GPU OFF
sem API externa
```

## Navigation

A aula deve nascer já integrada ao padrão oficial:

```text
← Aula 15
| Apresentação do curso |
Próxima aula →
```

A ordem e os links devem ser mantidos em:

`course/navigation.json`

e sincronizados por:

`scripts/sync_course_navigation.py`

## Suggested Lesson Flow

```text
1. Objetivos
2. Por que RAG existe
3. Generation-only baseline
4. Retrieval
5. Context construction
6. Grounded generation
7. Attribution
8. Top-k sensitivity
9. Missing evidence
10. Failure localization
11. Utility e trade-offs
12. Exercícios
13. Reprodutibilidade
14. Síntese
15. Ponte para Tools and Workflows
```

## Exercises

### Exercise 1 — Build the evidence context

Transformar um evidence pack em contexto estruturado.

### Exercise 2 — Compare top-k

Executar retrieval com diferentes valores de k e discutir efeito sobre o contexto.

### Exercise 3 — Should the system answer?

Dado um retrieval score e evidence pack vazio/inadequado, decidir entre:

- responder;
- sinalizar evidência insuficiente;
- ampliar busca.

### Exercise 4 — Locate the failure

Classificar cenários como:

- retrieval failure;
- context failure;
- generation failure;
- attribution failure.

Além da associação conceitual, o notebook deve apresentar um laboratório de diagnóstico em que o aluno inspeciona logs do pipeline e justifica a classificação com base na trajetória da evidência.

### Exercise 5 — Architecture decision

Comparar duas tarefas:

1. pergunta sobre informação estática que já está explicitamente na entrada;
2. pergunta sobre informação externa localizada em um corpus.

Decidir se RAG adiciona capacidade necessária.

## Acceptance Criteria

Student-ready somente quando:

1. objectives explícitos;
2. generation-only usado como baseline;
3. retrieval observável;
4. evidence pack observável;
5. context construction observável;
6. grounded answer rastreável;
7. missing evidence tratado;
8. failure taxonomy aplicada;
9. top-k sensitivity demonstrada;
10. custo/latência/risco discutidos;
11. exercícios seguem o padrão TIL;
12. Glossário Vivo atualizado;
13. navegação anterior/home/próxima presente;
14. Internet OFF no núcleo;
15. execução headless completa;
16. warnings revisados;
17. execução Kaggle concluída;
18. revisão pedagógica concluída.

## Exit Condition

A aula estará completa quando o aluno conseguir explicar:

> **RAG não é apenas “adicionar busca a um LLM”. É uma arquitetura em que retrieval, seleção de evidência, construção de contexto, geração, grounding e avaliação precisam ser observados separadamente.**

Essa compreensão prepara o próximo bloco: **Tools and Workflows**.
