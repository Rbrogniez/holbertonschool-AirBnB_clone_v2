#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello HBNB</h1>'
