#coding:utf-8

#Creation d'une liste
inventaire = range(20)

# 1ere méthode
i = 0
while i < len(inventaire):
    print(inventaire[i])
    i += 1

print("2eme méthode :", "-" * 20)

# 2eme méthode
for valeur in inventaire:
    print(valeur)

# 3eme méthode
print("3eme méthode :", "-" * 20)
inventaire2 = ["épée", "bouclier", "potion", "armure", "casque", "bottes"]
for index, valeur in enumerate(inventaire2):
    print("Indice : {} -> Valeur : {}".format(index, valeur))