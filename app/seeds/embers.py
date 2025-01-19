from app.models import db, Ember, environment, SCHEMA
from sqlalchemy.sql import text

def seed_embers():
    e1 = Ember(
        user_id=4, post_id=1, comment_text="This is the first ever comment on FireFly! Woohoo!"
    )
    db.session.add(e1)
    db.session.commit()

def undo_embers():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.embers RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM embers"))

    db.session.commit()
