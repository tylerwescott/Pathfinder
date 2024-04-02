from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import User
from . import db
#TODO: has password

auth = Blueprint('auth', __name__)
@auth.route('/login', methods=['GET', 'POST'])  # place '/login' in url to go to login page
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('pass')
        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password: # TODO: change to check_password_hash = password
                session['name'] = user.name
                return redirect(url_for('views.loginsuccess')) # redirects to sign up succesful page defined in views   
            else:
                flash('Invalid password. Try again.', category='error')
        else:
            flash('User does not exist. Try again or sign up', category='error')

    return render_template("login.html")

@auth.route('/logout')  # logout
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])  # user sign up
def sign_up():
    if request.method == 'POST': # creates new user from user submitted info when sign up button pressed
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('pass')
        # TODO: add email/password requirements
        new_user = User(name=name, email=email, password=password) # TODO: store password as hash
        db.session.add(new_user)
        db.session.commit()
        session['name'] = name # saves name to be passed to signup success page
        return redirect(url_for('views.signupsuccess')) # redirects to sign up succesful page defined in views
    return render_template("signup.html")