#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def helloHbnb():
    return 'HBNB'


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
