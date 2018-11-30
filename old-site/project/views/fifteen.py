"""
This module configures the routes to serve the ISTS 15 website.
"""
# External library imports
from flask import Blueprint, render_template

##
#   Attributes
##
bp = Blueprint(
    'fifteen', __name__,
    static_folder='static/15',
    url_prefix='/15',
)


##
#   Routes
##
@bp.route('/')
@bp.route('/index')
def index():
    return render_template('15/index.html')
