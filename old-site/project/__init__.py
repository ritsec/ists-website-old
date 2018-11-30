"""
This module stores the application factory.
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
    app = Flask(__name__, instance_relative_config=True)

    # Set development configuration
    if app.config['ENV'] == 'development':
        app.config.from_mapping(
            SECRET_KEY='dev',
            ISTS_NUMBER='00',
            YEAR='1970',
            MONTH='January',
            SETUP_DAY='1',
            FIRST_DAY='2',
            SECOND_DAY='3',
            ROOM='USC-1600',
            BLUE_REG_OPEN=True,
            BLUE_REG_LINK='https://google.com',
            WHITE_REG_LINK='https://google.com',
            CONTACT_EMAIL='ritsecclub@gmail.com',
        )

    # Set production configuration, if performing a production deployment
    if app.config['ENV'] == 'production':
        app.config.from_pyfile('config.py')

    # Register views
    for view in views:
        app.register_blueprint(view)

    return app
