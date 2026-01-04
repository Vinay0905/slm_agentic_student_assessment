from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def agent_algorithm(state: dict):
    print("--- Algorithm Agent ---")
    code = state.get('student_code', '')
    problem = state.get('problem_statement', '')
    
    prompt = ChatPromptTemplate.from_template(
        "Analyze the code for the given problem.\n"
        "Problem: {problem}\nCode: {code}\n\n"
        "Identify: 1. Algorithm utilized. 2. Time Complexity. 3. Space Complexity. "
        "Rate optimality (0-20). Return JSON-like string."
    )
    res = llm.invoke(prompt.format(problem=problem, code=code))
    return {"agent1_algo_analysis": {"raw": res.content}}

def agent_adaptability(state: dict):
    print("--- Adaptability Agent ---")
    code = state.get('student_code', '')
    problem = state.get('problem_statement', '')
    
    prompt = ChatPromptTemplate.from_template(
        "Propose a change to constraints (e.g. N increased by 100x, or memory / 2) "
        "and explain if this code would break or how it should change.\n"
        "Problem: {problem}\nCode: {code}"
    )
    res = llm.invoke(prompt.format(problem=problem, code=code))
    return {"agent3_adaptability_feedback": res.content}
