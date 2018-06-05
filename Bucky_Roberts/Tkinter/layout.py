from tkinter import *

root = Tk()


one = Label(root, text="One", bg="grey", fg="Black")
one.pack()
two = Label(root, text="Two", bg="grey", fg="Black")
two.pack(fill=X)
three = Label(root, text="Three", bg="Red", fg="Black")
three.pack(side=LEFT, fill=Y)
root.mainloop()
