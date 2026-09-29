# L'énoncé de l'exercice
''' A la naissance de Amal, son grand-père Ali, lui ouvre un compte bancaire.
Ensuite, à chaque anniversaire, le grand père de Amal verse sur son compte
500 dh, auxquels il ajoute le triple de l'âge de Amal. Par exemple,
lorsqu'elle a quatre ans, il lui verse 512 dh. Ecrire un programme
qui permet de déterminer quelle somme aura Amal lors
de son nième anniversaire. '''
# la solution corrigée de l'exercice
age_amal = -1
while age_amal < 0 :
    age_amal = int(input("Veuillez entrer l'âge d'amal : "))
compte_bancaire_amal = 0
for i in range(1, age_amal + 1) :
    compte_bancaire_amal += 500 + i * 3
print('Quand Amal aura', age_amal, 'ans, elle aura', compte_bancaire_amal, 'DH sur son compte bancaire.')