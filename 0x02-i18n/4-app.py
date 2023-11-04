#!/usr/bin/env python3
"""
   Basic Flask app with Config class
   And Babel setup for traduction
"""
from flask_babel import (
    Babel,
    _,
)
from flask import (
    Flask,
    render_template,
    request,
)

app = Flask(__name__)
babel = Babel(app)


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
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def simple():
    """
        Returns a simple template
    """
    return render_template('4-index.html')
