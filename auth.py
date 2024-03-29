from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')  # place '/login' in url to go to login page
def login():
    return "<p>Login</p>"

@auth.route('/logout')  # logout
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')  # user sign up
def sign_up():
    return "<p>Sign Up</p>"