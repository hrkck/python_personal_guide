from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

blackLine = canvas.create_line(0, 0, 100, 50, fill="red")
abox = canvas.create_rectangle(25, 25, 100, 50,)


root.mainloop()
