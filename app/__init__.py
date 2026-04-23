from flask import Flask, request
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    @app.context_processor
    def inject_layout_flags():
        return {
            "show_back_button": request.path != "/dashboard" and request.path != "/"
        }

    from .routes.activity_routes import activity_bp
    from .routes.auth_routes import auth_bp
    from .routes.dashboard_routes import dashboard_bp
    from .routes.languages_routes import languages_bp
    from .routes.main_routes import main_bp
    from .routes.profile_routes import profile_bp
    from .routes.stats_routes import stats_bp
    from .routes.repo_routes import repos_bp

    app.register_blueprint(activity_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(languages_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(stats_bp)
    app.register_blueprint(repos_bp)

    return app