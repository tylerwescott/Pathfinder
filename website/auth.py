from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user, login_user
from .models import User, QuizResult
from . import db

auth = Blueprint('auth', __name__)
SIGNUP_TEMPLATE = 'signup.html'

@auth.route('/startquiz')
def startquiz():
    return render_template('startquiz.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('pass')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                # Check if user has already taken the quiz
                quiz_result = QuizResult.query.filter_by(user_id=user.id).first()
                if quiz_result:
                    flash('You have already taken the quiz.', category='info')
                    return redirect(url_for('views.results'))  # Redirect to results page
                flash('Logged in successfully!', category='success')
                return redirect(url_for('views.startquiz'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template('login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('pass')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
            return render_template(SIGNUP_TEMPLATE, email=email, name=request.form.get('name'))
        elif password != request.form.get('confirmpass'):
            flash('Passwords do not match', category='error')
        elif not password:
            flash('Password is required.', category='error')
            return render_template(SIGNUP_TEMPLATE, email=email, name=request.form.get('name'))
        else:
            name = request.form.get('name')
            new_user = User(email=email, name=name, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    return render_template(SIGNUP_TEMPLATE)
