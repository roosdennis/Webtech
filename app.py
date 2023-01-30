from Project import app, db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from Project.models import User
from Project.forms import LoginForm, RegistrattionForm
from werkzeug.security import generate_password_hash, check_password_hash


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

