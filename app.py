from flask import Flask, render_template, redirect, url_for, request
from secret import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail, Message
app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.yourmailserver.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'
mail = Mail(app)
#Creating Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(200), nullable = False, unique = True)
    date_added = db.Column(db.DateTime, default = datetime.utcnow)
    password = db.Column(db.String(50), nullable = False)


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


#For sending the email(NOT WORKING ATM)
@app.route('/send_email', methods=['POST'])
def send_email():
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    msg = Message(subject, sender=email, recipients=['recipient@example.net'])
    msg.body = message

    try:
        mail.send(msg)
        return 'Email sent successfully!'
    except Exception as e:
        return str(e)


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