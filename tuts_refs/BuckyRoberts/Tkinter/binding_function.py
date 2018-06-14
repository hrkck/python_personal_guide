from tkinter import *

root = Tk()


def printname(event):
    print("Hey Man")

button_1 = Button(root, text="Printname Function")
button_1.bind("<Button-1>", printname)
button_1.pack()


root.mainloop()
