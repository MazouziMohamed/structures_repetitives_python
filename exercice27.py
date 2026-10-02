# L'énoncé de l'exercice
''' Ecrire un programme permettant de prendre un nombre L, puis de
réaliser un « Parallélogramme d’étoiles » de la longueur L dans chaque coté. '''
# la solution corrigée de l'exercice
while True :
    nombre_lignes = int(input('Veuillez entrer le nombre de lignes : '))
    if nombre_lignes < 2 :
        print('Erreur de saisie! le nombre de lignes doit être supérieur ou égale à 2.')
        continue
    break
for ligne in range(nombre_lignes) :
    for colonne in range(nombre_lignes-ligne-1) :
        print(end = '  ')
    for etoile in range(nombre_lignes) :
        print(end = '* ')
    print()