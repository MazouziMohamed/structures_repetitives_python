# L'énoncé de l'exercice
''' Ecrire un programme qui demande à l'utilisateur de taper un entier
n (rang) et qui calcule le terme Un de la suite U défini par :
U0 = 6
Un+1 = 4Un + 10 '''
# la solution corrigée de l'exercice
n = -1
while n < 0 :
    n = int(input('Veuillez entrer la valeur de n (n est un entier naturel) : '))
Un = 6
for i in range(1, n+1) :
    Un = 4*Un + 10
print(f"U{n} = {Un}")
