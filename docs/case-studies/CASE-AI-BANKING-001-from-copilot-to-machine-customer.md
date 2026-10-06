# CASE-AI-BANKING-001 — From Copilot to Machine Customer

## Status

Reviewed / candidate for curricular integration

## Purpose

Este estudo de caso conecta vários temas do TIL em uma única narrativa de transformação empresarial:

```text
model capability
→ tools
→ orchestration
→ governance
→ agent harness
→ operational KPI
→ business value
→ agent-to-agent interaction
```

A provocação central é:

> **O que muda quando não apenas a empresa usa agentes, mas o próprio cliente também passa a ser representado por um agente?**

## Source layers

### Layer A — Learner-provided synthesis

O ponto de partida é uma síntese narrativa produzida com Gemini Notebook / NotebookLM e fornecida pelo aluno.

Ela combina temas como:

- IA empresarial em larga escala;
- Santander e adoção corporativa de IA;
- copilots em contact centers;
- LangChain como metáfora de orquestração;
- Databricks como camada de plataforma/governança;
- human augmentation;
- avaliação por concordância humana;
- code review de software assistido por IA;
- machine customers;
- negociação agent-to-agent.

Esta síntese é tratada como **secondary synthesis** e não como fonte primária de evidência.

## Verified claims

As afirmações abaixo foram verificadas em fontes externas primárias ou independentes.

### Santander — impacto operacional e escala

Fonte primária Santander:

- iniciativas de IA geraram mais de €200 milhões em economia em 2024;
- copilots apoiam mais de 40% das interações de contact center;
- Speech Analytics processa cerca de 10 milhões de chamadas por ano na Espanha;
- mais de 6.000 desenvolvedores usam ferramentas de IA;
- algumas tarefas de desenvolvimento apresentam ganho de produtividade de 20–30%;
- treinamento obrigatório em IA foi planejado para toda a força de trabalho a partir de 2026.

### Santander — metas 2026–2028

Fonte primária Santander:

- objetivo de mais de 210 milhões de clientes até 2028;
- lucro superior a €20 bilhões em 2028;
- efficiency ratio em torno de 36%;
- mais de €1 bilhão por ano em business value proveniente de data & AI até 2028.

### Machine customers / customer agents

Fontes Gartner descrevem uma progressão em que:

1. agentes aconselham seus proprietários humanos;
2. passam a atuar em nome deles;
3. negociam diretamente com bancos e provedores;
4. tornam machine-to-machine interactions parte normal da relação de consumo.

Essa evidência sustenta a provocação de agentes pessoais negociando diretamente com agentes institucionais.

## Interpretations, not direct evidence

As seguintes formulações são pedagogicamente úteis, mas devem ser apresentadas como interpretação:

- “o banco está virando uma empresa de software”;
- “LangChain é o maestro”;
- “Databricks é uma blindagem”;
- “IA libera o humano para ser humano”;
- “agente do banco negocia com agente do cliente”.

Elas ajudam a raciocinar sobre arquitetura, mas não devem ser confundidas com definições técnicas formais.

## Claims requiring source recovery before curricular promotion

Não promover como evidência até localizar a fonte original:

- números específicos sobre crescimento e headcount da Pulse Client Experts;
- descrição exata da vaga brasileira citada na síntese;
- alegação de projeto jurídico específico com quase 12 mil documentos, 88% de precisão e economia anual multimilionária;
- estudo específico de sentimento no YouTube e valores exatos de Cohen's Kappa;
- detalhes técnicos atribuídos a “Chat Databricks” como wrapper de governança.

## Technical corrections

### Temperature

Formulação fraca:

```text
temperature baixa
→ modelo determinístico
```

Formulação recomendada:

```text
temperature baixa
→ reduz variabilidade do sampling

mas:
→ não garante determinismo universal
→ não garante correção factual
→ não elimina hallucination
```

### Orchestration

Formulação fraca:

```text
LangChain
→ guia a linha de raciocínio da IA
```

Formulação recomendada no TIL:

```text
orchestration runtime / framework
→ coordena estado
→ routing
→ tool calls
→ transitions
→ retries
→ persistence
→ human intervention
```

### Hallucination

Formulação fraca:

```text
orchestration + governance
→ elimina hallucination
```

Formulação recomendada:

```text
orchestration + grounding + controls
→ podem reduzir risco
→ aumentar rastreabilidade
→ limitar efeitos

mas não:
→ eliminar hallucination por definição
```

## Pedagogical value for TIL

### 1. Model is not the system

```text
modelo
≠
produto de IA

produto de IA
=
modelo
+ dados
+ tools
+ integração
+ runtime
+ governança
+ observabilidade
+ avaliação
```

### 2. Technical metric → operational KPI → business value

O case permite ensinar explicitamente:

```text
capability
↓
system behavior
↓
operational metric
↓
business metric
↓
business value
```

Exemplo:

```text
summarization / retrieval / auto-fill
↓
menos trabalho pós-atendimento
↓
menor tempo operacional
↓
maior capacidade do contact center
↓
valor econômico
```

### 3. Human augmentation

O case favorece uma leitura mais sofisticada que “automação = substituição”.

```text
máquina
→ busca
→ síntese
→ registro
→ recomendação

humano
→ julgamento
→ exceção
→ empatia
→ responsabilidade
```

### 4. Evaluation under human disagreement

O trecho sobre concordância abre uma pergunta importante:

> **Se especialistas humanos discordam entre si, qual deve ser o benchmark razoável para o modelo?**

Conceitos relacionados:

- inter-annotator agreement;
- Cohen's Kappa;
- label uncertainty;
- ambiguous ground truth;
- evaluation ceiling.

### 5. Governance of AI-generated code

O case também conecta desenvolvimento assistido por IA a:

```text
generation
→ automated checks
→ policy
→ human review
→ approval
→ merge
```

Isso reforça a regra da Aula 20:

> **decision ≠ authorization ≠ execution**

## Curriculum map

```text
Aula 13C
→ business utility / orchestration

Aula 17
→ tool contracts

Aula 18
→ controlled workflow

Aula 19
→ capability integration via MCP

Aula 20
→ agentic loop + agent harness

Aula 21
→ planning / replanning

Aula 22 (proposta)
→ orchestration runtimes

Futuro
→ agent-to-agent interaction / machine customers
```

## Machine Customer progression

Uma progressão pedagógica futura pode ser:

```text
assistant
→ copilot
→ delegated agent
→ autonomous customer agent
→ agent-to-agent negotiation
```

Isso introduz temas novos:

- identity;
- delegation;
- authorization;
- negotiation;
- conflicting utility functions;
- trust;
- protocols;
- audit trail;
- liability;
- human override.

## Core discussion questions

1. Onde está o modelo e onde está o sistema?
2. Quem decide, quem autoriza e quem executa?
3. Como uma capability técnica chega a um KPI operacional?
4. Como o KPI operacional se converte em business value?
5. Em quais etapas o humano continua indispensável?
6. Qual parte pertence ao Agent Harness?
7. Qual parte pertence ao orchestrator?
8. O que muda quando o cliente também possui um agente?
9. Como representar objetivos conflitantes entre agentes?
10. Que evidência seria necessária antes de permitir negociação autônoma?

## TIL decision

Integrar como **case study transversal**, não como aula autônoma neste momento.

O case deve ser usado para conectar arquitetura técnica, utility, governança, human oversight e tendências de machine customers.

Antes de qualquer uso de números específicos em notebooks, cada claim deve ter proveniência explícita e status de verificação.
