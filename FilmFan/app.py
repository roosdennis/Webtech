from myproject import app, db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user,login_required,logout_user
from myproject.models import User, Film, Regisseur, Acteur, Rol
from myproject.forms import LoginForm, RegistrationForm, AddFilmForm, AddRegisseurForm, AddActeurForm, DelFilmForm, DelRegisseurForm, DelActeurForm
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3



@app.route('/')
def index():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Logged in successfully.')
            next = request.args.get('next')
            if next == None or not next[0]=='/':
                next = url_for('welcome_user')
            return redirect(next)
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/addfilm', methods=['GET', 'POST'])
def add_film():
    form = AddFilmForm()
    if form.validate_on_submit():
        titel = form.titel.data
        jaartal = form.jaartal.data
        regisseur = form.regisseur.data
        youtube = form.youtube.data
        new_film = Film(titel, jaartal, regisseur, youtube)
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

@app.route('/addacteur', methods=['GET', 'POST'])
def add_acteur():
    form = AddActeurForm()
    if form.validate_on_submit():
        voornaam = form.voornaam.data
        achternaam = form.achternaam.data
        new_acteur = Acteur(voornaam, achternaam)
        db.session.add(new_acteur)
        db.session.commit()
        return redirect(url_for('list_acteurs'))
    return render_template('addacteur.html', form=form)

@app.route('/lisacteurs')
def list_acteurs():
    acteurs = Acteur.query.all()
    return render_template('listacteurs.html', acteurs = acteurs)

@app.route('/delacteur', methods=['GET', 'POST'])
def del_acteur():
    form = DelActeurForm()
    if form.validate_on_submit():
        id = form.id.data
        acteur = Acteur.query.get(id)
        db.session.delete(acteur)
        db.session.commit()
        return redirect(url_for('list_acteurs'))
    return render_template('/delacteur.html', form=form)

@app.route('/films/<film_naam>')
def retrieve_video_link_from_database(film_naam):
    conn = sqlite3.connect("data.sqlite")
    c = conn.cursor()
    c.execute("SELECT youtube FROM  film WHERE titel=?",(film_naam))
    video_link = c.fetchone()[0]
    conn.close()
    return video_link

def film_pagina(film_naam):
    video_link = retrieve_video_link_from_database(film_naam)
    return render_template('film.html', film_naam=film_naam, video_link=video_link)
    return render_template('film.html', film_naam=film_naam)

# @app.route('/films/turksfruit')
# def turksfruit():
#     return render_template('films/turksfruit.html')

# @app.route('/films/soldaatvanoranje')
# def soldaatvanoranje():
#     return render_template('films/soldaatvanoranje.html')

# @app.route('/films/spetters')
# def spetters():
#     return render_template('films/spetters.html')

# @app.route('/films/zwartboek')
# def zwartboek():
#     return render_template('films/zwartboek.html')

@app.route('/regisseurs/<regisseur_naam>')
def regisseur_pagina(regisseur_naam):
    return render_template('regisseur.html', regisseur_naam=regisseur_naam)

@app.route('/acteurs/<acteur_naam>')
def acteur_pagina(acteur_naam):
    return render_template('acteur.html', acteur_naam=acteur_naam)

if __name__ == '__main__':
    app.run(debug=True)
