from app.models import db, Spark, environment, SCHEMA
from sqlalchemy.sql import text

def seed_sparks():
    s1 = Spark(liked_post_id=1, user_id=4)
    s2 = Spark(liked_post_id=1, user_id=5)
    s3 = Spark(liked_post_id=1, user_id=6)
    s4 = Spark(liked_post_id=1, user_id=7)
    db.session.add(s1)
    db.session.add(s2)
    db.session.add(s3)
    db.session.add(s4)
    db.session.commit()

def undo_sparks():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.sparks RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM sparks"))

    db.session.commit()
