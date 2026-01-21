#coding:utf-8

import tkinter
from tkinter import messagebox


"""
showinfo: affiche une fenêtre modale avec un message d'information
showwarning: affiche une fenêtre modale avec un message d'avertissement
showerror: affiche une fenêtre modale avec un message d'erreur
askquestion: affiche une fenêtre modale avec une question et des boutons Oui/Non
askokcancel: affiche une fenêtre modale avec une question et des boutons OK/Annuler
askyesno: affiche une fenêtre modale avec une question et des boutons Oui/Non
askretrycancel: affiche une fenêtre modale avec une question et des boutons Réessayer/Annuler
Chaque fonction retourne une valeur en fonction de l'interaction de l'utilisateur avec la fenêtre modale.
"""

def show_modal_window():
    messagebox.askquestion("Fenêtre Modale", "Ceci est une fenêtre modale.")

app = tkinter.Tk()
btn = tkinter.Button(app, text="Ouvrir une fenêtre modale", command=show_modal_window)
btn.pack()

app.minsize(300, 300)
app.mainloop()