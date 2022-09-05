#!/usr/bin/python3
""" Flask Introduction """
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ Prints when going in the web app """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Prints when going in the web app with route """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_whatever(text):
    """ Prints custom text when entering the route """
    text = text.replace('_', ' ')
    print(text)
    return "C {}".format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
