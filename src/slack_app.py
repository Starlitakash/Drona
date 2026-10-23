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


@app.event("app_mention")
def handle_app_mention(event, say, client):
    channel_id = event["channel"]
    thread_ts = event.get("thread_ts") or event["ts"]

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

    # Call LangGraph Agent (returns answer + Langfuse trace_id)
    result = ask_agent(clean_question, thread_id=thread_ts)
    answer = result["answer"]
    trace_id = result.get("trace_id", "")

    # Reply in Slack with the buttons attached to this specific trace
    say(
        blocks=build_feedback_blocks(answer, trace_id),
        text=answer,
        thread_ts=thread_ts
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