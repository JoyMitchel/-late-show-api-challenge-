from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
# models/__init__.py
from .user import User
from .guest import Guest
from .episode import Episode
from .appearance import Appearance