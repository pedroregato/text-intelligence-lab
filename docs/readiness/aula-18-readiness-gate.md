# TIL Readiness Gate — Aula 18

## Purpose

Registrar a evidência de promoção da **Aula 18 — Deterministic Workflows** para `Available / student-ready`.

## Decision Rule

A Aula 18 é promovida somente quando os critérios pedagógicos, técnicos, de execução e integração curricular estiverem atendidos.

## Mandatory Criteria

### G1 — Conteúdo curricular

Status: **PASS**

Evidence:

- tool vs workflow;
- estado explícito;
- retries controlados;
- idempotência;
- checkpoints;
- approval gates;
- recovery;
- observabilidade;
- failure taxonomy;
- architecture decision lab.

### G2 — Decision Contracts and Routing

Status: **PASS**

Evidence:

- `DecisionProvider → Typed Decision → Routing Policy → Workflow`;
- contrato com `choice`, `confidence`, `source`, `latency_ms` e `cost`;
- confidence-gated routing;
- thresholds explicitamente apresentados como exemplos pedagógicos, não regras universais.

### G3 — Representação visual

Status: **PASS**

Evidence:

Diagramas textuais adicionados para:

- fluxo de estados;
- workflow principal;
- retry;
- approval gate;
- recovery;
- decision contract / routing policy.

### G4 — Glossário Vivo

Status: **PASS**

Evidence:

- termos centrais integrados contextualmente no notebook;
- links PT-BR presentes;
- CI atualizado para validar cobertura dos termos da Aula 18.

### G5 — Reprodutibilidade

Status: **PASS**

Evidence:

- Internet OFF;
- GPU OFF;
- nenhuma API externa;
- nenhum side effect real;
- estado e publicação simulados em memória;
- dados simulados explicitamente separados do estado real do TIL.

### G6 — Execução Kaggle

Status: **PENDING REVALIDATION**

Evidence:

- a versão anterior foi executada integralmente no Kaggle;
- a revisão pedagógica permanece válida;
- após a conversão das soluções para o padrão opt-in, um novo Run All será feito na bateria final.

### G7 — Revisão pedagógica

Status: **PASS**

Evidence:

- comentários adicionados sobre uso de `dict` e `list`;
- distinção entre estado real do curso e estado simulado do laboratório;
- diagramas de fluxo incorporados;
- fluxo revisado após execução real.

### G8 — Navegação e promoção

Status: **PASS**

Evidence:

- README atualizado;
- ROADMAP atualizado;
- Course Home atualizado;
- `course/navigation.json` marca Aula 18 como publicada;
- Aula 17 aponta para Aula 18 no Kaggle;
- TIL-AIE-001 registra a Aula 18 como `Available / student-ready`.

## Current Gate Status

```text
G1 Conteúdo curricular                 PASS
G2 Decision contracts / routing       PASS
G3 Representação visual               PASS
G4 Glossário Vivo                     PASS
G5 Reprodutibilidade                  PASS
G6 Execução Kaggle                    PENDING REVALIDATION
G7 Revisão pedagógica                 PASS
G8 Navegação e promoção               PASS
```

## Release Status

**AULA 18: PEDAGOGICALLY READY / TECHNICAL REVALIDATION PENDING**

## Exit Principle

> Um workflow determinístico deve ser preferido a maior autonomia quando já resolve o problema com menor risco e complexidade.

## Architectural Bridge

```text
Tool
→ Deterministic Workflow
→ Standardized Capability Exposure
→ MCP
→ Agentic Systems
```
