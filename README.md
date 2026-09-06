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
Aulas 10–11

Módulo V — LLMs, RAG e agentes
Em planejamento

Módulo VI — Engenharia, avaliação e produção
Em planejamento

Capstone — Kaggle
Em planejamento
```

## Glossário Vivo

O curso possui um glossário bilíngue PT-BR/EN, mantido a partir de uma fonte canônica estruturada:

```text
docs/glossary/glossary.yaml
→ glossary.pt-BR.md
→ glossary.en.md
→ web/index.html
```

Os notebooks apontam para o glossário nos conceitos centrais de cada aula.

## Princípio de engenharia

```text
Arquitetar
→ Implementar pequeno
→ Executar
→ Observar
→ Avaliar
→ Corrigir
→ Versionar
→ Expandir
```

## Reprodutibilidade

O GitHub é a fonte de verdade do projeto.

Os notebooks oficiais usam **internet desabilitada por padrão**. A internet é habilitada apenas quando uma dependência externa fizer parte intencional do objetivo pedagógico.

Dados pequenos podem ser embutidos no notebook. Datasets maiores e modelos externos devem, quando apropriado, ser versionados ou anexados via recursos do Kaggle.

## Execução

```text
GitHub
  ↓
Git local / PyCharm / Codex
  ↓
Kaggle CLI / Kaggle UI
  ↓
Kaggle Notebooks
```

Detalhes de infraestrutura, arquitetura de execução e runbooks estão em `docs/ENGINEERING.md`.

## Estrutura do repositório

```text
text-intelligence-lab/
├── course/
├── data/
├── docs/
│   ├── decisions/
│   ├── experiments/
│   ├── glossary/
│   ├── readiness/
│   ├── runbooks/
│   └── templates/
├── experiments/
├── requirements/
├── README.md
└── setup_structure.py
```

## Status

O curso está em construção ativa.

As Aulas 0–11 já possuem notebooks oficiais no repositório e estão sendo revisadas tecnicamente e pedagogicamente antes de serem marcadas como prontas para alunos.

## Licenciamento

A política de licenciamento está sendo formalizada em ADR específico antes da publicação ampla do material.

## Qualidade

O projeto segue o `docs/TIL-COURSE-DESIGN-CONTRACT.md`, que define critérios pedagógicos, técnicos, de reprodutibilidade e de integração com o Glossário Vivo.
