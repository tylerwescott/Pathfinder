from flask import Blueprint, render_template, session, url_for, request, redirect
from .models import User, db
views = Blueprint('views', __name__)

# adds value of user's selection to current score and returns new score as string
def incrementScore(score, value):
    score = str(int(score) + int(value));
    print(score)
    return score;

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/signupsuccess')
def signupsuccess(name  = None):
    return render_template('signupsuccess.html', name= session['name']) # shows sign up success page, gets user's name from sign up page

@views.route('/loginsuccess')
def loginsuccess(name =  None):
    return render_template('loginsuccess.html', name= session['name']) # shows log in success page

@views.route('/startquiz', methods=['GET', 'POST'])
def startquiz():
    session['score'] = '0'
    if request.method == 'POST':
        return redirect(url_for('views.question1'))
    return render_template('startquiz.html')


# for each question: gets score from last session. If submit button is pressed, increments score and sends new score to next session
@views.route('/question1', methods=['GET', 'POST'])
def question1(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question2'))
    return render_template('question1.html', score=score)

@views.route('/question2', methods=['GET', 'POST'])
def question2(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question3'))
    return render_template('question2.html', score=score)

@views.route('/question3', methods=['GET', 'POST'])
def question3(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question4'))
    return render_template('question3.html', score=score)

@views.route('/question4', methods=['GET', 'POST'])
def question4(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question5'))
    return render_template('question4.html', score=score)

@views.route('/question5', methods=['GET', 'POST'])
def question5(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question6'))
    return render_template('question5.html', score=score)

@views.route('/question6', methods=['GET', 'POST'])
def question6(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question7'))
    return render_template('question6.html', score=score)

@views.route('/question7', methods=['GET', 'POST'])
def question7(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question8'))
    return render_template('question7.html', score=score)

@views.route('/question8', methods=['GET', 'POST'])
def question8(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question9'))
    return render_template('question8.html', score=score)

@views.route('/question9', methods=['GET', 'POST'])
def question9(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question10'))
    return render_template('question9.html', score=score)

@views.route('/question10', methods=['GET', 'POST'])
def question10(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question11'))
    return render_template('question10.html', score=score)

@views.route('/question11', methods=['GET', 'POST'])
def question11(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question12'))
    return render_template('question11.html', score=score)

@views.route('/question12', methods=['GET', 'POST'])
def question12(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question13'))
    return render_template('question12.html', score=score)

@views.route('/question13', methods=['GET', 'POST'])
def question13(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question14'))
    return render_template('question13.html', score=score)

@views.route('/question14', methods=['GET', 'POST'])
def question14(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.question15'))
    return render_template('question14.html', score=score)

@views.route('/question15', methods=['GET', 'POST'])
def question15(score = None):
    score=session['score']
    if request.method == 'POST':
        session['score'] = incrementScore(score, request.form["agreement"])
        return redirect(url_for('views.results'))
    return render_template('question15.html', score=score)


# calculates job match based on total score from questions
@views.route('/results')
def results(score = None):
    score = session['score']
    jobMatch = ''
    if (-60 <= int(score) < -30):
        jobMatch = 'Product Manager'
    elif (-30 <= int(score) < 0):
        jobMatch = 'Technical Writer/Project Manager'
    elif (0 <= int(score) < 30):
        jobMatch = 'QA Tester'
    elif (30 <= int(score) <= 60):
        jobMatch = 'Full-Stack Developer'

    user = User.query.filter_by(id=session['user_id']).first()  # Assuming user ID is stored in session
    if user:
        user.job_role = jobMatch  # Save the job role to the user's record
        db.session.commit()

    return render_template('results.html', jobMatch=jobMatch, score=score)