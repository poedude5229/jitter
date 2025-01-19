from flask.cli import AppGroup
from .users import seed_users, undo_users
from .flickers import seed_flickers, undo_flickers
from .embers import seed_embers, undo_embers
from app.models.db import db, environment, SCHEMA

seed_commands = AppGroup('seed')

@seed_commands.command('all')
def seed():
    if environment == 'production':
        undo_embers()
        undo_flickers()
        undo_users()
    seed_users()
    seed_flickers()
    seed_embers()

@seed_commands.command('undo')
def undo():
    undo_embers()
    undo_flickers()
    undo_users()
