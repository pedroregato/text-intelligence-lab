# Text Intelligence Lab (TIL) with Kaggle

Laboratório educacional e experimental de **Text Intelligence, NLP, Machine Learning, Transformers e LLMs**, construído com foco em compreensão, experimentação, reprodutibilidade e engenharia aplicada.

O TIL foi desenhado para ensinar a transformar texto em dados, features, modelos e sistemas capazes de apoiar decisões reais.

## Para quem é este curso

O curso é indicado para quem deseja avançar de fundamentos de NLP até sistemas modernos de linguagem, com uma abordagem prática e orientada a experimentos.

Você não precisa começar dominando Transformers ou LLMs. A progressão parte do texto como dado e constrói os conceitos gradualmente.

## Como estudar

A unidade principal de aprendizagem é o notebook no Kaggle.

```text
Notebook oficial = referência do curso
Cópia do aluno    = ambiente pessoal de aprendizagem
```

Fluxo recomendado:

```text
Ler
→ Executar
→ Observar
→ Interpretar
→ Resolver exercício
→ Comparar solução
→ Registrar aprendizado
```

## Trilha atual

| Aula | Tema |
| --- | --- |
| 0 | Como o TIL funciona e validação do ambiente |
| 1 | Texto como dado |
| 2 | Tokenização e normalização |
| 3 | Bag-of-Words |
| 4 | TF-IDF |
| 5 | Primeiro classificador de textos |
| 6 | Avaliação de classificadores |
| 7 | Seleção de modelos e tuning |
| 8 | N-grams e engenharia de features textuais |
| 9 | Word Embeddings |
| 10 | Embeddings contextuais e Transformers |
| 11 | BERT para classificação de texto |
| 12 | Baselines clássicos fortes |
| 13 | Métricas e indicadores: da fórmula à decisão |
| 13B | Metric Scenario Lab: cenários, thresholds e custos de erro |
| 13C | Model Routing, Orchestration e Utility: sistemas compostos de IA |

A trilha continua em desenvolvimento com tarefas aplicadas de NLP, LLMs, RAG, agentes, avaliação avançada, observabilidade e capstone Kaggle.

## Organização conceitual

```text
Módulo I — Texto como dado
Aulas 0–2

Módulo II — Representações clássicas e classificação
Aulas 3–8

Módulo III — Representações distribuídas
Aula 9

Módulo IV — Transformers aplicados
Aulas 10–12

Módulo V — Avaliação, métricas e decisões de engenharia
Aula 13 + Labs 13B e 13C

Módulo VI — LLMs, RAG, agentes e sistemas compostos
Em desenvolvimento

Módulo VII — Engenharia, observabilidade e produção
Em planejamento

Capstone — Kaggle
Em planejamento
```

## Da avaliação de modelos à avaliação de sistemas

A partir da Aula 13, o TIL amplia a pergunta de avaliação:

```text
Qual modelo tem a maior métrica?
            ↓
Qual sistema entrega valor suficiente
com qualidade, custo, latência e risco aceitáveis?
```

O laboratório **13C — Model Routing, Orchestration e Utility** introduz `single`, `cascade`, `quality gates`, funções de utilidade e métricas de sistemas orquestrados, usando o Project HydraFusion como estudo de caso contemporâneo.

A Aula 13C foi validada em duas camadas: execução headless local via `nbconvert` e execução completa no Kaggle. A partir dessa validação, o TIL adotou oficialmente a regra **headless-first** para notebooks interativos.

```text
camada determinística
        ↓
Run All deve terminar sem intervenção humana
        ↓
camada interativa opcional
```

A decisão está registrada em `docs/decisions/ADR-009-headless-first-interactive-notebooks.md`.

## Evidência real para a Aula 13C

A Aula 13C funciona em dois modos:

- `DEMO` — proxies didáticos explicitamente sintéticos;
- `EVIDENCE` — medições versionadas e comparáveis do próprio TIL.

O experimento **EDU-ORCH-001 — Baseline vs Transformer Evidence Lab** está em execução para produzir o primeiro conjunto real de evidências do curso:

```text
Olist / Polarity
        ↓
TF-IDF + Multinomial Naive Bayes
        ↕
DistilBERT multilingual
        ↓
F1 macro + accuracy
+ latência média/p50/p95
+ proxy de custo computacional
+ hardware + versões + proveniência
        ↓
data/model-evidence/til-model-evidence.csv
        ↓
Aula 13C em modo EVIDENCE
```

O notebook experimental está em:

```text
experiments/edu-orch-001-baseline-vs-transformer/
```

A execução GPU inicial revelou um caso real de incompatibilidade de runtime: a Tesla P100 atribuída pelo Kaggle possui compute capability `sm_60`, enquanto o build observado do PyTorch 2.10.0+cu128 suportava `sm_70` ou superior. A falha foi reproduzida com uma operação CUDA mínima, isolando o problema do `Trainer` e do DistilBERT.

A coleta de evidência segue temporariamente em CPU, com a decisão documentada em `docs/experiments/EDU-ORCH-001-model-evidence-baseline-vs-transformer.md`. Nenhuma métrica comparativa é publicada antes da conclusão e revisão da execução.

Esse episódio também refinou a política de engenharia do TIL: **GPU detectada não significa GPU operacional**. Experimentos acelerados devem validar compute capability, build do framework e uma operação mínima antes do treinamento principal.

## Glossário Vivo

O curso possui um glossário bilíngue PT-BR/EN, mantido a partir de uma fonte canônica estruturada:

```text
docs/glossary/glossary.yaml
→ glossary.pt-BR.md
→ glossary.en.md
→ web/index.html
```

Os notebooks apontam para o glossário nos conceitos centrais de cada aula.

## Biblioteca Viva de Referências

O TIL também mantém referências externas em uma fonte canônica estruturada:

```text
docs/references/references.yaml
```

Cada item registra tipo da fonte, papel (`primary`, `secondary` ou `commentary`), temas, aulas relacionadas, resumo, uso pedagógico, limitações e estado de revisão.

O objetivo não é acumular links, mas transformar referências em uma cadeia de aprendizagem:

```text
Evidência
→ contexto
→ leitura crítica
→ conceito
→ experimento
```

Sempre que possível, o TIL combina **fonte primária + análise independente**. O primeiro conjunto oficial dessa abordagem usa o Project HydraFusion e conecta a fonte técnica do GitHub a uma análise crítica da VentureBeat.

A política e o fluxo editorial estão documentados em `docs/references/README.md`.

## Princípio de engenharia

```text
Arquitetar
→ Implementar pequeno
→ Executar headless
→ Executar no Kaggle
→ Observar
→ Avaliar
→ Corrigir
→ Versionar
→ Expandir
```

## Reprodutibilidade

O GitHub é a fonte de verdade do projeto.

Os notebooks oficiais usam **internet desabilitada por padrão**. A internet é habilitada apenas quando uma dependência externa fizer parte intencionalmente do objetivo pedagógico.

Dados pequenos podem ser embutidos no notebook. Datasets maiores e modelos externos devem, quando apropriado, ser versionados ou anexados via recursos do Kaggle.

A interatividade é uma camada pedagógica adicional: nenhum notebook oficial deve depender de cliques, callbacks ou widgets ativos para concluir uma execução `Run All`.

## Execução

```text
GitHub
  ↓
Git local / PyCharm / Codex
  ↓
validação headless local
  ↓
Kaggle CLI / Kaggle UI
  ↓
Kaggle Notebooks
```

Detalhes de infraestrutura, arquitetura de execução e políticas estão em `docs/ENGINEERING.md`.

## Estrutura do repositório

```text
text-intelligence-lab/
├── course/
├── data/
│   └── model-evidence/
├── docs/
│   ├── case-studies/
│   ├── decisions/
│   ├── experiments/
│   ├── glossary/
│   ├── references/
│   ├── readiness/
│   ├── runbooks/
│   └── templates/
├── experiments/
│   └── edu-orch-001-baseline-vs-transformer/
├── requirements/
├── README.md
└── setup_structure.py
```

## Status

O curso está em construção ativa.

As Aulas 0–13 e os laboratórios 13B e 13C possuem material oficial no repositório. A 13C possui execução Kaggle validada e segue o padrão headless-first.

O marco técnico atual é o **EDU-ORCH-001**, que está coletando evidência comparável entre um baseline clássico e um Transformer para ativar o modo `EVIDENCE` da Aula 13C com medições reais do TIL.

## Licenciamento

A política de licenciamento está sendo formalizada em ADR específico antes da publicação ampla do material.

## Qualidade

O projeto segue o `docs/TIL-COURSE-DESIGN-CONTRACT.md`, que define critérios pedagógicos, técnicos, de reprodutibilidade e de integração com o Glossário Vivo.
