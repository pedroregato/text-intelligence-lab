# EDU-INFRA-002 — Kaggle Model Resource Validation

## Status
PARTIAL PASS — Aula 10 operationally validated

## Objective

Validar um recurso Kaggle Model versionado para substituir o download remoto do Hugging Face nas Aulas 10–11.

## Target model

`distilbert-base-multilingual-cased`

## Why this model

- multilíngue;
- compatível com português;
- pequeno o suficiente para demonstrações didáticas;
- já adotado nas aulas em construção.

## Discovery evidence — 2026-09-06

A documentação oficial do Kaggle confirma:

- Models integrados a Notebooks;
- integração com Hugging Face Hub;
- acesso programático com `kagglehub.model_download()`;
- possibilidade de versionar a referência.

A busca pública não identificou, com confiança suficiente, um Kaggle Model oficial exato para `distilbert-base-multilingual-cased`.

Foi identificado um Dataset antigo com o mesmo nome, porém não será utilizado por não atender aos critérios de governança do TIL.

## Pending validation

Preencher após execução no Kaggle:

- Kaggle model page: GODDiao / distilbert-base-multilingual-cased
- owner: goddiao
- model: distilbert-base-multilingual-cased
- framework: pytorch
- variation: default
- version: 1
- license: Apache 2.0
- language: multilingual
- exact handle: goddiao/distilbert-base-multilingual-cased/pyTorch/default
- mounted path: /kaggle/input/models/goddiao/distilbert-base-multilingual-cased/pytorch/default/1
- model directory: /kaggle/input/models/goddiao/distilbert-base-multilingual-cased/pytorch/default/1/distilbert-base-multilingual-cased
- internet setting: OFF — PASS
- tokenizer load: PASS — DistilBertTokenizer
- model load: PASS — DistilBertModel
- model_type: distilbert
- vocab_size: 119547
- Aula 10 local model load with Internet OFF: PASS
- Aula 11 classification model load with Internet OFF: PASS
- SHA-256 observed for model.safetensors: 45620facecba512b46c58430d27e20af43952eda9c1be56e023d0bbcfdcf10cb
- copied notebook preserves resource: PENDING

## Decision gate

Somente após todos os itens críticos em PASS:

```text
HF fallback
→ remove
Kaggle Model versionado
→ torna-se dependência oficial
Internet
→ OFF
```


## Evidence from offline execution

With Kaggle Internet set to OFF, the attached model loaded successfully using local files only.

Observed:

```text
DistilBertTokenizer
DistilBertModel
distilbert
119547
```

This validates the model resource operationally for Aula 10.

Remaining gates before full acceptance for Aula 11:

1. SHA-256 integrity comparison of `model.safetensors`;
2. offline load with `AutoModelForSequenceClassification`;
3. offline fine-tuning execution;
4. confirmation that a copied notebook preserves the attached model resource.


## Aula 11 classification-head validation

With Internet OFF, the attached Kaggle model loaded successfully as:

```text
DistilBertForSequenceClassification
distilbert
3
```

Load report:

```text
classifier.bias       MISSING
pre_classifier.bias   MISSING
pre_classifier.weight MISSING
classifier.weight     MISSING
```

Interpretation:

This is the expected behavior for the TIL lesson. The checkpoint contains the pretrained DistilBERT encoder, while the downstream classification head is newly initialized for the three-class task.

Therefore:

```text
pretrained encoder         PASS
new classification head    PASS
offline loading            PASS
num_labels = 3             PASS
```

Observed SHA-256 for `model.safetensors`:

```text
45620facecba512b46c58430d27e20af43952eda9c1be56e023d0bbcfdcf10cb
```

This hash must not yet be treated as equivalent to the canonical upstream artifact until provenance/integrity comparison is completed.

Remaining gates:

1. verify upstream artifact/hash provenance;
2. run a minimal offline fine-tuning;
3. confirm copied notebook preserves the attached model resource.
