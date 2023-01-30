## Dit script enkel 1 x draaien!##
from models import db, Film, Regisseur, Acteur

#Creating Films
filmnaam1 = Film('Pinokkio', 1933, 'Walt Disney','https://youtube.com', 'https://picture.com/pinokkio', 'https:wikipedia.com/pinokkio')
filmnaam2 = Film('Sneewwitje', 1963, 'Walt Disney','https://youtube.com', 'https://picture.com/sneeuwwitje', 'https:wikipedia.com/pinokkio')

#Creating Regiseurs
regisseur1
#Creating Acteurs
#Creating Rollen


#Add everything to the DB
db.session.add_all([filmnaam1,filmnaam2])
db.sesseion.commit()
