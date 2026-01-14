#coding:utf-8

#creatin d'une liste 
inventaire = ["épée", "bouclier", "potion", "armure", "casque", "bottes"]

print(inventaire[1])  # Affiche "bouclier"

print(inventaire[:]) # Affiche toute la liste

print(inventaire[1:3]) # Affiche de l'index 1 à 2 (3 non inclus)

print(inventaire[-1])  # Affiche le dernier élément "bottes"



inventaire2 = ["épée", "bouclier", "potion", "armure", "casque", "bottes"]

inventaire2[:] = ["autre chose"] * 2 # Remplace tout le contenu de la liste par deux éléments "autre chose"
print(inventaire2[:])

inventaire2[:] = ["autre chose"] * len(inventaire2) # Remplace tout le contenu de la liste par autant d'éléments "autre chose" que d'éléments initiaux
print(inventaire2[:])