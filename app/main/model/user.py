from app.main import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(), unique=True)
    public_id = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return "User: {}".format(self.username)
