import requests
from flask import current_app
from .utility import get_all_pages

API_BASE_URL = "https://api.github.com"

BASE_HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "Flask-App"
}

def get_auth_url():
    return f"https://github.com/login/oauth/authorize?client_id={current_app.config['GITHUB_CLIENT_ID']}&scope=repo"

def get_access_token(code):
    url = "https://github.com/login/oauth/access_token"

    response = requests.post(url, data={
        "client_id": current_app.config["GITHUB_CLIENT_ID"],
        "client_secret": current_app.config["GITHUB_CLIENT_SECRET"],
        "code": code
    }, headers=BASE_HEADERS)

    return response.json().get("access_token")

def get_user(token):
    headers = {
        **BASE_HEADERS,
        "Authorization": f"token {token}"
    }

    res = requests.get(f"{API_BASE_URL}/user", headers=headers)
    return res.json()


def get_repos(token):
    headers = {
        **BASE_HEADERS,
        "Authorization": f"token {token}"
    }

    return get_all_pages(
        f"{API_BASE_URL}/user/repos",
        headers
    )

def get_top_languages(token):
    repos = get_repos(token)
    
    languages = {}

    for repo in repos:
        lang = repo["language"]
        if lang:
            languages[lang] = languages.get(lang, 0) + 1

    languages = dict(sorted(languages.items(), key=lambda x: x[1], reverse=True))
    
    return languages

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