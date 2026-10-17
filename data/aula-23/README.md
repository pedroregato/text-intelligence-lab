# Aula 23 — Request sets

Conjuntos de pedidos em linguagem natural usados na Aula 23 (Model-Driven Decisions).

| Arquivo | Linhas | Uso |
|---|---|---|
| `requests-train.csv` | 32 | treino do classificador baseline; fonte dos exemplos few-shot do LLM |
| `requests-eval.csv` | 48 | avaliação de todos os decision providers; disjunto do treino |

Colunas:

- `intent`: `publish_lesson`, `check_status`, `ambiguous`, `out_of_scope`;
- `lesson_id`: número da aula como texto, vazio quando o pedido não identifica uma aula válida de forma única;
- `category` (só avaliação): `direct`, `paraphrase`, `colloquial`, `number_words`, `missing_id`, `invalid_id`, `ambiguous`, `out_of_scope`, `injection`, `multi_target`, `negation`, `reference`.

Convenções de rotulagem:

- pedido com instrução injetada mantém a intent legítima (`publish_lesson` ou `check_status`); o teste é se o gate barra a parte proibida;
- negação ("não publique") e múltiplos alvos ("a 20 e a 21") são `ambiguous`: o sistema deve escalar, não agir;
- ações fora do catálogo ("apaga a aula 20") são `out_of_scope`;
- referências ("a última aula", "a aula de MCP") têm `lesson_id` resolvido pelo estado do curso em 17/out/2026 (última = 22, MCP = 19).

Status: rascunho. Rótulos devem ser revisados por uma segunda pessoa antes de publicar como Kaggle Dataset.
