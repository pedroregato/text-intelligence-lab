# EDU-ORCH-002 — Routing Evidence Matrix

## Status
**Planned**

## Objective
Medir, de forma reproduzível, uma arquitetura de routing/cascade que combine os dois sistemas já medidos no `EDU-ORCH-001`:

1. TF-IDF + Multinomial Naive Bayes;
2. DistilBERT multilíngue com cabeça de classificação.

O objetivo é substituir a atual interpolação didática da Aula 13C por evidência medida de uma arquitetura composta.

## Research Question
Quando vale a pena aceitar a decisão do baseline clássico e quando vale a pena escalar a entrada para o Transformer?

Pergunta operacional:

```text
Como variam qualidade, latência, custo computacional e taxa de escalonamento
quando o threshold de confiança do baseline é alterado?
```

## Hypothesis
À medida que o threshold de confiança do baseline aumenta:

```text
threshold ↑
    ↓
mais exemplos escalam para o Transformer
    ↓
escalation_rate ↑
    ↓
qualidade tende a aumentar
    ↓
latência e runtime tendem a aumentar
```

A hipótese não assume monotonicidade perfeita. Os resultados reais devem ser medidos.

## Architecture

```text
Entrada
  ↓
TF-IDF + MultinomialNB
  ↓
max(proba_baseline) >= threshold?
  ├── sim → aceita predição do baseline
  └── não → escala para DistilBERT
                 ↓
              decisão final
```

## Dataset
Manter exatamente o mesmo recorte do `EDU-ORCH-001` para preservar comparabilidade:

- Kaggle Dataset: `fredericods/ptbr-sentiment-analysis-datasets`
- subset: Olist / Polarity
- input: `review_text`
- target: `polarity`
- ratings 1–2: negativos
- ratings 4–5: positivos
- ratings 3: excluídos
- folds 1–8: treino
- fold 9: validação
- fold 10: teste
- test sample size esperado: 3807

## Candidate Thresholds
Primeira matriz experimental:

```text
0.60
0.70
0.80
0.90
```

Os thresholds poderão ser refinados após a primeira execução, mas qualquer expansão deve preservar os resultados originais.

## Metrics

### Quality
- `f1_macro`
- `accuracy`

### Routing
- `threshold`
- `escalation_rate`
- `baseline_share`
- `transformer_share`

### Latency
- `latency_ms`
- `latency_p50_ms`
- `latency_p95_ms`

### Computational Cost Proxy
- `cost_per_1000`
- `cost_unit = runtime_seconds_per_1000`
- `cost_method = measured_batch_runtime_proxy`

O proxy de custo continua sendo computacional, não monetário.

## Measurement Rule
Cada threshold deve produzir uma linha de evidência medida.

Exemplo conceitual:

```text
cascade_t060
cascade_t070
cascade_t080
cascade_t090
```

Nenhuma linha poderá ser marcada como `measured` se for derivada apenas por interpolação matemática entre os sistemas do `EDU-ORCH-001`.

## Latency Methodology
A latência do cascade deve ser medida end-to-end.

Isso significa contabilizar:

```text
baseline inference
+ routing decision
+ transformer inference quando houver escalonamento
```

Não usar apenas média ponderada das latências previamente medidas como substituto para execução real.

## Confidence Rule
A primeira versão utilizará:

```python
confidence = max(predict_proba_baseline)
```

Routing:

```python
if confidence >= threshold:
    final_prediction = baseline_prediction
else:
    final_prediction = transformer_prediction
```

A definição deve permanecer fixa durante a primeira matriz experimental.

## Fairness of Comparison
Para todos os thresholds:

- mesmo conjunto de teste;
- mesma ordem dos exemplos;
- mesmos modelos treinados/configurados;
- mesma definição de confiança;
- mesma infraestrutura de execução;
- mesma metodologia de medição.

## Expected Artifact
Criar um artefato versionado específico para routing, por exemplo:

```text
data/model-evidence/til-routing-evidence.csv
```

Campos mínimos recomendados:

```text
system
threshold
quality
quality_metric
accuracy
escalation_rate
baseline_share
transformer_share
cost_per_1000
cost_unit
cost_method
latency_ms
latency_p50_ms
latency_p95_ms
source
measured_at
evidence_status
dataset
hardware
sample_size
model_version
notes
```

## Relationship with Lesson 13C
A Aula 13C atualmente possui endpoints medidos para os modelos isolados e cenários compostos simulados.

O `EDU-ORCH-002` deve permitir a evolução:

```text
Model evidence
    ↓
Routing evidence
    ↓
Measured cascade
    ↓
Utility over real architectures
```

Após a conclusão, a aula deverá distinguir explicitamente:

- modelos isolados medidos;
- cascades medidos;
- cenários ainda hipotéticos.

## Utility
A primeira execução deve preservar separadas as métricas brutas.

A função de utility será aplicada depois da medição:

```text
measured metrics
    ↓
utility function
    ↓
decision analysis
```

Isso evita misturar aquisição de evidência com preferência de engenharia.

## Hardware
A primeira execução pode continuar em CPU para manter consistência com o `EDU-ORCH-001`.

Se houver execução futura em GPU, ela deverá ser registrada como outro contexto experimental, e não sobrescrever os resultados CPU.

## Reproducibility
Registrar:

- versão do Python;
- versão do scikit-learn;
- versão do transformers;
- versão do PyTorch;
- identificação de hardware disponível;
- dataset e folds;
- seed;
- batch size;
- modelo Kaggle/versionamento utilizado;
- timestamp da medição.

## Acceptance Criteria
1. pelo menos quatro thresholds executados;
2. todas as linhas com `evidence_status = measured`;
3. mesmo conjunto de teste do `EDU-ORCH-001`;
4. F1 macro e accuracy calculados sobre a decisão final do cascade;
5. escalation rate medido diretamente;
6. latência end-to-end medida;
7. runtime proxy por 1000 medido;
8. nenhuma métrica obtida somente por interpolação;
9. proveniência suficiente para reprodução;
10. artefato consumível pela Aula 13C.

## Failure Conditions
O experimento não deve ser considerado concluído se:

- o Transformer for executado para todos os exemplos antes da decisão de routing e o tempo correspondente for contado como se fosse cascade real;
- a latência for apenas estimada a partir do `EDU-ORCH-001`;
- os thresholds forem avaliados em conjuntos de teste diferentes;
- houver mudança de modelo entre thresholds sem registro;
- o CSV não distinguir evidência medida de estimativa.

## Experimental Notebook
Planejado:

```text
experiments/edu-orch-002-routing-evidence-matrix/
└── edu-orch-002-routing-evidence-matrix.ipynb
```

## Expected Learning
O experimento deve permitir ao aluno observar empiricamente que:

```text
modelo mais forte ≠ melhor escolha para todas as entradas
```

e que routing é uma decisão mensurável envolvendo:

```text
qualidade
↕
latência
↕
custo
↕
taxa de escalonamento
↕
utility
```

## Next Step
Construir o notebook experimental headless-first, reutilizando a preparação de dados, o baseline e o Transformer do `EDU-ORCH-001`, sem copiar resultados como se fossem novas medições.
