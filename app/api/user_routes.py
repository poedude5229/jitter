from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Ember

user_routes = Blueprint('users', __name__)

@user_routes.route('/')
def users():
    """
    Queries all users and returns them as a list of dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}
