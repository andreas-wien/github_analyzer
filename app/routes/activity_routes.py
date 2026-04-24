from flask import Blueprint, render_template, redirect, session

from ..github.user import *
from ..github.activity import *

activity_bp = Blueprint("activity", __name__)

@activity_bp.route("/activity")
def activity():
    token = session.get("github_token")

    if not token:
        return redirect("/")

    user = get_user(token)
    events = get_user_events(token, user)
    events = format_events(events)

    return render_template("activity.html", user=user, events=events)