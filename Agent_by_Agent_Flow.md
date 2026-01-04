## Agent 0 — Orchestrator / Supervisor

Role: Traffic cop with a brain.

Input:

Problem statement

Final code (already passed test cases)

Interpreter logs

Output:

Task routing

Final consolidated score

➡️ Dispatches work to Agents 1–5 and enforces time limits.

## Agent 1 — Algorithm & Complexity Analyzer

Goal: What level problem did they actually solve?

Inputs: Code AST + runtime behavior
Tasks:

Identify algorithm class

Infer time & space complexity

Detect optimal vs suboptimal approach

Output (0–20 pts):

20 → optimal & minimal

14 → correct but non-optimal

8 → brute force survives by luck

0 → red-flag logic

## Agent 2 — Concept Ownership Probe

Goal: Does the candidate own the solution?

Method:
Auto-generates 5–7 questions based on their exact code:

Why this DS?

What invariant is maintained?

Which constraint makes this fail?

Timed. Text-only. No editor.

Scoring (0–25 pts):

Accuracy

Precision (no hand-waving)

Speed

## Agent 3 — Constraint Mutation & Adaptability

Goal: Can they generalize?

Method:
Agent mutates constraints:

N × 10

memory reduced

streaming input

relaxed guarantees

Candidate must:

explain required changes

or patch minimal logic

Scoring (0–20 pts):

20 → clean adaptation

12 → partial understanding

5 → restart-from-zero mentality

0 → frozen

## Agent 4 — Originality & AI-Likelihood Evaluator

Goal: Detect dependency, not usage.

Signals Used:

similarity to known AI clusters

symmetry / over-polished structure

explanation ↔ code mismatch

entropy of reasoning

Outputs:

Originality Score (0–15)

AI-Assistance Probability (informational, not penalizing)

## Agent 5 — Process Trace Analyzer

Goal: How did they think while coding?

Uses interpreter telemetry:

edit iterations

backtracking

refactors

run frequency

Scoring (0–20 pts):

Iterative refinement → high

One-shot perfection → suspicious

Random chaos → beginner

---

## Example

Algorithmic Strength: 18 / 20
Concept Ownership: 21 / 25
Adaptability: 15 / 20
Originality: 12 / 15
Process Quality: 17 / 20

Final Score: 83
Level: PRO (Hireable)

AI Assistance Probability: 22%
Confidence: High

---

## Meanings

### 🧮 Rubric → Numeric Meaning

| Dimension        | 0–5      | 6–10    | 11–15      | 16–20      |
| ---------------- | -------- | ------- | ---------- | ---------- |
| **Algorithm**    | Wrong    | Brute   | Acceptable | Optimal    |
| **Concepts**     | Guessing | Partial | Clear      | Sharp      |
| **Adaptability** | Frozen   | Weak    | Good       | Strong     |
| **Originality**  | Template | Common  | Distinct   | Unique     |
| **Process**      | Chaotic  | Linear  | Iterative  | Thoughtful |

---

### 🧩 Final Skill Mapping (Verdict)

| Score Range | Level                   | Meaning                      |
| ----------- | ----------------------- | ---------------------------- |
| 0–39        | **Beginner**            | Syntax-level coder           |
| 40–59       | **Intermediate**        | Can solve, weak fundamentals |
| 60–74       | **Strong Intermediate** | Real understanding           |
| 75–84       | **Pro**                 | Hireable engineer            |
| 85–100      | **Elite**               | Thinks like a senior         |

---

### 🤖 A️⃣ Agentic Grading Flow — Logical Diagram

**High-level flow (linear but supervised):**

1. **Candidate submits code**
2. **Code already passed all test cases**
3. **Interpreter logs are captured**

---

### 🧭 Supervisor / Orchestrator Agent

- Validates inputs
- Dispatches parallel agents
- Enforces time + ordering

---

### ⚙️ Parallel Evaluation Layer

- **Algorithm Analyzer Agent**
- **Concept Ownership Agent**
- **Adaptability Agent**
- **Originality / AI-likelihood Agent**
- **Process Trace Agent**

---

### 📊 Scoring Aggregation

- Normalize scores
- Apply weighted formula
- Compute confidence

---

### 🧩 Skill Mapping

- Beginner / Intermediate / Pro / Hireable

---

### 📑 Final Report Output

- Numeric score
- Skill level
- AI-likelihood _(non-punitive)_
- Audit trail

![Student prediction flowchart](flowcharts/studentprediction.png)
