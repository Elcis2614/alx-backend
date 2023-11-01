#!/usr/bin/env python3
""" 
   Basic Flask app
"""
form flask import Flask
from flask import render_template

app = Flask(__name__)

@app_view.route('/')
def simple():
    return render_template('0-index.html')
