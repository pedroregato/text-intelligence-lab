# ADR-003 — Kaggle Models for Transformer Lessons

## Status
Proposed

## Context
As Aulas 10 e 11 usam ou planejam usar modelos pré-treinados.

O TIL usa internet OFF por padrão, mas a Aula 11 atualmente depende do Hugging Face Hub por exceção pedagógica.

## Decision to evaluate
Priorizar, quando viável, modelos versionados ou anexados como recursos Kaggle para aulas oficiais de Transformers.

## Options

### A. Hugging Face Hub com internet ON
Vantagens:
- fluxo moderno e comum;
- menos preparação inicial.

Riscos:
- dependência externa;
- disponibilidade remota;
- mudanças de artefato;
- menor controle reprodutível.

### B. Kaggle Model / recurso anexado
Vantagens:
- dependência explícita;
- melhor controle de versão;
- possibilidade de internet OFF;
- maior alinhamento com o ambiente do curso.

Riscos:
- exige preparação e validação do fluxo;
- pode aumentar manutenção de artefatos.

## Recommendation
Validar operacionalmente Kaggle Models antes de alterar as Aulas 10–11.

Se o fluxo for estável, preferir recurso anexado para o notebook oficial e manter Hugging Face Hub como alternativa pedagógica documentada.
