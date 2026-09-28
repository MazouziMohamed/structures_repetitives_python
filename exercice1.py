# L'énoncé de l'exercice
''' Ecrire un programme qui demande un nombre de départ, et qui ensuite
affiche les dix nombres suivants en utilisant la boucle for.
Par exemple, si l'utilisateur entre le nombre 33, le programme affichera
les nombres de 34 à 43. '''
# la solution corrigée de l'exercice
nombre_depart = int(input('Veuillez entrer le nombre de départ : '))
for i in range(nombre_depart+1, nombre_depart+11) :
    print(i, end = '\t')