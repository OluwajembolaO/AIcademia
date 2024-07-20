from flask import Flask, redirect_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():




if __name__ == '__main__':
    app.run(debug = True)