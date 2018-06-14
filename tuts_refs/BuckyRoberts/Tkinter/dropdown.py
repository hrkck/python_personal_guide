from tkinter import *


def doNothing():
    print(" Okay ")


def doNothing2():
    print(" Allright ")


root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project", command=doNothing)
subMenu.add_command(label="NEWEST Project", command=doNothing2)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)


root.mainloop()
