"""
TODO: module docstring
"""
from flask import Blueprint


# Define views
root = Blueprint('root', __name__, template_folder='templates')

# Pack views for registration
views = [
    root,
]
