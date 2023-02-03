from myproject import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
# By inheriting the UserMixin we get access to a lot of built-in attributes
# which we will be able to call in our views!
# is_authenticated()
# is_active()
# is_anonymous()
# get_id()


# The user_loader decorator allows flask-login to load the current user
# and grab their id.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

class Film(db.Model):
    __tablename__ = 'film'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    titel = db.Column(db.Text)
    jaartal = db.Column(db.Integer)
    regisseur_id = db.Column(db.Integer)
    youtube = db.Column(db.Text)
    
    def __init__(self, titel, jaartal, regisseur_id, youtube):
        self.titel = titel
        self.jaartal = jaartal
        self.regisseur_id = regisseur_id
        self.youtube = youtube
        
    def __repr__(self):
        return f"Film {self.titel} is uitgekomen in {self.jaartal} en is geregisseerd door {self.regisseur_id}, het id van deze film is: {self.id}"    

class Regisseur(db.Model):
    __tablename__ = 'regisseur'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    voornaam = db.Column(db.Text)
    achternaam = db.Column(db.Text)
    
    def __init__(self, voornaam, achternaam):
        self.voornaam = voornaam
        self.achternaam = achternaam

    def __repr__(self):
        return f"{self.voornaam} {self.achternaam}"    

class Acteur(db.Model):
    __tablename__ = 'acteur'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    voornaam = db.Column(db.Text)
    achternaam = db.Column(db.Text)

    def __init__(self, voornaam, achternaam):
        self.voornaam = voornaam
        self.achternaam = achternaam

    def __repr__(self):
        return f"{self.voornaam} {self.achternaam}"    

class Rol(db.Model):
    __tablename__ = 'rol'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    acteur_id = db.Column(db.Integer)
    film_id = db.Column(db.Integer)
    personage = db.Column(db.Text)

    def __init__(self, acteur_id, film_id, personage):
        self.acteur_id = acteur_id
        self.film_id = film_id
        self.personage = personage

    def __repr__(self):
        ...    