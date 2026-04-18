from flask import Flask, render_template, request, redirect, session
import requests
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
ENVIRONMENT = os.getenv("ENVIRONMENT")

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    github_auth_url = (
        "https://github.com/login/oauth/authorize"
        f"?client_id={GITHUB_CLIENT_ID}&scope=repo"
    )
    
    return redirect(github_auth_url)

@app.route("/callback")
def callback():
    code = request.args.get("code")

    token_url = "https://github.com/login/oauth/access_token"
    
    response = requests.post(token_url, data={
        "client_id": GITHUB_CLIENT_ID,
        "client_secret": GITHUB_CLIENT_SECRET,
        "code": code
    }, headers={"Accept": "application/json"})

    token = response.json()["access_token"]
    session["github_token"] = token
    
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    token = session.get("github_token")

    if not token:
        return redirect("/")

    headers = {
        "Authorization": f"token {token}"
    }

    user_res = requests.get("https://api.github.com/user", headers=headers)
    repos_res = requests.get("https://api.github.com/user/repos", headers=headers)

    user = user_res.json()
    repos = repos_res.json()

    return render_template("dashboard.html", user=user, repos=repos)

@app.route("/profile", methods=["POST"])
def profile():
    username = request.form["username"]
    
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    data = response.json()

    return f"User: {data['login']}, Public repos: {data['public_repos']}"

if __name__ == "__main__":
    if ENVIRONMENT == "DEV":
        app.run(debug=True)
    else:
        port = int(os.environ.get("PORT", 5000))
        app.run(host="0.0.0.0", port=port)