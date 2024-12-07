from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Flicker(db.Model, UserMixin):
    __tablename__ = 'flickers'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    source = db.Column(db.String, nullable=False)
    type = db.Column(db.String(255), nullable=False)
