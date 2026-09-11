# TIL Model Evidence Contract

Este diretório define o contrato de evidências consumido pela Aula 13C.

## Arquivo esperado

`til-model-evidence.csv`

Cada linha representa um modelo ou sistema medido em condições documentadas.

### Campos mínimos

| Campo | Tipo | Regra |
| --- | --- | --- |
| `system` | texto | identificador curto e estável |
| `quality` | número | valor entre 0 e 1 |
| `cost_per_1000` | número | custo por 1.000 inferências em unidade consistente |
| `latency_ms` | número | latência média por inferência em milissegundos |

### Campos recomendados

| Campo | Uso |
| --- | --- |
| `quality_metric` | nome da métrica, por exemplo `f1_macro` |
| `source` | experimento, notebook ou relatório de origem |
| `measured_at` | data/hora da medição |
| `evidence_status` | `measured`, `estimated` ou `demo` |
| `dataset` | dataset/split usado |
| `hardware` | ambiente de execução |
| `sample_size` | número de exemplos avaliados |
| `model_version` | versão/modelo exato |
| `notes` | ressalvas e contexto |

## Regra de comparabilidade

As linhas comparadas precisam usar uma definição compatível de `quality`, a mesma unidade de custo e metodologia de latência comparável. Se isso não for possível, normalize ou mantenha experimentos separados.

## Proveniência

O CSV é um resumo para consumo pelo simulador. A medição completa deve permanecer registrada em `docs/experiments/` com dataset/split, configuração, hardware, versão do código/modelo e metodologia de custo.

## Modos da Aula 13C

- **EVIDENCE**: o notebook encontrou pelo menos duas linhas válidas em `til-model-evidence.csv`.
- **DEMO**: não há evidência suficiente; o notebook usa proxies sintéticos explicitamente rotulados.

Valores `demo` nunca devem ser apresentados como benchmark real do TIL.

## Fluxo esperado

```text
experimento reproduzível
        ↓
qualidade + latência + custo
        ↓
registro de proveniência
        ↓
til-model-evidence.csv
        ↓
Aula 13C
        ↓
decisão arquitetural
```
