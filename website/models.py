from datetime import datetime
from .database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(128))

class QuizResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score = db.Column(db.Integer)
    date_taken = db.Column(db.DateTime, default=datetime.utcnow)
    job_role = db.Column(db.String(100))

class JobRole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<JobRole {self.title}>'