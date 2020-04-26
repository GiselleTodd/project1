from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "SUBJECTTTT2CHA@NGE"
app.config['SQLALCHEMY_DATABASE_URI'] = ""
app.config['UPLOAD_FOLDER'] = './app/static/images'

db = SQLAlchemy(app)

app.config
from app import views
