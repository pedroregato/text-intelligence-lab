# TIL Model Evidence Contract

Este diretório define o contrato de evidências consumido pela Aula 13C.

## Arquivos esperados

### `til-model-evidence.csv`

Cada linha representa um modelo isolado medido em condições documentadas.

### `til-routing-evidence.csv`

Cada linha representa uma configuração medida de routing/cascade, incluindo threshold e taxa de escalonamento.

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
| `evidence_status` | `measured`, `measured-recovered`, `estimated` ou `demo` |
| `dataset` | dataset/split usado |
| `hardware` | ambiente de execução |
| `sample_size` | número de exemplos avaliados |
| `model_version` | versão/modelo exato |
| `notes` | ressalvas e contexto |

## Regra de comparabilidade

As linhas comparadas precisam usar uma definição compatível de `quality`, a mesma unidade de custo e metodologia de latência comparável. Se isso não for possível, normalize ou mantenha experimentos separados.

## Protocolo mínimo de medição

Uma linha marcada como `measured` deve ter suporte em um experimento reproduzível que registre, no mínimo:

1. dataset e split;
2. métrica de qualidade e sua implementação;
3. número de exemplos avaliados;
4. hardware/ambiente;
5. versão do modelo e código relevante;
6. metodologia de latência;
7. metodologia de custo;
8. data da medição.

Para latência, preferir registrar média e, no relatório completo, também p50/p95 quando isso trouxer valor. Para custo, declarar explicitamente se o valor representa preço monetário observado, estimativa ou proxy computacional.



### Evidência recuperada

`measured-recovered` deve ser usado quando:

- a métrica veio de uma execução realmente medida;
- o artefato original não permaneceu disponível;
- os valores foram reconstruídos a partir de output, log ou outra evidência observável;
- alguma parte da proveniência planejada não pôde ser recuperada integralmente.

Esse status não equivale a `estimated`: os números não são inferidos nem interpolados. Ele também não equivale a `measured` pleno, porque o artefato original e/ou parte da proveniência foi perdida.

O motivo da recuperação deve ser registrado em `notes` e no relatório do experimento.

## Proveniência

O CSV é um resumo para consumo pelo simulador. A medição completa deve permanecer registrada em `docs/experiments/` com dataset/split, configuração, hardware, versão do código/modelo e metodologia de custo.

## Modos da Aula 13C

- **EVIDENCE**: o notebook encontrou evidência válida em `til-model-evidence.csv` e, quando disponível, em `til-routing-evidence.csv`.
- **DEMO**: não há evidência suficiente; o notebook usa proxies sintéticos explicitamente rotulados.

Aula e experimento têm papéis diferentes:

```text
AUTHOR / EVIDENCE
→ executa treino e medição
→ produz artefatos

STUDENT
→ carrega artefatos versionados
→ explora e interpreta
```

Princípio: **experimentos produzem evidência; aulas consomem evidência**.

Valores `demo` nunca devem ser apresentados como benchmark real do TIL.

## Evolução da matriz de evidências

O `EDU-ORCH-001` mediu modelos isolados e o `EDU-ORCH-002` mediu routing/cascade. Expansões futuras podem acrescentar novas camadas da arquitetura abaixo:

```text
TF-IDF + classificador clássico
        ↓
DistilBERT multilíngue
        ↓
LLM e/ou revisão humana
```

A primeira meta é comparar o baseline clássico e o Transformer usando o mesmo dataset/split e a mesma métrica de qualidade. A camada LLM/humana só deve entrar quando houver uma metodologia de avaliação e custo claramente documentada.

Nenhum valor deve ser incluído no CSV apenas para completar o simulador.

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
