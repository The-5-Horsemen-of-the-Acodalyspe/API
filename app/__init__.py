from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt import JWT
from werkzeug.security import check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models


def authenticate(username, password):
    user = models.User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return user


def identity(payload):
    return models.User.query.get(payload["identity"])


jwt = JWT(app, authenticate, identity)