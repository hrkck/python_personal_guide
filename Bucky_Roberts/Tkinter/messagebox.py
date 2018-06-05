from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Window title', 'Mount Blanc')

answer = tkinter.messagebox.askquestion('Quest', 'Is your Quest finite?')

# if answer == 'yes':
#	print('Go find Font.')


root.mainloop()
