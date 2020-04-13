from . import db



class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer(), primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    biography = db.Column(db.String(150))
    gender = db.Column(db.String(10))
    location = db.Column(db.String(80))
    profilepicture= db.Column(db.String(255))
    datejoined = db.Column(db.String(20))

    def __init__(self, firstname, lastname, email, biography, gender, location, profilepicture, datejoined):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.biography = biography
        self.gender = gender
        self.profilepicture = profilepicture
        self.datejoined = datejoined
        self.location = location

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.first_name)
