from flask import Blueprint

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return "<h1>Test</h1>"  # test page for the startup of website
@views.route('/quiz')
def quiz():
    return "<p>Quiz</p>" # test page for quiz