# TIL-EP-001 — Ficha aplicada de decisão: Aula 21

**Estado:** exemplo didático de aplicação, não decisão arquitetural universal.  
**Fontes:** [notebook da Aula 21](../../course/21-planning-and-goal-decomposition/21-til-planning-and-goal-decomposition.ipynb), [registro de validação](../readiness/AULA-21-EVIDENCE-REVIEW-2026-10-17.md).  
**Princípios exercitados:** 001, 002, 003, 005, 006, 007, 008.

## Pergunta da decisão

Para **publicar uma aula num ambiente simulado e delimitado**, precisamos introduzir planning ou replanning, além de um executor reativo protegido por guards?

**Hipótese:** planning/replanning poderia justificar seu overhead por segurança, redução de retrabalho ou melhoria de coordenação. A hipótese **não** deve ser tratada como resultado observado.

## Alternativas examinadas

| Variante | Diferença principal | Proteção comum |
|---|---|---|
| Reactive + Guards | Próxima ação por política fixa, sem plano persistido | Guard de autorização e status |
| Planning + Guards | Plano explícito, validado antes de executar | Mesmo guard |
| Planning + Guards + Replanning | Registra plano v2 após mudança de estado | Mesmo guard |

## Comparabilidade antes de custo

Os custos somente são interpretáveis como comparação de eficiência quando tarefa, regras, resultado alcançado e restrições relevantes são equivalentes. **A publicação em `contract_violation` não é comparação de eficiência:** um sistema conclui o objetivo e outro o rejeita sem executar.

## Evidência disponível

Nos cenários básicos comparáveis (custos proxy, não reais):

| Cenário | Reactive | Plan-based | Diferença (planning − reactive) |
|---|---:|---:|---:|
| `simple_ready` | 6.0 | 8.5 | +2.5 |
| `not_ready` | 2.0 | 4.5 | +2.5 |
| `state_changes` | 5.0 | 9.0 | +4.0 |

Esses números constam da revisão executada da Aula 21 e são **unidades didáticas arbitrárias**. `not_ready` e `state_changes` representam interrupções apropriadas da publicação, não sucesso de publicação. É importante comparar resultados equivalentes (inclusive interrupções de segurança com a mesma finalidade), mas não interpretar essa comparação como custo por publicação bem-sucedida.

**Observações:** os guards interrompem publicação insegura nas variantes comparadas; `replan:v2` prova que um plano de recuperação foi construído, mas não prova ganho independente de segurança. O cenário de contrato rejeita um plano que poderia, em uma sequência protegida, publicar com segurança.

**Não demonstrado:** economia financeira, latência real, mitigação de incidentes em produção, vantagem de planning em tarefas complexas ou eficácia estatística de `risk_violations` (coluna constante nos cenários).

## Decisão contextual

**Não há evidência, nos cenários estudados, para preferir planning pelo critério de menor custo ou maior segurança de publicação.** Não concluir que planning nunca tem valor. Dependências externas, auditoria e obrigações contratuais podem tornar sua adoção justificável por critérios adicionais, mesmo sem economia no proxy.

## Como contestar esta conclusão

1. Modelar uma tarefa com dependências reais na qual a sequência reativa incorra em retrabalho mensurável.
2. Garantir que as três variantes recebam a mesma informação, política de autorização e limites de orçamento.
3. Registrar objetivo, sucesso, interrupção segura, custo, latência real (se medida), falhas e intervenções.
4. Repetir execuções em amostra representativa; quantificar incerteza, quando aplicável.
5. Se o planejamento produzir ganho incremental que supere overhead e risco, **revisar a decisão para aquele contexto**, mantendo o histórico.

## Ficha de conformidade (exemplo)

| Princípio | Aplicação verificável | Resultado no caso |
|---|---|---|
| 001 / 002 | Baseline, mecanismos e custo incremental explícitos | Atendido no escopo do laboratório |
| 003 | Separar o efeito do guard do efeito do planner | Atendido na análise; causalidade adicional não demonstrada |
| 005 | Não deduzir mecanismo apenas pelo resultado | Atendido ao inspecionar traces |
| 006 | Rejeição contratual ≠ incidente evitado | Atendido na interpretação |
| 007 | Relatar o não ganho sem transformar em falha do aluno | Atendido no exercício |
| 008 | Validar estado e autorização antes de publicação | Atendido na simulação, não extrapolável para produção |

**Juízo de revisão:** a ficha ilustra como aplicar o framework; **não** equivale à adoção formal dos princípios ou à aprovação de uma arquitetura empresarial.
