"""
This module configures the archival blueprints and the links to the old
websites and scores.
"""
# External library imports
from flask import Blueprint, render_template

##
#   Attributes
##
bp = Blueprint(
    'archive', __name__,
    template_folder='templates',
    url_prefix='/archive',
)


##
#   Routes
##
@bp.route('/')
@bp.route('/index')
def index():
    return render_template('archive/index.html')


@bp.route('/scores')
def scores():
    return render_template('archive/scores.html')
