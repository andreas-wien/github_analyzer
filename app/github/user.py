import requests
from .utility import get_all_pages
from .constans import *

def get_user(token):
    headers = {
        **BASE_HEADERS,
        "Authorization": f"token {token}"
    }

    res = requests.get(f"{API_BASE_URL}/user", headers=headers)
    return res.json()

def get_followers(token, user):
    headers = {
        **BASE_HEADERS,
        "Authorization": f"token {token}"
    }
    
    return get_all_pages(
        user["followers_url"],
        headers
    )

def get_social_acccounts(token):
    headers = {
        **BASE_HEADERS,
        "Authorization": f"token {token}"
    }

    res = requests.get(f"{API_BASE_URL}/user/social_accounts", headers=headers)
    
    return res.json()