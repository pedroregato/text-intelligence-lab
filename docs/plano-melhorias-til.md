# Plano de Melhorias — Text Intelligence Lab (TIL)

> **Data:** 2026-09-28 · **Autor:** Pedro Gentil (com Claude)
> **Base:** README do `text-intelligence-lab` e o levantamento de recursos do Kaggle Data Hub feito nesta sessão.
> **Princípio:** *toda complexidade adicional deve ser justificada por evidência.*
> **Plano irmão:** [`melhorias/plano-melhorias-vichara.md`](https://github.com/pedroregato/process2diagram/blob/main/melhorias/plano-melhorias-vichara.md) no repositório `process2diagram` (Vichāra).

---

## 0. Diagnóstico

| | Text Intelligence Lab (TIL) |
|---|---|
| **Maturidade** | Curso com Aulas 0–18 publicadas, 2 experimentos com evidência medida |
| **Força** | Rigor experimental: headless-first, proveniência (`measured-recovered`), ADRs, glossário e referências canônicos |
| **Lacuna principal** | **Licenciamento indefinido** antes da publicação ampla; Capstone ainda sem desenho |
| **Risco aberto** | Artefato do EDU-ORCH-002 reconstruído, não original |

**Tese do plano:** o TIL já sabe *medir*; o Vichāra já sabe *fazer*. A maior alavanca é transferir o método de evidência do TIL para o Vichāra, e usar o Vichāra como caso real do TIL.

---

## 1. Onda 1 — Pré-requisitos de publicação

### T1 · ADR de licenciamento — 🔴 Prioridade máxima
- **Situação:** o README diz que a política está "sendo formalizada em ADR específico antes da publicação ampla".
- **Decisão sugerida para discutir no ADR:** separar **código** (MIT ou Apache-2.0) de **conteúdo didático** (CC BY 4.0 ou CC BY-SA 4.0), e registrar a licença de **cada dataset** usado nas aulas (o Olist, por exemplo, tem licença própria no Kaggle).
- **Entregável adicional:** um campo `license` obrigatório em `references.yaml` e numa futura `data/DATASETS.yaml`.

### T2 · README coerente com o estado real — 🟢 Rápido
- A seção **Status** ainda diz que "o próximo movimento curricular é avançar para LLM Foundations, Retrieval/Grounding, Tools/Workflows", mas a **Trilha atual** já mostra as Aulas 14–18 como *Available*.
- **Ação:** atualizar a seção Status e, de preferência, gerá-la a partir de `course/navigation.json` para não divergir de novo.

### T3 · CI de reprodutibilidade — 🟠 Alta
Transformar em GitHub Actions as regras que hoje dependem de disciplina:
1. Execução headless (`nbconvert --execute`) dos notebooks oficiais em CPU, seguindo o ADR-009.
2. `sync_course_navigation.py --check` (falha se o rodapé estiver dessincronizado).
3. Gerador do glossário em modo check (falha em ID duplicado ou arquivo gerado desatualizado).
4. Validação de schema de `references.yaml`.

---

## 2. Onda 2 — Evidência e engenharia

### T4 · Reexecutar o EDU-ORCH-002 para eliminar `measured-recovered` — 🟠 Média
- Hoje a evidência de routing foi reconstruída a partir do output observado. Reexecutar e salvar o CSV como **output versionado do notebook** (ou nova versão de dataset no Kaggle), promovendo o status para `measured`.
- **Política derivada:** todo experimento grava a evidência em `/kaggle/working/` **e** publica uma versão de dataset ao final. Registrar como ADR.

### T5 · Célula padrão de *GPU preflight* — 🟢 Rápido
- Transformar a lição do P100 (sm_60 vs. PyTorch com build para sm_70+) em um módulo reutilizável, `til_utils/preflight.py`: detecta a GPU, verifica a compute capability contra o build do framework, roda uma operação CUDA mínima e cai para CPU com aviso explícito.
- Vale para o curso e para qualquer notebook do Vichāra que rode no Kaggle.

### T6 · Aula 17 + Structured Output Benchmark — 🟠 Média
- A Aula 17 (*Tool Use, Function Calling and Contracts*) ganha um laboratório de avaliação de contratos usando o **[Structured Output Benchmark](https://www.kaggle.com/datasets/interfazeai/structured-output-benchmark)** (CC BY-SA 4.0). A ideia é mostrar a diferença entre "JSON válido" e "JSON correto por valor".
- Gera um terceiro experimento de evidência (`EDU-CONTRACT-001`), coerente com o modelo em que os experimentos produzem evidência e as aulas consomem.

---

## 3. Onda 3 — Currículo

### T7 · Capstone com um problema real (ligação com o Vichāra) — 🟠 Média
- **Proposta de capstone:** *"Da reunião à decisão"*. Os alunos constroem um extrator de action items e decisões com o **[Teams Meeting Transcripts](https://www.kaggle.com/datasets/yusufayta/teams-meeting-transcripts)** (MIT) e percorrem a trilha inteira: baseline TF-IDF → Transformer → LLM com contrato → cascade com quality gate → avaliação de sistema (utility).
- **Vantagens:** usa as quatro macrocamadas do TIL num único problema; o gabarito já existe; e o resultado alimenta de volta o V2 do Vichāra.

### T8 · Aulas 19+ (Bloco Agentic Systems)
Sequência sugerida, coerente com o diagrama *Model → … → Human Oversight → Utility* do próprio README:
- **19 · Observability & Tracing:** telemetria de LLM, custo e latência por passo. Pode usar como exemplo o desenho do `llm_telemetry.py` do Vichāra.
- **20 · Agent Evaluation & Failure Analysis:** taxonomia de falhas com o **[Agent Failure Atlas 2026](https://www.kaggle.com/datasets/abishek9324/agent-failure-atlas-2026)** (CC BY-SA 4.0). **Deixar explícito aos alunos que o dataset é sintético.**
- **21 · Safety & Red Teaming de código gerado:** pares vulnerável/corrigido com **[CVE Fix Pairs](https://www.kaggle.com/datasets/hasaber8/cve-fix-pairs)** (CC BY 4.0). Tem sinergia direta com o AEEF.
- **22 · Human Oversight & Governance:** quality gates humanos, auditoria e LGPD, usando como caso a sanitização de PII do Vichāra.

---

## 4. Sinergias com o Vichāra

```
TIL (método)                               Vichāra (produto)
─────────────────────────────              ─────────────────────────────
ADR / evidence CSV / headless   ───────▶   V2 eval harness no mesmo formato
EDU-ORCH-002 (cascade medido)   ───────▶   V4 routing de passes BPMN / thinking
T5 GPU preflight                ───────▶   notebooks Kaggle do Vichāra
                                ◀───────   Caso real para o capstone (T7)
                                ◀───────   llm_telemetry / PII como material das Aulas 19 e 22
```

Recursos compartilhados: **Teams Meeting Transcripts** (T7 + V2 do Vichāra), **SOB** (T6 + V2 do Vichāra), **CVE Fix Pairs** (T8 + AEEF).

---

## 5. Roadmap

| Onda | Itens | Critério de saída |
|---|---|---|
| **1 — Base** | T1 licença · T2 README · T3 CI | CI verde |
| **2 — Evidência** | T4 reexecução · T5 preflight · T6 Aula 17 + SOB | Nenhum `measured-recovered` restante |
| **3 — Expansão** | T7 capstone · T8 Aulas 19–22 | Capstone publicado |

**Registro:** cada decisão vira ADR em `docs/decisions/`.

---

## 6. Premissas e riscos

- **Premissa:** o estado do repositório é o descrito no README em 2026-09-28. Itens podem ter avançado localmente sem push.
- **Qualidade dos datasets do Kaggle:** vários têm notas de usabilidade baixas ou são sintéticos. Todos os recomendados aqui tiveram a licença conferida na página do dataset, mas o conteúdo deve ser inspecionado antes de entrar nas aulas.
- **Idioma:** os datasets recomendados estão em inglês; o capstone e os laboratórios herdam essa limitação.
