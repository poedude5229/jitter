from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text

def seed_users():
    bigjoe = User(
        username="bigjoe", email='edgelord420@zune.net', password='password69', bio='Founder. Innovator. I made this website for real for real.', profile_pic='', profile_banner=''
    )

    db.session.add(bigjoe)
    db.session.commit()

def undo_users():
    if environment == 'production':
        db.session.execute(f"TRUCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
