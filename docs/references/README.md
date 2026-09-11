# Biblioteca Viva de Referências do TIL

A **TIL Living Reference Library** organiza referências externas como parte da infraestrutura pedagógica do curso.

O objetivo não é acumular links. Cada referência deve responder a três perguntas:

1. **Que evidência ou ideia esta fonte oferece?**
2. **Como ela se conecta aos conceitos e aulas do TIL?**
3. **Que atividade pedagógica ela permite criar?**

## Fonte canônica

O catálogo oficial está em:

```text
docs/references/references.yaml
```

Esse arquivo é a fonte de verdade para referências externas usadas pelo curso.

## Fluxo editorial

```text
Referência encontrada
        ↓
Registrar no references.yaml
        ↓
Classificar tipo e papel da fonte
        ↓
Revisar limitações e contexto
        ↓
Relacionar a aulas e conceitos
        ↓
Criar leitura, discussão, estudo de caso ou experimento
        ↓
Marcar como integrated
```

## Tipos de referência

| Tipo | Uso típico |
| --- | --- |
| `foundational` | Material conceitual fundamental |
| `official-doc` | Documentação ou anúncio técnico oficial |
| `research-paper` | Artigo científico ou preprint |
| `industry-article` | Tendências e práticas da indústria |
| `case-study` | Caso concreto analisado pelo curso |
| `benchmark` | Resultado experimental comparativo |
| `tutorial` | Material prático complementar |
| `critical-analysis` | Contraponto, crítica ou interpretação independente |

## Papel da fonte

Além do tipo, cada item recebe um `source_role`:

- `primary`: fonte original da afirmação, sistema, pesquisa ou dado;
- `secondary`: análise, reportagem ou síntese baseada em fontes primárias;
- `commentary`: opinião ou interpretação adicional.

O TIL procura ensinar **triangulação de fontes**. Quando possível, uma afirmação relevante deve ser lida primeiro na fonte primária e depois comparada com uma análise independente.

## Regra editorial central

> Um artigo jornalístico ou post de terceiros não deve ser usado como única base de uma afirmação técnica quando houver documentação, paper, benchmark ou repositório primário disponível.

Essa regra é especialmente importante em temas de IA, onde resultados dependem frequentemente de versão de modelo, benchmark, configuração, preço, infraestrutura e metodologia de avaliação.

## Como relacionar uma referência a uma aula

Cada registro pode incluir:

```yaml
related_lessons:
  - "13C"

topics:
  - model-routing
  - multi-model-orchestration

pedagogical_use:
  - "estudo de caso"
  - "exercício de leitura crítica"
```

A referência deixa então de ser uma leitura isolada e passa a fazer parte da arquitetura educacional do curso.

## Reference sets

O catálogo também suporta conjuntos de referências (`reference_sets`). Eles servem para agrupar fontes que devem ser lidas em conjunto.

Exemplo:

```text
Fonte oficial
    +
Análise independente
    ↓
Comparação crítica
    ↓
Experimento no TIL
```

O primeiro conjunto oficial do catálogo é `set-hydrafusion-2026`.

## Caso HydraFusion

A integração inicial da Biblioteca Viva usa duas fontes complementares:

- GitHub Blog como fonte primária;
- VentureBeat como análise secundária/crítica.

O material pedagógico derivado está em:

```text
docs/case-studies/github-hydrafusion-multi-model-orchestration.md
course/13-metrics-and-indicators/13c-model-routing-and-orchestration.ipynb
```

## Estados de revisão

```text
candidate  → referência identificada, ainda não revisada
reviewed   → conteúdo e metadados revisados
integrated → já utilizada em aula, laboratório ou estudo de caso
archived   → mantida por histórico, mas não recomendada como referência atual
```

## Evolução planejada

Como `references.yaml` é estruturado, ele poderá alimentar automaticamente:

- uma página HTML filtrável por tema, aula, tipo e data;
- listas de leitura por aula;
- cartões de referência nos notebooks;
- validações automáticas de links e campos obrigatórios;
- busca semântica e um RAG do próprio TIL.

O princípio é o mesmo do Glossário Vivo: **uma fonte canônica estruturada, múltiplas formas de consumo**.
