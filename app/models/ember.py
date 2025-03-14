from .db import db, environment, SCHEMA, add_prefix_for_prod


class Ember(db.Model):
    __tablename__ = 'embers'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('flickers.id')), nullable=False)
    comment_text = db.Column(db.String(255))

    flickers = db.relationship('Flicker', back_populates='embers')
    user = db.relationship('User', back_populates='embers')
    emberlikes = db.relationship('EmberLike', back_populates='ember', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'post_id': self.post_id,
            'comment_text': self.comment_text
        }
