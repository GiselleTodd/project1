from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "SUBJECTTTT2CHA@NGE"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://rfgrorretkdxcd:1a882fb4cef3e67c2ab85f24c906434832190334004b9b111ae86ee6da82b7ec@ec2-34-225-82-212.compute-1.amazonaws.com:5432/d7ru2pa69qs41"
app.config['UPLOAD_FOLDER'] = './app/static/images'

db = SQLAlchemy(app)

app.config
from app import views
