from Tkinter import *

root = Tk()

photo = PhotoImage(file="photo.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()
