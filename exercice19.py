# L'énoncé de l'exercice
''' Ecrire un programme qui calcule le pgcd de deux nombres entiers positifs. '''
# la solution corrigée de l'exercice
premier_entier = int(input('Veuillez entrer le premier entier : '))
deuxieme_entier = int(input('Veuillez entrer le deuxième entier : '))
if premier_entier == deuxieme_entier == 0 :
    print("PGCD(0 ; 0) non défini")
    exit()
elif premier_entier == 0 :
    pgcd = abs(deuxieme_entier)
elif deuxieme_entier == 0 :
    pgcd = abs(premier_entier)
else :
    if premier_entier == 1 :
        pgcd = abs(premier_entier)
    elif deuxieme_entier == 1 :
        pgcd = abs(deuxieme_entier)
    else :
        temp1, pgcd, temp2 = abs(premier_entier), abs(premier_entier), abs(deuxieme_entier)
        while temp1 != 0 :
            temp1 = pgcd % temp2
            pgcd = temp2
            temp2 = temp1
print(f"PGCD({premier_entier} ; {deuxieme_entier}) = {pgcd}")
