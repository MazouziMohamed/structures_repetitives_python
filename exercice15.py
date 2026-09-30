# L'énoncé de l'exercice
''' Ecrire un programme qui utilise un menu pouvant effectuer les
opérations suivantes: somme, soustraction, multiplication, division, le
reste d'une division entière et puissance.
Après avoir choisi l'opération, le programme doit demander à l'utilisateur
d'entrer les deux termes de l'opération, puis le programme affiche le
résultat.
Le programme doit également demander à l'utilisateur s'il souhaite
démarrer une autre opération ou quitter le programme. '''
# la solution corrigée de l'exercice
while True :
    print('+' + '-'*20 + ' MENU ' + '-'*20 + '+')
    print('1 : Somme')
    print('2 : soustraction')
    print('3 : Multiplication')
    print('4 : Division')
    print('5 : Reste de la division entière')
    print('6 : Puissance')
    print('0 : Quitter le programme')
    print('+' + '-'*46 + '+')
    choix = int(input('Veuillez entrer votre choix (1, 2, 3, 4, 5, 6, 0) : '))
    if choix == 0 :
        print("Au revoir !")
        break
    else :
        premier_terme = float(input("Veuillez entrer le premier terme : "))
        deuxieme_terme = float(input("Veuillez entrer le deuxième terme : "))
        if choix == 1 :
            print(f"{premier_terme} + {deuxieme_terme} = {premier_terme + deuxieme_terme}")
        elif choix == 2 :
            print(f"{premier_terme} - {deuxieme_terme} = {premier_terme - deuxieme_terme}")
        elif choix == 3 :
            print(f"{premier_terme} * {deuxieme_terme} = {premier_terme * deuxieme_terme}")
        elif choix == 4 :
            if deuxieme_terme != 0 :
                print(f"{premier_terme} / {deuxieme_terme} = {premier_terme / deuxieme_terme}")
            else :
                print('La division par 0 est impossible.')
        elif choix == 5 :
            if deuxieme_terme != 0 :
                print(f"{int(premier_terme)} % {int(deuxieme_terme)} = {int(premier_terme) % int(deuxieme_terme)}")
            else :
                print('La division par 0 est impossible.')
        elif choix == 6 :
            print(f"{premier_terme} ** {deuxieme_terme} = {premier_terme ** deuxieme_terme}")
        else :
            print('Erreur de saisie ! Votre choix doit être (1, 2, 3, 4, 5, 6, 0)')