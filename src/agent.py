import os
from typing import TypedDict, List
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from langfuse.langchain import CallbackHandler


from src.retriever import search_knowledge_base

load_dotenv()

# 1. Initialize Groq LLM
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2,  # Low temperature for factual, consistent answers
)



# 2. Define the Agent's State (The memory box passed between steps)
class AgentState(TypedDict):
    question: str
    documents: List[dict]
    answer: str
    action_type: str        # "chat", "retrieve", or "jira_approval"
    ticket_data: dict       # Extracted ticket fields


# ----------------------------------------------------
# 3. Define the Nodes (The Actions)
# ----------------------------------------------------

def router_node(state: AgentState):
    """Classifies if the question requires document retrieval or is casual chat."""
    question = state["question"]
    
    prompt = f"""You are an intent classifier.
Is the following user message asking about company policies, runbooks, engineering, HR, benefits, travel, or expenses?
Or is it a casual greeting/general chat (e.g. 'hi', 'how are you', 'thanks')?

Message: "{question}"

Answer with only ONE word: "RETRIEVE" or "CHIT_CHAT"."""

    response = llm.invoke([HumanMessage(content=prompt)]).content.strip().upper()
    return {"decision": "RETRIEVE" if "RETRIEVE" in response else "CHIT_CHAT"}


def direct_chat_node(state: AgentState):
    """Answers casual greetings directly without touching the database."""
    question = state["question"]
    prompt = f"You are a helpful, professional Slack workplace assistant. Reply cordially to: '{question}'"
    response = llm.invoke([HumanMessage(content=prompt)])
    return {"answer": response.content}


def retrieve_node(state: AgentState):
    """Searches Qdrant for the top 3 relevant chunks."""
    question = state["question"]
    docs = search_knowledge_base(question, limit=3)
    return {"documents": docs}


def generate_node(state: AgentState):
    """Generates a grounded answer citing the source documents."""
    question = state["question"]
    docs = state.get("documents", [])

    if not docs:
        return {"answer": "I searched our enterprise knowledge base, but couldn't find any relevant policies on this topic."}

    # Format the retrieved chunks for the LLM
    context_text = ""
    sources = set()
    for d in docs:
        context_text += f"\n--- Source: {d['source']} ({d['category']}) ---\n{d['text']}\n"
        sources.add(f"{d['source']}")

    system_prompt = """You are Acme Corp's official AI Workplace Assistant.
Answer the user's question accurately using ONLY the provided context.
Rules:
1. If the answer is not contained in the context, say: "I don't have information on this in our company records."
2. Never make up facts or policies.
3. Always include a '📚 Sources cited:' line at the end mentioning which document you used."""

    user_prompt = f"""Context:
{context_text}

User Question: {question}"""

    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ])
    
    return {"answer": response.content}


# ----------------------------------------------------
# 4. Build the LangGraph Workflow
# ----------------------------------------------------

workflow = StateGraph(AgentState)

# Add our nodes to the graph                
workflow.add_node("retrieve", retrieve_node)
workflow.add_node("generate", generate_node)
workflow.add_node("direct_chat", direct_chat_node)

# Conditional router logic
def route_decision(state):
    decision = router_node(state)["decision"]
    if decision == "RETRIEVE":
        return "retrieve"
    return "direct_chat"

# Set graph entry point
workflow.set_conditional_entry_point(
    route_decision,
    {
        "retrieve": "retrieve",
        "direct_chat": "direct_chat",
    }
)

# Connect edges
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)
workflow.add_edge("direct_chat", END)

# In-memory checkpointer for thread memory
memory = MemorySaver()
agent_app = workflow.compile(checkpointer=memory)


# ----------------------------------------------------
# 5. Public helper function for Slack
# ----------------------------------------------------

def ask_agent(question: str, thread_id: str = "default_thread") -> dict:
    """Runs LangGraph, traces execution to Langfuse, and returns both answer and trace_id."""
    # Initialize Langfuse tracer (new Langfuse v5 API)
    langfuse_handler = CallbackHandler()
    
    config = {
        "configurable": {"thread_id": thread_id},
        "callbacks": [langfuse_handler],
        "metadata": {
            "session_id": thread_id,
            "user_id": "slack_user",
        }
    }
    
    initial_state = {"question": question, "documents": [], "answer": ""}
    final_output = agent_app.invoke(initial_state, config=config)
    
    # In Langfuse v5+, trace ID is accessed via last_trace_id
    trace_id = langfuse_handler.last_trace_id or ""
    return {
        "answer": final_output["answer"],
        "trace_id": trace_id
    }


# Test directly in terminal
if __name__ == "__main__":
    print("Testing LangGraph Agent in terminal...\n")

    # Test 1: Casual Greeting (Should skip Qdrant)
    print("--- Test 1: Chit-Chat ---")
    print("Q: 'Hello, good morning!'")
    print("A:", ask_agent("Hello, good morning!"), "\n")

    # Test 2: HR Question (Should retrieve from leave_and_benefits.md)
    print("--- Test 2: HR Policy ---")
    print("Q: 'How many days of paid parental leave do primary caregivers get?'")
    print("A:", ask_agent("How many days of paid parental leave do primary caregivers get?"), "\n")

    # Test 3: Engineering Question (Should retrieve from incident_runbooks.md)
    print("--- Test 3: Engineering Runbook ---")
    print("Q: 'What are the immediate steps for Postgres connection pool exhaustion?'")
    print("A:", ask_agent("What are the immediate steps for Postgres connection pool exhaustion?"), "\n")