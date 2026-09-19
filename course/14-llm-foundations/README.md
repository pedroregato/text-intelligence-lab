# Aula 14 — LLM Foundations

Status: `Draft`

Esta aula inaugura o bloco LLM Foundations do TIL e cobre a transição de classificação/representação para geração autoregressiva.

## Arquivos

- `14-til-llm-foundations.ipynb` — notebook da aula;
- `kernel-metadata.json` — configuração Kaggle com Internet OFF.

## Escopo

- next-token prediction;
- logits e probabilidades;
- greedy decoding;
- sampling;
- temperature;
- top-k e top-p;
- structured outputs;
- failure modes;
- custo, latência e utility.

## Fora de escopo nesta aula

- RAG;
- tool calling;
- agentes;
- frameworks de orquestração;
- APIs proprietárias.

## Gates antes de student-ready

- [x] completar os conceitos novos no Glossário Vivo;
- [x] regenerar PT-BR, EN e HTML do glossário;
- [ ] validar execução headless do notebook completo;
- [ ] publicar/executar no Kaggle;
- [ ] revisar warnings da execução;
- [ ] revisar pedagogicamente em perspectiva de aluno.

Os experimentos determinísticos centrais (softmax, temperature, top-k, top-p e validação de structured output) já passaram por **execução sequencial local do código** sem erros.

Resultado observado:

```text
status: PASS
softmax: distribuição normalizada
greedy: ótimo
top-k=2: [ótimo, bom]
structured output: [válido, inválido, inválido, inválido]
```

Essa validação testa o código substantivo, mas **não substitui** a execução headless integral do arquivo `.ipynb` via `nbconvert` nem a execução real no Kaggle.

Especificação: `docs/curriculum/AULA-14-llm-foundations.md`.
