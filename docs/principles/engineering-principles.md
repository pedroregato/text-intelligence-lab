# TIL — Catálogo inicial de princípios de engenharia

**Status:** Proposed · **Origem:** [TIL-EP-001](../proposals/TIL-EP-001-engineering-principles.md) · **Aplicação-piloto:** Aula 21

Os lemas abaixo são **transcrições literais da especificação**; exemplos, critérios e contraexemplos são interpretações propostas e devem ser revisados. Nenhum enunciado é lei universal. **Aderência a um princípio é julgamento normativo contextual; testes de aplicação auditam decisões e evidências, não demonstram que um lema seja uma lei empírica.** A proposta não cria exigências retroativas para aulas já homologadas.

## TIL-PRINCIPLE-001 — Complexidade conquistada

> Complexidade arquitetural precisa ser conquistada por evidência.

**Status:** Proposed

**Falha evitada:** Adotar solução mais sofisticada por prestígio técnico.

**Critério verificável:** Comparar alternativa simples e complexa sob condições e objetivos equivalentes, registrando qualidade, custo, latência e riscos.

**Teste de aplicação (auditável):** Verificar se o registro da decisão contém alternativa baseline, critérios de resultado, restrições e custo adicional. **Não conformidade:** complexidade promovida apenas por preferência ou prestígio, sem justificar requisitos não medidos.

**Exemplo:** Aula 21: reactive preserva a segurança do guard com menor custo proxy nos cenários comparáveis.

**Contraexemplo ou condição de contorno:** Mesmo com custo proxy maior, planning pode ser necessário em contextos com dependências auditáveis ou obrigações normativas não representadas no laboratório.

**Limitação:** O proxy da Aula 21 é sintético; não generalizar como benchmark real.

**Proveniência:** TIL-EP-001 §2; [Aula 21 — revisão de evidências](../readiness/AULA-21-EVIDENCE-REVIEW-2026-10-17.md), quando aplicável.

## TIL-PRINCIPLE-002 — Benefício demonstrável

> Não basta demonstrar que uma arquitetura consegue planejar, validar ou replanejar. É necessário demonstrar qual benefício cada mecanismo efetivamente produz, em quais condições e a que custo.

**Status:** Proposed

**Falha evitada:** Confundir capacidade técnica demonstrada com utilidade empresarial ou educacional.

**Critério verificável:** Declarar hipótese incremental; definir baseline, mecanismo, métrica de resultado e orçamento antes do teste.

**Teste de aplicação (auditável):** Verificar hipótese de benefício marginal, métrica, orçamento, baseline e condições de comparação. **Não conformidade:** apenas demonstrar a existência de um plano v2 e chamar isso de ganho de utility.

**Exemplo:** Aula 21: replan:v2 é observável, mas não demonstra segurança incremental frente ao guard compartilhado.

**Contraexemplo ou condição de contorno:** Um contrato obrigatório pode justificar rastreabilidade mesmo se utility operacional for neutra.

**Limitação:** Demonstrar valor depende de objetivo e restrições explícitos; não reduzir tudo ao custo.

**Proveniência:** TIL-EP-001 §2; [Aula 21 — revisão de evidências](../readiness/AULA-21-EVIDENCE-REVIEW-2026-10-17.md), quando aplicável.

## TIL-PRINCIPLE-003 — Atribuição causal

> Não atribua ao planejamento um benefício produzido por um mecanismo de segurança compartilhado.

**Status:** Proposed

**Falha evitada:** Creditar a componente errada um resultado positivo.

**Critério verificável:** Inventariar guards, políticas e informação recebida por cada arquitetura; isolar intervenções e comparar contrafactuais plausíveis.

**Teste de aplicação (auditável):** Identificar os controles comuns e avaliar se a conclusão isola o mecanismo adicional. **Não conformidade:** atribuir ao replanejamento a segurança produzida pelo guard presente nos dois grupos.

**Exemplo:** Em state_changes, ambos os executores releem status antes de publicar e interrompem a publicação.

**Contraexemplo ou condição de contorno:** Quando planejador efetivamente antecipa conflito antes de qualquer guard, pode haver ganho causal mensurável, exigindo experimento que isole esse efeito.

**Limitação:** Cenários controlados ajudam, mas não eliminam automaticamente confundimento.

**Proveniência:** TIL-EP-001 §2; [Aula 21 — revisão de evidências](../readiness/AULA-21-EVIDENCE-REVIEW-2026-10-17.md), quando aplicável.

## TIL-PRINCIPLE-004 — Evidência antes de preferência

> A arquitetura preferida deve ser consequência da evidência, não uma premissa do experimento.

**Status:** Proposed

**Falha evitada:** Desenhar cenário para provar que a tecnologia mais avançada vence.

**Critério verificável:** Pré-declarar hipótese, baseline e condições de equivalência; registrar também resultados negativos.

**Teste de aplicação (auditável):** Conferir se critérios de escolha e alternativas estavam definidos antes da interpretação, e se resultados desfavoráveis permanecem no relatório. **Não conformidade:** ocultar cenários em que a solução preferida perde.

**Exemplo:** Aula 21 mantém em evidência a ausência de ganho em tarefas simples.

**Contraexemplo ou condição de contorno:** Escolhas podem depender de restrições legais ou pedagógicas não traduzidas em métricas do laboratório.

**Limitação:** Resultados favoráveis em um dataset ou cenário não bastam para alegar superioridade geral.

**Proveniência:** TIL-EP-001 §2; [Aula 21 — revisão de evidências](../readiness/AULA-21-EVIDENCE-REVIEW-2026-10-17.md), quando aplicável.

## TIL-PRINCIPLE-005 — Resultado não é mecanismo

> Observar um resultado correto não demonstra que o mecanismo responsável por ele foi corretamente identificado.

**Status:** Proposed

**Falha evitada:** Usar sucesso final como prova de execução ou planejamento corretos.

**Critério verificável:** Inspecionar traces por etapa e verificar causas alternativas para mesmo resultado.

**Teste de aplicação (auditável):** Confrontar o resultado final com traces e pelo menos uma hipótese causal alternativa. **Não conformidade:** inferir que o planning foi responsável por uma publicação correta apenas porque ela terminou corretamente.

**Exemplo:** Publicação concluída no fluxo reativo não implica que um plano formal tenha sido executado.

**Contraexemplo ou condição de contorno:** Uma execução pode ter um único caminho determinístico, e a instrumentação adicional custar mais do que esclarecer.

**Limitação:** O trace é evidência parcial; ausência de eventos instrumentados não prova ausência de comportamento.

**Proveniência:** TIL-EP-001 §2; [Aula 21 — revisão de evidências](../readiness/AULA-21-EVIDENCE-REVIEW-2026-10-17.md), quando aplicável.

## TIL-PRINCIPLE-006 — Validação não é segurança demonstrada

> Rejeitar um plano inválido demonstra que uma regra foi aplicada; não demonstra, por si só, que um incidente foi evitado.

**Status:** Proposed

**Falha evitada:** Confundir violação contratual com falha operacional contrafactual.

**Critério verificável:** Separar validade estrutural, executabilidade, política e resultado; descrever o incidente que ocorreria sem o validador e confrontar com guards existentes.

**Teste de aplicação (auditável):** Distinguir contrato violado, execução factível, política aplicável e contrafactual do dano. **Não conformidade:** chamar uma rejeição contratual de incidente evitado sem traço ou experimento que demonstre esse risco.

**Exemplo:** Em contract_violation, planning rejeita plano sem depends_on direto, mas reativo publica com guard e autorização.

**Contraexemplo ou condição de contorno:** Se ausência de uma dependência permitir publicação prévia à aprovação num executor sem guard, o risco pode ser real — precisa ser demonstrado.

**Limitação:** Rejeição conservadora pode ser mandatória por compliance, mas não equivale a incidente evitado.

**Proveniência:** TIL-EP-001 §2; [Aula 21 — revisão de evidências](../readiness/AULA-21-EVIDENCE-REVIEW-2026-10-17.md), quando aplicável.

## TIL-PRINCIPLE-007 — Resultado negativo legítimo

> Não encontrar evidências suficientes para justificar uma arquitetura mais complexa é um resultado legítimo do experimento.

**Status:** Proposed

**Falha evitada:** Tratar empate ou ganho não demonstrado como falha do aluno ou da ciência.

**Critério verificável:** Reportar hipótese, dados, intervalos/limites, resultado e decisão, inclusive quando não há ganho.

**Teste de aplicação (auditável):** Documentar resultados sem ganho, incerteza e limites de escopo; não exigir superioridade da arquitetura complexa. **Não conformidade:** reclassificar empate como vitória sem justificativa.

**Exemplo:** Aula 21 aceita a conclusão de que planning não pagou o overhead nos cenários comparáveis.

**Contraexemplo ou condição de contorno:** Ausência de evidência não demonstra equivalência ou impossibilidade de benefício em outros cenários.

**Limitação:** Poder estatístico, cobertura de cenários e escolha de métricas limitam a conclusão.

**Proveniência:** TIL-EP-001 §2; [Aula 21 — revisão de evidências](../readiness/AULA-21-EVIDENCE-REVIEW-2026-10-17.md), quando aplicável.

## TIL-PRINCIPLE-008 — Planejamento e governança

> O plano orienta a execução; as políticas e os mecanismos de segurança limitam o que a execução está autorizada a fazer.

**Status:** Proposed

**Falha evitada:** Permitir que um plano previamente aprovado dispense controle antes de efeitos sensíveis.

**Critério verificável:** Aplicar guards de autorização, política e estado imediatamente antes de ação irreversível, com traces e razão de término.

**Teste de aplicação (auditável):** Verificar que a autorização e o estado são novamente observados antes da ação sensível. **Não conformidade:** supor que aprovação do plano substitui guard de execução.

**Exemplo:** Aula 21: revalidação de prontidão antes da publicação, tanto no reactive quanto no planning.

**Contraexemplo ou condição de contorno:** Uma automação simples sem plano explícito ainda pode atender plenamente à governança.

**Limitação:** O caso de publicação é simulado e não substitui testes de segurança reais.

**Proveniência:** TIL-EP-001 §2; [Aula 21 — revisão de evidências](../readiness/AULA-21-EVIDENCE-REVIEW-2026-10-17.md), quando aplicável.
