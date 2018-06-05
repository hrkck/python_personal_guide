from tkinter import *

root = Tk()

# Top Frame
topFrame = Frame(root)
topFrame.pack()

# Bottom Frame
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


# Buttons
button1 = Button(topFrame, text="Click Me!", fg="red")
button2 = Button(topFrame, text="Click Me Too!", fg="blue")
button3 = Button(topFrame, text="Don't Forget ME!", fg="green")
button4 = Button(bottomFrame, text="MEEE!", fg="purple")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)


root.mainloop()
