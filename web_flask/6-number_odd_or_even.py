#!/usr/bin/python3
""" Flask Introduction """
from flask import Flask
from flask import render_template
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
    return "C {}".format(text)


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_whatever(text="is cool"):
    """ Prints custom text when entering the route """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def n_is_int(n):
    """ Prints n only if its integer """
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def show_html(n):
    """ Prints html page only if n its integer """
    if isinstance(n, int):
        return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def show_html_dynamic(n):
    """ Prints html page only if n its integer """
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
