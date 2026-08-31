"""Application factory for the Customer Accounts service."""
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman

db = SQLAlchemy()
cors = CORS()
talisman = Talisman()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object("service.config.Config")
    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    cors.init_app(app)
    force_https = app.config.get("TALISMAN_FORCE_HTTPS", False)
    talisman.init_app(app, force_https=force_https and not app.config.get("TESTING", False))

    from service.routes import accounts_bp
    app.register_blueprint(accounts_bp)

    @app.get("/")
    def index():
        return jsonify(name="Customer Accounts Service", version="1.0"), 200

    @app.get("/health")
    def health():
        return jsonify(status="OK"), 200

    with app.app_context():
        db.create_all()
    return app
