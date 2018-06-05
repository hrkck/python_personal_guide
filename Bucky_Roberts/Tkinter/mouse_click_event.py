from tkinter import *

root = Tk()

# Mouse Click Functions


def leftClick(event):
    print("left")


def rightClick(event):
    print("right")


def middleClick(event):
    print("middle")

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-3>", rightClick)
frame.bind("<Button-2>", middleClick)
frame.pack()

root.mainloop()
