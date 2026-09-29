# L'énoncé de l'exercice
# Écrire un programme qui demande à l'utilisateur de taper un entier naturel n (n >= 0, donc l'utilisateur peut entrer 0, 1 ou plus), 
# jusqu'à ce que la réponse convienne, puis qui calcule et affiche le terme Fn de la suite de Fibonacci.
# La suite de Fibonacci est définie comme suite :
# F0 = 0
# F1 = 1
# Fn = Fn_1 + Fn_2
# la solution corrigée de l'exercice
n = -1
while n < 0 :
    n = int(input('Veuillez entrer la valeur de n (n est un entier naturel) : '))
Fn_2, Fn_1 = 0,1
if n < 2 :
    print(f"F{n} = {n}")
else :
    for i in range(2, n+1) :
        Fn = Fn_1 + Fn_2
        Fn_2 = Fn_1
        Fn_1 = Fn
    print(f"F{n} = {Fn}")
