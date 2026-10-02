# L'énoncé de l'exercice
''' Ecrire un programme permettant de prendre un nombre C de colonnes,
puis de réaliser la forme suivante : '''
# la solution corrigée de l'exercice
while True :
    nombre_colonnes = int(input('Veuillez entrer le nombre de colonnes : '))
    if nombre_colonnes < 3 :
        print('Erreur de saisie! le nombre de colonnes doit être supérieur ou égale à 3.')
        continue
    break
for ligne in range(nombre_colonnes) :
    for colonne in range(ligne+1) :
        print(end = '* ')
    print()
for ligne in range(nombre_colonnes-1) :
    for colonne in range(nombre_colonnes-1-ligne) :
        print(end = '* ')
    print()