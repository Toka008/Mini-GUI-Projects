from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")

def time():
    string = strftime("%H:%M:%S %p")
    lbl.config(text = string)
    lbl.after(1000,time)

lbl = Label (root,font = ("arial",90,"bold"),bg = "light green",fg = "grey")
lbl.pack(anchor = "center",fill = "both",expand = 1) 

time()
mainloop()