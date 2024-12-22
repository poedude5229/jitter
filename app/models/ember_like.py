from .db import db, environment, SCHEMA, add_prefix_for_prod

class EmberLike(db.Model):
    __tablename__ = 'emberlikes'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    ember_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('embers.id')), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)

    ember = db.relationship('Ember', back_populates='emberlikes')
    user = db.relationship('User', back_populates='emberlikes')

    def to_dict(self):
        return {
            'id': self.id,
            'ember_id': self.ember_id,
            'user_id': self.user_id
        }
