# Student Prediction System: Multi-Agent Coding Assessment

## 🚀 Project Overview

This system uses a **Multi-Agent LLM Architecture** (powered by `LangGraph` and `gpt-4o-mini`) to autonomously assess student coding submissions. Unlike simple unit testers, this system evaluates **Algorithm Complexity**, **Code Originality (AI Detection)**, **Conceptual Ownership**, and **Process Quality**.

## 🏗️ Technical Architecture

- **Orchestration**: `LangGraph` (Parallel Node Execution).
- **Model**: `gpt-4o-mini` (High reasoning, low cost).
- **Optimization Strategy**:
  - **Structured Outputs**: All agents return Strict JSON (via Pydantic) to eliminate conversational filler.
  - **Instruction Distillation**: High-density prompts to reduce input tokens.
  - **Context Trimming**: Agents only receive relevant state data.

## 🤖 Agent Roles

1.  **Algorithm Agent**: Analyzes Time/Space complexity (O(N) vs O(N^2)).
2.  **Ownership Agent**: Generates "Forensic" questions to verify the student actually wrote the code (detects blind copying).
3.  **Adaptability Agent**: Proposes constraint changes to test code robustness.
4.  **Originality Agent**: Scores code 0-15 based on "AI-isms", over-engineering, and suspicious style patterns.
5.  **Process Agent**: Analyzes execution logs to detect "Copy-Paste" behavior vs. genuine iteration.
6.  **Supervisor**: Aggregates all structured results into a final Markdown report with a weighted score.

## 📅 Progress Log (Jan 2026)

### Completed

- [x] **Project Setup**: Environment, `.env`, dependency management.
- [x] **Prototype v1**: Initial sequential graph in Jupyter.
- [x] **Migration to Parallel Graph**: Optimized for speed.
- [x] **Token Optimization**: Implemented Pydantic models for all 5 agents.
- [x] **Intelligence Upgrade**:
  - Refined "Originality" agent to detect obfuscated/Y-combinator code.
  - Added "Verification Questions" to the final report.

### 🛑 Current Stopping Point

We have fully validated the **Optimized Architecture** in `backend/app/notebooks/agent_prototype.ipynb`. The agents are now capable of detecting advanced obfuscation and generating specific reasoning.

**Next Immediate Task:**

- **Sync Backend**: Copy the optimized Pydantic schemas and Prompts from the Notebook into the actual Python files in `backend/app/agents/`.
- The notebook is the "Source of Truth" right now; the backend files are outdated (still using unstructured returns).

## 🔮 Roadmap

1.  **Port Notebook to Codebase**: Update `coding_agent.py`, `behavioral_agents.py`, etc.
2.  **Create Main Entry**: Build `main.py` to run the graph via CLI/API.
3.  **Frontend Integration**: Connect to the Streamlit/React dashboard.
