import datetime
from flask import (
    abort,
    current_app,
    request
)
from functools import wraps
import jwt

from authorizerapp import db
from authorizerapp.models.temp import BlacklistToken
from authorizerapp.models.users import Users


def blacklist_token(token):
    curr_token = BlacklistToken(token=token)
    try:
        db.session.add(curr_token)
        db.session.commit()
    except:
        return False
    return True

def remove_from_blacklist(token):
    curr_token = BlacklistToken.query.filter_by(token=token).first()
    if curr_token == None:
        return True
    
    try:
        db.session.delete(curr_token)
        db.session.commit()
    except:
        return False
    return True

def get_token(public_key,delta):
    return jwt.encode(
            {
                'public_key':public_key,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=delta)
            },
            current_app.config['SECRET_KEY'],
            algorithm="HS256"
        )
    
def token_required(func):
    @wraps(func)
    def decorator(*args,**kwargs):
        token = request.headers.get('x-access-token') or request.headers.get('X-Access-Token')

        if not token:
            abort(400,description="Token Missing")
        
        try:
            data = jwt.decode(token,current_app.config['SECRET_KEY'],algorithms=["HS256"])
            curr_user = Users.query.filter_by(public_key=data["public_key"]).first()
            token = BlacklistToken.query.filter_by(token=token).first()
            if token:
                abort(401,description="Invalid Token")
        except:
            abort(401,"Invalid token")
        return func(curr_user,*args,**kwargs)
    return decorator