# L'énoncé de l'exercice
''' Créer un programme qui permet d'automatiser le jeu Pierre, Feuille,
Ciseaux. '''
# la solution corrigée de l'exercice
from random import randint
score_utilisateur = score_ordinateur = score_egalites = 0
while True :
    ordinateur = randint(1, 3)
    if ordinateur == 1 :
        ordinateur = 'p' # p : pierre
    elif ordinateur == 2 :
        ordinateur = 'f' # f : feuille
    else :
        ordinateur = 'c' # c : ciseaux 
    utilisateur = input('À vous de jouer : Pierre(p), Feuille(f) ou Ciseaux(c) ?')
    if utilisateur == 'p' :
        if ordinateur == 'p' : score_egalites += 1
        elif ordinateur == 'f' : score_ordinateur += 1
        else : score_utilisateur += 1
    elif utilisateur == 'f' :
        if ordinateur == 'p' : score_utilisateur += 1
        elif ordinateur == 'f' : score_egalites += 1
        else : score_ordinateur += 1
    elif utilisateur == 'c' :
        if ordinateur == 'p' : score_ordinateur += 1
        elif ordinateur == 'f' : score_utilisateur += 1
        else : score_egalites += 1
    else :
        print('Choix invalide, veuillez réessayer.')
        continue
    print('+' + '-'*30 + '+')
    print(f"Utilisateur : {score_utilisateur}")
    print(f"Égalités : {score_egalites}")
    print(f"Ordinateur : {score_ordinateur}")
    print('+' + '-'*30 + '+')
    choix = input(("Souhaitez-vous continuer le jeu ? (oui ou non) : "))
    if choix == 'oui' :
        continue
    else :
        break