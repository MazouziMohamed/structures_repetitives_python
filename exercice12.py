# L'énoncé de l'exercice
''' Ecrire un programme qui détermine si un nombre est premier ou non
(rappel : un nombre premier n'est divisible que par 1 et par lui-même). '''
# la solution corrigée de l'exercice
n = int(input('Veuillez entrer un nombre entier : '))
if n < 2 :
    print(f"{n} n'est pas un nombre premier.")
else :
    for i in range(2, n//2 + 1) :
        if n%i == 0 :
            print(f"{n} n'est pas un nombre premier.")
            break
    else :
        print(f"{n} est un nombre premier.")