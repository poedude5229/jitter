from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    bio = db.Column(db.String(255), nullable=True)
    profile_pic = db.Column(db.String(255))
    profile_banner = db.Column(db.String(255))


    flickers = db.relationship('Flicker', back_populates='user', cascade='all, delete-orphan')
    embers = db.relationship('Ember', back_populates='user', cascade='all, delete-orphan')
    emberlikes = db.relationship('EmberLike', back_populates='user', cascade='all, delete-orphan')
    sparks = db.relationship('Spark', back_populates='user', cascade='all, delete-orphan')

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'bio': self.bio,
            'profile_pic': self.profile_pic,
            'profile_banner': self.profile_banner,
            'bio': self.bio
        }
