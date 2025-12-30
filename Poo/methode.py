#coding:utf-8

"""
methode           : fonction lié à une instance (objet)
methode de classe : fonction liée à une classe
methode statique  : fonction indépendante de l'instance et de la classe
"""

class Humain:
    adresse = "Inconnu"
    def __init__(self, c_nom, c_age):
        self.nom = c_nom
        self.age = c_age
    
    def parler(self, message): #self fait référence à l'instance
        print(f"{self.nom} dit: {message}")

    def changer_adresse(cls, nouvelle_adresse): #cls fait référence à la classe
        Humain.adresse = nouvelle_adresse

    ca = classmethod(changer_adresse)

    def definition():
        print("Un humain est un être vivant appartenant à l'espece Homo sapience")

    d = staticmethod(definition)


print("Lancement du programme...")

h1 = Humain("Vivien", 30)
h1.parler("Bonjour tout le monde!")

print(f"Adresse avant changement: {h1.adresse}")

Humain.ca("Paris")

print(f"Adresse après changement: {h1.adresse}")

Humain.d()