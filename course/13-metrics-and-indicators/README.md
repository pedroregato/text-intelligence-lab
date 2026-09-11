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

## DEMO → EVIDENCE

A Aula 13C começa em modo `DEMO` quando não há medições comparáveis disponíveis. Nesse modo, os valores são proxies didáticos e não benchmarks reais.

O próximo marco é ativar o modo `EVIDENCE` com medições produzidas pelo experimento:

`docs/experiments/EDU-ORCH-001-model-evidence-baseline-vs-transformer.md`

Contrato dos dados:

`data/model-evidence/README.md`

Fluxo esperado:

```text
TF-IDF + classificador clássico
        ↓
DistilBERT multilíngue
        ↓
medir qualidade + latência + custo
        ↓
registrar proveniência
        ↓
til-model-evidence.csv
        ↓
13C em modo EVIDENCE
```

## Regra de engenharia

Os notebooks interativos desta família seguem `docs/decisions/ADR-009-headless-first-interactive-notebooks.md`:

> Interatividade enriquece a aula, mas nunca é requisito para a execução completa do notebook.
