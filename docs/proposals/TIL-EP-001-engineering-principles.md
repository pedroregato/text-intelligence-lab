# TIL-EP-001 — Engineering Principles: Evidence, Utility & Responsibility

**Projeto:** Text Intelligence Lab (TIL) with Kaggle  
**Versão:** 1.0 — especificação inicial  
**Status:** PROPOSED / IN REVIEW  
**Registro:** 17/10/2026  
**Dependência:** concluir a revisão e homologação da Aula 21 — Planning and Goal Decomposition (Issue #3, PR #4).  
**Escopo original do registro:** preservar e especificar a iniciativa. **Retomada após encerramento da Aula 21:** catálogo documental inicial proposto em `docs/principles/`, ainda sem adoção nem alteração de notebooks.

## 1. Motivação

A evolução do TIL de Text Intelligence para Applied AI Engineering revelou enunciados duradouros sobre ciência, causalidade, utility, validação, planejamento, segurança e responsabilidade. Esses enunciados surgiram com especial clareza na revisão crítica da Aula 21. Não devem se perder em conversas nem ficar restritos a um notebook.

**Tese orientadora:** princípios memoráveis têm valor quando geram critérios verificáveis de engenharia, experimentação e decisão, e quando podem ser contestados à luz de novas evidências.

## 2. Lemas iniciais — preservar as formulações

### TIL-PRINCIPLE-001 — Complexidade conquistada
> **Complexidade arquitetural precisa ser conquistada por evidência.**

Nenhum sistema deve ser considerado melhor apenas por ser mais sofisticado.

### TIL-PRINCIPLE-002 — Benefício demonstrável
> **Não basta demonstrar que uma arquitetura consegue planejar, validar ou replanejar. É necessário demonstrar qual benefício cada mecanismo efetivamente produz, em quais condições e a que custo.**

Capacidade demonstrada não equivale a utilidade demonstrada.

### TIL-PRINCIPLE-003 — Atribuição causal
> **Não atribua ao planejamento um benefício produzido por um mecanismo de segurança compartilhado.**

Exemplo: se reactive e planning usam o mesmo guard antes de publicar, o benefício de segurança observado não deve ser atribuído exclusivamente ao planning.

### TIL-PRINCIPLE-004 — Evidência antes de preferência
> **A arquitetura preferida deve ser consequência da evidência, não uma premissa do experimento.**

Cenários não devem ser desenhados artificialmente para favorecer a opção ensinada.

### TIL-PRINCIPLE-005 — Resultado não é mecanismo
> **Observar um resultado correto não demonstra que o mecanismo responsável por ele foi corretamente identificado.**

Um resultado seguro pode depender de salvaguardas e não do mecanismo anunciado.

### TIL-PRINCIPLE-006 — Validação não é segurança demonstrada
> **Rejeitar um plano inválido demonstra que uma regra foi aplicada; não demonstra, por si só, que um incidente foi evitado.**

Distinguir validade estrutural, conformidade contratual, viabilidade de execução e qualidade do resultado. Uma rejeição pode ser correta pelo contrato e ainda não representar um incidente evitado; também pode decorrer de regra excessivamente restritiva.

### TIL-PRINCIPLE-007 — Resultado negativo legítimo
> **Não encontrar evidências suficientes para justificar uma arquitetura mais complexa é um resultado legítimo do experimento.**

A resposta negativa é válida quando fundamentada e reprodutível.

### TIL-PRINCIPLE-008 — Planejamento e governança
> **O plano orienta a execução; as políticas e os mecanismos de segurança limitam o que a execução está autorizada a fazer.**

Um plano aprovado não dispensa revalidação de estado, autorização e política imediatamente antes de uma ação sensível.

## 3. Arquitetura conceitual da iniciativa

Preservar três camadas distintas:

1. **Princípios:** proposições duradouras e contestáveis que orientam julgamento e desenho de sistemas.
2. **Critérios de decisão:** heurísticas, regras e avaliações contextuais que operacionalizam princípios.
3. **Evidências:** experimentos, métricas, traces e limitações que sustentam, contestam ou refinam decisões.

Não confundir proxy com medida real, correlação com causalidade, capacidade com utility, sucesso operacional com compliance ou segurança.

## 4. Esquema proposto para cada princípio

- `id` estável e nome curto;
- **lema original preservado**, sem reescrita silenciosa;
- fundamentação e contexto de aplicação;
- problema ou modo de falha prevenido;
- consequências operacionais e critérios verificáveis;
- exemplos e contraexemplos;
- limitações, condições de contorno e hipóteses;
- proveniência (aula, discussão, experimento, issue ou ADR);
- relações com demais princípios, aulas e decisões;
- status: `Proposed`, `Reviewed` ou `Adopted`.

A adoção exige revisão pedagógica e técnica; um lema não é uma verdade universal.

## 5. Integração proposta — não executar nesta fase

Avaliar, à luz das convenções existentes em `docs/README.md`, eventual criação de:

```text
docs/principles/
  README.md
  engineering-principles.md
  principles-catalog.yaml
  principles-to-lessons.md
```

Prever referências cruzadas nos notebooks, glossário, ADRs, experimentos, course home e readiness gates, evitando redundância editorial.

## 6. Caso-piloto: Aula 21

A revisão da Aula 21 é a origem e primeiro estudo de caso para aplicação:

- Nos cenários simulados comparáveis, o reactive apresentou menor `cost_proxy`; não extrapolar para o mundo real.
- Guards compartilhados impediram publicação com status incompatível.
- O replanning gerou um novo artefato, sem evidência de ganho incremental de segurança nesses cenários.
- O caso `invalid_plan` diferenciou aplicação de contrato de prevenção comprovada de incidentes.
- Métricas sem variação ou sem cenário discriminativo não constituem evidência forte.
- Alterar pesos de custo não cria economias operacionais inexistentes; análise de sensibilidade deve respeitar dominância e limitações do experimento.

Ao implementar o framework, revisitar a versão homologada da Aula 21; não congelar como fatos as interpretações de versões preliminares.

## 7. Entregáveis quando retomado

1. Análise crítica do framework, com alternativas de organização.
2. Catálogo inicial, mantendo lemas originais e separando comentários aperfeiçoados.
3. Política de proposição, revisão, adoção, revisão posterior e eventual depreciação.
4. Mapa de relações entre princípios, currículo, glossário, evidências e ADRs.
5. Versão documental e eventual índice estruturado, prontos para revisão e publicação.

## 8. Critérios de aceitação futuros

- Lemas originais preservados e corretamente atribuídos a seus contextos.
- Cada princípio tem pelo menos um critério de aplicação verificável, um exemplo e uma limitação.
- Nenhuma inferência causal é atribuída sem comparação apropriada.
- Evidências, hipóteses, interpretação e decisão ficam separadas.
- Catálogo navegável, versionado, sem duplicar glossário ou ADR.
- Revisão humana antes de status `Adopted`.

## 9. Condição explícita de retomada

**Retomar esta especificação assim que a revisão da Aula 21 estiver encerrada**, com os resultados de execução e homologação disponíveis. A conclusão da Aula 21 é um marco de trabalho, não uma condição técnica para que o registro exista.

**Nota histórica (17/10/2026):** o registro inicial foi deliberadamente adiado até o encerramento da Aula 21. **Estado atual:** retomada para elaboração e revisão do catálogo em `docs/principles/`; nenhum princípio foi automaticamente adotado e nenhuma integração curricular foi publicada.
