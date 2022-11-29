#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    return 'Hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python(text='is cool'):
    text = text.replace("_", " ")
    return "Python {}".format(text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
