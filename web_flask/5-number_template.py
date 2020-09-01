#!/usr/bin/python3
'''Python Route'''

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def helloHbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Pyt(text):
    return 'Python {}'.format(str(text).replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def htm(n):
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
