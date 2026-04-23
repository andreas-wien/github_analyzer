from flask import Blueprint, render_template, redirect, session

from ..github.activity import *
from ..github.charts import *
from ..github.user import *

activity_bp = Blueprint("activity", __name__)

@activity_bp.route("/activity")
def activity():
    token = session.get("github_token")

    if not token:
        return redirect("/")

    user = get_user(token)
    events = get_user_events(token, user)
    fig_pushes_per_day = pushes_per_day(events)
    fig_events_breakdown = event_type_breakdown(events)

    return render_template("activity.html", user=user, fig_pushes_per_day=fig_pushes_per_day, fig_events_breakdown=fig_events_breakdown)