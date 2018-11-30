"""
This module configures the root blueprint and its associated routes.
"""
# Default library imports
import os.path

# External library imports
from flask import Blueprint, current_app, render_template
from markdown import markdown as md

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
    # Create path to post files
    post_path = os.path.join(current_app.instance_path, 'posts', 'post-{}.md')

    # Loop to open each post file until there are none left
    posts = []
    try:
        post_num = 1
        while True:
            with open(post_path.format(post_num), 'r') as fp:
                posts.append(fp.read())
            post_num += 1
    except FileNotFoundError:
        pass

    # Reverse the posts - the highest-numbered posts should appear first
    posts = posts[::-1]

    # Pass the posts to the template so they get rendered
    return render_template('news.html', posts=posts, generate_html=md)


@bp.route('/register')
def register():
    return render_template('register.html')
