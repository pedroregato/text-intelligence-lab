# TIL-EP-001 — Template mínimo de decisão baseada em evidências

**Status:** modelo pedagógico proposto; não substitui ADR, avaliação de risco formal ou aprovação institucional.

Use para uma decisão relevante ou como resposta ao [Decision Lab 01](DECISION-LAB-01.md). Uma decisão simples pode ser explicada em um parágrafo; não transforme esta ficha em burocracia obrigatória.

| Pergunta | Resposta fundamentada |
|---|---|
| **Decisão e finalidade** | O que escolher, para atender a que objetivo? |
| **Contexto e limitações** | Quais restrições de negócio, segurança, dados e tempo? |
| **Baseline e alternativas** | Qual opção suficientemente simples serve de comparação? |
| **Hipótese incremental** | Que ganho adicional justifica complexidade? |
| **Critérios de sucesso** | Que resultados, custos, riscos e limites mediremos? |
| **Evidências observadas** | Fontes e saídas rastreáveis, com origem e versão |
| **Mecanismos compartilhados** | Quais controles ou informações são comuns às alternativas? |
| **Interpretação** | O que os resultados sugerem? Há confundimento ou contrafactual ausente? |
| **O que não foi demonstrado** | Que inferência ainda seria indevida? |
| **Decisão provisória** | Escolha / adiar / exigir ensaio, com justificativa |
| **Condição de revisão** | Que nova evidência mudaria a escolha? |
| **Princípios aplicados** | IDs e como cada critério influenciou a escolha |

### Verificação leve de qualidade

Uma ficha é suficientemente útil se outra pessoa consegue identificar o **porquê**, os **limites** e **como contestar** a decisão. Nem toda decisão precisa de valores numéricos; quando números não são adequados, registrar exigências, riscos e argumentos de forma explícita. Não preencher os campos com métricas inventadas.

### Integração com ADR

Se a escolha tornar-se uma regra arquitetural duradoura, abrir ou vincular um ADR em `docs/decisions/`, preservando alternativas e consequências. O template educativo não aprova a decisão nem promove princípios de `Proposed` para `Adopted`.
