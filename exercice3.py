# L'énoncé de l'exercice
''' Ecrire un programme qui calcule et affiche la somme :
S = 1/1 + 1/2 + 1/3 + ... + 1/n '''
# la solution corrigée de l'exercice
n = 0
while n < 1 :
    n = int(input('Veuillez entrer la valeur de n (n est un entier naturel non nul) : '))
somme = 0
for i in range(1, n+1) :
    somme += 1 / i
print(f"La somme est : {somme}")
