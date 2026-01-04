def supervisor_node(state: dict):
    print("--- Supervisor Agent ---")
    
    # Simple consolidation
    data = {
        "algorithm": state.get('agent1_algo_analysis'),
        "ownership": state.get('agent2_ownership_questions'),
        "adaptability": state.get('agent3_adaptability_feedback'),
        "originality": state.get('agent4_originality_score'),
        "process": state.get('agent5_process_score')
    }
    
    # In a real system, we might use an LLM here to write a coherent narrative.
    summary = f"Final Aggregation Report:\nAlgorithm: {data['algorithm']}\nOriginality: {data['originality']}\nProcess: {data['process']}"
    
    return {"final_report": summary}
