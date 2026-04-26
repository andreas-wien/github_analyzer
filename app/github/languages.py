import requests
from ..github.repos import get_repos
from .constans import *

def get_language_usage_sum(token):
    headers = {
        **BASE_HEADERS,
        "Authorization": f"token {token}"
    }
    
    repos = get_repos(token)
    
    languages = {}
    for repo in repos:
        url = repo["languages_url"]
        res = requests.get(url, headers=headers)
        for lang, bytes in res.json().items():
            if lang:
                languages[lang] = languages.get(lang, 0) + bytes
    
    return languages