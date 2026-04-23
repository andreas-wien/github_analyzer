from flask import Blueprint, render_template, redirect, session
from ..github.user import *
from ..github.repos import *

repos_bp = Blueprint("repos", __name__)

@repos_bp.route("/repos")
def repos():
    token = session.get("github_token")

    if not token:
        return redirect("/")

    user = get_user(token)
    repos = get_repos(token)

    return render_template("repos.html", user=user, repos=repos)
