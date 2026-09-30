# L'énoncé de l'exercice
''' Écrire un programme qui demande à l'utilisateur de saisir le nombre
d'équipes participant à un championnat, puis le programme affiche la
liste des matchs à domicile et à l'extérieur pour ce championnat. '''
# la solution corrigée de l'exercice
while True :
    nombre_equipes = int(input("Veuillez entrer le nombre d'équipes (le nombre d'équipes doit être supérieur ou égale à 2): "))
    if nombre_equipes < 2 :
        continue
    break
for equipe_domicile in range(1, nombre_equipes + 1) :
    print(f"------------ Pour l'équipe {equipe_domicile} ------------")
    for equipe_exterieur in range(1, nombre_equipes + 1) :
        if equipe_exterieur != equipe_domicile :
            print(f"équipe {equipe_domicile} VS équipe {equipe_exterieur}")