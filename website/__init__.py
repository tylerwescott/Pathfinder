from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path
from .models import User, JobRole
from .database import db
from dotenv import load_dotenv
import os
load_dotenv()

DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key_for_development')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .views import views
    from .auth import auth
    from .models import User, JobRole

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()
        insert_job_roles()

    return app

def insert_job_roles():
    if JobRole.query.count() == 0:  # Only insert if there are no job roles already
        roles = [
            {"title": "Product Manager", "description": "As a Product Manager, your quiz results indicate a strong aptitude for strategic decision-making and leadership. This role involves overseeing the development and marketing of products from conception through launch. You'll be responsible for identifying customer needs, defining product vision, and working closely with engineering, marketing, and sales teams to ensure that the product aligns with business goals and user expectations."},
            {"title": "Technical Writer/Project Manager", "description": "Your quiz results suggest you are adept at detailed communication and organization, making you ideal for roles as a Technical Writer or Project Manager. Technical Writers are crucial in making complex information understandable, creating manuals, guides, and documentation that articulate product specifications and procedures."},
            {"title": "QA Tester", "description": "Scoring as a QA Tester reflects your analytical skills and attention to detail, essential for this role. QA Testers are vital to the software development process, responsible for ensuring software functionality by identifying bugs and issues before the product reaches the market."},
            {"title": "Full-Stack Developer", "description": "As a Full-Stack Developer, your quiz results show proficiency in both front-end and back-end development, capable of handling all aspects of web applications. This role requires designing user interactions on websites, developing servers and databases for website functionality, and coding for mobile platforms."}
        ]
        for role in roles:
            job_role = JobRole(title=role['title'], description=role['description'])
            db.session.add(job_role)
        db.session.commit()

def create_database(app):  # Checks if db exists. If not, creates db
    if not path.exists("website/" + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Database created successfully')
