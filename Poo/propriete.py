#coding:utf-8


"""
Propriété : manière de manipuler/contrôler des attributs
            principe d'encapsulation
"""

class Humain:
    def __init__(self, nom, age):
        print("création d'un humain...")
        self.nom = nom
        self._age = age
    
    def _getage(self):
        try:
            return self._age
        except AttributeError:
            print("L'attribut age n'existe plus.")
    
    def _setage(self, new_age):
        if new_age < 0:
            self._age = 0
        else:
            self._age = new_age

    def _delage(self):
        del self._age
        
    
    # property(<getter>, <setter>, <deleter>, <doc>)
    property_age = property(_getage, _setage, _delage, "je suis la propriete age d'un humain")



H1 = Humain("Jean", 25)

print(H1.property_age)

del H1.property_age

print(H1.property_age)