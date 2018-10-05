"""
This module configures the root blueprint and its associated routes.
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
    return render_template('index.html')


@bp.route('/about')
def about():
    return render_template('about.html')


@bp.route('/news')
def news():
    return render_template('news.html')


@bp.route('/register')
def register():
    return render_template('register.html')
