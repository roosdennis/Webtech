## Dit script enkel 1 x draaien!##
from models import db, Film, Regisseur, Acteur, Rol

#Creating Films
film1 = Film('Pinoccio', 1963, 1)
film2 =Film('Sneeuwwitje', 1987, 2)

#Creating Regiseurs
regisseur1 = Regisseur('Pietje', 'Puk')
regisseur2 = Regisseur('', '')

#Creating Acteurs
acteur1 = Acteur('','')
acteur2 = Acteur('','')

#Creating Rollen
rol1 = Rol()

#Add everything to the DB
db.session.add_all([film1,film2])
db.sesseion.commit()
