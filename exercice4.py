# L'énoncé de l'exercice
''' Ecrire un programme qui calcule et affiche la somme :
S = 1 + 10 + 100 + ... + 10^n '''
# la solution corrigée de l'exercice
n = -1
while n < 0 :
    n = int(input('Veuillez entrer la valeur de n (n est un entier naturel) : '))
somme = 1
for i in range(1, n+1) :
    somme += 10 ** i
print(f"La somme est : {somme}")
