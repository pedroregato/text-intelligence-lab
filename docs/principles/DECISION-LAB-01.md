# TIL-EP-001 — Decision Lab: arquiteturas sob evidência incompleta

**Estado:** piloto pedagógico proposto · **Modalidade:** exercício de interpretação e decisão, sem código obrigatório.  
**Objetivo:** usar os princípios do TIL para justificar uma arquitetura, contestar a própria escolha e identificar evidências ausentes.  
**Pré-requisitos:** [catálogo de princípios](engineering-principles.md) e [protocolo de revisão](REVIEW-AND-ADOPTION.md).

> **Regra pedagógica:** escolha uma decisão, não um slogan. É legítimo recomendar um experimento adicional, uma solução simples ou suspender uma implantação.

## 1. Caso — triagem de documentos (cenário inteiramente fictício)

Uma equipe quer classificar documentos recebidos em cinco categorias. Ela considera três alternativas:

- **A — Baseline clássico:** TF-IDF + classificador supervisionado; requer revisão humana para casos de baixa confiança.
- **B — Transformer:** classificador mais complexo; mantém a mesma revisão humana para casos de baixa confiança.
- **C — Agente com ferramentas:** usa classificador, roteia consultas a ferramentas e oferece tratamento de exceções; também mantém a revisão humana.

A equipe apresenta o seguinte **quadro hipotético criado apenas para esta atividade**. **Não** é resultado de notebook, medição de Kaggle, benchmark ou produção. Todos os valores e limiares são ilustrativos.

| Indicador fictício | A | B | C |
|---|---:|---:|---:|
| Macro-F1 em um único holdout | 0,88 | 0,90 | 0,90 |
| Custo relativo por 1.000 documentos (proxy) | 1,0 | 2,4 | 5,3 |
| Latência p95 em segundos (proxy) | 0,8 | 2,6 | 7,5 |
| Taxa de encaminhamento para revisão humana | 12% | 10% | 9% |
| Violações de autorização registradas no teste | 0 | 0 | 0 |

**Restrições informadas:** os documentos podem incluir dados pessoais; não existe validação de campo independente, estimativa de custo de revisão humana, intervalo de confiança para as diferenças de F1, nem evidência de que o agente resolve exceções melhor que A/B. A avaliação foi feita apenas com registros históricos, sem monitoramento de drift.

**Solicitação da gestão:** “Recomende uma arquitetura para piloto e diga se já podemos automatizar toda a operação.”

## 2. Sua decisão — antes de consultar a referência

Preencha uma resposta curta:

| Campo | Sua análise |
|---|---|
| Decisão provisória | Qual alternativa levaria ao piloto, ou por que suspenderia a escolha? |
| Objetivo e restrições | Que medida define sucesso e quais limites são inegociáveis? |
| Benefício incremental alegado | Que vantagem de B ou C é de fato observada? |
| Benefício não demonstrado | Que alegações seriam exageradas? |
| Mecanismos compartilhados | Que controles impedem atribuir ganhos à arquitetura? |
| Métricas ausentes | Qual dado ou teste poderia mudar a decisão? |
| Condição de reversão | Que nova evidência faria você mudar de alternativa? |
| Governança | Quais controles antecedem um eventual side effect? |

### Perguntas de aprofundamento

1. A diferença entre macro-F1 0,88 e 0,90 **é suficiente**, isoladamente, para justificar C? Por quê?
2. `risk_violations=0` comprova segurança? Que ensaio seria necessário?
3. Se C produz resumos explicativos, isso demonstra que classificou melhor?
4. A variação de revisão humana (12% → 9%) representa economia líquida? Quais custos faltam?
5. Quais dos princípios 001–008 você usou para fundamentar sua análise? Cite pelo menos **três** e associe cada um a uma afirmação concreta da sua decisão.

## 3. Teste adversarial

Antes de concluir, critique sua própria recomendação usando duas mudanças hipotéticas **independentes**:

- **Mudança X:** existe uma obrigação contratual comprovada de manter uma cadeia explícita de decisões e aprovações, com trilha auditável.
- **Mudança Y:** uma avaliação independente revela grande heterogeneidade por categoria; a média macro-F1 agregada não representa adequadamente a classe de maior custo de erro.

Explique **se** e **por que** sua decisão mudaria. Não presuma que rastreabilidade exige LLM ou agente: workflows tradicionais também podem fornecê-la.

## 4. Rubrica formativa

Avalie cada critério como `Atendeu`, `Parcial` ou `Ainda não`, acompanhando uma justificativa. A atividade **não** exige que todos escolham a mesma arquitetura.

| Critério | Evidência de atendimento |
|---|---|
| Comparabilidade | Não mistura custo de entrega com custo de rejeição, nem compara resultados não equivalentes |
| Honestidade epistêmica | Distingue dado fornecido, hipótese, interpretação e ausência de evidência |
| Causalidade | Não atribui à complexidade um ganho devido a mecanismo compartilhado |
| Utility | Considera qualidade, custo, latência, intervenção humana e risco |
| Segurança/governança | Não conclui segurança a partir de zero violações sem teste sensível |
| Contestabilidade | Explicita o experimento que poderia refutar a escolha |
| Comunicação | Entrega recomendação **condicional** e defensável à gestão |

### Respostas de referência — consultar somente após sua tentativa

<details>
<summary>Exibir uma possível análise (não é o único gabarito)</summary>

**Decisão provisória plausível:** recomendar A como baseline para **piloto supervisionado**, sem automatizar integralmente. Outra resposta aceitável é **adiar a seleção final** e pedir testes adicionais. Nenhuma das duas equivale a provar superioridade universal de A.

**Por que não selecionar automaticamente C?** A macro-F1 ilustrativa é igual à de B e apenas 0,02 acima de A, num único holdout sem incerteza quantificada. O custo e a latência proxies são maiores. Não existe evidência de ganho incremental de resolução de exceções pelo agente.

**Quais evidências faltam?** Intervalos de incerteza, avaliação por categoria e custo de erro, validação temporal/externa, drift, custo completo da revisão humana, controles de autorização, teste capaz de revelar violações, privacidade dos dados, qualidade das explicações e observabilidade.

**Mudança X:** uma trilha auditável passa a ser requisito, mas pode ser atendida por workflow determinístico ou camada de orquestração auditável; não justifica C automaticamente.

**Mudança Y:** diferenças por categoria podem inverter a escolha; avaliar custos de falso positivo/negativo e métricas específicas da classe crítica antes de decidir.

**Princípios envolvidos:** 001/002 (ônus do benefício incremental), 003/005 (atribuição de mecanismos), 004 (evitar preferência prévia), 007 (não ganho é resultado) e 008 (políticas e guards, mesmo sem agente).

**Condição de revisão:** adotar B ou C somente se novos testes mostrarem ganho material na tarefa relevante ou se uma exigência de governança não atendida por opções mais simples tornar a complexidade proporcional ao risco.

</details>

## 5. Nota ao instrutor — validação pedagógica

Este é um **exercício de desenho curricular**, ainda não testado com alunos. Para sua homologação, pedir que ao menos um estudante ou revisor produza decisão independente **antes** de ler a resposta de referência; inspecionar justificativa, confundimento, custo e condição de reversão. Ajustar a atividade se ela induzir escolha por marca de tecnologia ou respostas de memorização.

**Gatilho para atualização:** se alunos acertam a alternativa por eliminação mas não conseguem defender o contrafactual, o exercício ainda não demonstra julgamento de engenharia.

**Separação de fontes:** os números e restrições desta página são inventados para ensino; **não** devem entrar no repositório de evidências medidas nem em relatórios de desempenho do TIL.
