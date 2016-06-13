from app import db


class User(db.Model):
    """
    Model User
    """
    __tablename__ = 'Users'
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(120), unique=True)
    email = Column(db.String(120), unique=True)
    password = Column(db.String(30))
