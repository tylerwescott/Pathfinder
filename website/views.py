from flask import Blueprint, render_template, session, url_for
views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")
@views.route('/signupsuccess:firstname')
def signupsuccess(name = None):
    return render_template('signupsuccess.html', name=session['name']) # test page for quiz