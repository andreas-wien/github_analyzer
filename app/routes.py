from flask import Blueprint, render_template, request, redirect, session
from .github import *

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


@main.route("/profile")
def profile():
    token = session.get("github_token")

    if not token:
        return redirect("/")

    user = get_user(token)
    followers = get_followers(token, user)
    social_accounts = get_social_acccounts(token)
    print(social_accounts)

    return render_template("profile.html", user=user, followers=followers, social_accounts=social_accounts)

@main.route("/activity")
def activity():
    token = session.get("github_token")

    if not token:
        return redirect("/")

    user = get_user(token)

    return render_template("activity.html", user=user)

@main.route("/stats")
def stats():
    token = session.get("github_token")

    if not token:
        return redirect("/")

    user = get_user(token)

    return render_template("stats.html", user=user)

@main.route("/languages")
def languages():
    token = session.get("github_token")

    if not token:
        return redirect("/")

    user = get_user(token)

    return render_template("languages.html", user=user)
