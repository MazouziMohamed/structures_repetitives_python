# L'énoncé de l'exercice
''' Ecrire un programme qui demande un nombre de départ, et qui ensuite
affiche les dix nombres suivants en utilisant la boucle while.
Par exemple, si l'utilisateur entre le nombre 33, le programme affichera
les nombres de 34 à 43. '''
# la solution corrigée de l'exercice
nombre_depart = int(input('Veuillez entrer le nombre de départ : '))
i = nombre_depart + 1
while i <= nombre_depart + 10 :
    print(i, end = '\t')
    i += 1