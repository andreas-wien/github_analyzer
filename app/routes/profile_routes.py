from flask import Blueprint, render_template, redirect, session
from ..github.user import *
from ..github.utility import *

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/profile")
def profile():
    token = session.get("github_token")

    if not token:
        return redirect("/")

    user = get_user(token)
    followers = get_followers(token, user)
    social_accounts = get_social_acccounts(token)
    user_created_at = format_date_string(user["created_at"])

    return render_template("profile.html",
                           user=user,
                           user_created_at=user_created_at,
                           followers=followers,
                           social_accounts=social_accounts
                           )