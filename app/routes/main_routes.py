from flask import Blueprint, render_template, redirect, session

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    token = session.get("github_token")

    if token:
        return redirect("/dashboard")
    
    return render_template("index.html")
