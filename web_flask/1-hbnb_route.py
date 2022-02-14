#!/usr/bin/python3
""" Starts Flask. """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ DISPLAY Hello HBNB!!! """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ DISPLAY HBNB!!! """
    return ("HBNB")


if __name__ == '__main__':
    app.run()
