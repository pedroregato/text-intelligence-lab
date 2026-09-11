# Estudo de caso — GitHub Project HydraFusion

## Por que este caso entra no TIL

O Project HydraFusion é útil para o TIL porque desloca a análise de **seleção de modelo** para **engenharia de sistemas compostos de IA**.

A pergunta tradicional é:

> Qual modelo apresenta a melhor qualidade?

A pergunta de engenharia passa a ser:

> Qual combinação de modelos, regras, mecanismos de avaliação e escalonamento entrega qualidade suficiente com custo, latência e risco aceitáveis?

## Estratégias

### Single
Um único modelo resolve a tarefa. É a arquitetura mais simples e previsível.

### Cascade
Um modelo mais econômico atende primeiro. Um `quality gate` decide se a resposta é suficiente ou se a tarefa deve ser escalada para um modelo mais forte.

### Critique
Um modelo produz a solução, outro avaliador ou modelo independente critica a resposta e a solução pode ser revisada antes da entrega.

## Leitura dos resultados

Nos resultados divulgados pelo GitHub, o HydraFusion apresentou redução de custo em diferentes benchmarks. A vantagem em qualidade, entretanto, não foi uniforme em todos eles.

Essa combinação é pedagogicamente importante porque mostra que comparar sistemas exige uma visão multiobjetivo.

| Dimensão | Pergunta de engenharia |
| --- | --- |
| Qualidade | O sistema resolve a tarefa suficientemente bem? |
| Custo | Quanto custa cada tarefa processada ou resolvida? |
| Latência | Quanto tempo o usuário espera? |
| Roteamento | Quantos casos chegam ao modelo premium? |
| Gate | Quantos casos difíceis são aceitos indevidamente? |
| Confiabilidade | Quantos retries, timeouts ou falhas ocorrem? |
| Humano | Quanto trabalho manual ainda é necessário? |

## Utility como instrumento didático

Uma função simples pode tornar os trade-offs explícitos:

```text
U = wq * Q - wc * C - wl * L
```

onde:

- `Q` = qualidade normalizada;
- `C` = custo normalizado;
- `L` = latência normalizada;
- `wq`, `wc`, `wl` = prioridades do negócio.

A função não pretende produzir uma verdade universal. Ela força o projetista a declarar as prioridades que normalmente ficam implícitas.

## Conexão com o TIL

O caso conecta diretamente os seguintes conceitos:

```text
Métricas de classificação
        ↓
Custos de erro
        ↓
Thresholds e abstenção
        ↓
Quality gates
        ↓
Model routing
        ↓
Model orchestration
        ↓
Compound AI Systems
```

Uma extensão natural para classificação de textos no TIL é:

```text
TF-IDF + Naive Bayes
        ↓ baixa confiança
Transformer
        ↓ caso crítico
LLM ou revisão humana
```

O objetivo não é usar sempre a camada mais sofisticada, mas direcionar capacidade computacional e humana para os casos em que ela agrega mais valor.

## Perguntas para discussão

1. Em que condições uma pequena perda de qualidade é aceitável em troca de uma grande redução de custo?
2. Como medir se o `quality gate` está escalando casos demais ou de menos?
3. Qual seria o custo de um falso aceite do gate em uma aplicação crítica?
4. Um modelo mais caro deveria sempre ser usado nos casos de baixa confiança?
5. Quando a revisão humana deve fazer parte da arquitetura?
6. Que métricas seriam necessárias para comparar dois sistemas compostos de IA?

## Leituras

- GitHub Blog — *Project HydraFusion: Frontier quality via multi-model orchestration*  
  https://github.blog/ai-and-ml/github-copilot/project-hydrafusion-frontier-quality-via-multi-model-orchestration/
- VentureBeat — *GitHub's HydraFusion cuts AI coding costs in every benchmark. It only matches quality in one*  
  https://venturebeat.com/orchestration/githubs-hydrafusion-cuts-ai-coding-costs-in-every-benchmark-it-only-matches-quality-in-one

## Nota metodológica

Benchmarks não devem ser tratados como propriedades permanentes de um sistema. Resultados dependem de dataset, configuração, conjunto de modelos, preços, critérios de avaliação e versão das ferramentas. No TIL, o caso deve ser usado para ensinar **como raciocinar sobre trade-offs**, não para declarar um vencedor definitivo.
