# TIL — Kaggle Revalidation Batch

## Objetivo

Executar, observar e revalidar no Kaggle as aulas reengenheiradas do TIL antes da promoção final para `Available / student-ready`.

Fonte dos critérios pedagógicos:

`docs/readiness/TIL-REENGINEERING-VALIDATION-BATCH.md`

## 1. Atualize o repositório

No PowerShell, a partir da raiz do TIL:

```powershell
git pull
```

Confirme:

```powershell
kaggle --version
```

## 2. Push automatizado

O repositório contém:

```text
scripts/push_revalidation_batch.ps1
```

Para publicar/reexecutar todas as aulas com metadata Kaggle dedicado:

```powershell
.\scripts\push_revalidation_batch.ps1
```

O script faz, para cada aula:

```text
kaggle kernels push
→ kaggle kernels status
```

Aulas incluídas:

```text
02 03 04 05 06 07
09 10 11 12
14 15 16 17 18 19
```

## 3. Consultar status sem novo push

```powershell
.\scripts\push_revalidation_batch.ps1 -StatusOnly
```

## 4. Aula 13C — tratamento separado

Notebook fonte:

```text
course/13-metrics-and-indicators/13c-model-routing-and-orchestration.ipynb
```

Kernel Kaggle esperado:

```text
pedrogentil/til-13c-model-routing-orchestration-and-utility
```

No estado atual do repositório não existe um `kernel-metadata.json` dedicado à 13C ao lado desse notebook.

O arquivo:

```text
course/13-metrics-and-indicators/kernel-metadata.json
```

pertence à **Aula 13**, não à 13C.

Portanto, não publique a 13C com:

```powershell
kaggle kernels push -p course\13-metrics-and-indicators
```

pois esse comando se refere ao kernel da Aula 13.

Até existir um wrapper Kaggle dedicado, a 13C deve ser sincronizada/publicada separadamente.

## 5. Ordem de inspeção recomendada

Depois que os kernels terminarem, inspecione primeiro as aulas com invariantes fortes:

```text
04 → manual TF-IDF reconcilia com sklearn
05 → score/probabilidade manual reconcilia com NB
03 → colisão BoW
02 → colisões de normalização
06 → métricas manuais
07 → leakage procedural
09 → embedding estático
```

Depois:

```text
11 → experimentos one-factor-at-a-time
12 → ranking/variabilidade sem claims fixos
13C → utility relativa vs ancorada
14 → autoregressive generation
15 → retrieval real
16 → RAG e failure localization
17 → tool selection
18 → workflow revalidation
19 → final MCP Run All
```

## 6. Regra de promoção

```text
Kaggle COMPLETE
≠
student-ready automático
```

Para cada aula:

1. verificar warnings e erros;
2. verificar outputs centrais;
3. confrontar output com markdown;
4. confirmar failure modes;
5. confirmar exercícios;
6. atualizar readiness gate;
7. só então promover.

## 7. Comandos individuais

Exemplo:

```powershell
kaggle kernels push -p course\04-tfidf
kaggle kernels status pedrogentil/til-04-tfidf
```

Os demais diretórios e IDs estão codificados em:

```text
scripts/push_revalidation_batch.ps1
```

## 8. Resultado esperado da bateria

Ao final:

```text
review-candidate-v2
→ Kaggle COMPLETE
→ pedagogical output inspection
→ readiness PASS
→ Available / student-ready
```

Nenhuma aula deve ser promovida apenas pelo retorno `COMPLETE`.
