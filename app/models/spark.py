from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Spark(db.Model):
    __tablename__ = 'sparks'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    liked_post_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('flickers.id')), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)

    user = db.relationship('User', back_populates='sparks')
    flickers = db.relationship('Flicker', back_populates='sparks')

    def to_dict(self):
        return {
            'id': self.id,
            'liked_post_id': self.liked_post_id,
            'user_id': self.user_id
        }
