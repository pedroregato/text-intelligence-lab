# Aula 21 — Evidence Review (revisão evidence-first)

**Data:** 17/10/2026  
**Notebook:** `course/21-planning-and-goal-decomposition/21-til-planning-and-goal-decomposition.ipynb`  
**Kaggle:** `pedrogentil/til-21-planning-and-goal-decomposition`  
**PR:** #4 · **Issue:** #3  
**Head verificado:** `0011a81abaa09f0a3ff8d38e3fe2414ee4a73eea`

## Gates e proveniência

| Gate | Evidência | Resultado |
|---|---|---|
| JSON e cell IDs | GitHub Actions Aula 21 Evidence Headless, run 39049654284 | PASS |
| Execução completa headless | GitHub Actions, mesmo run, Python 3.11, nbconvert | PASS |
| Regressões do notebook | Células `l21-validation-regression`, `l21-evidence-regression`, `l21-advanced-tests` na execução headless | PASS |
| Kaggle | Usuário comunicou `COMPLETE` após `kaggle kernels push`; não há link de versão/artefato verificado independentemente aqui | USER-REPORTED COMPLETE |
| Revisão pedagógica | Revisões iterativas das versões v3–v5 e incorporação final do bug `not_ready` em ambos executores | REVIEWED; inspeção manual da execução mais recente do Kaggle não documentada |

## Resultado da experiência — não extrapolar

- A segurança de publicação no cenário `state_changes` decorre do guard compartilhado: não atribuir causalidade exclusiva ao replanning.
- Planejamento custa mais no proxy sintético dos cenários básicos comparáveis: `simple_ready` 6.0 vs 8.5; `not_ready` 2.0 vs 4.5; `state_changes` 5.0 vs 9.0 (reactive vs plan-based), conforme execução anterior. Revisão final muda rótulos/descrições, não a fórmula do proxy.
- O cenário `contract_violation` demonstra aplicação de contrato; o custo menor da rejeição **não** deve ser tratado como eficiência comparável a uma publicação bem-sucedida.
- `risk_violations=0`, `plan_budget_exhausted` e demais ramos não exercitados não demonstram qualidade discriminativa.
- O laboratório avançado oferece três arquiteturas, sete cenários, perguntas e limites explícitos.
- `not_ready` é classificado consistentemente nas duas arquiteturas do laboratório básico pelo analisador comum `trace_metrics`; há regressões para os dois traces.

## Pendências editoriais não bloqueantes

- Caso desejado, publicar `til-21-resultados.md` revisado, com tabelas produzidas a partir do artefato efetivo final e referência à versão exata no Kaggle.
- Registrar URL/número da versão Kaggle efetivamente publicada em revisão independente, sem inferir número a partir do status `COMPLETE`.

## Princípio de decisão

> Não basta demonstrar que uma arquitetura consegue planejar, validar ou replanejar. É necessário demonstrar qual benefício cada mecanismo efetivamente produz, em quais condições e a que custo.

O registro de princípios correlato é `docs/proposals/TIL-EP-001-engineering-principles.md` (proposta adiada até fechamento da Aula 21).

**Conclusão:** gates técnicos headless confirmados; publicação Kaggle comunicada como COMPLETE; revisão pedagógica incorporada ao notebook. Este registro separa evidências diretamente verificadas de evidências reportadas pelo usuário.
