"""
TODO: module docstring
"""
# Default library imports

# External library imports
from flask import Flask

# Internal imports
from project.views import views


def create_app():
    """
    Create the default application object.

    :return: the initialized Flask object
    """
    app = Flask(__name__, instance_relative_config=True)

    # Set development configuration
    if app.config['ENV'] == 'development':
        app.config.from_mapping(
            SECRET_KEY='dev',
            ISTS_NUMBER='00',
            YEAR='0000',
        )

    # Set production configuration, if performing a production deployment
    if app.config['ENV'] == 'production':
        app.config.from_pyfile('config.py')

    # Register views
    for view in views:
        app.register_blueprint(view)

    return app
