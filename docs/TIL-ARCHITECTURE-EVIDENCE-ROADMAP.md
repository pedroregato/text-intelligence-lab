# TIL — Architecture, Evidence & Roadmap

> **Text Intelligence Lab (TIL)**  
> *An evidence-driven path to Applied AI Engineering*

Esta página registra a arquitetura conceitual, as evidências acumuladas e a evolução do TIL. A **Course Home** permanece voltada ao aluno que chega pela primeira vez; aqui ficam os detalhes de manutenção, decisões arquiteturais, Evidence Labs, readiness e próximos movimentos.

## Identidade do TIL

O TIL começou em **Text Intelligence** e evoluiu para uma trajetória de **Applied AI Engineering**.

A progressão pedagógica oficial é:

```text
Text
→ Representation
→ Models
→ Evaluation
→ Routing
→ Retrieval
→ RAG
→ Tools
→ Workflows
→ MCP
→ Agents
→ Planning
→ Orchestration Runtimes
```

A evolução é organizada em quatro macrocamadas:

| Camada | Pergunta central |
| --- | --- |
| **I — Text Intelligence** | Como transformar linguagem em representação e sinal útil? |
| **II — Model Engineering** | Como construir, comparar e avaliar modelos? |
| **III — Intelligent Orchestration** | Como combinar modelos, contexto, retrieval e capacidades? |
| **IV — Agentic Systems** | Quando o sistema deve decidir, planejar e agir? |

Dimensões transversais:

```text
Evaluation · Utility · Cost · Latency · Observability
Governance · Security · Reproducibility · Human Oversight
```

## Tese central

> **Complexidade arquitetural precisa ser conquistada por evidência.**

O TIL não assume que uma tecnologia mais sofisticada é automaticamente melhor.

```text
maior capacidade de modelo ≠ maior utility
maior autonomia           ≠ maior utility
mais planejamento         ≠ maior utility
```

**Utility** é o valor líquido que uma solução entrega no contexto de uso, considerando qualidade, custo, latência, risco e o grau de complexidade ou autonomia necessário para produzir esse resultado.

A pergunta recorrente do curso é:

> **Que capacidade adicional melhora o resultado o suficiente para justificar seu custo, latência, risco e complexidade?**

## Como o projeto é mantido

| Componente | Papel |
| --- | --- |
| **GitHub** | Source of truth do curso, histórico, documentação e decisões |
| **Kaggle** | Ambiente principal de execução educacional e experimental |
| **Notebooks** | Unidades didáticas executáveis |
| **Outputs** | Evidências observáveis das execuções |
| **Glossário Vivo** | Vocabulário técnico bilíngue e cumulativo |
| **Evidence Labs** | Experimentos que produzem evidência para as aulas |
| **Readiness Gates** | Critérios formais de promoção das revisões |
| **Biblioteca Viva de Referências** | Fontes externas contextualizadas para uso pedagógico |
| **Case Studies** | Casos transversais que conectam conceitos, evidências e decisões |

O ciclo de engenharia permanece:

```text
Arquitetar
→ Implementar pequeno
→ Executar headless
→ Executar no Kaggle
→ Observar
→ Avaliar
→ Corrigir
→ Versionar
→ Expandir
```

## Evidence Labs

### EDU-ORCH-001 — Baseline vs Transformer

Produziu a primeira comparação medida do TIL entre:

- TF-IDF + Multinomial Naive Bayes;
- DistilBERT multilingual.

Artefato canônico:

```text
data/model-evidence/til-model-evidence.csv
```

### EDU-ORCH-002 — Routing Evidence Matrix

Mediu cascades entre baseline clássico e Transformer sob diferentes thresholds de confiança.

Artefato canônico:

```text
data/model-evidence/til-routing-evidence.csv
```

A arquitetura pedagógica adotada é:

```text
experimentos
→ produzem evidência

aulas
→ consomem evidência
```

## Readiness

A Course Home usa três estados para o aluno:

| Status | Significado |
| --- | --- |
| ✅ **Pronta** | Passou nos gates técnicos e pedagógicos |
| 🧪 **Em revisão** | Executa no Kaggle; revisão pedagógica pendente |
| 🧭 **Planejada** | Ainda não publicada |

Os critérios completos permanecem documentados em `docs/readiness/` e no contrato de design do curso.

## Distinções arquiteturais acumuladas

Ao longo da trilha, algumas distinções se tornaram estruturais:

```text
groundedness ≠ factuality ≠ governance

decision ≠ authorization ≠ execution

MCP ≠ workflow ≠ agent

Decision Provider ≠ Agent Harness

reactive next-action ≠ explicit planning
```

O princípio **mecanismo antes do framework** continua válido. Frameworks entram depois que o aluno entende o mecanismo vendor-neutral que eles implementam.

## Estudo de caso transversal

O caso:

```text
CASE-AI-BANKING-001 — From Copilot to Machine Customer
```

conecta enterprise AI, orchestration, governance, Agent Harness, indicadores operacionais, valor de negócio e evolução para interações agent-to-agent.

Material relacionado: `docs/case-studies/`.

## Extensões de Text Intelligence planejadas

O reposicionamento para Applied AI Engineering não elimina a origem do TIL. Pelo contrário, evidencia lacunas que devem ser cobertas formalmente na camada de Text Intelligence.

Itens planejados:

- Topic Modeling / descoberta de temas;
- clustering textual quando pedagogicamente útil;
- Named Entity Recognition (NER);
- extração estruturada de informação;
- similaridade textual;
- sumarização;
- QA e multilabel classification.

Esses módulos devem entrar quando seus pré-requisitos estiverem claros, sem interromper artificialmente a progressão já validada.

## Próxima fronteira

### Aula 22 — Agent Orchestration Runtimes

A próxima unidade proposta deve comparar orchestration procedural com graph runtimes, cobrindo:

- shared state;
- nodes e transitions;
- conditional routing;
- checkpoints;
- interrupt / resume;
- durable execution;
- recovery;
- human-in-the-loop.

LangGraph pode aparecer como implementação de referência **depois** dos mecanismos vendor-neutral.

## Regra de decisão arquitetural

Quando duas arquiteturas atingirem resultado pedagógico e operacional semelhante, preferir a mais simples.

```text
capacidade adicional
→ evidência adicional
→ complexidade justificada
```

Sem evidência suficiente:

```text
manter arquitetura mais simples
```

## Documentos relacionados

- `docs/architecture/TIL-AIE-001-agentic-intelligence-evolution.md`
- `docs/ROADMAP.md`
- `docs/ENGINEERING.md`
- `docs/TIL-COURSE-DESIGN-CONTRACT.md`
- `docs/readiness/`
- `docs/case-studies/`
- `docs/references/`
- `data/model-evidence/`
