"""
TODO: module docstring
"""
# External library imports
from flask import Blueprint, render_template

##
#   Attributes
##
bp = Blueprint('root', __name__, template_folder='templates')


##
#   Routes
##
@bp.route('/')
@bp.route('/index')
def index():
    # TODO: remove hardcoded year values
    return render_template('index.html', title='ISTS', ists_year='17', year='2019')


@bp.route('/about')
def about():
    # TODO: remove hardcoded year values
    return render_template('about.html', title='About:ISTS', ists_year='17', year='2019')


@bp.route('/sponsors')
def sponsors():
    # TODO: remove hardcoded year values
    return render_template('sponsors.html', title='sponsors', ists_year='17', year='2019')


@bp.route('/news')
def news():
    # TODO: remove hardcoded year values
    return render_template('news.html', title='sponsors', ists_year='17', year='2019')
