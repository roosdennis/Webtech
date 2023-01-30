from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

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
