from . import db

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    bio = db.Column(db.String(150))
    gender = db.Column(db.String(10))
    profilephoto = db.Column(db.String(255))

    def __init__(self, first_name, last_name, email, bio, gender, profilephoto):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.bio = bio
        self.gender = gender
        self.profilephoto = profilephoto

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
