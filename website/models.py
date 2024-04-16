from .database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(128))
    job_role = db.Column(db.String(150))

class JobRole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<JobRole {self.title}>'