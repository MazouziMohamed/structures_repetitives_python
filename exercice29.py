# L'énoncé de l'exercice
''' Ecrire un programme permettant de prendre un nombre L de lignes, puis
de réaliser triangle suivant : '''
# la solution corrigée de l'exercice
while True :
    nombre_lignes = int(input('Veuillez entrer le nombre de lignes : '))
    if nombre_lignes < 2 :
        print('Erreur de saisie! le nombre de lignes doit être supérieur ou égale à 2.')
        continue
    break
for ligne in range(nombre_lignes) :
    for colonne in range(2*nombre_lignes-1) :
        if (ligne == nombre_lignes-1 and colonne%2 == 0) or colonne == nombre_lignes-ligne-1 or colonne == nombre_lignes+ligne-1 :
            print(end = '* ')
        else :
            print(end='  ')
    print()