from flask import Blueprint, render_template, redirect, session
from ..github.user import *

languages_bp = Blueprint("languages", __name__)

@languages_bp.route("/languages")
def languages():
    token = session.get("github_token")

    if not token:
        return redirect("/")

    user = get_user(token)

    return render_template("languages.html", user=user)
