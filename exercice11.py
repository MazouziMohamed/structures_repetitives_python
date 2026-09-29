# L'énoncé de l'exercice
# Écrire un programme qui demande à l'utilisateur de taper un entier naturel n (n >= 0, donc l'utilisateur peut entrer 0, 1 ou plus), 
# jusqu'à ce que la réponse convienne, puis qui calcule et affiche le terme Fn de la suite de Fibonacci.
# La suite de Fibonacci est définie comme suite :
# F0 = 0
# F1 = 1
# Fn+2 = Fn+1 + Fn
# la solution corrigée de l'exercice
n = -1
while n < 0 :
    n = int(input('Veuillez entrer un entier naturel n : '))
Fn, Fn_1 = 0,1 # Remarque : Fn_1 représente Fn+1
if n < 2 :
    print('F', n, ' = ', n, sep = '')
else :
    for i in range(2, n+1) :
        Fn_2 = Fn_1 + Fn
        Fn = Fn_1
        Fn_1 = Fn_2
    print('F', n, ' = ', Fn_2, sep = '')