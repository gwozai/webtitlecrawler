from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['JSON_AS_ASCII'] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    from myapp.views import bp
    app.register_blueprint(bp)

    return app

from myapp import models