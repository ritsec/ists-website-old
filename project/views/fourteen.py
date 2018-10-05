"""
This module configures the routes to serve the ISTS 14 website.
"""
# External library imports
from flask import Blueprint, render_template

##
#   Attributes
##
bp = Blueprint(
    'fourteen', __name__,
    url_prefix='/14',
)


##
#   Routes
##
@bp.route('/')
@bp.route('/index')
def index():
    return render_template('14/index.html', title='ISTS', ists_year='14', year='2016')


@bp.route('/about')
def about():
    return render_template('14/about.html', title='About:ISTS', ists_year='14')


@bp.route('/sponsors')
def sponsors():
    return render_template('14/sponsors.html', title='sponsors', ists_year='14')


@bp.route('/news')
def news():
    return render_template('14/news.html', title='news', ists_year='14')
