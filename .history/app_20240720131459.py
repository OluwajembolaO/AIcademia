from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.confi

@app.route('/')
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

@app.route('/service')
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