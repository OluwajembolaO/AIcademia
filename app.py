from flask import Flask, render_template, redirect, url_for, request, session, request, jsonify
from secret import *
from flask_sqlalchemy import SQLAlchemy
from ai import *
from datetime import datetime
from flask_mail import Mail, Message
app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
messages = []
# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
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


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/', methods=["GET", "POST"])
def chatbot():
    global messages

    if request.method == "POST":
        user_input = request.form["user_input"]
        messages.append({
            "role": "user",
            "content": user_input
        })

        # Prepare prompt for the new model
        conversation = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in messages])
        ai_response = getResponse(conversation)

        messages.append({
            "role": "assistant",
            "content": ai_response
        })

        return jsonify({"response": ai_response})

    # For GET requests, render the chat interface
    return render_template('chatbot.html', messages=messages)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        # Replace with your database query logic
        # Example assumes User model has 'name' and 'password' fields
        user = User.query.filter_by(name=username).first()

        if user is None:
            error_message = f"This username ({username}) doesn't exist. Please try again."
            return render_template('login.html', error=error_message)
        else:
            if user.password == password:
                session['username'] = user.name  # Store the username in the session
                return redirect(url_for('index'))
            else:
                error_message = "Incorrect password. Please try again."
                return render_template('login.html', error=error_message)

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  # Clear the username from the session
    return redirect(url_for('login'))


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == "POST":
        userName = request.form.get('name')
        pwd = request.form.get('password')
        email = request.form.get('email')
        
        emailExsist = User.query.filter_by(email = email).first()
        userNameExsist = User.query.filter_by(name = userName).first()
        
        if emailExsist:
            error_message = f"This email ({email}) already exists."
            return render_template('signup.html', error=error_message)
        elif userNameExsist:
            error_message = f"This username ({userName}) already exists."
            return render_template('signup.html', error=error_message)
        elif len(pwd) < 5:
            error_message = "Your password is too short. It must be at least 8 characters long."
            return render_template('signup.html', error=error_message)
        else:
            newUser = User(name = userName, email = email, password = pwd)
            db.session.add(newUser)
            db.session.commit()
                  
        print(userName, pwd, email)
        session['username'] = userName  # Store the username in the session
        return redirect(url_for('index'))
    return render_template('signup.html')

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
    with app.app_context():
        db.create_all()
    app.run(debug = True)