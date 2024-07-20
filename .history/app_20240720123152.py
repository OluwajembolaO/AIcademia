from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template()



if __name__ == '__main__':
    app.run(debug = True)