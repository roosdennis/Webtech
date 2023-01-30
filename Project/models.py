import os
from forms import  AddFilmForm , DelFilmForm, AddRegisseurForm, AddActeurForm, LoginForm, RegistrationForm
from flask import Flask, render_template, url_for, redirect, request, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#############################

#loginstuff

#############################


from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

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
    regisseurs = Film.query.all()
    return render_template('listregisseurs.html', regisseurs = regisseurs)

# @app.route('/delregisseur', methods=['GET', 'POST'])
# def del_regisseur():
#     form = DelRegisseurForm()
#     if form.validate_on_submit():
#         id = form.id.data
#         regisseur = Regisseur.query.get(id)
#         db.session.delete(regisseur)
#         db.session.commit()
#         return redirect(url_for('list_regisseur'))
#     return render_template('/delregisseur.html', form=form)        


##########################################

           #register&login

##########################################

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welkom')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/logout')
@login_required
def logout():
    logout_user
    flash("u bent uitgelogd!")
    return redirect(url_for('home'))


@app.route('/login' ,methods=['GET','POST'])
def loginn():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not none:

            login_user(user)
            flash('succesvol ingelogd!')

            next = request.args.get('next')

            if next == Nnone or not next[0]=='/':

                next = url_for('welcome_user')
            return redirect(next)
        
        return render_template('login.html',form=form)


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrattionForm()

    if form.validate_on_submit():
        user = User(email=foorm.email.data,
                    username=form.username.data,
                    password = form.password.data)

        db.session.add(user)
        db.session.commit()
        flash("bedannkt voor hett regeristreren!")
        return rederect(url_for('login'))
    return render_template('register.html',form=form)

##########################################

           #endregister&login

##########################################


##########################################

        # Start de applicatie

##########################################



if __name__ == '__main__':
    app.run(debug=True)    

