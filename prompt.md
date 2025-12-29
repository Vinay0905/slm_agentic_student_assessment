# GenAI + SLM-Based Student Assessment Platform

## Master Build Prompt

You are tasked with building a GenAI-powered, SLM-first, multi-agent system that evaluates students across coding tests, aptitude tests, and AI-driven mock interviews.

This is not a chatbot or learning app.
This is a reliable, auditable student skill assessment and ranking system.

---

## Core Goals

- Evaluate actual student skill, not surface-level correctness
- Use Small Language Models (SLMs) as the primary intelligence
- Apply agentic workflows with strict context engineering
- Detect plagiarism and solution originality
- Produce fair, explainable scores and rankings

---

## High-Level Architecture

The system consists of:

1. Student Interface (login, tests, results)
2. Test Orchestrator (SLM)
3. Specialized Evaluation Agents:
   - Coding Evaluation Agent
   - Aptitude Evaluation Agent
   - Mock Interview Agent
4. Vector Database (comparative intelligence)
5. Supervisor Agent (quality & consistency control)
6. Meta-Scoring & Ranking Agent
7. Results & Analytics Dashboard

---

## Design Constraints

- SLMs must handle routing, evaluation, scoring, and supervision
- Larger LLMs may be used only for deep interview reasoning
- Agents must communicate via structured outputs (JSON)
- Context must be minimal, task-specific, and controlled
- Vector DB is used for similarity comparison, not raw memory

---

## Evaluation Logic Summary

### Coding

- Correctness
- Time & space complexity
- Plagiarism detection (vector similarity)
- Solution uniqueness (algorithmic diversity)

### Aptitude

- Accuracy
- Speed vs accuracy
- Difficulty-weighted scoring

### Interview

- Concept clarity
- Communication
- Reasoning depth
- Adaptive questioning using rolling summaries

---

## Reliability & Safety

- Supervisor agent validates all agent outputs
- Anomaly detection and consistency checks
- Confidence scores propagate through pipeline
- Meta agent only consumes supervisor-approved summaries

---

## Expected Output

- Section-wise scores
- Overall score and rank
- Strengths and weaknesses
- Skill-gap analysis
- Explainable feedback

---

## Success Criteria

- Copied solutions score lower despite correctness
- Strong reasoning is rewarded over memorization
- Rankings are reproducible and auditable
- Agents can be independently evaluated and replaced

Build the system strictly following this specification.
