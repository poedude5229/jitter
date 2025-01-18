from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Flicker(db.Model):
    __tablename__ = 'flickers'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    source = db.Column(db.String, nullable=False)
    caption = db.Column(db.String(255))
    type = db.Column(db.String(255), nullable=False)

    user = db.relationship('User', back_populates='flickers')
    embers = db.relationship('Ember', back_populates='flickers', cascade='all, delete-orphan')
    sparks = db.relationship('Spark', back_populates='flickers', cascade='all, delete-orphan')


    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'source': self.source,
            'type': self.type
        }
