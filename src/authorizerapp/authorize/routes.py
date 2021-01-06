from flask import (
    abort,
    Blueprint,
    current_app,
    jsonify,
    request
)
import os

from authorizerapp.models.users import Users

authorize = Blueprint('authorize',__name__)

@authorize.route('/api/login')
def login():
    return "<h1>Test</h1>"


def validate_register_data():
    pass
    
@authorize.route('/api/register')
def register():
    user_name = request.form.get('user_name')
    email = request.form.get('email')
    passowrd = request.form.get('password')
    return f"<h1>Test Register {user_name}</h1>"