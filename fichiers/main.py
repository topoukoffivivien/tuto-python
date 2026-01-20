#coding:utf-8

"""
Modes d'ouverture : r : lecture seule
                    w : écriture (écrase le fichier s'il existe)
                    a : ajout à la fin du fichier
                    r+ : lecture et écriture dans le meme fichier
                    x : lecture et écriture
"""

fic = open("donnee.txt", "r")

# content = fic.read()
# print(content)

content = fic.readline()
print(content)

content = fic.readline()
print(content)
content = fic.readlines()
print(content)

fic.close()

if fic.closed:
    print("Le fichier est bien fermé.")
else:
    print("Le fichier est encore ouvert.")