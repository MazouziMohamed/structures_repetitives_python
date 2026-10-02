# L'énoncé de l'exercice
''' Ecrire un programme permettant à l'utilisateur d'entrer la longueur d'un
côté L (impaire) d'un carré puis le programme dessine la forme suivante : '''
# la solution corrigée de l'exercice
while True :
    longueur_cote = int(input('Veuillez entrer la longueur du côté du carré (impair): '))
    if longueur_cote < 3 or longueur_cote % 2 == 0:
        print('Erreur de saisie! la longueur du côté du carré doit être impair et supérieur ou égale à 3.')
        continue
    break
for ligne in range(longueur_cote) :
    for colonne in range(longueur_cote) :
        if ligne == 0 or ligne == longueur_cote-1 or ligne == colonne or colonne == 0 or colonne == longueur_cote-1 or colonne == longueur_cote-ligne-1 :
            print(end = '* ')
        else :
            print(end = '  ')
    print()