from app.models import db, Ember, environment, SCHEMA
from sqlalchemy.sql import text

def seed_embers():
    e1 = Ember(
        user_id=4, post_id=1, comment_text="This is the first ever comment on FireFly! Woohoo!"
    )
    e2 = Ember(user_id=1, post_id=2, comment_text="Omg hey John Pork! You are the greatest travel blogger in existence. Will you please visit my hometown in WV?")
    e3 = Ember(user_id=1, post_id=2, comment_text="We love you Ben! Hope to hear you and Puffin back on the radio this year! LPOTL is not funny without you.")
    db.session.add(e1)
    db.session.add(e2)
    db.session.add(e3)
    db.session.commit()

def undo_embers():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.embers RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM embers"))

    db.session.commit()
