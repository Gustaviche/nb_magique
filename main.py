import random

"""nb = 0
vie = nb_vie
while nb != nb_magique and vie > 0:
  print("Il vous reste", vie,"vies.")
  nb = demander_nombre(nb_min, nb_max)
  if nb > nb_magique:
    print("C'est plus petit.")
    vie -=1
  elif nb < nb_magique:
    print("C'est plus grand.")
    vie -= 1
  else:
    print("Bravo ! C'est gagné !")
    break 

demander_nombre(nb_min, nb_max)

if vie == 0:
  print(f"Vous avez perdu. Le nombre magique était {nb_magique}.")"""

nb_min = 1
nb_max = 10
nb_magique = random.randint(nb_min, nb_max)
nb_vie = 4

def demander_nombre(nb_min, nb_max):
  nb_int = 0
  while nb_int == 0:
    nb_str = input(f"Quel est le nombre magique entre {nb_min} et {nb_max} ? ")
    try:
      nb_int = int(nb_str)
    except:
      print("On veut un chiffre.")
    else:
      if nb_int < nb_min or nb_int > nb_max:
        print(f"le nombre doit être entre {nb_min} et {nb_max}")
        nb_int = 0
    return nb_int

gagne = False
for i in range(0, nb_vie):
  vie = nb_vie-i
  print("Il vous reste", vie,"vies.")
  nb = demander_nombre(nb_min, nb_max)
  if nb > nb_magique:
    print("C'est plus petit.")
  elif nb < nb_magique:
    print("C'est plus grand.")
  else:
    print("Bravo ! C'est gagné !")
    gagne = True
    break 

demander_nombre(nb_min, nb_max)

if not gagne:
  print(f"Vous avez perdu. Le nombre magique était {nb_magique}.")