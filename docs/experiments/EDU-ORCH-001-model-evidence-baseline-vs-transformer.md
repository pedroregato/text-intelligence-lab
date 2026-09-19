# EDU-ORCH-001 — Model evidence: baseline clássico vs Transformer

## Status
**Completed — measured evidence collected and reviewed**

## Objective
Produzir o primeiro conjunto de evidências comparáveis do TIL para alimentar a Aula 13C em modo `EVIDENCE`.

Sistemas comparados:
1. TF-IDF + Multinomial Naive Bayes;
2. DistilBERT multilíngue com cabeça de classificação.

## Experimental Notebook
`experiments/edu-orch-001-baseline-vs-transformer/edu-orch-001-baseline-vs-transformer.ipynb`

Kaggle kernel: `pedrogentil/til-edu-orch-001-baseline-vs-transformer`

## Dataset
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
- test sample size: 3807

## Results

| Metric | TF-IDF + MultinomialNB | DistilBERT multilingual |
|---|---:|---:|
| F1 macro | 0.909915 | 0.930016 |
| Accuracy | 0.924087 | 0.940636 |
| Mean latency | 1.088 ms | 34.377 ms |
| Latency p50 | 1.075 ms | 30.938 ms |
| Latency p95 | 1.179 ms | 59.581 ms |
| Runtime proxy / 1000 | 0.03005 s | 51.99957 s |
| Test sample size | 3807 | 3807 |
| Evidence status | measured | measured |

Measured at: `2026-09-13T22:57:33.793831+00:00`

Official artifact: `data/model-evidence/til-model-evidence.csv`

## Interpretation
O DistilBERT aumentou o F1 macro de 0.909915 para 0.930016 (Δ ≈ +0.0201) e a accuracy de 0.924087 para 0.940636 (Δ ≈ +0.0165).

No ambiente CPU medido, a latência média aumentou de aproximadamente 1.09 ms para 34.38 ms. O proxy de runtime por 1000 previsões aumentou de aproximadamente 0.030 s para 52.00 s.

`cost_per_1000` é um proxy computacional medido, não preço monetário.

Esse trade-off fornece evidência concreta para:
`Selection → Routing → Orchestration → Utility → Compound AI Systems`.

## Cost Methodology
- `cost_unit = runtime_seconds_per_1000`
- `cost_method = measured_batch_runtime_proxy`

## GPU compatibility incident
Primeira tentativa Kaggle:
- PyTorch: `2.10.0+cu128`
- CUDA runtime: `12.8`
- GPU: `Tesla P100-PCIE-16GB`
- capability: `sm_60`
- capabilities suportadas pelo build do PyTorch: `sm_70 ... sm_120`

Embora `torch.cuda.is_available() == True`, uma operação CUDA mínima falhou com:
`AcceleratorError: CUDA error: no kernel image is available for execution on the device`

O teste confirmou que a falha não era específica do `Trainer`, do dataset nem do DistilBERT.

## CPU execution
O experimento foi reconfigurado para CPU:
- `enable_gpu = false`
- `use_cpu = True`
- `fp16 = False`

Execução Kaggle concluída com `KernelWorkerStatus.COMPLETE`.

## Hardware limitation
O CSV registra `hardware = x86_64`. Isso não identifica modelo da CPU, número de cores ou memória. Portanto, os valores absolutos de latência e runtime não devem ser generalizados para outros hardwares, nem tratados como estimativa de desempenho em GPU compatível.

## Infrastructure lesson
Antes de experimentos GPU, o TIL passa a verificar:
`GPU detectada → compute capability → architectures suportadas pelo framework → operação CUDA mínima → treinamento`

## Acceptance Criteria
1. dois sistemas com medições comparáveis — **PASS**
2. nenhuma métrica inventada — **PASS**
3. proveniência registrada — **PASS**
4. `til-model-evidence.csv` preenchido com evidência medida — **PASS**
5. evidência adequada para consumo pela Aula 13C — **PASS**
6. execução headless local e Kaggle concluída — **PASS**

## Evidence
Foram produzidas duas linhas com `evidence_status = measured`:
- `tfidf_multinomial_nb`
- `distilbert_multilingual`

Resultado central: o Transformer apresentou maior qualidade, enquanto o baseline clássico apresentou latência e proxy computacional muito menores no ambiente medido.

## Next Step
O papel do `EDU-ORCH-001` está concluído: produzir evidência medida de modelos isolados. A Aula 13C já consome `data/model-evidence/til-model-evidence.csv` em modo `EVIDENCE`.

A evolução passa a ocorrer na trilha AUTHOR / EVIDENCE, ampliando a matriz de modelos e condições de execução sem transferir treinamento longo para a aula do aluno.
