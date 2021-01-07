from authorizerapp import db

class Users(db.Model):
    """
        Table: Users
            Stores users data
    """
    user_id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(50),unique=True,nullable=False)
    email = db.Column(db.String(150),unique=True,nullable=False)
    password = db.Column(db.String(60),nullable=False)
    public_key = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return f"({self.user_name} , {self.email})"
        