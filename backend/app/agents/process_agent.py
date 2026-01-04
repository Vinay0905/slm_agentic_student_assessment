from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def agent_process(state: dict):
    print("--- Process Agent ---")
    logs = state.get('execution_logs', 'No logs provided')
    
    prompt = ChatPromptTemplate.from_template(
        "Analyze these coding session logs. Did they iterate? simple copy-paste? "
        "Logs: {logs}\n\nScore 0-20 (Process Quality)."
    )
    res = llm.invoke(prompt.format(logs=logs))
    return {"agent5_process_score": {"raw": res.content}}
