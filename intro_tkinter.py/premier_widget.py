#coding:utf-8

import tkinter

app = tkinter.Tk()
label = tkinter.Label(app, text="Bienvenue dans tkinter!")
label.config(bg="blue", fg="white", font=("Arial", 24))

input_field = tkinter.Entry(app)

button = tkinter.Button(app, text="cliquez moi")

label.pack()
input_field.pack()
button.pack()

app.mainloop()