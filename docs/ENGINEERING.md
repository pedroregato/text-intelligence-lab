# TIL Engineering

Este documento concentra informações de infraestrutura e engenharia que não precisam ocupar o README público do curso.

## Responsibility Boundaries

- **GitHub** — source of truth para código, documentação, histórico e decisões.
- **Kaggle UI** — inspeção interativa e experiência do aluno.
- **Kaggle CLI/API** — operações explícitas e reproduzíveis.
- **kagglehub** — acesso programático a recursos Kaggle.
- **Kaggle MCP** — integração opcional para clientes compatíveis.

O projeto deve continuar operacional mesmo sem Kaggle MCP.

## Execution Architecture

```text
                 GitHub
            source of truth
                  ▲
                  │
              Git local
                  │
        ┌─────────┴─────────┐
        │                   │
     PyCharm              Codex
        │                   │
   Kaggle CLI          Kaggle MCP
        │                   │
   kagglehub                │
        └─────────┬─────────┘
                  ▼
               Kaggle
                  ▲
                  │
              Kaggle UI
```

## Operating Model

```text
Arquitetar
→ Implementar pequeno
→ Executar
→ Observar
→ Avaliar
→ Corrigir
→ Versionar
→ Expandir
```

## Internet Policy

Internet OFF por padrão.

Internet ON apenas quando o acesso externo fizer parte do objetivo pedagógico e a dependência estiver explicitamente documentada.

## Data Policy

- exemplos mínimos e didáticos: podem ficar embutidos no notebook;
- datasets médios/grandes: preferir Kaggle Datasets versionados;
- dados sensíveis ou proprietários: não publicar no curso;
- datasets usados em capstone: documentar origem, licença e versão.

## Model Policy

- modelos pequenos ou pré-instalados: uso direto quando reprodutível;
- modelos externos: preferir recurso versionado/anexado ao Kaggle quando viável;
- Hugging Face Hub: permitido por exceção documentada;
- APIs proprietárias: usar Kaggle Secrets e nunca hardcode de chaves.

## Runtime Evidence

Não assumir versões do ambiente. Registrar versões observadas em execução real do Kaggle quando forem relevantes.

## Lesson Release Gates

Uma aula só deve ser considerada student-ready após:

1. execução técnica bem-sucedida no Kaggle;
2. warnings revisados;
3. dependências documentadas;
4. exercícios testados;
5. glossário atualizado;
6. revisão pedagógica;
7. aceite em perspectiva de aluno.
