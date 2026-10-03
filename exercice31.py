# L'énoncé de l'exercice
''' Ecrire un programme permettant de prendre un nombre de lignes, puis
de réaliser le diamant suivant : '''
# la solution corrigée de l'exercice
while True :
    nombre_lignes = int(input('Veuillez entrer le nombre de lignes : '))
    if nombre_lignes < 2 :
        print('Erreur de saisie! le nombre de lignes doit être supérieur ou égale à 2.')
        continue
    break
temp_espace, temp_etoile = nombre_lignes - 1, 1
for ligne in range(2*nombre_lignes - 1) :
    for espace in range(temp_espace) :
        print(end = '  ')
    for etoile in range(2*temp_etoile-1) :
        print(end = "* ")
    if (ligne+1) < nombre_lignes : 
        temp_espace -= 1
        temp_etoile += 1
    else : 
        temp_espace += 1
        temp_etoile -= 1
    print()