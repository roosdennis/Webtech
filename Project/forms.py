from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError



class AddFilmForm(FlaskForm):
    titel = StringField('Titel van de Film:')
    jaartal = IntegerField('In welk jaar kwam de film uit?')
    regisseur = IntegerField('Welke Regisseur heeft de film geregisseerd? (ID)')
    submit = SubmitField('Voeg de Film toe')

class AddRegisseurForm(FlaskForm):
    voornaam = StringField('Voornaam van de Regisseur:')
    achternaam = IntegerField('Achternaam van de Regiseur')
    submit = SubmitField('Voeg de Regiseur toe')

class AddActeurForm(FlaskForm):
    voornaam = StringField('Voornaam van de Acteur:')
    achternaam = IntegerField('Achternaam van de Acteur')
    submit = SubmitField('Voeg de Acteur toe')

class DelFilmForm(FlaskForm):

    id = IntegerField('Welke Film wil je verwijderen? (ID):')
    submit = SubmitField('Verwijder Film')


class LoginForm(FlaskForm):
#    email = StringField('Email',validators=[DataRequired(),Email()])
    Password = PasswordField('Password', validators=[DataRequired()])
    Submit = SubmitField("log in")

class RegistrationForm(FlaskForm):
    # email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Gebruikersnaam', validators=[DataRequired()])
    password = PasswordField('Wachtwoord', validators=[DataRequired(),EqualTo('pass_confirm',message='Wachtwoorden komen niet overeen')])
    pass_confirm = PasswordField('herhaal Wachtwoord',validators=[DataRequired()])
    submit = SubmitField('registreer!')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Dit email adress is al in gebruik!')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('deze Gebruikersnaam is al in gebruik.')