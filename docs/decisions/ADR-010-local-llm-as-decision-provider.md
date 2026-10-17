# ADR-010 — Local Open-Weight LLM as Decision Provider

## Status

Proposed

## Context

Até a Aula 22, nenhum LLM real participa do TIL. As aulas generativas e agentic usaram micro-modelos didáticos ou decisores determinísticos, e isso foi suficiente enquanto o objeto de estudo era o mecanismo.

A Aula 23 estuda o erro de um decision provider aprendido. Para isso é necessário um modelo que realmente gere saídas imprevisíveis: ações fora do catálogo, JSON inválido, argumentos inventados.

Restrições já vigentes no TIL:

- Internet OFF por padrão (Course Design Contract, Internet Policy);
- modelos pré-treinados como Kaggle Model anexado e versionado (ADR-003);
- custo zero para o aluno;
- resultados não fixados no markdown e reproduzíveis.

Alternativas avaliadas:

| Opção | Internet | Custo para o aluno | Reprodutibilidade | Atrito de acesso |
|---|---|---|---|---|
| LLM por API | ON + chave em Kaggle Secrets | por chamada | baixa (modelo muda no provedor) | conta e chave por aluno |
| Gemma 3 (270M / 1B) via Kaggle Models | OFF | zero | alta | aceite dos termos Gemma por aluno |
| Qwen2.5 Instruct (0.5B / 1.5B) via Kaggle Models | OFF | zero | alta | nenhum aceite de termos |

Verificação na API pública do Kaggle Models (17/out/2026):

- `qwen-lm/qwen2.5`, framework `transformers`, variações `0.5b-instruct` e `1.5b-instruct`, versão 1, licença **Apache 2.0**, sem campo de consentimento;
- as variações 3B e 72B de Qwen2.5 têm licença diferente e ficam fora;
- `google/gemma-3` tem `gemma-3-270m-it` e `gemma-3-1b-it` (licença Gemma); o Kaggle mantém uma página de consentimento aos termos Gemma.

## Decision

1. O decision provider LLM principal do TIL é **Qwen2.5-0.5B-Instruct**, handle `qwen-lm/qwen2.5/transformers/0.5b-instruct/1`, anexado ao notebook e carregado com Internet OFF.
2. **Qwen2.5-1.5B-Instruct** (`.../1.5b-instruct/1`) é a comparação opcional de tamanho.
3. Decoding greedy e `max_new_tokens` limitado no laboratório principal.
4. Toda execução live grava suas saídas brutas; um Kaggle Dataset de **replay** versionado permite reproduzir as análises sem o modelo.
5. O modo replay é sempre explícito e anunciado no notebook; nunca é um fallback silencioso.
6. LLM por API é permitido apenas como extensão opcional, desligada por padrão, documentada como exceção à política de Internet.
7. O handle e o caminho de carregamento devem ser validados no próprio Kaggle antes de serem codificados (regra do ADR-003); preferir `kagglehub.model_download(handle)` a caminhos `/kaggle/input` fixos.

## Consequences

Positivas:

- primeira exposição do aluno a um LLM real sem custo, sem rede e sem cadastro;
- falhas reais e frequentes para exercitar o harness;
- reprodutibilidade preservada pelo replay e pela versão fixada.

Negativas e riscos:

- modelo pequeno não representa LLMs grandes; a aula deve dizer isso;
- latência em CPU precisa ser medida; pode exigir reduzir o conjunto do modo live;
- greedy em CPU é estável, mas não há garantia formal de saída idêntica entre hardwares; o replay registra `device`;
- o português do modelo de 0,5B pode ser fraco; isso é evidência, não defeito do laboratório.

## Revisit when

- o TIL passar a exigir raciocínio de múltiplos passos que o modelo de 0,5B não sustente;
- a licença ou a disponibilidade da variação no Kaggle Models mudar;
- o capstone exigir um modelo maior.

## Sources

- Kaggle Models API, `qwen-lm/qwen2.5` (consultada em 17/out/2026)
- Kaggle Models API, `google/gemma-3` (consultada em 17/out/2026)
- Model card Qwen2.5-0.5B-Instruct (Hugging Face): Apache 2.0, ~0,49B parâmetros, suporte multilíngue incluindo português, ênfase em saída JSON
