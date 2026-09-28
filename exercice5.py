# L'énoncé de l'exercice
''' Ecrire un programme qui calcule la factorielle d'un nombre entier.
Par exemple, la factorielle de 6, notée 6!, vaut 1 * 2 * 3 * 4 * 5 * 6. '''
# la solution corrigée de l'exercice
n = -1
while n < 0 :
    n = int(input('Veuillez entrer la valeur de n (n doit être positif ou nul) : '))
fact = 1
for i in range(2, n+1) :
    fact *= i
print(n, '! =', fact)