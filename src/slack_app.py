import os
import sys
import re

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from langfuse import Langfuse

from src.agent import ask_agent
from src.memory import is_known_thread

load_dotenv()

# Initialize Slack Bolt App & Langfuse client
app = App(token=os.getenv("SLACK_BOT_TOKEN"))
langfuse = Langfuse()


def build_feedback_blocks(answer_text: str, trace_id: str):
    """Builds Slack Block Kit message with trace_id embedded inside the buttons."""
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": answer_text
            }
        },
        {"type": "divider"},
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "👍 Helpful", "emoji": True},
                    "style": "primary",
                    "action_id": "feedback_helpful",
                    "value": trace_id  # Pass the trace_id into the button payload
                },
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "👎 Not Helpful", "emoji": True},
                    "style": "danger",
                    "action_id": "feedback_unhelpful",
                    "value": trace_id  # Pass the trace_id into the button payload
                }
            ]
        }
    ]


import time


def format_slack_mrkdwn(text: str) -> str:
    """Converts standard Markdown **bold** to Slack mrkdwn *bold* and cleans up asterisk clutter."""
    # Convert **bold** to *bold* for clean native Slack rendering
    cleaned = re.sub(r"\*\*(.*?)\*\*", r"*\1*", text)
    # Remove any stray triple/quad asterisks
    cleaned = re.sub(r"\*{3,}", "*", cleaned)
    # Clean up empty bold spaces
    cleaned = re.sub(r"\*\s+\*", "", cleaned)
    return cleaned.strip()


def execute_agent_with_streaming(client, channel_id: str, thread_ts: str, prompt: str, conversation_id: str, metadata: dict):
    """
    Posts an initial placeholder message in the Slack thread and periodically streams
    the LLM generation tokens to Slack via chat_update, keeping responses fast and interactive.
    """
    # 1. Post initial 'thinking' message
    init_res = client.chat_postMessage(
        channel=channel_id,
        thread_ts=thread_ts,
        text="*Drona is thinking...* ✍️"
    )
    msg_ts = init_res["ts"]

    streamed_text = {"content": ""}
    last_update = {"time": time.time(), "len": 0}

    def on_llm_chunk(chunk: str):
        streamed_text["content"] += chunk
        now = time.time()
        # Throttled update to avoid hitting Slack's 1 req/sec rate limit
        # Updates if 0.8 seconds passed and at least 25 new characters are buffered
        if (now - last_update["time"] >= 0.8) and (len(streamed_text["content"]) - last_update["len"] >= 25):
            current_draft = format_slack_mrkdwn(streamed_text["content"]) + "\n\n_...typing..._"
            try:
                client.chat_update(
                    channel=channel_id,
                    ts=msg_ts,
                    text=current_draft
                )
                last_update["time"] = now
                last_update["len"] = len(streamed_text["content"])
            except Exception:
                pass

    # 2. Invoke the agent with on_chunk callback
    result = ask_agent(prompt, thread_id=conversation_id, metadata=metadata, on_chunk=on_llm_chunk)
    final_answer = result.get("answer") or streamed_text["content"] or "No response generated."
    final_answer = format_slack_mrkdwn(final_answer)
    trace_id = result.get("trace_id", "")

    # 3. Final update with the complete structured markdown and interactive feedback buttons
    try:
        client.chat_update(
            channel=channel_id,
            ts=msg_ts,
            blocks=build_feedback_blocks(final_answer, trace_id),
            text=final_answer
        )
    except Exception as e:
        print(f"[Slack Update Error]: {e}")


@app.event("app_mention")
def handle_app_mention(event, say, client):
    """Handles messages where @Drona is explicitly mentioned."""
    channel_id = event["channel"]
    thread_ts = event.get("thread_ts") or event["ts"]
    is_dm = channel_id.startswith("D") or event.get("channel_type") == "im"
    conversation_id = f"dm_{channel_id}" if is_dm else thread_ts

    # Clean the prompt
    raw_text = event.get("text", "")
    clean_question = re.sub(r"<@.*?>", "", raw_text).strip()

    if not clean_question:
        say("How can I help you today?", thread_ts=thread_ts)
        return

    # Add thinking reaction 👀
    try:
        client.reactions_add(channel=channel_id, name="eyes", timestamp=event["ts"])
    except Exception:
        pass

    metadata = {
        "user_id": event.get("user"),
        "channel_id": channel_id,
        "team_id": event.get("team")
    }

    # Stream agent generation in the Slack thread
    execute_agent_with_streaming(
        client=client,
        channel_id=channel_id,
        thread_ts=thread_ts,
        prompt=clean_question,
        conversation_id=conversation_id,
        metadata=metadata
    )


@app.event("message")
def handle_thread_reply(event, say, client):
    """
    Enables natural back-and-forth conversation inside an active thread or DM.
    Users do NOT need to re-type @Drona on follow-up questions in the same thread.
    """
    # 1. Ignore bot messages (including Drona's own replies) to prevent infinite loops
    if event.get("bot_id") or event.get("subtype") in ["bot_message", "message_changed"]:
        return

    raw_text = event.get("text", "").strip()
    if not raw_text:
        return

    # 2. If the user explicitly typed an @mention, handle_app_mention handles it
    if re.search(r"<@.*?>", raw_text):
        return

    channel_id = event.get("channel", "")
    thread_ts = event.get("thread_ts")
    is_dm = channel_id.startswith("D") or event.get("channel_type") == "im"

    # 3. Only respond if this message is inside a thread OR a 1-on-1 Direct Message
    if not thread_ts and not is_dm:
        return

    effective_thread_ts = thread_ts or event["ts"]
    conversation_id = f"dm_{channel_id}" if is_dm else effective_thread_ts

    # 4. Check if Drona has participated in this thread before (or if it's a DM)
    is_active = is_dm or is_known_thread(effective_thread_ts)
    if not is_active and thread_ts:
        # Check Slack thread history directly to see if Drona previously replied
        try:
            replies = client.conversations_replies(channel=channel_id, ts=thread_ts, limit=5)
            for msg in replies.get("messages", []):
                if msg.get("bot_id"):
                    is_active = True
                    break
        except Exception:
            pass

    if is_active:
        try:
            client.reactions_add(channel=channel_id, name="eyes", timestamp=event["ts"])
        except Exception:
            pass

        metadata = {
            "user_id": event.get("user"),
            "channel_id": channel_id,
            "team_id": event.get("team")
        }

        # Stream agent generation in the Slack thread
        execute_agent_with_streaming(
            client=client,
            channel_id=channel_id,
            thread_ts=effective_thread_ts,
            prompt=raw_text,
            conversation_id=conversation_id,
            metadata=metadata
        )


# When user clicks 👍 Helpful
@app.action("feedback_helpful")
def handle_helpful(ack, body, say):
    ack()
    trace_id = body["actions"][0]["value"]
    thread_ts = body["container"]["thread_ts"]

    # Send positive score to Langfuse dashboard!
    if trace_id:
        try:
            langfuse.create_score(
                trace_id=trace_id,
                name="user_feedback",
                value=1.0,
                comment="User marked helpful in Slack"
            )
            print(f"[Langfuse] Logged +1.0 score for trace {trace_id}")
        except Exception as e:
            print(f"[Langfuse Error] Could not log score: {e}")

    say(text="Thank you for your feedback! ⭐", thread_ts=thread_ts)


# When user clicks 👎 Not Helpful
@app.action("feedback_unhelpful")
def handle_unhelpful(ack, body, say):
    ack()
    trace_id = body["actions"][0]["value"]
    thread_ts = body["container"]["thread_ts"]

    # Send negative score to Langfuse dashboard!
    if trace_id:
        try:
            langfuse.create_score(
                trace_id=trace_id,
                name="user_feedback",
                value=0.0,
                comment="User marked unhelpful in Slack"
            )
            print(f"[Langfuse] Logged 0.0 score for trace {trace_id}")
        except Exception as e:
            print(f"[Langfuse Error] Could not log score: {e}")

    say(text="Thanks for letting us know. We'll improve our documentation! 🛠️", thread_ts=thread_ts)


if __name__ == "__main__":
    app_token = os.getenv("SLACK_APP_TOKEN")
    print("Connecting to Slack with Langfuse Observability...")
    handler = SocketModeHandler(app, app_token)
    handler.start()