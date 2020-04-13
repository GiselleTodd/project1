"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
from datetime import date
from app import app
from app import db
from flask import render_template, request, redirect, url_for,flash
from flask_login import login_user, logout_user, current_user, login_required
from .forms import ProfileForm
from .models import UserProfile
from werkzeug.utils import secure_filename




###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/profile', methods=['GET','POST'])
def profile():
    form = ProfileForm()
    if form.validate_on_submit():

            f = request.files['profilepicture']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            url = f.filename
            user = UserProfile(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data, biography=form.biography.data, gender=form.gender.data, profilepicture=url, datejoined=format_date_joined())
            db.session.add(user)
            db.session.commit()

            flash('Profile has been saved', 'success')
            return redirect(url_for('vprofiles'))
    return render_template('profile.html', form=form)

@app.route('/profiles')
def vprofiles():
    profiles = UserProfile.query.filter_by().all()
    return render_template('profiles.html', profiles=profiles)

@app.route('/profile/<userid>')
def uprofile(userid):
    profile = UserProfile.query.filter_by(id = userid).first()
    return render_template('single.html', profile=profile)

#This function formats the date joined to present the Month and Year
def format_date_joined():
    return date.today().strftime("%B, %Y")


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
