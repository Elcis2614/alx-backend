#!/usr/bin/env python3
"""
   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   Basic Flask app with Config class
   And Babel setup for traduction
   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
from flask_babel import (
    Babel,
    _,
)
from flask import (
    Flask,
    render_template,
    request,
    g,
)

app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
        Used as configuration for the app
        Contains default and available languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
        Determine the best match with our supported languages.
        Or forces locale with URL parameter
    """
    if "locale" in request.args:
        if (request.args["locale"] in Config.LANGUAGES):
            return request.args["locale"]
    elif "login_as" in request.args:
        user = get_user(resquest.args["login_as"])
        if user is not None:
            return user["locale"]
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.before_request
def before_request():
    """
        Uses get_user to find a user if any, and set it
        as a global on flask.g.user
    """
    if "login_as" in request.args:
        user = get_user(request.args["login_as"])
        if user is not None:
            g.user = user


def get_user(user_id: int) -> [dict, None]:
    """
        returns a user dictionary or None if the ID
        cannot be found or if login_as was not passed.
    """
    if user_id not in users.keys() or user_id is None:
        return None
    return users[user_id]


@app.route('/')
def simple():
    """
        Returns a simple template
    """
    usr = "NOBODY"
    if usr is not None:
        return render_template('5-index.html', username="NOBODY")
    return render_template('5-index.html')
