import requests
from .constans import *
from .utility import *

def get_user_events(token, user):
    headers = {
        **BASE_HEADERS,
        "Authorization": f"token {token}"
    }
    
    url = f"{API_BASE_URL}/users/{user["login"]}/events"
    res = requests.get(url, headers=headers)
    print(res.json())
    
    return res.json()

def format_events(events):
    formatted = []

    for e in events:
        repo = e["repo"]["name"]

        if e["type"] == "PushEvent":
            text = f"Pushed commits to {repo}"
            icon = "bi-git"
        elif e["type"] == "WatchEvent":
            text = f"Starred {repo}"
            icon = "bi-star"
        elif e["type"] == "PullRequestEvent":
            text = f"Opened PR in {repo}"
            icon = "bi-git-pull-request"
        else:
            text = f"{e['type']} in {repo}"
            icon = "bi-circle"

        date = format_date_string(e["created_at"])

        formatted.append({
            "text": text,
            "date": date,
            "icon": icon,
            "type": e["type"],
            "repo": repo,
            "url": f"https://github.com/{repo}"
        })

    return formatted