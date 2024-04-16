from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(128))
    job_role = db.Column(db.String(150))