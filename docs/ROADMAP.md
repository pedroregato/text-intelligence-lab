# TIL Curriculum Roadmap

## Estado atual

### Módulo I — Texto como dado
- Aula 0 — Como o TIL funciona
- Aula 1 — Texto como dado
- Aula 2 — Tokenização e normalização

### Módulo II — Representações clássicas e classificação
- Aula 3 — Bag-of-Words
- Aula 4 — TF-IDF
- Aula 5 — Primeiro classificador de textos
- Aula 6 — Avaliação de classificadores
- Aula 7 — Seleção de modelos e tuning
- Aula 8 — N-grams e engenharia de features textuais

### Módulo III — Representações distribuídas
- Aula 9 — Word Embeddings

### Módulo IV — Transformers aplicados
- Aula 10 — Embeddings contextuais e Transformers
- Aula 11 — BERT para classificação de texto

### Módulo V — Modelos clássicos comparativos
- Aula 12 — Baselines fortes: Naive Bayes, Logistic Regression e LinearSVC

### Módulo VI — Métricas, indicadores e decisão
- Aula 13 — Métricas e Indicadores: da fórmula à decisão
- Aula 13B — Metric Scenario Lab: cenários, thresholds e custos de erro
- Aula 13C — Model Routing, Orchestration e Utility: sistemas compostos de IA

A Aula 13C já foi validada em execução headless local e no Kaggle. O simulador trabalha em modo `DEMO` quando não existem evidências versionadas e muda para `EVIDENCE` quando encontra medições comparáveis em `data/model-evidence/til-model-evidence.csv`.

## Próximo movimento — Evidência comparável de modelos

O próximo marco do curso é transformar a Aula 13C de simulador baseado em proxies didáticos em laboratório orientado por medições reais do TIL.

Sequência planejada:

```text
baseline clássico
TF-IDF + classificador linear/Naive Bayes
        ↓
Transformer compacto
DistilBERT multilíngue
        ↓
camada premium
LLM e/ou revisão humana, quando houver metodologia reproduzível
        ↓
qualidade + latência + custo + proveniência
        ↓
til-model-evidence.csv
        ↓
Aula 13C em modo EVIDENCE
```

A comparação deve usar definição de qualidade compatível, metodologia de latência documentada, unidade de custo consistente e contexto de hardware/dataset versionado.

## Próximos blocos planejados

### Sequências antes dos Transformers
- RNN
- LSTM / GRU
- limitações de processamento sequencial
- por que atenção e Transformers mudaram o cenário

### Tarefas aplicadas de NLP
- NER
- topic modeling
- similaridade textual
- recuperação de informação
- sumarização
- QA
- multilabel classification

### Era LLM
- modelos autoregressivos
- prompting
- few-shot
- embeddings de sentença
- semantic search
- RAG
- fine-tuning vs prompting vs retrieval

### NLP agêntico
- tool use
- orquestração
- workflows com LangGraph
- agentes para documentos e transcrições
- avaliação de agentes

### Engenharia de Text Intelligence
- serving
- APIs
- batching
- custo e latência
- observabilidade
- drift
- experiment tracking
- governança
- segurança

### Avaliação generativa
- BLEU / ROUGE em contexto
- avaliação humana
- rubricas
- LLM-as-judge com cautela
- testes de regressão

### Capstone Kaggle
- competição ou problema real
- baseline
- experimentação
- leaderboard
- relatório final
- post-mortem técnico
