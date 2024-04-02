from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import User
from . import db
#TODO: has password

auth = Blueprint('auth', __name__)
@auth.route('/login', methods=['GET', 'POST'])  # place '/login' in url to go to login page
def login():
    data = request.form
    return render_template("login.html")

@auth.route('/logout')  # logout
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])  # user sign up
def sign_up():
    if request.method == 'POST': # creates new user from user submitted info when sign up button pressed
        print("!!")
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('pass')
        # TODO: add email/password requirements
        new_user = User(name=name, email=email, password=password) # TODO: store password as hash
        db.session.add(new_user)
        db.session.commit()
        session['name'] = name
        return redirect(url_for('views.signupsuccess')) # redirects to sign up succesful page defined in views
    return render_template("signup.html")