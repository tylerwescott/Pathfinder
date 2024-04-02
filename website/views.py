from flask import Blueprint, render_template, session, url_for
views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")
@views.route('/signupsuccess')
def signupsuccess(name = None):
    return render_template('signupsuccess.html', name=session['name']) # shows sign up success page, gets user's name from sign up page
@views.route('/loginsuccess')
def loginsuccess(name = None):
    return render_template('loginsuccess.html', name=session['name']) # shows log in success page