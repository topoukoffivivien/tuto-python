#coding:utf-8

import tkinter



"""
StringVar: pour les chaînes de caractères
IntVar: pour les entiers
DoubleVar: pour les nombres à virgule flottante
BooleanVar: pour les valeurs booléennes (True/False)
Chaque type de variable offre des méthodes pour obtenir et définir leur valeur, ainsi que pour lier la variable à des widgets tkinter afin que les modifications soient automatiquement reflétées dans l'interface utilisateur.
"""

#Observateur
def callback(*args):
    var_label.set(var_entry.get())

#création et configuration de la fenêtre principale
app = tkinter.Tk()
app.geometry("400x300")
app.title("Contrôle de variable Tkinter")

#Widgets liés aux variables
var_entry = tkinter.StringVar()
var_entry.trace("w", callback)
entry = tkinter.Entry(app, textvariable=var_entry)

var_label = tkinter.StringVar()
label = tkinter.Label(app, textvariable=var_label)


entry.pack()
label.pack()

#Boucle principale
app.mainloop()