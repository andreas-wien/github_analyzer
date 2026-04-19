from flask import Blueprint, render_template, request, redirect, session, current_app
from .github import get_user, get_repos, get_access_token, get_public_user

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")


@main.route("/login")
def login():
    github_auth_url = (
        "https://github.com/login/oauth/authorize"
        f"?client_id={current_app.config['GITHUB_CLIENT_ID']}&scope=repo"
    )
    return redirect(github_auth_url)


@main.route("/callback")
def callback():
    code = request.args.get("code")

    token = get_access_token(code)
    session["github_token"] = token

    return redirect("/dashboard")


@main.route("/dashboard")
def dashboard():
    token = session.get("github_token")

    if not token:
        return redirect("/")

    user = get_user(token)
    repos = get_repos(token)

    return render_template("dashboard.html", user=user, repos=repos)


@main.route("/profile", methods=["POST"])
def profile():
    username = request.form.get("username")

    data = get_public_user(username)

    if "login" not in data:
        return f"Error: {data.get('message')}"

    return f"User: {data['login']}, Public repos: {data['public_repos']}"