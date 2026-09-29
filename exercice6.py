# L'énoncé de l'exercice
''' Ecrire un programme qui demande à l'utilisateur de taper un entier naturel n,
puis qui calcule la somme des carrés des n premiers entiers impairs.
Par exemple, si n = 5 le résultat est : 1^2 + 3^2 + 5^2 + 7^2 + 9^2 = 165. '''
# la solution corrigée de l'exercice
n = -1
while n < 0 :
    n = int(input('Veuillez entrer la valeur de n (n est un entier naturel) : '))
somme = 1
if n <= 1:
    print(f"La somme de carré de {n} premier entier impair est : {n}")
else :
    for i in range(1, n*2, 2) :
        somme += i **2
    print(f"La somme des carrés des {n} premiers entiers impairs est : {somme}")
