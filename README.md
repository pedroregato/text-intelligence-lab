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
| 14 | LLM Foundations: da classificação à geração — `Draft` |

A próxima unidade especificada é a **Aula 14 — LLM Foundations: da classificação à geração**. Depois dela, a trilha avança para Retrieval/Grounding, Tools/Workflows e Agentic Systems.

## Organização conceitual

O TIL passa a organizar sua evolução em quatro macrocamadas:

```text
I — Text Intelligence
→ texto, representações, features e tarefas

II — Model Engineering
→ modelos, treinamento, comparação e avaliação

III — Intelligent Orchestration
→ routing, quality gates, cascades e utility

IV — Agentic Systems
→ tools, workflows, execução e autonomia
```

A **Aula 13C** é o ponto formal de transição entre Model Engineering e Intelligent Orchestration e prepara a entrada em Agentic Systems.

Observabilidade, segurança, governança, reprodutibilidade, custo, latência, avaliação e supervisão humana são dimensões transversais, não apenas um módulo final.

A especificação arquitetural está registrada em `docs/architecture/TIL-AIE-001-agentic-intelligence-evolution.md`.

Capstone — Kaggle permanece como etapa integradora futura.

## Da avaliação de modelos à avaliação de sistemas

A partir da Aula 13, o TIL amplia a pergunta de avaliação:

```text
Qual modelo tem a maior métrica?
            ↓
Qual sistema entrega valor suficiente
com qualidade, custo, latência e risco aceitáveis?
```

O laboratório **13C — Model Routing, Orchestration e Utility** introduz `single`, `cascade`, `quality gates`, funções de utilidade e métricas de sistemas orquestrados.

A aula agora também inclui um estudo de caso sobre a transição de **Model Intelligence para Agentic Systems**, usando o GPT-6 Astra como exemplo contemporâneo para separar `benchmark`, `capability`, `autonomy`, `utility`, `risk` e `marketing`.

```text
Model
→ Selection
→ Routing
→ Orchestration
→ Tools
→ Computer Use
→ Agentic Execution
→ Observability
→ Human Oversight
→ Utility
```

O Project HydraFusion permanece como referência de sistemas compostos, enquanto o case Astra amplia a discussão para sistemas agentes com ferramentas e execução.

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

O experimento **EDU-ORCH-001 — Baseline vs Transformer Evidence Lab** foi concluído e produziu o primeiro conjunto real de evidências do curso:

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

Resultados medidos no conjunto de teste (`n = 3807`):

| Métrica | TF-IDF + MultinomialNB | DistilBERT multilingual |
| --- | ---: | ---: |
| F1 macro | 0.9099 | 0.9300 |
| Accuracy | 0.9241 | 0.9406 |
| Latência média | 1.09 ms | 34.38 ms |
| Runtime proxy / 1000 | 0.030 s | 52.00 s |

O notebook experimental está em:

```text
experiments/edu-orch-001-baseline-vs-transformer/
```

A execução GPU inicial revelou um caso real de incompatibilidade de runtime: a Tesla P100 atribuída pelo Kaggle possui compute capability `sm_60`, enquanto o build observado do PyTorch 2.10.0+cu128 suportava `sm_70` ou superior. A falha foi reproduzida com uma operação CUDA mínima, isolando o problema do `Trainer` e do DistilBERT.

A coleta oficial foi concluída em CPU. Por isso, os valores absolutos de latência e runtime não devem ser generalizados para outros hardwares ou GPUs compatíveis.

Esse episódio também refinou a política de engenharia do TIL: **GPU detectada não significa GPU operacional**. Experimentos acelerados devem validar compute capability, build do framework e uma operação mínima antes do treinamento principal.

## Routing medido — EDU-ORCH-002

O **EDU-ORCH-002 — Routing Evidence Matrix** mediu diretamente uma arquitetura cascade entre o baseline clássico e o DistilBERT, usando thresholds de confiança do baseline.

Resultados no mesmo conjunto de teste (`n = 3807`):

| Threshold | F1 macro | Accuracy | Escalation rate | Runtime proxy / 1000 | Latência média |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0.60 | 0.9178 | 0.9307 | 3.94% | 4.49 s | 5.13 ms |
| 0.70 | 0.9248 | 0.9364 | 8.25% | 8.97 s | 12.20 ms |
| 0.80 | 0.9330 | 0.9433 | 14.42% | 15.42 s | 22.28 ms |
| 0.90 | 0.9318 | 0.9422 | 23.46% | 25.15 s | 34.01 ms |

O threshold `0.80` apresentou o maior F1 observado entre os quatro cenários medidos. O threshold `0.90` escalou mais casos e consumiu mais runtime, sem melhorar a qualidade observada.

A evidência está versionada em:

```text
data/model-evidence/til-routing-evidence.csv
```

As linhas usam `evidence_status = measured-recovered`: os valores vieram da execução medida do Kaggle, mas o CSV precisou ser reconstruído a partir do output observado após perda do artefato original da sessão. Essa distinção preserva a proveniência e evita apresentar dados recuperados como se o artefato original estivesse intacto.

A arquitetura pedagógica também foi refinada:

```text
experimentos
→ produzem evidência

aulas
→ consomem evidência
```

O `EDU-ORCH-002` permanece como trilha **AUTHOR / EVIDENCE**, enquanto a Aula 13C funciona como trilha **STUDENT** e não exige treinamento longo do Transformer para explorar routing, escalation rate, latência, custo e utility.

## Glossário Vivo

O curso possui um glossário bilíngue PT-BR/EN, mantido a partir de fontes estruturadas:

```text
glossary.yaml
+ glossary.extensions.yaml
        ↓
glossary.pt-BR.md
glossary.en.md
web/index.html
```

`glossary.yaml` mantém a base estável; `glossary.extensions.yaml` recebe pequenas adições curriculares. O gerador mescla as duas fontes e rejeita IDs duplicados.

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

As Aulas 0–13 e os laboratórios 13B e 13C possuem material oficial no repositório. A 13C possui execução Kaggle validada, segue o padrão headless-first e já opera em modo `EVIDENCE` com medições reais do TIL.

O **EDU-ORCH-001** foi concluído e versionou a primeira comparação medida entre um baseline clássico e um Transformer.

O **EDU-ORCH-002** também foi concluído, medindo diretamente quatro configurações de routing/cascade. A Aula 13C agora pode consumir evidência de modelos isolados e de arquiteturas compostas.

A Aula 13C também passou a cobrir a transição de **Model Intelligence para Agentic Systems**, conectando routing, orchestration, tools, computer use, observability, human oversight e utility.

O próximo movimento curricular é avançar de Intelligent Orchestration para LLM Foundations, Retrieval/Grounding, Tools/Workflows e Agentic Systems, preservando o princípio de que toda complexidade adicional deve ser justificada por evidência.

## Licenciamento

A política de licenciamento está sendo formalizada em ADR específico antes da publicação ampla do material.

## Qualidade

O projeto segue o `docs/TIL-COURSE-DESIGN-CONTRACT.md`, que define critérios pedagógicos, técnicos, de reprodutibilidade e de integração com o Glossário Vivo.
