# TIL-EP-001 — Revisão crítica e protocolo de adoção

**Status deste documento:** proposta editorial para revisão humana. Nenhum princípio é promovido automaticamente.

## 1. Avaliação crítica

O catálogo inicial é valioso porque preserva oito formulações fortes e conecta ciência experimental, arquitetura e governança. Contudo, uma primeira revisão identificou quatro riscos:

1. **Confusão entre prescrição e hipótese.** “Deve haver evidência” é um princípio normativo; não é proposição estatística testada por um único caso. A inspeção deve verificar a **decisão que aplica o princípio**.
2. **Circularidade.** Uma arquitetura pode ser declarada “útil” pelo simples fato de possuir o mecanismo cuja utilidade se pretende demonstrar. Exigir baseline, resultado observável e custo adicional.
3. **Extrapolação indevida.** O experimento simulado da Aula 21 mostra comportamento sob regras pré-definidas, não níveis de segurança, desempenho ou economia em produção.
4. **Governança ritualística.** Uma checklist preenchida pode ser confundida com boa decisão. Exigir justificativa contextual, exceções registradas e possibilidade de contestar o julgamento.

Os princípios **001 e 004** podem se sobrepor (preferência prévia e justificação da complexidade), mas têm perguntas distintas: o 001 examina o *ônus da complexidade*; o 004 examina *viés de escolha e desenho experimental*. Os princípios **003 e 005** também são próximos, porém 003 trata *atribuição de efeito a um mecanismo compartilhado* e 005 trata *inferência indevida de mecanismo a partir de desfecho*. Manter IDs distintos, sem multiplicar formulações equivalentes.

## 2. Como avaliar uma aplicação

Cada alegação de conformidade deve preencher a ficha abaixo:

| Campo | Pergunta | Exemplo Aula 21 |
|---|---|---|
| Decisão | O que precisa ser escolhido? | Reactive com guard vs planning com guard |
| Contexto | Quais condições e restrições importam? | Publicação simulada, três cenários comparáveis |
| Alternativas | Qual baseline viável foi considerado? | `reactive` |
| Hipótese | Que ganho incremental foi esperado? | Replanning poderia acrescentar recuperação/segurança |
| Critério | Qual dado tornaria esse ganho observável? | Resultado, `cost_proxy`, traces, `replans` |
| Mecanismos comuns | Quais proteções os dois caminhos compartilham? | Guard de aprovação e prontidão |
| Evidência | Qual fonte reproduzível sustenta a observação? | Notebook e relatório da Aula 21 |
| Resultado | O que foi efetivamente observado? | Ambos interrompem publicação insegura no estado alterado |
| Limitação | O que o experimento **não** prova? | Não mede incidentes, preços ou latência reais |
| Decisão | A complexidade adicional se justifica? | Não demonstrada nesses cenários, sem generalização |
| Contestação | Que novo teste poderia mudar a conclusão? | Cenário controlado com ganho em retrabalho ou coordenação |

### Níveis de alegação

- **Observado:** apoiado por saída/trace verificável de experimento identificado.
- **Interpretado:** inferência plausível, com condições e limites explicitados.
- **Hipótese:** expectativa a testar; não escrever como resultado.
- **Não demonstrado:** dados insuficientes para sustentar alegação, inclusive quando há coluna constante.
- **Decisão normativa:** escolha baseada em valor, risco, política ou contrato; não disfarçar como estimativa empírica.

Uma observação pode ser verdadeira sem identificar seu mecanismo causal. “Sem evidência de benefício” não significa “evidência de ausência universal de benefício”.

## 3. Desafio adversarial obrigatório

Antes de qualificar um princípio como Reviewed, um revisor deve tentar encontrar pelo menos:

- um cenário em que aplicar o lema literalmente seria insuficiente para decidir;
- uma obrigação relevante não refletida nas métricas (ex.: compliance, direito de auditoria ou segurança);
- uma explicação causal alternativa para o resultado invocado;
- um cenário, fonte ou métrica que possa enfraquecer a interpretação atual;
- um custo de aplicar o princípio (instrumentação, revisão, atraso, complexidade adicional).

O teste adversarial não serve para “derrubar” qualquer lema: serve para definir seu alcance.

## 4. Protocolo de mudança de status

| Status | Condição de entrada | Evidência mínima |
|---|---|---|
| Proposed | Redação, ID, proveniência e teste de aplicação | Fonte do lema + critério + limite |
| Reviewed | Revisão técnica e pedagógica humana registrada | Ficha preenchida + contraponto + eventuais ressalvas |
| Adopted | Decisão de adoção explícita com escopo | Aprovação identificável, vínculo a decisão/ADR se normativa |
| Revised | Revisão substancial preservando história | Motivo, diff, impacto curricular, versão |
| Deprecated | Não recomendado para novas decisões | Motivo, substituto se aplicável, efeitos retroativos |

**Não promover status exclusivamente por PASS de CI, execução Kaggle, quantidade de exemplos ou aprovação de um único notebook.** O primeiro PR continua Draft enquanto os comentários humanos não forem resolvidos.

## 5. Rubrica de revisão proposta

Pontuar cada dimensão como `Pass`, `Needs work` ou `Not applicable`, com justificativa (sem score total mágico):

1. **Fidelidade:** o lema original foi preservado e contextualizado?
2. **Acionabilidade:** o decisor sabe qual evidência coletar?
3. **Auditabilidade:** existem documentos, traces ou resultados rastreáveis?
4. **Distinção causal:** efeito observado, atribuição e hipótese são separados?
5. **Proporcionalidade:** a burocracia e custo do princípio são proporcionais ao risco?
6. **Contraexemplo:** contexto, exceção e limitação aparecem?
7. **Convivência:** não duplica conceitos do glossário, ADRs ou do contrato pedagógico?
8. **Qualidade curricular:** melhora a capacidade de julgar, não apenas memorizar slogans?

**Gate de adoção:** todas as dimensões aplicáveis precisam estar `Pass` com evidência e revisão humana; qualquer `Needs work` impede adoção até resolução ou exceção formalmente aprovada. O gate é proposta, não regra já vigente.

## 6. Cuidado metodológico na Aula 21

Aula 21 é **caso de aplicação**, não validação universal dos oito princípios. O experimento tem sete cenários avançados e custos sintéticos; casos em que `success` diverge não servem para alegar menor custo por tarefa entregue. Não há denominador legítimo para `cost_per_success` no caso rejeitado. `risk_violations=0` sem cenários discriminativos não é prova de detector eficaz.

## 7. Próxima decisão humana

Ao revisar o PR, verificar se a rubrica está proporcional para um curso educacional, se a ficha é suficientemente objetiva e se há motivos para fundir conceitos sobrepostos. Manter os lemas preservados mesmo que a organização evolua. Somente após aceite registrar `Reviewed`, e **Adopted** exige decisão específica.
