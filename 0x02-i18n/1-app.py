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

    def __init__(self, babel):
        self._babel = babel

    def set_default_locale(self):
        """ sets local """
        self._babel.BABEL_DEFAULT_LOCALE = self.LANGUAGES[0]
        self._babel.BABEL_DEFAULT_TIMEZONE = 'UTF'


config = Config(babel)
config.set_default_locale()


@app.route('/')
def simple():
    """
        Returns a simple template
    """
    return render_template('0-index.html')
