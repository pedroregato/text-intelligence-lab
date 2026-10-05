# TIL — Reengineering Validation Batch

## Purpose

Consolidar a bateria final de validação das aulas reengenheiradas antes da promoção para `Available / student-ready`.

## Governing rule

> Execution is not the end of validation. Execution produces evidence, and the evidence must improve the lesson.

Promotion requires:

```text
runs
AND central mechanism observable
AND evidence supports claim
AND student is guided to interpret output
AND limitations are visible
AND exercises require reasoning
```

## Batch

| Aula | Principal ajuste | Estado antes da bateria final |
|---|---|---|
| 02 | accent/negation collision labs | review-candidate-v2 |
| 03 | observable Bag-of-Words order loss | review-candidate-v2 |
| 04 | manual TF-IDF + sklearn reconciliation | review-candidate-v2 |
| 05 | Naive Bayes score/probability path | review-candidate-v2 |
| 06 | TP/FP/FN/TN derivation + same-accuracy lab | review-candidate-v2 |
| 07 | honest model selection + leakage lab | review-candidate-v2 |
| 09 | static embedding + stability/polysemy evidence | review-candidate-v2 |
| 10 | contextualization evidence | Kaggle PASS; pedagogical gate pending |
| 11 | one-factor-at-a-time fine-tuning experiments | review-candidate-v2 |
| 12 | dynamic baseline evidence, no fixed results | review-candidate-v2 |
| 13C | anchored utility + normalization sensitivity | review-candidate-v2 |
| 14 | real autoregressive generation loop | review-candidate-v2 |
| 15 | real semantic retrieval + Recall@k | review-candidate-v2 |
| 16 | fair RAG comparison + failure localization | review-candidate-v2 |
| 17 | observable tool-selection layer | review-candidate-v2 |
| 18 | pedagogically ready; opt-in exercise update | technical revalidation pending |
| 19 | pedagogically approved MCP lab | final Kaggle revalidation pending |

## Structural audit completed

The final repository audit confirmed for the reengineered notebooks:

- no duplicate cell IDs;
- `metadata.til.pedagogical_status` normalized to `review-candidate-v2`;
- exercise solutions use opt-in reveal patterns;
- Aula 19 Failure Lab remains executable by design because its output is evidence, not an exercise answer;
- no approximate execution numbers hard-coded in explanatory markdown, except measured/versioned evidence that is explicitly identified by provenance;
- README, ROADMAP and TIL-AIE readiness wording synchronized with the revalidation batch.

## Final validation loop per lesson

For each notebook:

```text
1. Kaggle Run All
2. inspect warnings/errors
3. inspect key evidence output
4. compare output with explanatory markdown
5. verify exercise flow
6. verify limitations/failure modes
7. update readiness gate
8. promote only when evidence supports the lesson
```

## Special checks

### Aula 04
Manual TF-IDF and sklearn output must reconcile numerically.

### Aula 05
Manual log-score ordering must match `.predict()`; normalized manual probabilities must match `predict_proba()`.

### Aula 07
The leakage lesson must remain valid even if the contaminated holdout does not show an optimistic score in that particular run.

### Aula 09
Static-vector proof must not depend on a specific nearest-neighbor ranking.

### Aula 11
Interpret A vs B only as a data-size change, and B vs C only as an epoch-count change.

### Aula 13C
Adding the counterfactual candidate may change `utility_relative`, while existing candidates' `utility_anchored` values should remain stable under the frozen reference bounds.

### Aula 15
A generic DistilBERT encoder may not outperform lexical retrieval. Treat that as evidence, not as failure.

### Aula 16
Wrong evidence may produce a grounded but factually wrong answer; this is expected pedagogical evidence.

### Aula 17
Validation/execution can succeed after a semantically wrong tool choice. The failure must be localized to decision/tool selection.

### Aula 18
Pedagogical approval is preserved; fresh execution is needed only because exercise/helper cells changed.

### Aula 19
Pedagogical approval is complete. Final promotion depends on the final Kaggle Run All of the current revision.

## Promotion target

After successful execution and inspection:

```text
review-candidate-v2
→ validated
→ Available / student-ready
```

Do not promote mechanically from Kaggle `COMPLETE`; inspect the resulting evidence first.
