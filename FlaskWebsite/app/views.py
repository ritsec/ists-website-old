from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='ISTS', ists_year=app.config['ISTS_YEAR'], year=app.config['YEAR'])

@app.route('/about')
def about():
    return render_template('about.html', title='About:ISTS', ists_year=app.config['ISTS_YEAR'])

@app.route('/sponsors')
def sponsors():
    return render_template('sponsors.html', title='sponsors', ists_year=app.config['ISTS_YEAR'])

@app.route('/news')
def news():
    return render_template('news.html', title='news', ists_year=app.config['ISTS_YEAR'])
