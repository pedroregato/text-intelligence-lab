# Aula 13 — Métricas, cenários e sistemas compostos

Este diretório reúne a família da Aula 13, que leva o aluno da leitura de métricas à decisão arquitetural baseada em qualidade, custo e latência.

## Sequência recomendada

| Etapa | Notebook | Foco |
| --- | --- | --- |
| 13 | `13-til-metrics-and-indicators.ipynb` | interpretar métricas e custos de erro |
| 13B | `metric-scenario-lab/13b-til-metric-scenario-lab.ipynb` | explorar thresholds, cenários e trade-offs |
| 13C | `13c-model-routing-and-orchestration.ipynb` | routing, orchestration, quality gates e utility |

Fluxo conceitual:

```text
métrica
→ custo do erro
→ threshold / abstenção
→ cenário
→ quality gate
→ model routing
→ model orchestration
→ compound AI system
→ decisão baseada em evidências
```

## Aula 13C no Kaggle

Notebook publicado:

`https://www.kaggle.com/code/pedrogentil/til-13c-model-routing-orchestration-and-utility`

A versão atual foi validada com sucesso em:

1. execução local headless usando `jupyter nbconvert --execute`;
2. execução completa no Kaggle.

A interatividade é opcional e acionada explicitamente pelo aluno. O notebook não depende de cliques ou callbacks para concluir `Run All`.

## STUDENT MODE — evidência pronta

A Aula 13C consome evidências versionadas produzidas pelos experimentos autorais. Quando os artefatos estão disponíveis, a aula opera em modo `EVIDENCE`; o fallback `DEMO` existe apenas para manter o notebook executável quando a evidência não estiver acessível.

Artefatos canônicos:

- `data/model-evidence/til-model-evidence.csv` — modelos isolados medidos pelo `EDU-ORCH-001`;
- `data/model-evidence/til-routing-evidence.csv` — cascades medidos pelo `EDU-ORCH-002`.

As linhas de routing usam `evidence_status = measured-recovered`: os números vieram de execução real no Kaggle, mas o CSV original precisou ser reconstruído a partir do output observado após perda do artefato da sessão. Esse status não deve ser convertido para `measured`.

Contrato dos dados:

`data/model-evidence/README.md`

Arquitetura pedagógica:

```text
AUTHOR / EVIDENCE
→ experimentos executam treinamento e medição
→ produzem evidência

STUDENT
→ Aula 13C consome evidência pronta
→ execução rápida
→ interpretação e decisão
```

Princípio: **experimentos produzem evidência; aulas consomem evidência.**

## Regra de engenharia

Os notebooks interativos desta família seguem `docs/decisions/ADR-009-headless-first-interactive-notebooks.md`:

> Interatividade enriquece a aula, mas nunca é requisito para a execução completa do notebook.
