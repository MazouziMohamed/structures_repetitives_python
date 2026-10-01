# L'énoncé de l'exercice
''' Écrire un programme qui vérifie si un nombre est parfait ou non.
Un nombre est dit parfait s'il est égal à la somme de ses diviseurs
propres (diviseurs de ce nombre autres que lui-même). '''
# la solution corrigée de l'exercice
nombre_entier= int(input('Veuillez entrer un nombre entier : '))
somme_diviseurs_propres = 1
for i in range(2, nombre_entier//2 + 1) :
    if nombre_entier % i == 0 :
        somme_diviseurs_propres += i
if nombre_entier == somme_diviseurs_propres :
    print(f"{nombre_entier} est un nombre parfait.")
else :
    print(f"{nombre_entier} n'est pas un nombre parfait.")