from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')  # place '/login' in url to go to login page
def login():
    return render_template("login.html")

@auth.route('/logout')  # logout
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')  # user sign up
def sign_up():
    return render_template("signup.html")