# EDU-ORCH-001 — Model evidence: baseline clássico vs Transformer

## Status

Running — evidence collection in progress

## Objective

Produzir o primeiro conjunto de evidências comparáveis do TIL para alimentar a Aula 13C em modo `EVIDENCE`.

A primeira comparação mede, sob o mesmo dataset/split e a mesma métrica de qualidade:

1. TF-IDF + Multinomial Naive Bayes;
2. DistilBERT multilíngue com cabeça de classificação.

A camada LLM/revisão humana fica fora deste primeiro ciclo até existir uma metodologia reproduzível de custo e avaliação.

## Experimental Notebook

```text
experiments/edu-orch-001-baseline-vs-transformer/
├── edu-orch-001-baseline-vs-transformer.ipynb
└── kernel-metadata.json
```

Kaggle kernel:

```text
pedrogentil/til-edu-orch-001-baseline-vs-transformer
```

O notebook segue a política `headless-first`: deve executar localmente sem recursos Kaggle em modo de validação/SMOKE e executar no Kaggle com dataset e modelo anexados para coleta de evidência.

## Dataset

Primeiro ciclo:

- Kaggle Dataset: `fredericods/ptbr-sentiment-analysis-datasets`;
- subconjunto: Olist / Polarity;
- texto de entrada comum: `review_text`;
- target: `polarity`;
- ratings 1–2 são tratados como negativos;
- ratings 4–5 são tratados como positivos;
- ratings 3 são excluídos da formulação binária;
- folds 1–8: treino;
- fold 9: validação;
- fold 10: teste.

A transformação de estrelas em polaridade é uma escolha metodológica e deve permanecer explícita: o target é um proxy binário de sentimento e a exclusão dos casos intermediários altera a população representada pelo experimento.

## Model Resource

Recurso Kaggle versionado:

```text
goddiao/distilbert-base-multilingual-cased/PyTorch/default/1
```

O recurso é carregado localmente no runtime Kaggle, mantendo `Internet OFF`.

## Hypothesis

O Transformer tende a melhorar a qualidade em relação ao baseline clássico, mas com aumento de latência e custo computacional. O objetivo não é provar antecipadamente essa hipótese, e sim medir o trade-off real no ambiente do TIL.

## Required Evidence

Para cada sistema registrar:

- `system`;
- métrica de qualidade compatível, com `f1_macro` como métrica principal;
- `accuracy` como métrica complementar;
- `cost_per_1000` em unidade declarada;
- `latency_ms` média;
- p50/p95 de latência quando viável;
- dataset e split;
- sample size;
- hardware/ambiente;
- versão do modelo;
- data da medição;
- metodologia de custo;
- proveniência;
- observações relevantes.

## Experimental Controls

As comparações só serão consideradas válidas quando utilizarem:

- o mesmo conjunto de avaliação;
- a mesma definição de métrica de qualidade;
- pré-processamento documentado por pipeline;
- metodologia de medição de latência consistente;
- unidade de custo consistente ou conversão explicitamente documentada;
- configuração de hardware registrada.

## Systems

### Classical baseline

```text
review_text
→ TF-IDF
→ Multinomial Naive Bayes
→ predição
```

O baseline foi fixado antes da observação do resultado final para evitar seleção retrospectiva apenas do classificador mais favorável.

### Transformer

```text
review_text
→ tokenizer DistilBERT multilingual
→ DistilBERT
→ cabeça de classificação
→ predição
```

## Cost Methodology

O campo `cost_per_1000` não deve misturar preço monetário e proxy computacional silenciosamente.

No primeiro ciclo, se não houver preço monetário diretamente observável, é aceitável usar uma unidade de custo computacional normalizada, desde que:

- a unidade seja declarada;
- seja aplicada de forma consistente aos sistemas comparados;
- `evidence_status` e `notes` deixem claro que se trata de proxy computacional;
- o relatório não apresente o proxy como preço monetário.

## Runtime history — 2026-09-13

### GPU attempt

A primeira execução real do notebook no Kaggle foi configurada com GPU e alcançou o treinamento do Transformer, mas falhou por incompatibilidade entre a GPU atribuída e o build atual do PyTorch.

Ambiente observado:

```text
PyTorch: 2.10.0+cu128
CUDA runtime: 12.8
GPU: Tesla P100-PCIE-16GB
GPU compute capability: 6.0 (sm_60)
PyTorch supported capabilities: sm_70 ... sm_120
```

Erro observado:

```text
AcceleratorError: CUDA error: no kernel image is available for execution on the device
```

Um teste mínimo com tensor CUDA reproduziu a falha, confirmando que o problema não era específico do `Trainer` nem do DistilBERT.

### CPU fallback

Para não bloquear a coleta de evidência, o experimento foi reconfigurado para CPU:

- `kernel-metadata.json`: `enable_gpu = false`;
- `TrainingArguments`: `use_cpu=True`;
- mixed precision desativada: `fp16=False`;
- device do experimento explicitamente fixado em CPU.

A execução CPU está em andamento. Nenhum resultado de qualidade, latência ou custo é declarado neste documento antes da conclusão da execução.

### Infrastructure lesson

`torch.cuda.is_available() == True` não é evidência suficiente de que a GPU é operacional para o build atual do framework.

Para experimentos GPU, o TIL passa a tratar como evidência mínima de compatibilidade:

```text
GPU detectada
→ compute capability registrada
→ capabilities suportadas pelo PyTorch verificadas
→ operação CUDA mínima executada
→ somente então iniciar treinamento
```

## Procedure

```text
fixar dataset/split
→ executar baseline clássico
→ medir qualidade
→ medir latência
→ registrar custo
→ executar Transformer
→ medir qualidade
→ medir latência
→ registrar custo
→ revisar comparabilidade
→ publicar proveniência
→ atualizar til-model-evidence.csv
→ executar Aula 13C em modo EVIDENCE
```

## Acceptance Criteria

O experimento será considerado concluído quando:

1. pelo menos dois sistemas possuírem medições comparáveis;
2. nenhuma métrica for inventada ou inferida sem metodologia declarada;
3. a proveniência estiver registrada neste documento ou em artefatos associados;
4. `data/model-evidence/til-model-evidence.csv` puder ser preenchido com evidência defensável;
5. a Aula 13C detectar o CSV e executar em modo `EVIDENCE`;
6. o notebook resultante completar execução headless local e no Kaggle.

## Expected Output

- relatório experimental atualizado;
- `data/model-evidence/til-model-evidence.csv` com linhas medidas/estimadas claramente identificadas;
- Aula 13C executada em `EVIDENCE`;
- interpretação pedagógica do trade-off qualidade × custo × latência.

## Evidence

Coleta em andamento.

O documento registra evidência de infraestrutura já observada, mas ainda não declara resultados comparativos de modelos. Métricas finais só serão incorporadas após a conclusão e revisão da execução.