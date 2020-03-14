from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email

class ProfileForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('M','Male'),('F','Female'),('Othr','Other')], validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    location = StringField('Location', validators=[DataRequired()])
    biography = TextAreaField('Biography', validators=[DataRequired()])
    profilepicture = FileField('File Upload', validators=[FileRequired(),FileAllowed(['jpg', 'png'])])
