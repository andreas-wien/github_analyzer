from .utility import get_all_pages
from .constans import *

def get_repos(token):
    headers = {
        **BASE_HEADERS,
        "Authorization": f"token {token}"
    }

    return get_all_pages(
        f"{API_BASE_URL}/user/repos",
        headers
    )

def get_repo_languages(token, n):
    repos = get_repos(token)
    
    languages = {}
    
    for repo in repos:
        lang = repo["language"]
        if lang:
            languages[lang] = languages.get(lang, 0) + 1

    languages = dict(sorted(languages.items(), key=lambda x: x[1], reverse=True))
    languages = dict(list(languages.items())[:n])
    
    return languages