#coding:utf-8

import tkinter



#création et configuration de la fenêtre principale
app = tkinter.Tk()
app.geometry("400x300")
app.title("Contrôle de variable Tkinter")

#Widgers....
label = tkinter.Label(app, text="username :")
label2 = tkinter.Label(app, text="password :")
input_field = tkinter.Entry(app)
input_field2 = tkinter.Entry(app, show="*")
button = tkinter.Button(app, text="Cliquez ici")


label.grid(row=0, column=0, padx=10, pady=10)
input_field.grid(row=0, column=1, padx=10, pady=10)

label2.grid(row=1, column=0, padx=10, pady=10)
input_field2.grid(row=1, column=1, padx=10, pady=10)

button.grid(row=2, column=0, columnspan=2, pady=10)

#Boucle principale
app.mainloop()