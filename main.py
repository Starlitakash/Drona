import os
import sys
import argparse
from pathlib import Path
from dotenv import load_dotenv

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))

load_dotenv(PROJECT_ROOT / ".env")


BANNER = """
========================================================================
     DRONA - Enterprise Agentic Slack Assistant
     NexaTech Solutions Knowledge, IT & Jira Operations Platform
========================================================================
"""


def start_slack_bot():
    """Starts Drona in Slack Socket Mode."""
    print(BANNER, flush=True)
    print("[Mode: Slack Socket Mode]", flush=True)
    
    bot_token = os.getenv("SLACK_BOT_TOKEN")
    app_token = os.getenv("SLACK_APP_TOKEN")
    
    if not bot_token or not app_token:
        print("❌ Error: Missing SLACK_BOT_TOKEN or SLACK_APP_TOKEN in .env.", flush=True)
        print("Tip: Run in terminal test mode using: venv\\Scripts\\python main.py --cli", flush=True)
        sys.exit(1)

    print("[Drona] Initializing models, vector search, and Slack Socket Mode...", flush=True)
    from slack_bolt.adapter.socket_mode import SocketModeHandler
    from src.slack_app import app

    print("[Slack] Connecting to Slack via Socket Mode...", flush=True)
    print("⚡ Drona is online and listening! Mention @Drona in your Slack channels.", flush=True)
    print("Press Ctrl+C to stop the bot.\n", flush=True)
    handler = SocketModeHandler(app, app_token)
    handler.start()


def start_cli_session():
    """Starts an interactive terminal chat session with Drona."""
    print(BANNER)
    print("[Mode: Interactive CLI Session]")
    print("Type your message and press Enter. Type 'exit' or 'quit' to end.\n")

    from src.agent import ask_agent

    thread_id = "cli_interactive_session"
    while True:
        try:
            user_input = input("\nYou: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "q"]:
                print("\nGoodbye! Have a productive day at NexaTech.")
                break

            result = ask_agent(user_input, thread_id=thread_id)
            print(f"\nDrona:\n{result['answer']}")

        except (KeyboardInterrupt, EOFError):
            print("\nExiting interactive session.")
            break


def run_ingest():
    """Runs ingestion of markdown policy documents into Qdrant Cloud."""
    print(BANNER)
    print("[Mode: Knowledge Corpus Ingestion]")
    from src.retriever import ingest_all_documents
    docs_path = PROJECT_ROOT / "docs"
    result = ingest_all_documents(docs_dir=str(docs_path), recreate=False)
    print("\n[Ingestion Complete]:", result)


def run_evals():
    """Runs the Golden Dataset Evaluation Harness."""
    print(BANNER)
    print("[Mode: Evaluation Harness]")
    from evals.eval_harness import run_evaluation
    run_evaluation()


def run_pytest():
    """Runs the pytest test suite."""
    print(BANNER)
    print("[Mode: Pytest Evaluation Suite]")
    import subprocess
    cmd = [sys.executable, "-m", "pytest", "evals/test_eval.py", "-v", "-s"]
    subprocess.run(cmd, cwd=str(PROJECT_ROOT))


def main():
    parser = argparse.ArgumentParser(
        description="Drona: Enterprise Agentic Slack RAG Assistant for NexaTech Solutions",
        formatter_class=argparse.RawTextHelpFormatter
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--slack", action="store_true", help="Start the Slack Socket Mode bot (Default)")
    group.add_argument("--cli", "-c", action="store_true", help="Start an interactive terminal chat session")
    group.add_argument("--ingest", "-i", action="store_true", help="Ingest policy documents from /docs into Qdrant Cloud")
    group.add_argument("--eval", "-e", action="store_true", help="Run the 40-question Golden Dataset evaluation harness")
    group.add_argument("--test", "-t", action="store_true", help="Run the automated pytest test suite")

    args = parser.parse_args()

    if args.cli:
        start_cli_session()
    elif args.ingest:
        run_ingest()
    elif args.eval:
        run_evals()
    elif args.test:
        run_pytest()
    else:
        # Default behavior: run Slack bot
        start_slack_bot()


if __name__ == "__main__":
    main()
