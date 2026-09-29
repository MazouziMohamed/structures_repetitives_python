# L'énoncé de l'exercice
''' Ecrire un programme qui affiche les diviseurs positifs
d'un entier positif. '''
# la solution corrigée de l'exercice
nombre_naturel = -1
while nombre_naturel < 0 :
    nombre_naturel = int(input('Veuillez entrer un entier naturel: '))
if nombre_naturel != 0 :
    if nombre_naturel == 1 :
        print('1 admet un seul diviseur positif : lui-même.')
    else :
        print(f"Les diviseurs positifs de {nombre_naturel} sont : [1, ", end = '')
        for i in range(2, nombre_naturel // 2 + 1) :
            if nombre_naturel % i == 0 :
                print(i, end = ', ')
        print(f"{nombre_naturel}]")
else :
    print('Tout nombre entier est un diviseur de zéro.')