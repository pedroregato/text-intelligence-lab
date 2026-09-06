# TIL Glossary

## Status

Living document

## Purpose

This glossary supports the **Text Intelligence Lab (TIL) with Kaggle** by defining technical and methodological terms used throughout the course.

The glossary is intentionally cumulative: each lesson should add only the concepts it actually introduces.

Each entry contains:

- **Definition** — a concise technical meaning;
- **In the TIL** — how the concept appears in this course;
- **References** — suggested sources for deeper study.

---

## Core Concepts

### Data

**Definition**

A recorded representation of facts, observations, measurements, categories, events, or other information that can be stored, inspected, processed, or analyzed.

**In the TIL**

Text becomes data when it is represented in a form that can be organized, inspected, measured, transformed, and used in experiments.

**References**

- Provost, F.; Fawcett, T. *Data Science for Business*.
- NIST terminology resources.

---

### Observable Data

**Definition**

Data whose values, structure, state, or outputs can be directly examined.

**In the TIL**

A dataset is observable when the student can inspect records, columns, values, generated outputs, metrics, or runtime information instead of merely assuming that something happened.

**Example**

A DataFrame that displays the columns `id`, `channel`, `label`, and `text` is observable because the learner can inspect its contents directly.

---

### Inspectable Data

**Definition**

Data that can be systematically examined to understand structure, quality, consistency, anomalies, missing values, duplicates, or other relevant properties.

**In the TIL**

Inspection means asking questions such as:

- How many documents exist?
- Are some texts empty?
- Are labels missing?
- Are there duplicated records?
- What metadata is available?

Inspectable data supports disciplined analysis before modeling.

---

### Reproducible Data / Reproducible Result

**Definition**

A dataset, transformation, experiment, or result is reproducible when another person can follow the documented procedure under equivalent conditions and obtain the same or substantively equivalent outcome.

**In the TIL**

Reproducibility depends on:

- canonical source in GitHub;
- documented Kaggle execution environment;
- explicit inputs;
- visible code;
- observed outputs;
- recorded assumptions.

**Important**

Reproducibility is stronger than “it worked once”.

---

### Evidence

**Definition**

An observable artifact or result that supports a technical conclusion.

**In the TIL**

Examples include:

- a downloaded JSON output;
- a Kaggle execution status;
- a metric;
- a generated file;
- a visible DataFrame;
- a warning or error log.

The course prioritizes evidence over assumption.

---

### Observation

**Definition**

A unit of data represented as one record in a dataset.

**In the TIL**

In a tabular corpus, one row may represent one document or one message.

**Note**

The word “observation” is also used more generally in the course to mean the act of examining outputs. Context determines which meaning applies.

---

## Text Intelligence Concepts

### Text Intelligence

**Definition**

The use of computational methods to extract structure, patterns, meaning, categories, signals, or actionable information from textual data.

**In the TIL**

Text Intelligence is the umbrella concept of the course. NLP, Machine Learning, embeddings, transformers, and LLMs are some of the approaches that may be used within it.

---

### NLP — Natural Language Processing

**Definition**

A field of computing and artificial intelligence concerned with enabling computers to process, analyze, generate, or interact with human language.

**In the TIL**

NLP provides many of the techniques used to transform raw text into structured representations and predictive or analytical systems.

**References**

- Jurafsky, D.; Martin, J. H. *Speech and Language Processing*.
- Manning, C. D.; Raghavan, P.; Schütze, H. *Introduction to Information Retrieval*.

---

### Document

**Definition**

An individual unit of text selected for analysis.

**Examples**

- one customer message;
- one email;
- one news article;
- one review;
- one contract;
- one support ticket.

**In the TIL**

In Aula 1, each row of the example DataFrame corresponds to one document.

---

### Corpus

**Definition**

A collection of documents organized for linguistic, statistical, or computational analysis.

**In the TIL**

A corpus may be small and artificial for learning purposes or contain millions of real-world documents in production settings.

**References**

- Jurafsky & Martin.
- Bird, Klein & Loper. *Natural Language Processing with Python*.

---

### Dataset

**Definition**

An organized collection of data used for analysis, experimentation, or modeling.

**In the TIL**

A corpus is a dataset whose central analytical object is text.

A dataset may also include non-textual fields such as IDs, dates, channels, labels, or other metadata.

---

### Metadata

**Definition**

Data that describes or provides context about other data.

**In the TIL**

Examples from Aula 1:

- `id` — identifies a document;
- `channel` — indicates its source;
- `label` — indicates a known category.

The `text` column contains the textual content itself.

---

### Label / Rótulo

**Definition**

A known category, class, or target value associated with an observation.

**In the TIL**

Examples:

- `duvida`
- `reclamacao`
- `elogio`

Labels may later serve as targets in supervised Machine Learning tasks.

**References**

- scikit-learn User Guide — supervised learning terminology.

---

### Class

**Definition**

A category that a model may learn to predict.

**In the TIL**

If `reclamacao`, `elogio`, and `duvida` are possible labels, each one is a class in a classification problem.

---

### Feature

**Definition**

A measurable or encoded characteristic used as input to an analytical or predictive model.

**In the TIL**

The raw `text` field is not yet a numerical feature matrix.

Later lessons will show how text can be transformed into features using approaches such as Bag-of-Words, TF-IDF, embeddings, and transformer representations.

---

### Raw Text

**Definition**

Text in its original or minimally processed form before representation or transformation for modeling.

**In the TIL**

The `text` column in Aula 1 is raw text.

---

### Empty Text

**Definition**

A text field containing no meaningful characters after basic whitespace inspection.

**In the TIL**

Empty text is a data-quality issue because downstream NLP steps may fail, distort statistics, or produce meaningless representations.

---

### Missing Value

**Definition**

A field whose expected value is absent or undefined.

**In the TIL**

A missing `label` differs from an empty `text`:

- missing label = category unavailable;
- empty text = document content unavailable.

These conditions may require different treatment.

---

### Duplicate

**Definition**

A repeated observation or repeated value that appears more than once in a dataset.

**In the TIL**

Repeated text may represent:

- legitimate repeated messages;
- duplicated ingestion;
- copied content;
- data-quality problems.

Duplicates should be investigated before automatically removing them.

---

## Experimental and Engineering Concepts

### Runtime

**Definition**

The software and system environment in which code is actually executed.

**In the TIL**

Examples:

- Python version;
- operating system;
- working directory;
- installed libraries;
- accelerator availability.

The Kaggle runtime may differ from the local project environment.

---

### Output

**Definition**

Any result produced by executing code.

**In the TIL**

Outputs may include:

- displayed values;
- tables;
- files;
- metrics;
- logs;
- charts;
- serialized evidence.

---

### Artifact

**Definition**

A persistent object produced or maintained as part of an engineering or analytical process.

**In the TIL**

Examples:

- notebook;
- JSON evidence file;
- experiment record;
- runbook;
- dataset;
- model file.

---

### Experiment

**Definition**

A structured procedure designed to test a hypothesis or validate an assumption.

**In the TIL**

A typical experiment records:

- Objective
- Hypothesis
- Environment
- Procedure
- Evidence
- Result
- Conclusion

---

### Hypothesis

**Definition**

A testable expectation about what should happen under defined conditions.

**In the TIL**

Example:

> If the notebook executes in Kaggle, then `is_kaggle` should be `True` and the expected evidence file should be generated.

---

### Reproducibility

**Definition**

The ability to repeat an analytical or computational procedure from documented inputs, code, environment assumptions, and steps.

**In the TIL**

Reproducibility is a core quality criterion for every lesson.

---

### Source of Truth

**Definition**

The authoritative location considered the canonical version of an artifact.

**In the TIL**

GitHub is the source of truth for:

- notebooks;
- documentation;
- engineering decisions;
- version history.

Kaggle is the primary execution environment, not the canonical repository.

---

### Versioning

**Definition**

The systematic tracking of changes to code, documents, data, or other artifacts over time.

**In the TIL**

- Git/GitHub provides canonical version history.
- Kaggle Versions records notebook execution versions.

Notebook filenames should not contain manual suffixes such as `v2`, `final`, or `final-final`.

---

### Baseline

**Definition**

A simple reference solution or configuration used for comparison.

**In the TIL**

A baseline establishes the minimum performance or behavior that a more advanced approach should improve upon.

Later lessons will use simple NLP and Machine Learning baselines before introducing more complex methods.

---

### Pipeline

**Definition**

An ordered sequence of processing steps that transforms inputs into outputs.

**In the TIL**

A future NLP pipeline may include:

```text
raw text
→ validation
→ preprocessing
→ representation
→ model
→ evaluation
→ output
```

---

### Checkpoint

**Definition**

A defined point in a learning or execution flow used to confirm that an expected state has been reached.

**In the TIL**

Example:

> Confirm that `is_kaggle` is `True` before continuing.

A checkpoint is not necessarily a saved model state; in this course it is primarily a pedagogical validation point unless explicitly stated otherwise.

---

## Statistical and Machine Learning Terms

### Sample

**Definition**

A subset of observations selected from a larger population or dataset.

**In the TIL**

The meaning may vary by context. In statistical discussion, a sample represents observations drawn from a population. In Machine Learning practice, the term may informally refer to a subset of the available dataset.

---

### Model

**Definition**

A mathematical or computational representation learned or specified to describe patterns or make predictions.

**In the TIL**

Models will later be used for tasks such as classification and semantic representation.

---

### Training

**Definition**

The process of estimating model parameters from data.

**In the TIL**

Training appears only after the course has established data quality, representation, and evaluation foundations.

---

### Classification

**Definition**

A predictive task in which an observation is assigned to one of a predefined set of classes.

**In the TIL**

Examples:

- classifying a document as `contrato`, `recibo`, or `ata`;
- classifying a customer message as `reclamacao`, `elogio`, or `duvida`.

---

### Metric

**Definition**

A quantitative measure used to evaluate a property of data, a process, or a model.

**In the TIL**

Future examples include accuracy, precision, recall, F1-score, latency, and coverage.

A metric must be interpreted in relation to the actual problem.

---

## How to Use This Glossary

When a new concept appears in a lesson:

1. the notebook should provide enough context for the student to continue;
2. the glossary may provide a more formal definition;
3. references may be used for deeper study.

The glossary should support learning, not interrupt it.

---

## References Used Across the Course

- Jurafsky, D.; Martin, J. H. *Speech and Language Processing*.
- Manning, C. D.; Raghavan, P.; Schütze, H. *Introduction to Information Retrieval*.
- Bird, S.; Klein, E.; Loper, E. *Natural Language Processing with Python*.
- Provost, F.; Fawcett, T. *Data Science for Business*.
- scikit-learn User Guide.
- NIST technical terminology and data/AI resources.
