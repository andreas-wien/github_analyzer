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

    from .routes import main
    app.register_blueprint(main)

    return app