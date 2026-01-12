#coding:utf-8



"""
Fonctions utiles :
    - issubclass(<classe_fille>, <classe_mere>) : retourne True si la classe_fille hérite de la classe_mere
    - isinstance(<objet>, <classe>) : retourne True si l'objet est une instance de la classe
    
"""
#Claas Mère
class Vehicule:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

    def _sedeplacer(self):
        print("Le vehicule {} se deplace...".format(self.marque))


#Classe Fille
class Voiture(Vehicule):
    def __init__(self, marque, modele, puissance):
        super().__init__(marque, modele)
        self.puissance = puissance



#Programme Principal
v1 = Voiture("Peugot", "208", 100)
v1._sedeplacer()
print("Marque: {}, Modèle: {}, Puissance: {} ch".format(v1.marque, v1.modele, v1.puissance))


print(issubclass(Voiture, Vehicule))