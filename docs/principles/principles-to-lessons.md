# TIL — Relação entre princípios, aulas e evidências

**Status:** Proposed. Estes vínculos são sugestões editoriais, não exigências já introduzidas nos notebooks.

| Princípio | Conteúdo-piloto | Evidência ou fronteira | Integração futura sugerida |
|---|---|---|---|
| 001 — Complexidade conquistada | Aula 13C; Aula 21 | Comparação de utility e custo proxy | Pergunta final: o ganho incremental justifica a arquitetura? |
| 002 — Benefício demonstrável | Aula 21 | Replanning gera v2 sem ganho de segurança identificado | Hipótese e análise incremental por mecanismo |
| 003 — Atribuição causal | Aulas 20–21 | Guard compartilhado explica interrupção segura | Quadro "mecanismo versus resultado" |
| 004 — Evidência antes de preferência | Aula 13C; Aula 21 | Baselines e cenário comparável | Pré-registro de hipóteses e critérios |
| 005 — Resultado não é mecanismo | Aulas 17, 20–21 | Trace de seleção, publicação e estados | Exercício de atribuição causal |
| 006 — Validação não é segurança demonstrada | Aulas 17 e 21 | `contract_violation` rejeitado, sem incidente contrafactual demonstrado | Comparar contrato, execução e política |
| 007 — Resultado negativo legítimo | Aulas 13C e 21 | Ausência de ganho líquido em cenários sintéticos | Resposta negativa fundamentada como legítima |
| 008 — Planejamento e governança | Aulas 17–21 | Guard antes da publicação; plano v2 rastreável | Contrato de autorização antes de side effects |

## Evidências e interpretações

- **Fonte do resultado da Aula 21:** [registro de readiness/evidência](../readiness/AULA-21-EVIDENCE-REVIEW-2026-10-17.md). Os números são proxies simulados, não métricas financeiras ou benchmarks de produção.
- **Fonte da concepção dos princípios:** [TIL-EP-001](../proposals/TIL-EP-001-engineering-principles.md).
- **Regras pedagógicas já adotadas:** [TIL Course Design Contract](../TIL-COURSE-DESIGN-CONTRACT.md); este documento propõe ligações e não altera o contrato.
- **Glossário e ADRs:** nenhuma alteração é proposta na primeira rodada, para evitar duplicação. Referências contextuais só serão adicionadas após revisão.

## Caminho de integração proposto

1. Revisar formulações e critérios; manter os lemas originais.
2. Conferir o registro de evidências antes de promover qualquer claim causal.
3. Escolher poucas aulas-piloto e incluir links contextuais discretos, sem substituir o glossário.
4. Executar gates de notebook quando qualquer célula for alterada.
5. Documentar decisão de adoção e eventuais exceções numa ADR, se houver mudança normativa duradoura.

**Não confundir vincular um princípio a uma aula com demonstrar experimentalmente sua validade universal.**
