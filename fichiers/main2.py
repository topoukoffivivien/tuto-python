#coding:utf-8

with open("donnee.txt", "w") as fic:
    nombre = 15

    fic.write(str(nombre)+"\n")
    fic.write("Bonjour le monde!\n")
    fic.write("Et une autre lingne.\n")
    # Le fichier sera automatiquement fermé à la fin du bloc with