# Dépendances

from ma_rue import rue, affiche
from rectangle import rectangle
from couleur_aleatoire import couleur_aleatoire
from math import pi
from random import randint

# Définitions

# Fonction portes()       

def portes(x,y):
    if randint(1,2) == 1:
         # Porte rectangulaire
        rectangle(x, y, 25, 35, couleur_aleatoire()  )
    else:
        # Porte arrondi
        couleur = couleur_aleatoire()
        rectangle(x, y, 25, 25, couleur  )
        rue.fill_style:couleur
        rue.fill_arc(x, y - 25, 12.5, pi, 0 )
        rue.line_width = 1
        rue.stroke_arc(x, y -25, 12.5, pi, 0)
        rue.fill_rect(x - 11, y -25, 25, 10 )
        
# Tests
affiche(rue)
for i in range(21) :
    portes(0 + i * 40,rue.height)