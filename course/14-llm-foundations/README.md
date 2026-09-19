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
- [x] validar execução headless do código do notebook com `nbconvert`;
- [ ] publicar/executar no Kaggle;
- [x] revisar warnings da execução local;
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


## Headless validation — 2026-09-19

Validação local com `nbconvert 7.17.1`:

```text
python -m jupyter nbconvert
→ execute
→ COMPLETE
→ sem warnings após inclusão de IDs estáveis nas células
```

A primeira execução revelou `MissingIDFieldWarning`. O notebook canônico foi corrigido com IDs estáveis em todas as 26 células e o teste foi repetido sem warnings.

A validação local confirma o caminho de código e a compatibilidade headless. O gate final continua sendo uma execução `Run All` do artefato oficial no Kaggle.
