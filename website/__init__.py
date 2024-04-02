from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #set up database
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'TeamPathFinder'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
