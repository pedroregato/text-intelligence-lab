# ADR-003 — Kaggle Models for Transformer Lessons

## Status
Accepted

## Context
As Aulas 10 e 11 usam modelos pré-treinados.

O TIL adota Internet OFF por padrão e habilita acesso externo apenas quando ele fizer parte intencional da aprendizagem.

A documentação oficial do Kaggle confirma que:

- Kaggle Models é integrado aos Kaggle Notebooks;
- modelos podem ser anexados pelo editor;
- cópias/forks de notebooks preservam os modelos anexados;
- modelos podem ser acessados programaticamente com `kagglehub.model_download()`;
- uma versão específica pode ser referenciada;
- modelos originados do Hugging Face também fazem parte do ecossistema Kaggle Models.

## Decision

Para notebooks oficiais do TIL que dependam de modelos pré-treinados:

1. **Preferir Kaggle Model anexado e versão fixada** quando o recurso estiver disponível e validado.
2. Manter o modelo como dependência explícita do notebook.
3. Preferir execução com **Internet OFF** quando o modelo anexado satisfizer toda a execução.
4. Usar Hugging Face Hub com **Internet ON** somente como:
   - etapa de descoberta/provisionamento;
   - fallback pedagógico;
   - ou quando o acesso remoto for parte explícita do objetivo da aula.
5. Registrar no notebook:
   - modelo;
   - origem;
   - versão/handle Kaggle quando aplicável;
   - política de internet;
   - implicações de reprodutibilidade.

## Preferred execution pattern

```text
Kaggle Model versionado
→ anexado ao Notebook
→ dependência explícita
→ Internet OFF
→ execução reproduzível
```

Fallback:

```text
Hugging Face Hub
→ Internet ON
→ download remoto explícito
→ menor controle reprodutível
```

## Implementation note

O handle exato de um modelo Kaggle deve ser obtido e validado no próprio recurso/model page antes de ser codificado em um notebook oficial.

Não inventar handles nem assumir caminhos `/kaggle/input`.

Quando possível, preferir `kagglehub.model_download('owner/model/framework/variation/version')`.

## Consequences

- A Aula 10 deve continuar tolerante à indisponibilidade do recurso enquanto o modelo Kaggle oficial não estiver anexado.
- A Aula 11 mantém temporariamente o download Hugging Face como fallback, mas a arquitetura preferida passa a ser Kaggle Model versionado.
- Uma aula só pode ser marcada student-ready após o recurso externo ter sido executado e validado no Kaggle.


## Discovery update — 2026-09-06

A busca pública não encontrou com confiança suficiente um Kaggle Model oficial exato para `distilbert-base-multilingual-cased`.

Um Dataset antigo com esse nome foi identificado, mas foi rejeitado como dependência oficial por não ser Kaggle Model e por apresentar licença desconhecida.

Portanto, a decisão arquitetural permanece aceita, porém a migração das Aulas 10–11 fica condicionada ao experimento `EDU-INFRA-002` e ao runbook `docs/runbooks/kaggle-model-provisioning.md`.
