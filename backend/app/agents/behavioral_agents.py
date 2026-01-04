from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

def agent_ownership(state: dict):
    print("--- Ownership Agent ---")
    code = state.get('student_code', '')
    
    prompt = ChatPromptTemplate.from_template(
        "You are an interviewer. Generate 3 hard technical questions based SPECIFICALLY on this code "
        "to test if the student wrote it. Ask about specific variables or logic choices.\n"
        "Code: {code}\n\nReturn a list of strings."
    )
    res = llm.invoke(prompt.format(code=code))
    # Naive split
    questions = [q for q in res.content.split('\n') if '?' in q]
    return {"agent2_ownership_questions": questions}

def agent_originality(state: dict):
    print("--- Originality Agent ---")
    code = state.get('student_code', '')
    
    prompt = ChatPromptTemplate.from_template(
        "Analyze this code for signs of AI generation or copy-pasting. "
        "Look for: over-commenting, textbook structure, or unused imports characteristic of LLMs.\n"
        "Code: {code}\n\nGive a score 0-15 (15=Original, 0=AI/Copied) and reasoning."
    )
    res = llm.invoke(prompt.format(code=code))
    return {"agent4_originality_score": {"raw": res.content}}
