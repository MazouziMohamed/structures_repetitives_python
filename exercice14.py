# L'énoncé de l'exercice
''' Ce jeu est très simple. L'ordinateur tire un nombre au hasard entre 1 et 30 et
vous avez cinq essais pour le trouver. Après chaque tentative, l'ordinateur
vous dira si le nombre que vous avez proposé est trop grand, trop petit, ou si
vous avez trouvé le bon nombre. '''
# la solution corrigée de l'exercice
from random import randint
ordinateur = randint(1, 30)
nombres_tentatives = 1
print("J'ai choisi un nombre entre 1 et 30, A vous de le devinir en 5 tentatives au maximum.")
while nombres_tentatives <= 5 :
    print('Quel est le nombre ? ', end = '')
    utilisateur = int(input())
    if utilisateur == ordinateur :
        print(f"Bravo! vous avez trouve {ordinateur} en {nombres_tentatives} essais")
        break
    else :
        print('------------------------------')
        if utilisateur < ordinateur :
            print("C'est plus !")
        else :
            print("C'est moins !")
        print('------------------------------')
    nombres_tentatives += 1
else :
    print(f" Oups! vous avez dépassé les 5 tentatives autorisées, le nombre était : {ordinateur}")