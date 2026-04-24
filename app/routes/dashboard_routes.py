from flask import Blueprint, render_template, redirect, session
from ..github.user import *
from ..github.repos import *

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
def dashboard():
    token = session.get("github_token")

    if not token:
        return redirect("/")

    user = get_user(token)
    repos = get_repos(token)
    languages = get_top_languages(token, 5)

    return render_template("dashboard.html", user=user, repos=repos, languages=languages)
