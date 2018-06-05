from tkinter import *


def doNothing():
    print(" Okay ")


def doNothing2():
    print(" Allright ")


root = Tk()

#  **** Main Menu ****

menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project", command=doNothing)
subMenu.add_command(label="NEWEST Project", command=doNothing2)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

#  **** Toolbar ****

toolbar = Frame(root, bg="blue")
insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

root.mainloop()
