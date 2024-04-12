from flask import Blueprint, render_template, session, url_for, request, redirect
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

@views.route('/question1', methods=['GET', 'POST'])
def question1(name = None):
    if request.method == 'POST':
        return redirect(url_for('views.question2'))
    return render_template('question1.html', name=session['name'])

@views.route('/question2', methods=['GET', 'POST'])
def question2(name = None):
    if request.method == 'POST':
        return redirect(url_for('views.question3'))
    return render_template('question2.html', name=session['name'])

@views.route('/question3', methods=['GET', 'POST'])
def question3(name = None):
    if request.method == 'POST':
        return redirect(url_for('views.question4'))
    return render_template('question3.html', name=session['name'])

@views.route('/question4', methods=['GET', 'POST'])
def question4(name = None):
    if request.method == 'POST':
        return redirect(url_for('views.question5'))
    return render_template('question4.html', name=session['name'])

@views.route('/question5', methods=['GET', 'POST'])
def question5(name = None):
    if request.method == 'POST':
        return redirect(url_for('views.question6'))
    return render_template('question5.html', name=session['name'])

@views.route('/question6', methods=['GET', 'POST'])
def question6(name = None):
    if request.method == 'POST':
        return redirect(url_for('views.question7'))
    return render_template('question6.html', name=session['name'])

@views.route('/question7', methods=['GET', 'POST'])
def question7(name = None):
    if request.method == 'POST':
        return redirect(url_for('views.question8'))
    return render_template('question7.html', name=session['name'])

@views.route('/question8', methods=['GET', 'POST'])
def question8(name = None):
    if request.method == 'POST':
        return redirect(url_for('views.question9'))
    return render_template('question8.html', name=session['name'])

@views.route('/question9', methods=['GET', 'POST'])
def question9(name = None):
    if request.method == 'POST':
        return redirect(url_for('views.question10'))
    return render_template('question9.html', name=session['name'])

@views.route('/question10', methods=['GET', 'POST'])
def question10(name = None):
    if request.method == 'POST':
        return redirect(url_for('views.question11'))
    return render_template('question10.html', name=session['name'])

@views.route('/question11', methods=['GET', 'POST'])
def question11(name = None):
    if request.method == 'POST':
        return redirect(url_for('views.question12'))
    return render_template('question11.html', name=session['name'])

@views.route('/question12', methods=['GET', 'POST'])
def question12(name = None):
    if request.method == 'POST':
        return redirect(url_for('views.question13'))
    return render_template('question12.html', name=session['name'])

@views.route('/question13', methods=['GET', 'POST'])
def question13(name = None):
    if request.method == 'POST':
        return redirect(url_for('views.question14'))
    return render_template('question13.html', name=session['name'])

@views.route('/question14', methods=['GET', 'POST'])
def question14(name = None):
    if request.method == 'POST':
        return redirect(url_for('views.question15'))
    return render_template('question14.html', name=session['name'])

@views.route('/question15', methods=['GET', 'POST'])
def question15(name = None):
    if request.method == 'POST':
        return redirect(url_for('views.results'))
    return render_template('question15.html', name=session['name'])

@views.route('/results')
def results(name = None):
    return render_template('results.html', name=session['name'])