from tkinter import *

root = Tk()

# Creating Labels
label_1 = Label(root, text=" Name ")
label_2 = Label(root, text=" Password ")

# Creating Entries
entry_1 = Entry(root)
entry_2 = Entry(root)

### GRID LAYOUT ###
label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

# CheckBox
check = Checkbutton(root, text=" Keep me alive! ")
check.grid(columnspan=2)


root.mainloop()
