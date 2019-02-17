from flask import Flask
from flask_mail import Mail
app = Flask(__name__)
app.config['SECRET_KEY'] = 'jonno'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525' # (or try 2525)
app.config['MAIL_USERNAME'] = 'd8d8727929223a'
app.config['MAIL_PASSWORD'] = '21461frun014a25c3'
mail = Mail(app)
from app import views