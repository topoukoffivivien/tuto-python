#coding:utf-8

"""
classe    : plan de conception pour créer des objets
bojet     : instance d'une classe
Attribut  : caractéristiques d'un objet
"""
class Humain:
    humains_crees = 0
    def __init__(self, c_nom, c_age):
        print("Creation d'un humain")
        self.nom = c_nom
        self.age = c_age
        Humain.humains_crees += 1


print("Lancement du programme...")

h1 = Humain("Alice", 25)
print(f"Nom: {h1.nom}, Âge: {h1.age}")
print(f"Nombre d'humains créés: {Humain.humains_crees}")

h2 = Humain("Bob", 30)
print(f"Nom: {h2.nom}, Âge: {h2.age}")
print(f"Nombre d'humains créés: {Humain.humains_crees}")