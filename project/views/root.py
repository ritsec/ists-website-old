"""
TODO: module docstring
"""
# External library imports
from flask import render_template

# Internal imports
from project.views import root


##
#   Routes
##
@root.route('/')
@root.route('/index')
def index():
    # TODO: remove hardcoded year values
    return render_template('index.html', title='ISTS', ists_year='17', year='2019')


@root.route('/about')
def about():
    # TODO: remove hardcoded year values
    return render_template('about.html', title='About:ISTS', ists_year='17', year='2019')


@root.route('/sponsors')
def sponsors():
    # TODO: remove hardcoded year values
    return render_template('sponsors.html', title='sponsors', ists_year='17', year='2019')


@root.route('/news')
def news():
    # TODO: remove hardcoded year values
    return render_template('news.html', title='sponsors', ists_year='17', year='2019')
