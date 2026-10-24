import os
import random
import requests
from urllib.parse import urlparse
from typing import Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()

# Real Jira credentials from .env (if configured)
raw_server = os.getenv("JIRA_SERVER", "https://nexatech.atlassian.net").strip()
p = urlparse(raw_server)
JIRA_SERVER = f"{p.scheme}://{p.netloc}" if (p.scheme and p.netloc) else raw_server.rstrip("/")
JIRA_EMAIL = os.getenv("JIRA_EMAIL", "").strip()
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN", "").strip()
JIRA_PROJECT = os.getenv("JIRA_PROJECT", "KAN").strip()


def is_jira_configured() -> bool:
    """Checks whether valid Jira credentials are set in environment."""
    return bool(JIRA_EMAIL and JIRA_API_TOKEN and "atlassian.net" in JIRA_SERVER)


def create_jira_ticket(
    summary: str,
    issue_type: str = "Bug",
    priority: str = "High",
    project: str = "KAN",
    description: Optional[str] = None
) -> Dict[str, Any]:
    """
    Creates a Jira ticket via Jira REST API (v3).
    Includes automatic URL sanitization, issue type fallback, and mock fallback.
    """
    desc_text = description or summary
    target_project = JIRA_PROJECT if project in ["NEXA", ""] else project

    if is_jira_configured():
        try:
            url = f"{JIRA_SERVER}/rest/api/3/issue"
            auth = (JIRA_EMAIL, JIRA_API_TOKEN)
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
            
            payload = {
                "fields": {
                    "project": {"key": target_project},
                    "summary": summary,
                    "description": {
                        "type": "doc",
                        "version": 1,
                        "content": [
                            {
                                "type": "paragraph",
                                "content": [{"type": "text", "text": desc_text}]
                            }
                        ]
                    },
                    "issuetype": {"name": issue_type},
                    "priority": {"name": priority}
                }
            }

            response = requests.post(url, json=payload, headers=headers, auth=auth, timeout=10)

            # If project uses Task instead of Bug, retry automatically with Task
            if response.status_code == 400 and ("issuetype" in response.text.lower() or "valid issue type" in response.text.lower()):
                payload["fields"]["issuetype"] = {"name": "Task"}
                issue_type = "Task"
                response = requests.post(url, json=payload, headers=headers, auth=auth, timeout=10)

            if response.status_code == 201:
                data = response.json()
                key = data.get("key", f"{target_project}-000")
                return {
                    "status": "success",
                    "mode": "real_api",
                    "key": key,
                    "url": f"{JIRA_SERVER}/browse/{key}",
                    "summary": summary,
                    "issue_type": issue_type,
                    "priority": priority,
                    "project": target_project
                }
            else:
                return {
                    "status": "error",
                    "mode": "real_api",
                    "status_code": response.status_code,
                    "error_message": response.text,
                    "summary": summary
                }

        except requests.exceptions.RequestException as e:
            print(f"[Jira API Exception]: {e}")
            return _mock_create_ticket(summary, issue_type, priority, target_project, error=str(e))

    return _mock_create_ticket(summary, issue_type, priority, target_project)


def get_jira_ticket(ticket_key: str) -> Dict[str, Any]:
    """
    Retrieves details of an existing Jira ticket via GET /rest/api/3/issue/{key}.
    """
    ticket_key = ticket_key.strip().upper()

    if is_jira_configured():
        try:
            url = f"{JIRA_SERVER}/rest/api/3/issue/{ticket_key}"
            auth = (JIRA_EMAIL, JIRA_API_TOKEN)
            headers = {"Accept": "application/json"}

            response = requests.get(url, headers=headers, auth=auth, timeout=10)

            if response.status_code == 200:
                data = response.json()
                fields = data.get("fields") or {}
                issuetype_obj = fields.get("issuetype") or {}
                priority_obj = fields.get("priority") or {}
                status_obj = fields.get("status") or {}
                assignee_obj = fields.get("assignee") or {}

                return {
                    "status": "success",
                    "mode": "real_api",
                    "key": data.get("key", ticket_key),
                    "url": f"{JIRA_SERVER}/browse/{ticket_key}",
                    "summary": fields.get("summary", "No summary"),
                    "issue_type": issuetype_obj.get("name", "Unknown"),
                    "priority": priority_obj.get("name", "Unknown"),
                    "status_name": status_obj.get("name", "Unknown"),
                    "assignee": assignee_obj.get("displayName", "Unassigned")
                }
            elif response.status_code == 404:
                return {
                    "status": "not_found",
                    "key": ticket_key,
                    "message": f"Ticket '{ticket_key}' was not found in Jira."
                }
            else:
                return {
                    "status": "error",
                    "status_code": response.status_code,
                    "key": ticket_key,
                    "message": f"Jira API returned error code {response.status_code}: {response.text}"
                }
        except Exception as e:
            return {
                "status": "error",
                "key": ticket_key,
                "message": f"Failed to connect to Jira server: {e}"
            }

    # Realistic mock ticket lookup
    return {
        "status": "success",
        "mode": "mock",
        "key": ticket_key,
        "url": f"{JIRA_SERVER}/browse/{ticket_key}",
        "summary": "Database connection pool exhaustion on read replica",
        "issue_type": "Bug",
        "priority": "High",
        "status_name": "In Progress",
        "assignee": "Rajesh Kumar (SRE Team)"
    }


def update_jira_ticket(ticket_key: str, comment: str) -> Dict[str, Any]:
    """
    Adds a comment or note to an existing Jira ticket via POST /rest/api/3/issue/{key}/comment.
    """
    ticket_key = ticket_key.strip().upper()

    if is_jira_configured():
        try:
            url = f"{JIRA_SERVER}/rest/api/3/issue/{ticket_key}/comment"
            auth = (JIRA_EMAIL, JIRA_API_TOKEN)
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
            payload = {
                "body": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [{"type": "text", "text": comment}]
                        }
                    ]
                }
            }

            response = requests.post(url, json=payload, headers=headers, auth=auth, timeout=10)

            if response.status_code in [200, 201]:
                return {
                    "status": "success",
                    "mode": "real_api",
                    "key": ticket_key,
                    "url": f"{JIRA_SERVER}/browse/{ticket_key}",
                    "message": f"Successfully updated ticket '{ticket_key}' with comment."
                }
            else:
                return {
                    "status": "error",
                    "key": ticket_key,
                    "status_code": response.status_code,
                    "message": f"Failed to update ticket: {response.text}"
                }
        except Exception as e:
            return {
                "status": "error",
                "key": ticket_key,
                "message": f"Connection error updating ticket: {e}"
            }

    return {
        "status": "success",
        "mode": "mock",
        "key": ticket_key,
        "url": f"{JIRA_SERVER}/browse/{ticket_key}",
        "message": f"Updated ticket '{ticket_key}' with: '{comment}'"
    }


def _mock_create_ticket(
    summary: str,
    issue_type: str,
    priority: str,
    project: str,
    error: Optional[str] = None
) -> Dict[str, Any]:
    """Generates a realistic mock ticket when real Jira credentials are not present."""
    num = random.randint(101, 999)
    ticket_key = f"{project}-{num}"
    return {
        "status": "success",
        "mode": "mock",
        "key": ticket_key,
        "url": f"{JIRA_SERVER}/browse/{ticket_key}",
        "summary": summary,
        "issue_type": issue_type,
        "priority": priority,
        "project": project,
        "note": "Mock Mode: Real credentials not configured in .env" if not error else f"Fell back to mock due to error: {error}"
    }


if __name__ == "__main__":
    print("Testing Jira Tool against configured Jira server...")
    print(f"Jira Server: {JIRA_SERVER}")
    print(f"Jira Project: {JIRA_PROJECT}")
    print(f"Is Configured: {is_jira_configured()}\n")
    
    created = create_jira_ticket("Postgres connection pool exhausted on replica 2", issue_type="Bug", priority="High")
    print("Created:", created)
    
    test_key = created.get("key", "KAN-4")
    fetched = get_jira_ticket(test_key)
    print("Fetched:", fetched)
    
    updated = update_jira_ticket(test_key, "Assigned to SRE on-call engineer.")
    print("Updated:", updated)