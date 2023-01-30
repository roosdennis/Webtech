import os
from forms import  AddFilmForm , DelFilmForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

##########################################

        # SQL DATABASE
        
##########################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

class Film(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    titel = db.Column(db.Text)
    jaartal = db.Column(db.Integer)
    regisseur_id = db.Column(db.Integer)
    #regiseur_id = db.Relationship('Regisseur', backref="puppy", lazy="dynamic")
    

    def __init__(self, titel, jaartal, regisseur_id):
        self.titel = titel
        self.jaartal = jaartal
        self.regisseur_id = regisseur_id
        

    def __repr__(self):
        return f"Film {self.titel} is uitgekomen in {self.jaartal} en is geregisseerd door {self.regisseur_id}"    

class Regisseur(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    voornaam = db.Column(db.Text)
    achternaam = db.Column(db.Text)
    # film_id = db.Column(db.Integer, db.ForeignKey('Film.id'))

    def __init__(self, voornaam, achternaam):
        self.voornaam = voornaam
        self.achternaam = achternaam

    def __repr__(self):
        ...    

class Acteur(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    voornaam = db.Column(db.Text)
    achternaam = db.Column(db.Text)

    def __init__(self, voornaam, achternaam):
        self.voornaam = voornaam
        self.achternaam = achternaam

    def __repr__(self):
        ...

class Rol(db.Model):
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

##########################################

        # ROUTERINGEN

##########################################

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)    

