"""
TODO: module docstring
"""
# External library imports
from flask import Flask

# Internal imports
from project.views import views


def create_app():
    """
    Create the default application object.

    :return: the initialized Flask object
    """
    app = Flask(__name__)

    # Register views
    for view in views:
        app.register_blueprint(view)

    return app
