from flask import Blueprint, request, redirect, session
from ..github.auth import *

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login")
def login():
    return redirect(get_auth_url())

@auth_bp.route("/logoff")
def logoff():
    session.clear()
    return redirect("/")

@auth_bp.route("/callback")
def callback():
    code = request.args.get("code")

    token = get_access_token(code)
    session["github_token"] = token

    return redirect("/dashboard")
