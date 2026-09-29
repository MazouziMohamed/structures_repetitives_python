# L'énoncé de l'exercice
''' La population de la ville Marrakech est de 1,000,000 d'habitants
et elle augmente de 50,000 habitants par an. Celle de la ville Agadir
est de 500,000 habitants et elle augmente de 8% par an.
Ecrire un programme permettant de déterminer dans combien d'années
la population de la ville Agadir dépassera celle de la ville Marrakech. '''
# la solution corrigée de l'exercice
population_marrakech, population_agadir, nombre_annees = 1000000, 500000, 0
while population_agadir <= population_marrakech :
    population_marrakech += 50000
    population_agadir += population_agadir * 0.08
    nombre_annees += 1
print(f"La population de la ville agadir dépassera celle de la ville marrakech après {nombre_annees} ans.")
