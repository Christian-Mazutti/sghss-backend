from flask import Flask
from .extensions import db, migrate, bcrypt, jwt
from .config import Config
from .routes.auth import bp as auth_bp
from .routes.patients import bp as patients_bp
from .routes.professionals import bp as professionals_bp
from .routes.consultations import bp as consultations_bp
from .utils.errors import register_error_handlers
from .utils.logging_conf import configure_logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # extensões
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # logging para arquivo
    configure_logging(app)

    # blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(patients_bp, url_prefix='/patients')
    app.register_blueprint(professionals_bp, url_prefix='/professionals')
    app.register_blueprint(consultations_bp, url_prefix='/consultations')

    # handlers de erro
    register_error_handlers(app)

    @app.get('/')
    def healthcheck():
        return {'status': 'ok', 'service': 'SGHSS Backend'}

    return app
