# TIL — Didactic Validation Strategy

## Status

Active project standard.

## Purpose

This standard defines how every new TIL lesson and every substantial lesson reengineering must be validated.

The governing idea is:

> A central teaching claim must be supported by observable execution evidence, not only by explanatory markdown.

The standard exists to prevent a notebook from being considered successful merely because it runs.

---

## 1. Core validation loop

Every important concept should follow:

```text
claim
→ prediction
→ executable evidence
→ observed output
→ guided interpretation
→ limitation / failure mode
→ application or decision
```

When useful, use the shorter pattern:

```text
predict
→ observe
→ explain
```

A lesson should make the student answer:

1. What happened?
2. Why did it happen?
3. What does this prove about the concept?
4. What does it NOT prove?
5. Under what condition could the conclusion fail?

---

## 2. Mechanism visibility

If a lesson teaches a mechanism, the mechanism should become observable.

Examples:

- attention → compute or inspect attention;
- contextual embeddings → compare contextual representations;
- retrieval → retrieve real candidates and measure retrieval quality;
- generation → execute a real generation loop when generation is the teaching objective;
- tool use → show how a tool is selected/called and how the result is handled;
- MCP → expose schemas, discovery, result contracts and host policy;
- routing → expose the routing decision and its evidence.

A stub is acceptable only when the stub itself is NOT the central concept being taught.

---

## 3. Evidence quality

Prefer controlled comparisons over isolated numbers.

Weak:

```text
cosine = 0.82
therefore the model understood the sense
```

Stronger:

```text
within-group similarity
vs
between-group similarity
vs
control group
```

Whenever possible, add:

- baseline;
- control group;
- counterexample;
- ambiguity case;
- failure case;
- sensitivity analysis.

Do not interpret a single metric without a reference when the metric is context-dependent.

---

## 4. Execution evidence must drive the lesson

Outputs are part of the teaching material.

After a Run All, inspect:

- unexpected warnings;
- exceptions;
- schema differences;
- null fields;
- library/runtime behavior;
- model outputs that contradict the prose;
- hidden asymmetries between success and failure cases.

If an output teaches something important, promote that observation into the lesson.

> Warnings, conflicts and surprising outputs are learning signals when they illuminate the system being taught.

Do not hide useful execution evidence merely to make the notebook look cleaner.

Reduce noise when the noise prevents the student from seeing the important behavior.

---

## 5. Do not invent execution results

Do not place fixed numerical results in markdown unless they are invariant by construction.

Avoid prose such as:

```text
"You should observe F1 ≈ 0.73."
"The cosine will be about 0.80."
```

Prefer:

```text
"Run the cell and compare the observed values."
"Did the within-group score exceed the between-group score?"
```

The notebook must remain truthful if a library, runtime or random seed changes.

---

## 6. Dependencies are part of the lesson contract

Critical dependencies must be explicit and validated early.

For each dependency:

- declare the required version/resource;
- use versioned Kaggle Dataset/Model resources when appropriate;
- keep Internet OFF when the lesson is designed for offline execution;
- fail early if a mandatory resource is missing;
- do not silently skip the central experiment.

Distinguish:

```text
dependency required by the lesson
≠
global compatibility of every package in the shared runtime
```

---

## 7. Exercise quality

Exercises should require at least one of:

- interpretation;
- modification;
- comparison;
- prediction;
- diagnosis;
- counterexample;
- architecture decision;
- failure analysis.

Avoid exercises that only ask the student to repeat the demonstration with different values.

Preferred pattern:

```text
prediction
→ student attempt
→ hint
→ solution/reference interpretation
```

Use the TIL interaction pattern:

```python
qN.hint()
qN.solution()
```

when applicable.

A solution should not be automatically executed immediately below the exercise.

---

## 8. Failure labs

A strong lesson should include at least one meaningful failure or ambiguity when the subject allows it.

The failure lab should identify:

- what the student predicted;
- what actually happened;
- what layer produced the failure;
- what the caller observed;
- what information remained internal;
- how the system should react.

Do not merely show an exception. Interpret the boundary.

---

## 9. Architecture and utility

When a lesson introduces additional architectural complexity, ask whether the complexity earns its place.

Use:

```text
simpler baseline
→ added mechanism
→ measurable benefit
→ new cost/risk
→ utility judgment
```

Do not assume:

```text
Transformer > classical ML
LLM > Transformer
agent > workflow
MCP > direct integration
```

Complexity must be justified by evidence.

---

## 10. Protocol/API/library distinction

When the lesson uses an SDK or framework, separate:

```text
concept/protocol
≠
SDK convenience API
≠
transport/runtime implementation
```

If possible, expose the underlying payload/schema/contract so the student learns something that survives a library change.

---

## 11. Readiness gates

Every materially new or reengineered lesson should have a readiness gate.

Recommended gates:

```text
G1  conceptual scope
G2  central mechanism observable
G3  dependency/resource contract
G4  controlled evidence
G5  failure/ambiguity coverage
G6  exercise quality
G7  reproducibility
G8  local/headless execution when applicable
G9  Kaggle Run All
G10 pedagogical inspection
```

A lesson is not student-ready merely because the notebook executes.

After executable cells change, reopen the relevant execution gates.

---

## 12. Pedagogical inspection after successful execution

After a successful Run All, review the notebook as a student, not as its author.

For each major block ask:

- What happened?
- Why did it happen?
- What does this prove?
- What limitation is visible?
- Is the important evidence buried in raw logs?
- Did the output reveal something the prose failed to explain?
- Does the exercise require reasoning or only imitation?

If execution reveals a better lesson than the one originally written, change the lesson.

---

## 13. Cross-lesson reuse

When a lesson creates a real reusable capability, prefer carrying it forward instead of replacing it with a synthetic stub in later lessons.

Examples:

```text
Aula 10 contextual encoder
→ Aula 15 semantic retrieval

retrieval evidence
→ Aula 16 RAG

tool contracts
→ MCP
→ agentic systems
```

This keeps the curriculum cumulative rather than episodic.

---

## 14. Promotion rule

A lesson can be promoted to student-ready only when:

```text
it runs
AND
the central mechanism is observable
AND
the evidence supports the claim
AND
the student is guided to interpret the output
AND
known limitations are visible
AND
the exercises require reasoning
```

## Governing principle

> In TIL, execution is not the end of validation. Execution produces evidence, and the evidence must improve the lesson.
