from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin): #create object for information to be stored
    id = db.Column(db.Integer, primary_key=True) #define columns of db table with unique ids for each user
    email = db.Column(db.String(320), unique=True) #stores email addresses of users with max length 320 that are not the same as others already in db
    password = db.Column(db.String(128)) #stores passwords under with max length 128