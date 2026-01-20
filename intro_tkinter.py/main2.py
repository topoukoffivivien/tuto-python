#coding:utf-8

import tkinter

mainapp = tkinter.Tk()
mainapp.title("Ma première fenêtre Tkinter")

screen_x = int(mainapp.winfo_screenwidth())
screen_y = int(mainapp.winfo_screenheight())

window_x = 400
window_y = 300

pos_x = (screen_x // 2) - (window_x // 2)
pos_y = (screen_y // 2) - (window_y // 2)

geo = "{}x{}+{}+{}".format(window_x, window_y, pos_x, pos_y)
mainapp.geometry(geo)
mainapp.mainloop()