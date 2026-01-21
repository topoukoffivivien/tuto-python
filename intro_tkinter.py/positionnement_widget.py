#coding:utf-8

import tkinter



#création et configuration de la fenêtre principale
app = tkinter.Tk()
app.geometry("400x300")
app.title("Contrôle de variable Tkinter")

#Widgers....
mainframe = tkinter.Frame(app, width=300, height=200, bg="lightgrey")
mainframe.pack()

#Boucle principale
app.mainloop()