import os
from forms import  AddFilmForm , DelFilmForm, AddRegisseurForm, DelRegisseurForm, AddActeurForm, DelActeurForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#############################

#loginstuff

#############################


from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager

login_manager = LoginManager() #create instance loginmanager






#####

#end login stuff

#####

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
        return f"Film {self.titel} is uitgekomen in {self.jaartal} en is geregisseerd door {self.regisseur_id}, het id van deze film is: {self.id}"    

class Regisseur(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    voornaam = db.Column(db.Text)
    achternaam = db.Column(db.Text)
    # film_id = db.Column(db.Integer, db.ForeignKey('Film.id'))

    def __init__(self, voornaam, achternaam):
        self.voornaam = voornaam
        self.achternaam = achternaam

    def __repr__(self):
        return f"Regisseur {self.voornaam} {self.achternaam} heeft het volgende ID: {self.id}"   

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


#####
#Loginn user class
####

class User(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(64), unique = True,index=True)
    username = db.Column(db.String(64), unique= True, index=True)
    password_hash = db.column(db.String(128))

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password.hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

#####
#END Loginn user class
####

##########################################

        # ROUTERINGEN

##########################################

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/addfilm', methods=['GET', 'POST'])
def add_film():
    form = AddFilmForm()
    if form.validate_on_submit():
        titel = form.titel.data
        jaartal = form.jaartal.data
        regisseur = form.regisseur.data
        new_film = Film(titel, jaartal, regisseur)
        db.session.add(new_film)
        db.session.commit()
        return redirect(url_for('list_films'))
    return render_template('addfilm.html', form=form)

@app.route('/listfilms')
def list_films():
    films = Film.query.all()
    return render_template('listfilms.html', films = films)

@app.route('/delfilm', methods=['GET', 'POST'])
def del_film():
    form = DelFilmForm()
    if form.validate_on_submit():
        id = form.id.data
        film = Film.query.get(id)
        db.session.delete(film)
        db.session.commit()
        return redirect(url_for('list_films'))
    return render_template('/delfilm.html', form=form)

@app.route('/addregisseur', methods=['GET', 'POST'])
def add_regisseur():
    form = AddRegisseurForm()
    if form.validate_on_submit():
        voornaam = form.voornaam.data
        achternaam = form.achternaam.data
        new_regisseur = Regisseur(voornaam, achternaam)
        db.session.add(new_regisseur)
        db.session.commit()
        return redirect(url_for('list_regisseurs'))
    return render_template('addregisseur.html', form=form)

@app.route('/listregisseurs')
def list_regisseurs():
    regisseurs = Regisseur.query.all()
    return render_template('listregisseurs.html', regisseurs = regisseurs)

@app.route('/delregisseur', methods=['GET', 'POST'])
def del_regisseur():
    form = DelRegisseurForm()
    if form.validate_on_submit():
        id = form.id.data
        regisseur = Regisseur.query.get(id)
        db.session.delete(regisseur)
        db.session.commit()
        return redirect(url_for('list_regisseurs'))
    return render_template('/delregisseur.html', form=form)        

##########################################

        # Start de applicatie

##########################################



if __name__ == '__main__':
    app.run(debug=True)    

