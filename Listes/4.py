#coding:utf-8

inventaire = []
print(inventaire[:])  # Affiche []
inventaire.append("épée")
print(inventaire[:])  # Affiche ["épée"]
inventaire.append("bouclier")
print(inventaire[:])  # Affiche ["épée", "bouclier"]
inventaire.append("potion")
print(inventaire[:])  # Affiche ["épée", "bouclier", "potion"]


inventaire.insert(1, "armure")
print(inventaire[:])  # Affiche ["épée", "armure", "bouclier", "potion"]


inventaire.remove("bouclier")
print(inventaire[:])  # Affiche ["épée", "armure", "potion"]

del inventaire[0] 
print(inventaire[:])  # Affiche ["armure", "potion"]

inventaire.sort()
print(inventaire[:]) 

inventaire.reverse()
print(inventaire[:])