# L'énoncé de l'exercice
''' Écrire un programme qui vérifie si un nombre est palindrome ou non.
(rappel : Un nombre palindrome est un nombre qui peut se lire
indifféremment de gauche à droite ou de droite à gauche, Exemple 161). '''
# la solution corrigée de l'exercice
nombre_entier = int(input('Veuillez entrer un entier : '))
if abs(nombre_entier) < 10 :
    nombre_inverse = nombre_entier
else :
    temporaire = abs(nombre_entier)
    nombre_inverse = ""
    while temporaire != 0 :
        nombre_inverse += str(temporaire % 10)
        temporaire //= 10
    nombre_inverse = int(nombre_inverse)
    if nombre_entier < 0 :
        nombre_inverse *= -1
print(f"L'inverse de {nombre_entier} est : {nombre_inverse}")
if nombre_entier == nombre_inverse :
    print(f"{nombre_entier} est un nombre palindrome.")
else :
    print(f"{nombre_entier} n'est pas un nombre palindrome.")