from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

from authorizerapp.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()


def init_app(config_class = Config):
    """
        Returns instance of app configured to config_class
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)

    from authorizerapp.authorize.routes import authorize
    from authorizerapp.main.routes import main
    app.register_blueprint(authorize)
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app

