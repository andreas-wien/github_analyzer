import requests
from .constans import *

def get_user_events(token, user):
    headers = {
        **BASE_HEADERS,
        "Authorization": f"token {token}"
    }
    
    url = f"{API_BASE_URL}/users/{user["login"]}/events"
    res = requests.get(url, headers=headers)
    print(res.json())
    
    return res.json()
