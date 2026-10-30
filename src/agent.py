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
from src.memory import save_message, format_history_for_llm, get_chat_history
from src.semantic_cache import semantic_cache

load_dotenv()

# 1. Initialize Groq LLM
GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")
llm = ChatGroq(
    model=GROQ_MODEL,
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.1,
)


# 2. Define the Agent's State & Guardrail Configuration
RERANK_THRESHOLD = float(os.getenv("RERANK_THRESHOLD", "-2.5"))


from contextvars import ContextVar

# Thread-safe context var for streaming callback
_STREAM_CALLBACK: ContextVar[Optional[Any]] = ContextVar("_STREAM_CALLBACK", default=None)


class AgentState(TypedDict, total=False):
    question: str
    thread_id: Optional[str]
    chat_history: Optional[str]
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
    guardrail_triggered: Optional[bool]
    cache_hit: Optional[bool]
    cache_matched_query: Optional[str]


def extract_section_header(chunk_text: str, default: str = "General Provisions") -> str:
    """Extracts the most descriptive Markdown section header from chunk text."""
    headers = re.findall(r"(?:^|\n)(#{1,4}\s+[^\n]+)", chunk_text)
    if headers:
        # Prefer level 2 or 3 headers (## or ###)
        sub_headers = [h for h in headers if h.startswith("##")]
        chosen = sub_headers[0] if sub_headers else headers[0]
        return re.sub(r"^#+\s*", "", chosen).strip()

    first_line = chunk_text.strip().split("\n")[0].strip("#* \t\r")
    if 5 <= len(first_line) <= 60 and not first_line.endswith("."):
        return first_line

    return default


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

    # C. LLM Classification & Entity Extraction (with thread memory context)
    history = state.get("chat_history", "").strip()
    router_user_prompt = (
        f"Recent Conversation History in this thread:\n{history}\n\nCurrent User Message: {question}"
        if history else question
    )

    try:
        response = llm.invoke([
            SystemMessage(content=ROUTER_SYSTEM_PROMPT),
            HumanMessage(content=router_user_prompt)
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
    """Generates a warm, professional, and context-aware conversational response as Drona."""
    question = state.get("question", "")
    history_text = state.get("chat_history", "").strip()
    history_block = f"Recent Conversation History:\n{history_text}\n\n" if history_text else ""
    on_chunk = _STREAM_CALLBACK.get()

    prompt = f"""You are 'Drona', the friendly and professional AI Workplace Assistant.
{history_block}Current User Message: "{question}"

Instructions:
1. If the user is telling you their name, role, or personal details, acknowledge it warmly and remember it for this conversation!
2. If the user asks about something mentioned earlier in the conversation (such as "What is my name?", "Who am I?", or a follow-up), check the Recent Conversation History above and answer accurately!
3. If this is a general greeting or casual chat, give a polite, warm response (2-3 sentences max) and let them know you're ready to help with company policies, procedures, or Jira tickets.
4. Structure any list items cleanly with bullets or numbers."""

    messages = [
        SystemMessage(content="You are Drona, an intelligent enterprise assistant with conversational memory."),
        HumanMessage(content=prompt)
    ]

    if callable(on_chunk):
        full_text = ""
        for chunk in llm.stream(messages):
            token = chunk.content or ""
            full_text += token
            on_chunk(token)
        return {"answer": full_text.strip()}

    response = llm.invoke(messages)
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
    """Checks semantic cache first, then retrieves top relevant chunks if cache miss."""
    question = state.get("question", "")

    # 1. Check Semantic Cache (Cosine similarity match for repeated / paraphrased questions)
    cached = semantic_cache.get(question)
    if cached:
        cached_answer = cached["answer"]
        on_chunk = _STREAM_CALLBACK.get()
        if callable(on_chunk):
            on_chunk(cached_answer)
        return {
            "answer": cached_answer,
            "documents": [],
            "guardrail_triggered": False,
            "cache_hit": True,
            "cache_matched_query": cached.get("matched_query")
        }

    # 2. Cache Miss: Execute Hybrid Retrieval (Dense Vector + BM25)
    docs = search_knowledge_base(question, limit=5)

    # Attach section header to each retrieved doc
    for d in docs:
        d["section_header"] = extract_section_header(d.get("text", ""))

    # Check rerank score threshold (Anti-Hallucination Guardrail)
    top_score = docs[0].get("rerank_score", -99.0) if docs else -99.0
    if not docs or top_score < RERANK_THRESHOLD:
        print(f"[Guardrail Check] Top score {top_score:+.4f} < threshold {RERANK_THRESHOLD}. Triggering anti-hallucination guardrail.")
        return {
            "documents": [],
            "guardrail_triggered": True,
            "cache_hit": False
        }

    # Dynamic Context Pruning based on Cross-Encoder Reranker Confidence:
    # If the top chunk has high confidence (rerank_score >= 1.5), pass only top 2 chunks
    # instead of 5 to cut prompt tokens by >60% and improve generation speed.
    if len(docs) > 2 and top_score >= 1.5:
        print(f"[Dynamic Pruning] Top score {top_score:+.2f} >= 1.5 (High Confidence). Pruned context from {len(docs)} chunks down to 2 chunks to save tokens.")
        docs = docs[:2]

    return {
        "documents": docs,
        "guardrail_triggered": False,
        "cache_hit": False
    }


def rag_generate_node(state: AgentState) -> Dict[str, Any]:
    """Generates grounded answer strictly citing source documents and section headers."""
    # Fast exit on semantic cache hit
    if state.get("cache_hit"):
        return {"answer": state.get("answer", "")}

    if state.get("guardrail_triggered"):
        return {"answer": "I don't have enough information on that in our company records."}

    question = state.get("question", "")
    docs = state.get("documents", [])

    if not docs:
        return {"answer": "I don't have enough information on that in our company records."}

    # Format context with source metadata and section headers
    context_text = ""
    citations_dict: Dict[str, List[str]] = {}
    for d in docs:
        src = d.get("source", "Unknown Document")
        sec = d.get("section_header", "General Provisions")
        cat = d.get("category", "General")
        cid = d.get("chunk_id", "")
        context_text += f"\n--- Document: {src} | Section: {sec} | Category: {cat} | Chunk: {cid} ---\n{d.get('text', '')}\n"
        if src not in citations_dict:
            citations_dict[src] = []
        if sec not in citations_dict[src]:
            citations_dict[src].append(sec)

    system_prompt = """You are 'Drona', the official enterprise AI Workplace Assistant for NexaTech Solutions.
Answer the user's question accurately, professionally, and directly using ONLY the provided documentation context.

Response Structure & Styling Rules:
1. Grounding: Rely strictly on the provided context. If the answer is not explicitly found in the context, state:
   "I don't have enough information on that in our company records."
2. Formatting Layout (Clean, Professional, ZERO ASTERISKS):
   • Title / Heading: Start with a clear plain-text title on line 1 (e.g. Americans with Disabilities Act (ADA) Overview).
   • Overview Paragraph: Follow with a clear, readable 1-2 sentence paragraph answering the core question in plain English.
   • Key Points / Details: Add a clean section with bullet points (•) or numbered steps (1., 2., 3.) covering important requirements, conditions, and exceptions. Use clean prefixes (e.g. "• Scope: ...", "• Definition: ...").
   • ZERO ASTERISKS: Do NOT use any asterisks (*) or stars anywhere in your response. No **bold** and no *italics*. Keep the text completely clean without any star characters.
3. Citations: At the end, always include a clean source section:
   📚 Sources Cited:
   - Document-Name.pdf (Section: Section Name)"""

    history_text = state.get("chat_history", "").strip()
    history_block = f"Recent Thread Conversation History:\n{history_text}\n\n" if history_text else ""
    on_chunk = _STREAM_CALLBACK.get()

    user_prompt = f"""{history_block}Context from Knowledge Base:
{context_text}

User Question: {question}"""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]

    if callable(on_chunk):
        full_text = ""
        for chunk in llm.stream(messages):
            token = chunk.content or ""
            # Strip asterisks in real-time
            token = token.replace("*", "")
            full_text += token
            on_chunk(token)
        answer = full_text.strip()
    else:
        response = llm.invoke(messages)
        answer = response.content.strip().replace("*", "")

    # Ensure standardized section header citations if LLM truncated them
    if "📚" not in answer and "Sources Cited" not in answer:
        citations_lines = []
        for src, secs in citations_dict.items():
            sec_formatted = ", ".join(secs)
            citations_lines.append(f"- {src} (Section: {sec_formatted})")
        citations_suffix = "\n\n📚 Sources Cited:\n" + "\n".join(citations_lines)
        if callable(on_chunk):
            on_chunk(citations_suffix)
        answer += citations_suffix
    else:
        answer = answer.replace("*", "")

    # Cache valid enterprise answers in the Semantic Cache
    if not state.get("guardrail_triggered") and "I don't have enough information" not in answer:
        semantic_cache.set(question, answer, intent="RAG")

    return {"answer": answer}


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

def ask_agent(
    question: str,
    thread_id: str = "default_thread",
    metadata: Optional[Dict[str, Any]] = None,
    on_chunk: Optional[Any] = None
) -> Dict[str, Any]:
    """Runs LangGraph agent pipeline, manages thread memory, and captures Langfuse tracing."""
    callbacks = []
    trace_id = ""

    if CallbackHandler is not None and os.getenv("LANGFUSE_PUBLIC_KEY"):
        try:
            handler = CallbackHandler()
            callbacks.append(handler)
        except Exception as e:
            print(f"[Langfuse Warning]: {e}")

    # 1. Retrieve recent thread dialogue turns for conversational context
    history_text = format_history_for_llm(thread_id, max_turns=4)

    # 2. Persist the incoming user message to memory (MongoDB / cache)
    save_message(
        thread_id=thread_id,
        role="user",
        content=question,
        metadata=metadata or {"channel": "slack"}
    )

    # Fast Pre-Execution Semantic Cache Check (Bypasses Router, Retriever, and LLM)
    q_lower = question.lower().strip()
    is_special_action = (
        any(w in q_lower for w in ["confirm", "cancel", "jira", "create ticket", "update ticket"])
        or len(q_lower.split()) < 3
    )

    if not is_special_action:
        cached = semantic_cache.get(question)
        if cached:
            cached_answer = cached["answer"]
            if callable(on_chunk):
                on_chunk(cached_answer)
            save_message(
                thread_id=thread_id,
                role="assistant",
                content=cached_answer,
                metadata={"intent": "RAG", "cache_hit": True, "trace_id": ""}
            )
            return {
                "answer": cached_answer,
                "intent": "RAG",
                "trace_id": "",
                "cache_hit": True
            }

    config = {
        "configurable": {"thread_id": thread_id},
        "callbacks": callbacks,
        "metadata": {
            "session_id": thread_id,
            "user_id": (metadata or {}).get("user_id", "slack_user"),
        }
    }

    token = _STREAM_CALLBACK.set(on_chunk)
    try:
        initial_state = {
            "question": question,
            "thread_id": thread_id,
            "chat_history": history_text
        }
        final_output = agent_app.invoke(initial_state, config=config)
    finally:
        _STREAM_CALLBACK.reset(token)
    answer = final_output.get("answer", "")
    intent = final_output.get("intent", "")
    cache_hit = final_output.get("cache_hit", False)

    if callbacks and hasattr(callbacks[0], "last_trace_id"):
        trace_id = callbacks[0].last_trace_id or ""

    # 3. Persist the generated assistant reply to memory
    save_message(
        thread_id=thread_id,
        role="assistant",
        content=answer,
        metadata={"intent": intent, "trace_id": trace_id, "cache_hit": cache_hit}
    )

    return {
        "answer": answer,
        "intent": intent,
        "trace_id": trace_id,
        "cache_hit": cache_hit
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