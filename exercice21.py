# L'énoncé de l'exercice
''' Écrivez un programme qui permet de convertir un nombre décimal (entier naturel) en
binaire. '''
# la solution corrigée de l'exercice
nombre_decimal = int(input('Veuillez entrer un nombre entier naturel : '))
if nombre_decimal < 0:
    print(f"Voulez-vous dire {abs(nombre_decimal)} au lieu de {nombre_decimal} ? ")
    choix = input('oui ou non : ')
    if choix == 'oui' :
        nombre_decimal = abs(nombre_decimal)
    else :
        print("Je ne peux pas convertir un nombre négatif en binaire. Veuillez entrer un entier naturel lors d'un prochain essai.")
        exit()
temp = nombre_decimal
nombre_binaire = str(temp % 2)
temp //= 2
while temp != 0 :
    nombre_binaire = str(temp % 2) + nombre_binaire
    temp //= 2
print(f"{nombre_decimal} en binaire est : {nombre_binaire}")
