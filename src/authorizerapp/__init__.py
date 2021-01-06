from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from authorizerapp.config import Config

db = SQLAlchemy()

def init_app(config_class = Config):
    """
        Returns instance of app configured to config_class
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from authorizerapp.authorize.routes import authorize
    app.register_blueprint(authorize)

    return app

