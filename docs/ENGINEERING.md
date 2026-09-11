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

## Headless-first Notebook Policy

Todo notebook oficial do TIL deve conseguir executar integralmente em `Run All` sem depender de cliques, callbacks, widgets ativos ou estado interativo do navegador.

```text
camada determinística
        ↓
execução completa em modo headless
        ↓
outputs mínimos observáveis
        ↓
camada interativa opcional
```

A interatividade deve enriquecer a experiência do aluno, nunca ser requisito para concluir a execução automática.

Para notebooks com `ipywidgets`:

- não disparar renderização automaticamente no final da célula quando isso puder bloquear a execução;
- preferir botão explícito para ações interativas;
- não depender de `observe()` para produzir a saída mínima da aula;
- fechar figuras Matplotlib após exibição quando apropriado;
- manter uma saída estática ou determinística que permita compreender a aula mesmo sem interação;
- evitar buscas recursivas amplas em diretórios de entrada quando caminhos controlados forem suficientes.

Antes de publicar no Kaggle, preferir um teste local de execução headless, por exemplo com `jupyter nbconvert --execute`, seguido de uma execução real no Kaggle.

Esta regra foi consolidada após a validação da Aula 13C e está registrada em `docs/decisions/ADR-009-headless-first-interactive-notebooks.md`.

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

1. execução headless local bem-sucedida quando aplicável;
2. execução técnica bem-sucedida no Kaggle;
3. warnings revisados;
4. dependências documentadas;
5. exercícios testados;
6. glossário atualizado;
7. revisão pedagógica;
8. aceite em perspectiva de aluno.
