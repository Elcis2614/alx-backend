#!/usr/bin/env python3
"""
   Basic Flask app
   WIth Babel setup
"""
from flask_babel import Babel
from flask import (
    Flask,
    render_template,
)

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
        COnfigure available languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ determine the best match with our supported languages."""
    return babel.localeselector.best_match(Config.LANGUAGES)


@app.route('/')
def simple():
    """
        Returns a simple template
    """
    return render_template('2-index.html')
