from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def error():
    return render_template('404.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = True)