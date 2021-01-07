from flask import (
    abort,
    Blueprint,
    json,
    jsonify,
    request
)
import jwt
import os
import uuid
from werkzeug.exceptions import HTTPException 

from authorizerapp import (
    bcrypt,
    db
)

from authorizerapp.authorize.utils import (
    get_token,
    blacklist_token,
    token_required,
    remove_from_blacklist
)
from authorizerapp.models.users import Users

authorize = Blueprint('authorize',__name__)

@authorize.errorhandler(HTTPException)
def handle_exception(e):
    """
        Return JSON response for HTTP Error
    """
    response = e.get_response()
    response.data = json.dumps({
        "status":e.code,
        "code":e.code,
        "name":e.name,
        "description":e.description
    })
    response.content_type = "application/json"
    return response

@authorize.route('/api/login',methods=['POST'])
def login():
    """
        Handles route for logging in user
    """
    data = request.get_json()
    if not data:
        abort(400,description = "missing parameters")


    name = data.get('name')
    password = data.get('password')

    if not password or not name:
        abort(400,description = "missing parameters")
    
    
    user = Users.query.filter_by(user_name=name).first()

    if not user:
        user = Users.query.filter_by(email=name).first()

    if not user or not bcrypt.check_password_hash(user.password,password):
        abort(401,"verification failed")

    token = get_token(user.public_key,60)
    return jsonify({
        'token':token,
        "user_name":user.user_name,
        "email":user.email
    }),200


@authorize.route('/api/logout')
@token_required
def logout(current_user):
    """
        Handles route for loggin user out
    """
    token = request.headers.get('x-access-token') or request.headers.get('X-Access-Token')
    blacklist_token(token)
    return jsonify({'success':True,'message':'Logged out'}),200


@authorize.route('/api/register',methods=['POST'])
def register():
    """
        Handles route for registering new user
    """
    data = request.get_json()
    if not data:
        abort(400,"missing parameters")
    
    user_name = data.get('user_name')
    email = data.get('email')
    password = data.get('password')
    
    if not user_name or not email or not password:
        abort(400,"missing parameters")
    
    if Users.query.filter_by(user_name=user_name).first():
        abort(409,"username is already taken")
    
    if Users.query.filter_by(email=email).first():
        abort(409,"email already exists")

    h_password = bcrypt.generate_password_hash(password).decode('utf-8')
    public_key = str(uuid.uuid4())
    while Users.query.filter_by(public_key=public_key).first()!=None:
        public_key = str(uuid.uuid4())
    
    new_user = Users(user_name=user_name,email=email,password=h_password,public_key=public_key)

    try:
        db.session.add(new_user)
        db.session.commit()
    except:
        abort(500,"Internal Error")

    return jsonify({'success':True,'message':'New user created'}),200


@authorize.route('/api/verify')
@token_required
def verify_user(current_user):
    """
        Handles route for verifying existing user
    """
    return jsonify({
        "user_name":current_user.user_name,
        "email":current_user.email,
        "status":200
    }),200
