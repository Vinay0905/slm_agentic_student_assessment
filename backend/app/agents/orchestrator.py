import os
from typing import TypedDict, List, Dict, Optional, Any
from langgraph.graph import StateGraph, END
from dotenv import load_dotenv

# Import agent functions (Lazy import inside nodes or at top if generic)
# We will assume they are implemented in their respective modules.
# For now, I will define the State here.

class AgentState(TypedDict):
    """
    Shared state for the Multi-Agent Coding Assessment Flow.
    """
    # Inputs
    problem_statement: str
    student_code: str
    language: str
    execution_logs: Optional[str]

    # Agent Outputs
    agent1_algo_analysis: Optional[Dict[str, Any]]
    agent2_ownership_questions: Optional[List[str]]
    agent3_adaptability_feedback: Optional[str]
    agent4_originality_score: Optional[Dict[str, Any]]
    agent5_process_score: Optional[Dict[str, Any]]

    # Final
    final_report: Optional[str]

class Orchestrator:
    def __init__(self):
        load_dotenv()
        self.workflow = StateGraph(AgentState)
        self._build_graph()

    def _build_graph(self):
        # 1. Define Nodes (Lazy loading to avoid circular imports if we move these out)
        from .coding_agent import agent_algorithm, agent_adaptability
        from .behavioral_agents import agent_ownership, agent_originality
        from .process_agent import agent_process
        from .supervisor_agent import supervisor_node

        self.workflow.add_node("agent_algorithm", agent_algorithm)
        self.workflow.add_node("agent_ownership", agent_ownership)
        self.workflow.add_node("agent_adaptability", agent_adaptability)
        self.workflow.add_node("agent_originality", agent_originality)
        self.workflow.add_node("agent_process", agent_process)
        self.workflow.add_node("supervisor", supervisor_node)

        # 2. Define Edges (Parallel Execution)

        # Ideally: self.workflow.add_edge(START, "agent_...") for all.
        # But to be safe with imports, let's just make a dummy or fan out from algorithm if we want 100% simple.
        # Actually, let's use the explicit START node if we import it.
        # Since I didn't import START in the original write, let's add it.
        
        # Parallel Pattern:
        from langgraph.graph import START
        self.workflow.add_edge(START, "agent_algorithm")
        self.workflow.add_edge(START, "agent_ownership")
        self.workflow.add_edge(START, "agent_adaptability")
        self.workflow.add_edge(START, "agent_originality")
        self.workflow.add_edge(START, "agent_process")

        # Converge
        self.workflow.add_edge("agent_algorithm", "supervisor")
        self.workflow.add_edge("agent_ownership", "supervisor")
        self.workflow.add_edge("agent_adaptability", "supervisor")
        self.workflow.add_edge("agent_originality", "supervisor")
        self.workflow.add_edge("agent_process", "supervisor")
        
        self.workflow.add_edge("supervisor", END)

        self.app = self.workflow.compile()

    def run_flow(self, problem: str, code: str, logs: str = ""):
        inputs = {
            "problem_statement": problem,
            "student_code": code,
            "execution_logs": logs,
            "language": "python" # Default for now
        }
        return self.app.invoke(inputs)
