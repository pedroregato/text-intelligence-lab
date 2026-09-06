# EDU-INFRA-002 — Kaggle Model Resource Validation

## Status
OPEN

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

- Kaggle model page:
- owner:
- model:
- framework:
- variation:
- version:
- license:
- language:
- exact handle:
- internet setting:
- tokenizer load: PASS / FAIL
- model load: PASS / FAIL
- Aula 10 execution: PASS / FAIL
- Aula 11 fine-tuning: PASS / FAIL
- copied notebook preserves resource: PASS / FAIL

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
