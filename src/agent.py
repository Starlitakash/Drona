import os
import sys
import json
import re
from typing import TypedDict, List, Optional, Dict, Any
from dotenv import load_dotenv

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

try:
    from langfuse.langchain import CallbackHandler
except ImportError:
    CallbackHandler = None

from pathlib import Path
# Ensure workspace root is in sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.retriever import search_knowledge_base
from src.jira_tool import create_jira_ticket, get_jira_ticket, update_jira_ticket

load_dotenv()

# 1. Initialize Groq LLM
GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")
llm = ChatGroq(
    model=GROQ_MODEL,
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.1,
)


# 2. Define the Agent's State
class AgentState(TypedDict, total=False):
    question: str
    documents: List[dict]
    answer: str
    intent: str
    pending_ticket: Optional[dict]
    ticket_key: Optional[str]
    ticket_summary: Optional[str]
    ticket_type: Optional[str]
    ticket_priority: Optional[str]
    ticket_comment: Optional[str]
    clarifying_question: Optional[str]


# ----------------------------------------------------
# 3. Router Node (Intent Classification & Parameter Extraction)
# ----------------------------------------------------

ROUTER_SYSTEM_PROMPT = """You are the intelligent router for 'Drona', the enterprise AI workplace assistant at NexaTech Solutions.
Analyze the user's message and classify it into exactly ONE of these intents:

1. DIRECT_CHAT: Greetings, casual pleasantries, or questions about who you are (e.g., "Hello!", "Good morning", "Who are you?", "Thanks").
2. AMBIGUOUS: Vague, single-word, or under-specified inputs where intent is completely unclear (e.g., "leave", "wifi", "vpn", "laptop", "help", "policy").
3. JIRA_CREATE: User explicitly wants to create, file, or report a bug, issue, or ticket (e.g., "Create a Jira ticket: Database connection pool exhausted", "File a bug for payment timeout").
4. JIRA_CHECK: User wants to check status or details of a Jira ticket (e.g., "Check status of ticket NEXA-101", "What is the status of NEXA-245?").
5. JIRA_UPDATE: User wants to update or add a comment/note to a Jira ticket (e.g., "Update ticket NEXA-101 with comment: SRE investigating").
6. RAG: User is asking a knowledge question about NexaTech policies, HR benefits, technical runbooks, engineering standards, travel per diem, or company guidelines.

Return ONLY a valid JSON object with the following fields:
{
  "intent": "DIRECT_CHAT" | "AMBIGUOUS" | "JIRA_CREATE" | "JIRA_CHECK" | "JIRA_UPDATE" | "RAG",
  "ticket_key": "NEXA-123" (extracted ticket key, or null),
  "ticket_summary": "Short title of ticket" (or null),
  "ticket_type": "Bug" | "Task" | "Story" (or null),
  "ticket_priority": "Low" | "Medium" | "High" | "Highest" (or null),
  "ticket_comment": "comment text to add" (or null),
  "clarifying_question": "suggested clarifying question with 2-3 specific NexaTech options if AMBIGUOUS" (or null)
}
Strictly output JSON only."""


def router_node(state: AgentState) -> Dict[str, Any]:
    """Classifies user intent and extracts relevant entities or handles pending confirmation."""
    question = state.get("question", "").strip()
    pending = state.get("pending_ticket")

    # A. Check if user is confirming or cancelling a pending ticket creation
    if pending:
        q_lower = question.lower()
        confirm_words = ["confirm", "yes", "proceed", "go ahead", "approved", "ok create", "sure", "yep", "do it", "please create"]
        cancel_words = ["cancel", "no", "abort", "don't create", "nevermind", "stop", "dismiss"]

        if any(w in q_lower for w in confirm_words):
            return {"intent": "JIRA_EXECUTE"}
        elif any(w in q_lower for w in cancel_words):
            return {"intent": "JIRA_CANCEL"}

    # B. Fast regex checks for Jira check/update patterns
    jira_key_match = re.search(r"\b([A-Za-z]{2,10}-\d+)\b", question)
    extracted_key = jira_key_match.group(1).upper() if jira_key_match else None

    # C. LLM Classification & Entity Extraction
    try:
        response = llm.invoke([
            SystemMessage(content=ROUTER_SYSTEM_PROMPT),
            HumanMessage(content=question)
        ])
        content = response.content.strip()
        # Clean any markdown code fences if LLM wrapped in ```json
        content = re.sub(r"^```(?:json)?\s*", "", content, flags=re.MULTILINE)
        content = re.sub(r"\s*```$", "", content, flags=re.MULTILINE).strip()
        parsed = json.loads(content)

        intent = parsed.get("intent", "RAG").upper()
        ticket_key = parsed.get("ticket_key") or extracted_key
        ticket_summary = parsed.get("ticket_summary")
        ticket_type = parsed.get("ticket_type") or "Bug"
        ticket_priority = parsed.get("ticket_priority") or "High"
        ticket_comment = parsed.get("ticket_comment")
        clarifying_question = parsed.get("clarifying_question")

        # Map JIRA_CREATE to JIRA_PROPOSE (confirmation strictly required)
        if intent == "JIRA_CREATE":
            if not ticket_summary:
                ticket_summary = question
            return {
                "intent": "JIRA_PROPOSE",
                "ticket_summary": ticket_summary,
                "ticket_type": ticket_type,
                "ticket_priority": ticket_priority,
            }

        return {
            "intent": intent,
            "ticket_key": ticket_key,
            "ticket_summary": ticket_summary,
            "ticket_type": ticket_type,
            "ticket_priority": ticket_priority,
            "ticket_comment": ticket_comment,
            "clarifying_question": clarifying_question,
        }

    except Exception as e:
        print(f"[Router Fallback]: {e}")
        # Deterministic rule-based fallback if LLM classification fails
        q_lower = question.lower()
        if any(w in q_lower for w in ["hi", "hello", "hey", "good morning", "good evening"]):
            return {"intent": "DIRECT_CHAT"}
        elif len(question.split()) <= 2 and not any(w in q_lower for w in ["how", "what", "where", "who", "when", "why", "is"]):
            return {
                "intent": "AMBIGUOUS",
                "clarifying_question": f"Could you please provide more details on what you need regarding '{question}'? For example, are you looking for company policies, IT assistance, or raising a request?"
            }
        elif "jira" in q_lower or "ticket" in q_lower:
            if extracted_key and any(w in q_lower for w in ["check", "status", "view", "details"]):
                return {"intent": "JIRA_CHECK", "ticket_key": extracted_key}
            elif extracted_key and any(w in q_lower for w in ["update", "comment", "note"]):
                return {"intent": "JIRA_UPDATE", "ticket_key": extracted_key, "ticket_comment": question}
            else:
                return {
                    "intent": "JIRA_PROPOSE",
                    "ticket_summary": question,
                    "ticket_type": "Bug",
                    "ticket_priority": "High"
                }
        return {"intent": "RAG"}


# ----------------------------------------------------
# 4. Handler Nodes
# ----------------------------------------------------

def direct_chat_node(state: AgentState) -> Dict[str, Any]:
    """Generates a warm, professional greeting as Drona."""
    question = state.get("question", "")
    prompt = f"""You are 'Drona', the friendly and professional AI Workplace Assistant for NexaTech Solutions.
A team member just said: "{question}".
Give a polite, warm response (2-3 sentences max).
Mention that you can answer questions about NexaTech company policies, technical runbooks, HR benefits, or create and check Jira tickets."""
    response = llm.invoke([HumanMessage(content=prompt)])
    return {"answer": response.content.strip()}


def clarify_node(state: AgentState) -> Dict[str, Any]:
    """Asks clarifying question when the user's input is ambiguous or too brief."""
    clarifying_q = state.get("clarifying_question")
    question = state.get("question", "")

    if not clarifying_q:
        clarifying_q = f"Could you please provide a bit more detail on what you are looking for regarding '{question}'?"

    answer = (
        f"❓ **Could you please clarify your request?**\n\n"
        f"{clarifying_q}\n\n"
        f"*(You can also ask about NexaTech leave policies, travel allowances, laptop upgrades, or file a Jira ticket!)*"
    )
    return {"answer": answer}


def jira_confirm_node(state: AgentState) -> Dict[str, Any]:
    """Requests explicit user confirmation before creating any Jira ticket."""
    summary = state.get("ticket_summary") or state.get("question", "Untitled Issue")
    issue_type = state.get("ticket_type") or "Bug"
    priority = state.get("ticket_priority") or "High"
    project = "NEXA"

    pending_ticket = {
        "summary": summary,
        "issue_type": issue_type,
        "priority": priority,
        "project": project
    }

    answer = (
        f"⚠️ **Confirmation Required Before Creating Ticket**\n\n"
        f"I have prepared the following Jira ticket for NexaTech Solutions:\n\n"
        f"• **Project:** `{project}`\n"
        f"• **Summary:** {summary}\n"
        f"• **Issue Type:** {issue_type}\n"
        f"• **Priority:** {priority}\n\n"
        f"👉 Please reply with **'confirm'** (or **'yes'**) to create this ticket, or **'cancel'** to abort."
    )

    return {
        "answer": answer,
        "pending_ticket": pending_ticket
    }


def jira_execute_node(state: AgentState) -> Dict[str, Any]:
    """Executes ticket creation via Jira REST API after user confirmation."""
    pending = state.get("pending_ticket", {})
    summary = pending.get("summary", "New Ticket")
    issue_type = pending.get("issue_type", "Bug")
    priority = pending.get("priority", "High")
    project = pending.get("project", "NEXA")

    result = create_jira_ticket(
        summary=summary,
        issue_type=issue_type,
        priority=priority,
        project=project
    )

    if result.get("status") == "success":
        key = result.get("key", "NEXA-001")
        url = result.get("url", f"https://nexatech.atlassian.net/browse/{key}")
        mode_note = " *(Mock Mode: Credentials not configured)*" if result.get("mode") == "mock" else ""
        answer = (
            f"✅ **Jira Ticket Created Successfully!**{mode_note}\n\n"
            f"• **Ticket Key:** `{key}`\n"
            f"• **Summary:** {summary}\n"
            f"• **Issue Type:** {issue_type}\n"
            f"• **Priority:** {priority}\n"
            f"• **Status:** Open\n"
            f"• **Link:** {url}"
        )
    else:
        answer = (
            f"❌ **Failed to Create Jira Ticket**\n\n"
            f"Error details: {result.get('error_message') or result.get('status_code')}"
        )

    # Clear pending ticket from state
    return {"answer": answer, "pending_ticket": None}


def jira_cancel_node(state: AgentState) -> Dict[str, Any]:
    """Cancels the pending Jira ticket creation."""
    return {
        "answer": "🚫 **Ticket Creation Cancelled.** No Jira ticket was created.",
        "pending_ticket": None
    }


def jira_check_node(state: AgentState) -> Dict[str, Any]:
    """Fetches details of an existing Jira ticket via Jira REST API."""
    key = state.get("ticket_key")
    if not key:
        return {"answer": "Could not identify a ticket key (e.g. `NEXA-101`). Please specify the ticket key to check."}

    result = get_jira_ticket(key)

    if result.get("status") == "success":
        mode_note = " *(Mock Mode)*" if result.get("mode") == "mock" else ""
        answer = (
            f"📋 **Jira Ticket Details: {result.get('key')}**{mode_note}\n\n"
            f"• **Summary:** {result.get('summary')}\n"
            f"• **Status:** `{result.get('status_name')}`\n"
            f"• **Priority:** {result.get('priority')}\n"
            f"• **Issue Type:** {result.get('issue_type')}\n"
            f"• **Assignee:** {result.get('assignee')}\n"
            f"• **Link:** {result.get('url')}"
        )
    elif result.get("status") == "not_found":
        answer = f"🔍 **Ticket Not Found**: `{key}` does not exist in NexaTech's Jira instance."
    else:
        answer = f"❌ **Error retrieving ticket {key}**: {result.get('message')}"

    return {"answer": answer}


def jira_update_node(state: AgentState) -> Dict[str, Any]:
    """Adds a comment or note to an existing Jira ticket via Jira REST API."""
    key = state.get("ticket_key")
    comment = state.get("ticket_comment") or "Updated via NexaTech Drona Slack bot."

    if not key:
        return {"answer": "Could not identify which ticket to update. Please provide a ticket key like `NEXA-101`."}

    result = update_jira_ticket(key, comment)

    if result.get("status") == "success":
        mode_note = " *(Mock Mode)*" if result.get("mode") == "mock" else ""
        answer = (
            f"💬 **Jira Ticket Updated: {key}**{mode_note}\n\n"
            f"• **Comment added:** \"{comment}\"\n"
            f"• **Link:** {result.get('url')}"
        )
    else:
        answer = f"❌ **Failed to update ticket {key}**: {result.get('message')}"

    return {"answer": answer}


def rag_retrieve_node(state: AgentState) -> Dict[str, Any]:
    """Retrieves top relevant chunks from NexaTech knowledge base using hybrid search + reranking."""
    question = state.get("question", "")
    docs = search_knowledge_base(question, limit=5)
    return {"documents": docs}


def rag_generate_node(state: AgentState) -> Dict[str, Any]:
    """Generates grounded answer strictly using retrieved NexaTech documents and cites sources."""
    question = state.get("question", "")
    docs = state.get("documents", [])

    if not docs:
        return {"answer": "I searched our enterprise knowledge base, but could not find relevant documentation on this topic."}

    # Format context with source metadata
    context_text = ""
    sources_cited = []
    for d in docs:
        src = d.get("source", "Unknown Document")
        cat = d.get("category", "General")
        cid = d.get("chunk_id", "")
        context_text += f"\n--- Document: {src} | Category: {cat} | Chunk: {cid} ---\n{d.get('text', '')}\n"
        if src not in sources_cited:
            sources_cited.append(src)

    system_prompt = """You are 'Drona', the official enterprise AI Workplace Assistant for NexaTech Solutions.
Answer the user's question accurately, professionally, and directly using ONLY the provided documentation context.

Strict Guidelines:
1. Ground your answer completely in the provided context. If the answer is not contained in the documents, state:
   "I don't have enough information on that in our company records."
2. Never hallucinate facts, numbers, dates, approval hierarchies, or monetary limits.
3. Keep the tone professional, helpful, and concise. Use bullet points or markdown tables when explaining limits, approval workflows, or step-by-step procedures.
4. At the end of your response, ALWAYS include a '📚 **Sources Cited:**' section listing the exact document filenames from which you drew the information."""

    user_prompt = f"""Context from NexaTech Knowledge Base:
{context_text}

User Question: {question}"""

    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ])

    return {"answer": response.content.strip()}


# ----------------------------------------------------
# 5. Build and Compile the LangGraph Workflow
# ----------------------------------------------------

workflow = StateGraph(AgentState)

# Add all nodes
workflow.add_node("router", router_node)
workflow.add_node("direct_chat", direct_chat_node)
workflow.add_node("clarify", clarify_node)
workflow.add_node("jira_confirm", jira_confirm_node)
workflow.add_node("jira_execute", jira_execute_node)
workflow.add_node("jira_cancel", jira_cancel_node)
workflow.add_node("jira_check", jira_check_node)
workflow.add_node("jira_update", jira_update_node)
workflow.add_node("rag_retrieve", rag_retrieve_node)
workflow.add_node("rag_generate", rag_generate_node)

# Entry point is always the router
workflow.set_entry_point("router")


def route_decision(state: AgentState) -> str:
    """Conditional routing based on classified intent."""
    intent = state.get("intent", "RAG")
    mapping = {
        "DIRECT_CHAT": "direct_chat",
        "AMBIGUOUS": "clarify",
        "JIRA_PROPOSE": "jira_confirm",
        "JIRA_EXECUTE": "jira_execute",
        "JIRA_CANCEL": "jira_cancel",
        "JIRA_CHECK": "jira_check",
        "JIRA_UPDATE": "jira_update",
        "RAG": "rag_retrieve",
    }
    return mapping.get(intent, "rag_retrieve")


workflow.add_conditional_edges("router", route_decision, {
    "direct_chat": "direct_chat",
    "clarify": "clarify",
    "jira_confirm": "jira_confirm",
    "jira_execute": "jira_execute",
    "jira_cancel": "jira_cancel",
    "jira_check": "jira_check",
    "jira_update": "jira_update",
    "rag_retrieve": "rag_retrieve",
})

# Terminal edges
workflow.add_edge("direct_chat", END)
workflow.add_edge("clarify", END)
workflow.add_edge("jira_confirm", END)
workflow.add_edge("jira_execute", END)
workflow.add_edge("jira_cancel", END)
workflow.add_edge("jira_check", END)
workflow.add_edge("jira_update", END)
workflow.add_edge("rag_retrieve", "rag_generate")
workflow.add_edge("rag_generate", END)

# Persistent in-memory checkpointer for conversational thread memory
memory = MemorySaver()
agent_app = workflow.compile(checkpointer=memory)


# ----------------------------------------------------
# 6. Public Helper Function for Slack & Evaluator
# ----------------------------------------------------

def ask_agent(question: str, thread_id: str = "default_thread") -> Dict[str, Any]:
    """Runs LangGraph agent pipeline, manages thread memory, and captures Langfuse tracing."""
    callbacks = []
    trace_id = ""

    if CallbackHandler is not None and os.getenv("LANGFUSE_PUBLIC_KEY"):
        try:
            handler = CallbackHandler()
            callbacks.append(handler)
        except Exception as e:
            print(f"[Langfuse Warning]: {e}")

    config = {
        "configurable": {"thread_id": thread_id},
        "callbacks": callbacks,
        "metadata": {
            "session_id": thread_id,
            "user_id": "slack_user",
        }
    }

    initial_state = {"question": question}
    final_output = agent_app.invoke(initial_state, config=config)

    if callbacks and hasattr(callbacks[0], "last_trace_id"):
        trace_id = callbacks[0].last_trace_id or ""

    return {
        "answer": final_output.get("answer", ""),
        "intent": final_output.get("intent", ""),
        "trace_id": trace_id
    }


# ----------------------------------------------------
# 7. Verification Tests
# ----------------------------------------------------

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("Testing NexaTech Drona Phase 3 Agentic Routing")
    print("=" * 70)

    # 1. Direct Chat
    print("\n[TEST 1: Direct Chat]")
    res1 = ask_agent("Hello! Good morning!", thread_id="t_chat")
    print("Answer:\n", res1["answer"])

    # 2. Ambiguous query
    print("\n[TEST 2: Ambiguous Query]")
    res2 = ask_agent("leave", thread_id="t_ambig")
    print("Answer:\n", res2["answer"])

    # 3. RAG Knowledge Question
    print("\n[TEST 3: RAG Knowledge Question]")
    res3 = ask_agent("How many days of paid maternity leave are female employees entitled to?", thread_id="t_rag")
    print("Answer:\n", res3["answer"])

    # 4. Jira Ticket Flow with Confirmation
    print("\n[TEST 4: Jira Creation - Step 1: Request Creation]")
    res4a = ask_agent("Create a Jira ticket: Database connection pool exhausted on replica 2", thread_id="t_jira_flow")
    print("Answer:\n", res4a["answer"])

    print("\n[TEST 4: Jira Creation - Step 2: Confirm in same thread]")
    res4b = ask_agent("confirm", thread_id="t_jira_flow")
    print("Answer:\n", res4b["answer"])

    # 5. Jira Check
    print("\n[TEST 5: Jira Status Check]")
    res5 = ask_agent("Check status of ticket NEXA-101", thread_id="t_check")
    print("Answer:\n", res5["answer"])

    # 6. Jira Update
    print("\n[TEST 6: Jira Update]")
    res6 = ask_agent("Update ticket NEXA-101 with comment: SRE team on-call investigating", thread_id="t_update")
    print("Answer:\n", res6["answer"])

    print("\n" + "=" * 70)
    print("All Phase 3 Routing Tests Completed!")
    print("=" * 70)