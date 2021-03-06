from authorizerapp import db

class BlacklistToken(db.Model):
    """
        Table: BlackListToken
            Stores token that is no longer valid
    """
    id = db.Column(db.Integer, primary_key = True)
    token = db.Column(db.String(300),nullable=False)

    def __repr__(self):
        return f"({self.token})"