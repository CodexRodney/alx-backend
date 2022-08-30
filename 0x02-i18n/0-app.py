#!/usr/bin/env python3
"""
Set up for a simple Flask app
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home_page() -> None:
    """
    returns a template
    """
    return render_template('index.html')
