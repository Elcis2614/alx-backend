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

@babel.localeselector
def get_local():
    """
        gets local
    """
    return Config.LANGUAGES[0]

@app.route('/')
def simple():
    """
        Returns a simple template
    """
    return render_template('0-index.html')
