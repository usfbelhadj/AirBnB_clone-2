#!/usr/bin/python3
'''C Route'''

from flask import Flask


app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def helloHbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    return 'C {}'.format(text)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
