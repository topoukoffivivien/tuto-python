#coding:utf-8

ageUser = input("Quel âge as-tu ? ")
try:
    ageUser = int(ageUser)
except:
    print("Erreur : Vous devez entrer un nombre entier pour l'âge.")
else:
    print("Tu as {} ans".format(ageUser))
finally:
    print("Merci d'avoir utilisé notre programme.")