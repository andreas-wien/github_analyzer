import requests
from flask import current_app

BASE_HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "Flask-App"
}


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

    res = requests.get("https://api.github.com/user", headers=headers)
    return res.json()


def get_repos(token):
    headers = {
        **BASE_HEADERS,
        "Authorization": f"token {token}"
    }

    res = requests.get("https://api.github.com/user/repos", headers=headers)
    return res.json()


def get_public_user(username):
    url = f"https://api.github.com/users/{username}"
    res = requests.get(url, headers=BASE_HEADERS)
    return res.json()