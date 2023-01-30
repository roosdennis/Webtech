from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddFilmForm(FlaskForm):
    titel = StringField('Titel van de Film:')
    jaartal = IntegerField('In welk jaar kwam de film uit?')
    regisseur = IntegerField('Welke Regisseur heeft de film geregisseerd? (ID)')
    submit = SubmitField('Voeg de Film toe')

class DelFilmForm(FlaskForm):

    id = IntegerField('Welke Film wil je verwijderen? (ID):')
    submit = SubmitField('Verwijder Film')
