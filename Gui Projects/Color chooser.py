from tkinter import *
from tkinter.colorchooser import *

#basic color chooser project#

root = Tk()
root.geometry("250x100")
root.title("Color Chooser")
root.config(bg = "light grey")


def mcolor():
    color = askcolor()
    mylabel = Label(text = "Your preferred Color",bg = color[1]).pack()


btn = Button(text = "Choose Color",bg = "light blue",fg = "black",command = mcolor).pack()


root.mainloop()