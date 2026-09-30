# L'énoncé de l'exercice
''' Écrire un programme qui demande à l'utilisateur d'entrer un entier, puis
le programme compte et affiche le nombre de chiffres qui composent cet
entier. '''
# la solution corrigée de l'exercice
nombre_entier = int(input('Veuillez entrer un entier : '))
if abs(nombre_entier) < 10 :
    print(f"{nombre_entier} est composé de 1 chiffre.")
else :
    nombre_chiffres = 1
    temporaire = abs(nombre_entier) // 10
    while temporaire != 0 :
        nombre_chiffres += 1
        temporaire //= 10
    print(f"{nombre_entier} est composé de {nombre_chiffres} chiffres.")