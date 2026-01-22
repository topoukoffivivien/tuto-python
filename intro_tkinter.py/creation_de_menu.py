#coding:utf-8

import tkinter

def about():
    about_window = tkinter.Toplevel()
    about_window.geometry("400x200")
    about_window.title("A propos")
    label = tkinter.Label(about_window, text="Ceci est une application Tkinter.")
    label.pack(pady=20)


#création et configuration de la fenêtre principale
app = tkinter.Tk()
app.geometry("600x300")
app.title("Contrôle de variable Tkinter")

#Widgers....
navBAr = tkinter.Menu(app)
first_menu = tkinter.Menu(navBAr, tearoff=0)
first_menu.add_command(label="option1")
first_menu.add_command(label="option2")
first_menu.add_separator()
first_menu.add_command(label="Quitter", command=app.quit)


second_menu = tkinter.Menu(navBAr, tearoff=0)
second_menu.add_command(label="commande1")
second_menu.add_separator()
second_menu.add_command(label="A propos", command=about)

navBAr.add_cascade(label="premier menu", menu=first_menu)
navBAr.add_cascade(label="second menu", menu=second_menu)



#Boucle principale
app.config(menu=navBAr)
app.mainloop()