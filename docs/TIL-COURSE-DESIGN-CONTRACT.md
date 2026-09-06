# TIL Course Design Contract

## Status

Accepted

## Purpose

This document defines the minimum pedagogical and operational standards for every lesson in the **Text Intelligence Lab (TIL) with Kaggle**.

The contract exists to preserve consistency, clarity, reproducibility, and learner autonomy as the course expands.

---

## 1. Core Principle

Every lesson must follow the TIL learning discipline:

```text
Architect
→ Implement small
→ Execute
→ Observe
→ Evaluate
→ Correct
→ Version
→ Expand
```

A notebook is not just a container for code. It is a guided learning experience.

---

## 2. Source of Truth and Execution

- **GitHub is the source of truth** for canonical notebooks, documentation, history, and decisions.
- **Kaggle is the primary educational and experimental execution environment**.
- The official Kaggle notebook is a course reference artifact.
- Students work in their **own Kaggle copy**.

Canonical rule:

```text
Official notebook = course reference
Student copy       = personal learning workspace
```

Students must not be added as editors of official course notebooks.

---

## 3. Student-First Design

Every lesson must be understandable without requiring external chat instructions.

A student should know:

- what to do;
- why to do it;
- what to observe;
- how to interpret the result;
- how to verify completion.

If a student must ask what a code cell is for before running it, the notebook is incomplete.

---

## 4. Explain Before Execute

No code cell should appear without sufficient context.

Before each meaningful code cell, the notebook should explain:

1. **Purpose** — why the cell exists;
2. **Action** — what the student should do;
3. **Expected observation** — what kind of output or effect to look for.

Avoid unexplained technical helper cells.

---

## 5. Default Lesson Structure

Use this structure when it adds pedagogical value:

1. Objectives
2. Context
3. Environment
4. Experiment
5. Observation
6. Interpretation
7. Exercise
8. Reproducibility
9. Summary

This is a default pattern, not a rigid template.

Sections may be omitted, merged, or adapted when that improves the lesson.

---

## 6. Learning Objectives

Each lesson must declare explicit learning objectives.

Objectives should describe what the student will be able to **recognize, explain, execute, compare, evaluate, or build** by the end of the lesson.

Avoid vague objectives such as “understand NLP better”.

---

## 7. Real-World Motivation

Important concepts should be connected to their practical value.

Whenever possible, explain:

- what problem the concept solves;
- why the problem matters;
- where the technique is useful;
- what trade-off or limitation the student should notice.

The course should consistently answer both:

```text
What is this?
Why does it matter?
```

---

## 8. Execution → Observation → Interpretation

Running code is never the end of an activity.

The preferred instructional loop is:

```text
Execute
→ Observe
→ Interpret
```

The notebook should explicitly direct the student to relevant outputs, metrics, warnings, or artifacts and explain what they mean.

---

## 9. Checkpoints

Use checkpoints to confirm progress at meaningful moments.

Example:

```text
Checkpoint:
Confirm that is_kaggle is True before continuing.
```

A checkpoint should validate one concrete learning or execution state.

Do not overuse them.

---

## 10. Exercises

Exercises should require the student to retrieve, interpret, modify, compare, or reason about what was taught.

### Mandatory pattern for coding exercises

Whenever the exercise requires Python or another programming language, the notebook must provide:

1. **A clear executable answer cell** where the student writes and runs the solution.
2. **A hint** that identifies the relevant language, library, API, functions, methods, or objects that may help.
3. **An executable solution** that the student can reveal and run for verification.
4. **A short explanation** of why the solution works when the code is not self-explanatory.

The preferred learner flow is:

```text
Read the problem
→ Write code in the student answer cell
→ Execute and inspect the result
→ Use hint if needed
→ Reveal and run the solution
→ Compare approaches
```

Whenever appropriate, follow the Kaggle-inspired interaction pattern:

```python
qN.hint()
qN.solution()
```

Recommended sequence:

```text
Try
→ Check when applicable
→ Hint if needed
→ Executable solution for verification
```

Hints must guide without immediately giving the final answer. For coding exercises, a good hint should usually mention the relevant library and a small set of useful functions or methods.

Solutions must be executable whenever the exercise itself is executable. Do not provide only a prose answer to a programming exercise.

The learner's answer cell must appear before the hint and solution cells.

For non-coding exercises, prose answers are acceptable when execution would add no pedagogical value.

---

## 11. Exercise Helper Cells

If an exercise requires setup code for hints, checking, or solutions:

- explain its purpose before the cell;
- state that it should be executed;
- clarify that it does not solve the exercise;
- keep the helper minimal and self-contained;
- place the student's executable answer cell before helper, hint, and solution cells;
- ensure that the revealed solution is executable for coding exercises.

Avoid dependencies on internal Kaggle teaching packages unless there is a strong reason.

---

## 12. Reproducibility

Every lesson must contain enough information to reproduce its execution.

When relevant, state:

- execution environment;
- language;
- accelerator;
- internet setting;
- datasets or inputs;
- generated outputs;
- assumptions that may vary across environments.

Never assume exact local/Kaggle Python minor-version parity unless explicitly required.

Observe the actual runtime.

---

## 13. Evidence Over Assumption

Do not claim that a lesson works without observable execution evidence.

A lesson is technically validated only when:

- the notebook executes successfully on Kaggle;
- expected outputs are produced;
- warnings and errors are reviewed;
- important runtime assumptions are verified.

Do not invent execution results.

---

## 14. Warnings Are Learning Signals

Warnings should not be ignored automatically.

For each relevant warning:

- determine whether it affects correctness;
- decide whether correction is necessary;
- document or fix it when appropriate.

The Aula 0 `nbformat` cell-id warning established this rule.

---

## 15. Student Copies

At the beginning of the course, students must learn to create their own Kaggle copy.

The original notebook remains the official reference.

Students may:

- execute;
- modify;
- experiment;
- break and repair their own copy.

They should not modify the course original.

---

## 16. Notebook Naming

Use stable numeric lesson prefixes:

```text
00-...
01-...
02-...
```

Recommended notebook pattern:

```text
NN-til-short-topic.ipynb
```

Recommended Kaggle slug:

```text
til-NN-short-topic
```

Do not encode version numbers such as `v1`, `v2`, or `final` in canonical filenames.

Git history and Kaggle Versions handle versioning.

---

## 17. Course Home

The Course Home is the learner's navigation entry point.

It should contain:

- course purpose;
- expected capabilities;
- real-world motivation;
- how to use the course;
- module and lesson map;
- lesson status;
- links to available notebooks.

Students should be able to navigate the course from Kaggle without needing to understand the repository structure.

---

## 18. Lesson Readiness

A lesson is considered **student-ready** when all items below are true:

- learning objectives are explicit;
- practical motivation is clear;
- code cells are introduced before execution;
- execution flow is understandable;
- outputs are explained;
- exercises are present when appropriate;
- hints/solutions follow the TIL pattern when appropriate;
- reproducibility information is included;
- the notebook executes successfully on Kaggle;
- warnings/errors were reviewed;
- the canonical source is versioned in GitHub;
- the lesson can be followed without external instructions.

---

## 19. Pedagogical Review

Before a lesson is accepted, someone should complete it from the learner perspective.

The reviewer should assess:

- **Clarity** — is it obvious what to do?
- **Flow** — does the sequence feel natural?
- **Cognitive load** — is unnecessary complexity avoided?
- **Motivation** — is the value of the topic clear?
- **Kaggle experience** — are copy, run, output, hint, and solution interactions understandable?
- **Independence** — can the lesson be completed without external guidance?

---

## 20. Quality Bar

The TIL does not aim to maximize content volume.

It aims to maximize useful learning per step.

Prefer:

- short experiments;
- explicit reasoning;
- observable evidence;
- practical examples;
- progressive difficulty;
- justified complexity.

Avoid:

- premature abstraction;
- unexplained code;
- unnecessary tooling;
- decorative complexity;
- advanced topics introduced before their prerequisites.

---

## 21. Definition of Done

A lesson is complete only when it passes both:

### Technical validation

```text
Source versioned
→ Kaggle execution complete
→ Outputs observed
→ Relevant warnings evaluated
```

### Pedagogical validation

```text
Student copy
→ Lesson followed independently
→ Exercises completed
→ Friction reviewed
→ Corrections incorporated
```

Only then should the lesson be listed as **Available** on the Course Home.

---

## 22. Governing Rule

When there is tension between adding more content and improving learner understanding, prefer learner understanding.

The TIL should grow by validated learning units, not by notebook volume.
