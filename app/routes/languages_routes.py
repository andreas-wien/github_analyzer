from flask import Blueprint, render_template, redirect, session, jsonify
from ..github.user import *
from ..github.languages import *

languages_bp = Blueprint("languages", __name__)

@languages_bp.route("/languages")
def languages():
    token = session.get("github_token")

    if not token:
        return redirect("/")

    user = get_user(token)

    return render_template("languages.html", user=user)

@languages_bp.route("/languages/load")
def load_languages():
    token = session.get("github_token")

    if not token:
        return redirect("/")
    
    languages = get_language_usage_sum(token)
    
    return jsonify(languages)