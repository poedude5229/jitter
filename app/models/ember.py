from .db import db, environment, SCHEMA, add_prefix_for_prod


class Ember(db.Model):
    __tablename__ = 'embers'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    post_id = db.Column(db.Integer)
    comment_text = db.Column(db.String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'post_id': self.post_id,
            'comment_text': self.comment_text
        }
