# Executive Summary

## SLM-Driven Multi-Agent Student Assessment Platform

### Problem

Traditional coding tests and interviews fail to accurately measure student skill in an era where AI assistance, memorization, and copied solutions are common. Existing platforms rely heavily on surface-level correctness, lack explainability, and provide limited protection against plagiarism or biased evaluation.

---

### Solution

We propose a **GenAI-powered, SLM-first, multi-agent assessment system** that evaluates students across **coding tests, aptitude tests, and AI-driven mock interviews**. The system focuses on **actual skill detection**, originality, and reasoning ability rather than raw correctness alone.

---

### Key Innovations

- **Agentic Architecture**: Specialized agents independently evaluate coding, aptitude, and interviews.
- **SLM-First Design**: Small Language Models handle routing, evaluation, supervision, and scoring—reducing cost and improving specialization.
- **Plagiarism & Uniqueness Detection**: Code solutions are compared via vector embeddings to detect similarity and measure algorithmic originality.
- **Supervisor Agent**: A dedicated agent validates all evaluations, ensuring consistency, fairness, and auditability.
- **Vector Database Intelligence**: Student performance is compared against historically similar profiles, enabling contextual ranking rather than absolute scoring.
- **Context Engineering**: Each agent receives strictly controlled, task-specific context to prevent bias and hallucination.

---

### System Flow

1. Students complete assessments via a unified interface.
2. A Test Orchestrator routes tasks to evaluation agents.
3. Agent outputs are embedded and stored in a vector database.
4. A Supervisor Agent validates and approves evaluations.
5. A Meta-Scoring Agent aggregates results, computes ranks, and generates explainable feedback.

---

### Impact

- Fairer, more reliable student assessment
- Improved detection of genuine skill vs copied solutions
- Actionable feedback for students and recruiters
- Scalable, auditable infrastructure for academic and hiring use cases

---

### Why Small Language Models

SLMs are faster, cheaper, and easier to specialize than large LLMs. By reserving large models only for deep interview reasoning, the system achieves strong performance while remaining cost-effective and production-ready.

---

### Conclusion

This platform demonstrates how **agentic workflows, context engineering, and vector-based intelligence** can be combined to create a trustworthy, scalable student assessment system aligned with real-world skill evaluation needs.
