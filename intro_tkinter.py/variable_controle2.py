#coding:utf-8

import tkinter

#Observateur
def callback(*args):
    if var_gender.get():
        print("Genre sélectionné : Homme")
        var_label_gender.set("Genre sélectionné : Homme")
    else:
        print("Genre sélectionné : Femme")
        var_label_gender.set("Genre sélectionné : Femme")

#création et configuration de la fenêtre principale
app = tkinter.Tk()
app.geometry("400x300")
app.title("Contrôle de variable Tkinter")

#Widgets...
var_gender = tkinter.IntVar()
var_gender.trace("w", callback)
radio1 = tkinter.Radiobutton(app, text="Homme", value=1, variable=var_gender)
radio2 = tkinter.Radiobutton(app, text="Femme", value=0, variable=var_gender)

var_label_gender = tkinter.StringVar()
label_gender = tkinter.Label(app, textvariable=var_label_gender)

radio1.pack()
radio2.pack()
label_gender.pack()

#Boucle principale
app.mainloop()