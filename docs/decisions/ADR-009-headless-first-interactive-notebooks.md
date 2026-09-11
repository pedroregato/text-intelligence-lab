# ADR-009 — Headless-first interactive notebooks

## Status

Accepted

## Context

A Aula 13C introduziu interatividade com `ipywidgets`, callbacks e gráficos dinâmicos. A primeira publicação no Kaggle permaneceu em execução indefinidamente, embora o código computacional fosse pequeno.

A versão corrigida removeu renderização automática, tornou a interação acionada por botão, reduziu dependências do estado dos widgets, controlou a busca de arquivos em `/kaggle/input` e fechou figuras Matplotlib após uso.

A versão corrigida foi validada em duas etapas:

1. execução local headless com `jupyter nbconvert --execute`;
2. execução completa no Kaggle.

Esse episódio mostrou que um notebook educacional interativo precisa separar claramente a execução determinística da camada de interação do aluno.

## Decision

Todos os notebooks oficiais do TIL adotarão o princípio **headless-first**.

```text
Notebook
  ├── camada determinística
  │     └── Run All deve terminar sem intervenção humana
  │
  └── camada interativa
        └── opcional e acionada pelo aluno
```

A interatividade nunca poderá ser condição para a execução completa do notebook.

Para widgets e visualizações interativas:

- evitar `render()` automático ao final de células interativas;
- preferir botões explícitos para ações que recalculam cenários;
- não exigir callbacks para produzir os resultados mínimos da aula;
- manter resultados estáticos suficientes para leitura e revisão;
- fechar figuras após exibição quando aplicável;
- limitar varreduras de arquivos a caminhos previsíveis;
- validar localmente em modo headless antes da publicação no Kaggle quando a aula incluir interação relevante.

## Alternatives Considered

### Interatividade como fluxo principal

Rejeitada porque torna a execução dependente do front-end e dificulta validação automatizada e reprodução.

### Remover widgets de todas as aulas

Rejeitada porque a interação tem valor pedagógico em laboratórios de cenários, thresholds, métricas e trade-offs.

### Manter widgets com execução automática

Rejeitada porque o caso da Aula 13C demonstrou risco operacional sem benefício pedagógico necessário.

## Consequences

### Positive

- maior reprodutibilidade;
- menor risco de notebooks presos em `RUNNING`;
- melhor compatibilidade com Kaggle `Run All`, CI e `nbconvert`;
- aluno ainda pode explorar cenários de forma interativa;
- outputs salvos continuam úteis mesmo quando widgets não estão ativos.

### Trade-offs

- algumas aulas terão uma pequena duplicação entre resultado estático e ferramenta interativa;
- callbacks precisarão ser desenhados com mais cuidado;
- testes de publicação passam a incluir uma validação headless explícita.

## Validation Reference

Aula 13C — `course/13-metrics-and-indicators/13c-model-routing-and-orchestration.ipynb`.

A execução corrigida completou localmente via `nbconvert` e posteriormente no Kaggle.