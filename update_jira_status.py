import requests
import os

jira_url = "https://your-jira-instance.atlassian.net"
jira_ticket_key = os.getenv("JIRA_TICKET_KEY")
new_status = os.getenv("NEW_STATUS")

headers = {
    "Content-Type": "application/json",
}

data = {
    "transition": {"id": "YOUR-TRANSITION-ID"}  # Replace with the actual transition ID
}

url = f"{jira_url}/rest/api/2/issue/{jira_ticket_key}/transitions"

response = requests.post(url, headers=headers, json=data, auth=(os.getenv("JIRA_USERNAME"), os.getenv("JIRA_API_TOKEN")))

if response.status_code == 204:
    print(f"Successfully updated Jira ticket {jira_ticket_key} to status: {new_status}")
else:
    print(f"Failed to update Jira ticket {jira_ticket_key}. Status code: {response.status_code}")
    print(response.text)

