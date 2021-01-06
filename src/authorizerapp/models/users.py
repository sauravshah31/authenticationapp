from authorizerapp import db

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(50),unique=True,nullable=False)
    email = db.Column(db.String(150),unique=True,nullable=False)
    passowrd = db.Column(db.String(60),nullable=False)

    def __repr__(self):
        return f"({self.user_name} , {self.email})"
        