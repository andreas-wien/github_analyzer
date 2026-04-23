from flask import Blueprint, render_template, redirect, session
from ..github.user import *

stats_bp = Blueprint("stats", __name__)

@stats_bp.route("/stats")
def stats():
    token = session.get("github_token")

    if not token:
        return redirect("/")

    user = get_user(token)

    return render_template("stats.html", user=user)