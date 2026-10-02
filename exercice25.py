# L'énoncé de l'exercice
''' Ecrire un programme permettant de prendre un nombre L de lignes et un
nombre C de colonnes, puis de réaliser un « cadre d’étoiles » de L lignes
par C colonnes. '''
# la solution corrigée de l'exercice
while True :
    nombre_lignes = int(input('Veuillez entrer le nombre de lignes : '))
    if nombre_lignes < 2 :
        print('Erreur de saisie! le nombre de lignes doit être supérieur ou égale à 2.')
        continue
    break
while True :
    nombre_colonnes = int(input('Veuillez entrer le nombre de colonnes : '))
    if nombre_colonnes < 2 :
        print('Erreur de saisie! le nombre de colonnes doit être supérieur ou égale à 2.')
        continue
    break
for ligne in range(nombre_lignes) :
    for colonne in range(nombre_colonnes) :
        if ligne == 0 or ligne == nombre_lignes-1 or colonne == 0 or colonne == nombre_colonnes-1 :
            print(end = '* ')
        else :
            print(end = '  ')
    print()