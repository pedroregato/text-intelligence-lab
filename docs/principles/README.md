# TIL Engineering Principles — Evidence, Utility & Responsibility

**Iniciativa:** [TIL-EP-001](../proposals/TIL-EP-001-engineering-principles.md)  
**Estado do catálogo:** Proposed (versão para revisão; nenhum princípio adotado automaticamente)  
**Caso-piloto:** [Aula 21 — Evidence Review](../readiness/AULA-21-EVIDENCE-REVIEW-2026-10-17.md)

> Complexidade arquitetural precisa ser conquistada por evidência.

## Por que este diretório existe

Este catálogo registra princípios **duradouros e questionáveis**, distintos de decisões contextuais (ADRs), resultados experimentais, verbetes do glossário e requisitos obrigatórios do [TIL Course Design Contract](../TIL-COURSE-DESIGN-CONTRACT.md).

A unidade de análise é **princípio → critério verificável → evidência e limites → decisão**. As evidências podem sustentar, restringir ou contestar decisões. Não há hierarquia presumida na qual agentes, LLMs ou Transformers sejam superiores.

## Navegação

- [Engineering principles](engineering-principles.md): formulações originais e fichas com critérios, exemplos, contraexemplos e limitações.
- [Structured catalog](principles-catalog.yaml): IDs, estados, lemas literais, critérios e proveniência para validações futuras.
- [Principles to lessons](principles-to-lessons.md): mapa contextual de aulas, evidências e pontos de integração propostos.

## Protocolo editorial

1. **Proposed:** registrar lema com ID estável, contexto, hipótese, exemplo, contraexemplo, limite e pelo menos um teste ou questão que possa refutá-lo. Preservar literalmente a formulação original e revisar interpretações separadamente.
2. **Reviewed:** exigir revisão humana da clareza, rigor lógico, caráter não universal e proveniência. Conferir resultados de execução e separação entre observação, interpretação e inferência causal.
3. **Adopted:** aceitar explicitamente após revisão técnica e pedagógica, documentando escopo, versão e decisão. A existência neste catálogo não promove o status automaticamente.
4. **Revised:** manter histórico e explicar motivo; não reescrever lemas originais silenciosamente. Alterações semânticas substanciais exigem versão ou novo ID com referência de substituição.
5. **Deprecated:** registrar motivo, evidência contraditória e substituto (se houver); nunca apagar retrospectivamente alegações ou resultados.

**Critério de aceitação:** ID único, lema rastreável, aplicação operacional verificável, pelo menos um contraexemplo ou limite, evidência ligada a fonte identificável, linguagem não causal na ausência de experimento apropriado. Exigir decisão explícita para adoção.

## Fronteiras de responsabilidade

- **Princípio:** orientação conceitual sujeita a teste e revisão.
- **Critério:** condição e método operacional para avaliar uma decisão em certo contexto.
- **Evidência:** resultado com ambiente, hipótese, métricas, metodologia e limites.
- **ADR:** registro de escolha contextual com alternativas e consequências.
- **Glossário:** definição terminológica, não regra nem prova empírica.
- **Readiness:** comprovação de requisitos para liberar uma aula, distinta da adoção dos princípios.

Os links para aulas abaixo são um **mapa piloto**, não integração efetiva aos notebooks. Nenhuma alteração dos notebooks ou do glossário é introduzida nesta revisão.

## Gates desta proposta

- [x] Preservar oito lemas originais na ordem definida em TIL-EP-001.
- [x] Separar princípios, critérios e evidências.
- [x] Fornecer exemplos, limitações e verificações para cada princípio.
- [x] Associar Aula 21 a observações com proveniência.
- [ ] Revisão humana do catálogo e dos termos.
- [ ] Decisão de adoção, com aprovação e registro apropriados.
- [ ] Integração curricular gradual sem duplicar glossário ou ADRs.
