from flask import Blueprint, render_template, request, redirect, session
from .github import get_auth_url, get_top_languages, get_user, get_repos, get_access_token, get_public_user

main = Blueprint("main", __name__)

@main.route("/")
def home():
    token = session.get("github_token")

    if token:
        return redirect("/dashboard")
    
    return render_template("index.html")


@main.route("/login")
def login():
    return redirect(get_auth_url())

@main.route("/logoff")
def logoff():
    session.clear()
    return redirect("/")

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
    languages = get_top_languages(token)

    return render_template("dashboard.html", user=user, repos=repos, languages=languages)

@main.route("/repos")
def repos():
    token = session.get("github_token")

    if not token:
        return redirect("/")

    user = get_user(token)
    repos = get_repos(token)

    return render_template("repos.html", user=user, repos=repos)


@main.route("/profile", methods=["POST"])
def profile():
    username = request.form.get("username")

    data = get_public_user(username)

    if "login" not in data:
        return f"Error: {data.get('message')}"

    return f"User: {data['login']}, Public repos: {data['public_repos']}"