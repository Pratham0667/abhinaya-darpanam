from .health_routes import health_bp
from .auth_routes import auth_bp
from .mudra_routes import mudra_bp
from .recognition_routes import recognition_bp
from .feedback_routes import feedback_bp
from .progress_routes import progress_bp


def register_blueprints(app):
    app.register_blueprint(health_bp, url_prefix="/api")
    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(mudra_bp, url_prefix="/api")
    app.register_blueprint(recognition_bp, url_prefix="/api")
    app.register_blueprint(feedback_bp, url_prefix="/api")
    app.register_blueprint(progress_bp, url_prefix="/api")
