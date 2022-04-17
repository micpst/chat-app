from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app import db


class User(UserMixin, db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False, unique=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False, unique=False)

    def __init__(self, name: str, email: str, password: str) -> None:
        self.name = name
        self.email = email
        self.set_password(password)

    def __repr__(self) -> str:
        return f'<User {self.name}>'

    def set_password(self, password: str):
        """
        Create hashed password.
        """
        self.password = generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        """
        Check hashed password.
        """
        return check_password_hash(self.password, password)
