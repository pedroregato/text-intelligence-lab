# Aula 13C — Readiness Gate

## Status

REVIEW CANDIDATE — reengineered v2, not yet student-ready.

## Central question

How should routing/orchestration utility be computed so that architectural decisions remain interpretable when the candidate set changes?

## Gates

### G1 — Measured evidence consumption

**PASS**

The lesson consumes versioned model and routing evidence when available and preserves explicit DEMO fallback.

### G2 — Routing provenance

**PASS**

Measured and measured-recovered evidence remain distinguishable.

### G3 — Relative normalization sensitivity

**PASS — IMPLEMENTED**

The lesson demonstrates that candidate-relative min-max normalization can change existing utility scores when a new candidate changes the observed extrema.

### G4 — Anchored utility

**PASS — IMPLEMENTED**

The main ranking now uses frozen reference bounds for quality, cost and latency within the execution session.

### G5 — Counterfactual sensitivity lab

**PASS — IMPLEMENTED**

A deliberately extreme candidate is added without changing original candidate metrics; relative and anchored utility changes are compared side by side.

### G6 — Utility governance

**PASS — IMPLEMENTED**

The lesson makes explicit that utility depends on policy choices such as dimensions, weights, normalization and reference bounds.

### G7 — Gate sensitivity

**PASS — IMPLEMENTED**

Measured thresholds remain separate points; the lesson does not interpolate unmeasured routing evidence.

### G8 — Reproducibility

**PASS — BY DESIGN**

The notebook keeps evidence provenance explicit and does not overwrite measured data with synthetic interpolation.

### G9 — Kaggle Run All

**PASS**

Fresh execution required after the utility-normalization changes.

### G10 — Pedagogical inspection

**PENDING**

Verify that the student can explain:

1. why candidate-relative min-max scores depend on the comparison set;
2. why adding a candidate can change another candidate's utility without changing its metrics;
3. what anchored normalization improves;
4. why anchor selection is itself a governance choice;
5. why highest F1 is not necessarily highest utility;
6. why utility is a policy function rather than an intrinsic property of a model.

## Promotion rule

Promote only after G9 and G10 pass.

## Governing principle

> Utility should make decision policy explicit and stable enough to support comparison; it should not silently change meaning when the candidate set changes.


## Final semantic execution check

**EVIDENCE mode verification: PASS** — the Kaggle output reported:

```text
Modelos: EVIDENCE
Routing: EVIDENCE
```

The output also displayed the measured `til-model-evidence.csv` and `til-routing-evidence.csv` tables, confirming that the lesson used EDU-ORCH measured evidence rather than the synthetic fallback.


## Semantic execution status

**PASS**

Observed in the completed Kaggle run:

- `Modelos: EVIDENCE`
- source: `data/model-evidence/til-model-evidence.csv`
- `Routing: EVIDENCE`
- source: `data/model-evidence/til-routing-evidence.csv`

The displayed model table contained measured EDU-ORCH-001 evidence, and the routing table contained measured-recovered EDU-ORCH-002 evidence. This closes the semantic execution gate for Aula 13C.
