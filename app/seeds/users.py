from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text

def seed_users():
    bigjoe = User(
        username="bigjoe", email='edgelord420@zune.net', password='password69',
    )
