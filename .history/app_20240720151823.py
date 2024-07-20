from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(200), nullable = False, unique = True)
    date_added = db.Column(db.DateTime, default = datetime.utcnow)
    password = db.Column(db.String(50), nullable = False)


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/error')
def error():
    return render_template('404.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/')
def service():
    return render_template('service.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')



if __name__ == '__main__':
    app.run(debug = True)