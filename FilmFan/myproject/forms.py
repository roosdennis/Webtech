from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
import email_validator


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self, field):
       if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is taken!')

class AddFilmForm(FlaskForm):
    titel = StringField('Titel van de Film:')
    jaartal = IntegerField('In welk jaar kwam de film uit?')
    regisseur = IntegerField('Welke Regisseur heeft de film geregisseerd? (ID)')
    submit = SubmitField('Voeg de Film toe')

class AddRegisseurForm(FlaskForm):
    voornaam = StringField('Voornaam van de Regisseur:')
    achternaam = StringField('Achternaam van de Regiseur')
    submit = SubmitField('Voeg de Regiseur toe')

class AddActeurForm(FlaskForm):
    voornaam = StringField('Voornaam van de Acteur:')
    achternaam = StringField('Achternaam van de Acteur')
    submit = SubmitField('Voeg de Acteur toe')

class DelFilmForm(FlaskForm):
    id = IntegerField('Welke Film wil je verwijderen? (ID):')
    submit = SubmitField('Verwijder Film')

class DelRegisseurForm(FlaskForm):
    id = IntegerField('Welke Regisseur wil je verwijderen? (ID):')
    submit = SubmitField('Verwijder Regisseur')

class DelActeurForm(FlaskForm):
    id = IntegerField('Welke Acteur wil je verwijderen? (ID):')
    submit = SubmitField('Verwijder Acteur')    