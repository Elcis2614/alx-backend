#!/usri/bin/env python3
"""
   Basic Flask app
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app_view.route('/')
def simple():
    """
        Returns a simple template
    """
    return render_template('0-index.html')
