from flask import Blueprint, render_template, request, session, redirect, url_for
from flask_login import login_required, current_user
from .database import db
from .models import User, QuizResult
from datetime import datetime

views = Blueprint('views', __name__)

# adds value of user's selection to current score and returns new score as string
def incrementScore(score, value):
    score = str(int(score) + int(value));
    print(score)
    return score;

@views.route('/')
def home():
    return render_template('home.html', user=current_user)

@views.route('/signupsuccess')
def signupsuccess(name  = None):
    return render_template('signupsuccess.html', name= session['name']) # shows sign up success page, gets user's name from sign up page

@views.route('/loginsuccess')
def loginsuccess(name =  None):
    return render_template('loginsuccess.html', name= session['name']) # shows log in success page

@views.route('/startquiz', methods=['GET', 'POST'])
@login_required
def startquiz():
    session['score'] = '0'
    if request.method == 'POST':
        return redirect(url_for('views.question1'))
    return render_template('startquiz.html')

# My (Tyler) attempt at search functionality
@views.route('/search_results', methods=['GET', 'POST'])
@login_required
def search_results():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        score_min = request.form.get('score_min')
        score_max = request.form.get('score_max')

        query = QuizResult.query
        if user_id:
            query = query.filter_by(user_id=user_id)
        if start_date and end_date:
            query = query.filter(QuizResult.date_taken.between(start_date, end_date))
        if score_min and score_max:
            query = query.filter(QuizResult.score.between(score_min, score_max))

        results = query.all()
        return render_template('search_results.html', results=results)
    return render_template('search_form.html')

# for each question: gets score from last session. If submit button is pressed, increments score and sends new score to next session
@views.route('/question1', methods=['GET', 'POST'])
@login_required
def question1(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question2'))
    return render_template('question1.html', score=score)

@views.route('/question2', methods=['GET', 'POST'])
@login_required
def question2(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question3'))
    return render_template('question2.html', score=score)

@views.route('/question3', methods=['GET', 'POST'])
@login_required
def question3(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question4'))
    return render_template('question3.html', score=score)

@views.route('/question4', methods=['GET', 'POST'])
@login_required
def question4(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question5'))
    return render_template('question4.html', score=score)

@views.route('/question5', methods=['GET', 'POST'])
@login_required
def question5(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question6'))
    return render_template('question5.html', score=score)

@views.route('/question6', methods=['GET', 'POST'])
@login_required
def question6(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question7'))
    return render_template('question6.html', score=score)

@views.route('/question7', methods=['GET', 'POST'])
@login_required
def question7(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question8'))
    return render_template('question7.html', score=score)

@views.route('/question8', methods=['GET', 'POST'])
@login_required
def question8(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question9'))
    return render_template('question8.html', score=score)

@views.route('/question9', methods=['GET', 'POST'])
@login_required
def question9(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question10'))
    return render_template('question9.html', score=score)

@views.route('/question10', methods=['GET', 'POST'])
@login_required
def question10(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question11'))
    return render_template('question10.html', score=score)

@views.route('/question11', methods=['GET', 'POST'])
@login_required
def question11(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question12'))
    return render_template('question11.html', score=score)

@views.route('/question12', methods=['GET', 'POST'])
@login_required
def question12(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question13'))
    return render_template('question12.html', score=score)

@views.route('/question13', methods=['GET', 'POST'])
@login_required
def question13(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question14'))
    return render_template('question13.html', score=score)

@views.route('/question14', methods=['GET', 'POST'])
@login_required
def question14(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question15'))
    return render_template('question14.html', score=score)

@views.route('/question15', methods=['GET', 'POST'])
@login_required
def question15(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.results'))
    return render_template('question15.html', score=score)


def calculate_job_match(score):
    if -60 <= int(score) < -30:
        return 'Product Manager'
    elif -30 <= int(score) < 0:
        return 'Technical Writer/Project Manager'
    elif 0 <= int(score) < 30:
        return 'QA Tester'
    elif 30 <= int(score) <= 60:
        return 'Full-Stack Developer'
    else:
        return 'Undefined Role'

@views.route('/results')
@login_required
def results():
    score = session.get('score', 0)
    job_match = calculate_job_match(score)

    new_result = QuizResult(
        user_id=current_user.id,
        score=score,
        job_role=job_match,
        date_taken=datetime.utcnow()
    )
    db.session.add(new_result)
    db.session.commit()

    current_user_result = new_result

    users_with_results = db.session.query(User, QuizResult).join(QuizResult, User.id == QuizResult.user_id).all()

    return render_template('results.html', jobMatch=job_match, score=score, user=current_user, current_user_result=current_user_result, users_with_results=users_with_results)

