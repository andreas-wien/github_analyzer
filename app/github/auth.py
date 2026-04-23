import requests
from flask import current_app
from .constans import *

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
