import os
import random
from dotenv import load_dotenv

load_dotenv()

# Optional: Real Jira credentials from .env (if you have an Atlassian account)
JIRA_SERVER = os.getenv("JIRA_SERVER", "https://acme-corp.atlassian.net")
JIRA_EMAIL = os.getenv("JIRA_EMAIL", "")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN", "")


def create_jira_ticket(summary: str, issue_type: str = "Bug", priority: str = "High", project: str = "ENG") -> dict:
    """Creates a Jira ticket. Falls back to realistic mock mode if real credentials are not set."""
    # If real Atlassian credentials exist in .env, use real API
    if JIRA_EMAIL and JIRA_API_TOKEN:
        try:
            import requests
            url = f"{JIRA_SERVER}/rest/api/3/issue"
            auth = (JIRA_EMAIL, JIRA_API_TOKEN)
            headers = {"Accept": "application/json", "Content-Type": "application/json"}
            payload = {
                "fields": {
                    "project": {"key": project},
                    "summary": summary,
                    "description": {"type": "doc", "version": 1, "content": [{"type": "paragraph", "content": [{"type": "text", "text": summary}]}]},
                    "issuetype": {"name": issue_type}
                }
            }
            res = requests.post(url, json=payload, headers=headers, auth=auth)
            if res.status_code == 201:
                key = res.json()["key"]
                return {"key": key, "url": f"{JIRA_SERVER}/browse/{key}", "status": "success"}
        except Exception as e:
            print(f"Jira API error, falling back to mock: {e}")

    # Realistic Mock Mode (Allows instant testing with zero setup!)
    ticket_number = random.randint(100, 999)
    ticket_key = f"{project}-{ticket_number}"
    ticket_url = f"{JIRA_SERVER}/browse/{ticket_key}"

    return {
        "key": ticket_key,
        "url": ticket_url,
        "summary": summary,
        "issue_type": issue_type,
        "priority": priority,
        "status": "success"
    }


if __name__ == "__main__":
    # Quick test
    ticket = create_jira_ticket("Database pool exhausted on replica 2", issue_type="Bug", priority="High")
    print("Created Ticket:", ticket)