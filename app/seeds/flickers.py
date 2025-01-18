from app.models import db, Flicker, environment, SCHEMA
from sqlalchemy.sql import text

def seed_flickers():
    f1 = Flicker(
        user_id=1, source="This is the very first ever post on Firefly", type="Text"
    )

    f2 = Flicker(
        user_id=2, source="John Pork here. Hello from London! This website is so much better than Twitter because I can actually open it at work without getting fired and no Elon Musk!", type="Text"
    )

    db.session.add(f1)
    db.session.commit()

def undo_flickers():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.flickers RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM flickers"))

    db.session.commit()
