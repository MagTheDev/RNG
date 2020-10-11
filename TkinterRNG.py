import random, sys, time
import tkinter as tk
from tkinter import *

win = Tk()

def Exit():
    exit()

def Add():
    import tk_add

def Rem():
    import tk_remove


def Roll():
    pass





Lf1 = LabelFrame(win, text = "", height=180, width=169).place(x = 10,y = 10)
#bottomlabel = Label(Lf1, text = "") 

Lf2 = LabelFrame(win, text = "", height=180, width=300).place(x = 190,y = 10) 
#bottomlabel = Label(Lf2, text = "")

label1 = Label(win, text="Label 1").place(x = 200, y = 15)
label2 = Label(win, text="Label 1").place(x = 200, y = 100)

border = 0
fg = "lightgrey"

b1 = Button(win, text= "Losovať", border=border, command=Roll, activebackground="gray", activeforeground="white", bg=fg, height=5, width=10).place(x = 15,y = 15)
b2 = Button(win, text= "Pridať", border=border, command=Add, activebackground="gray", activeforeground="white", bg=fg, height=5, width=10).place(x = 96,y = 15)
b3 = Button(win, text= "Odobrať", border=border, command=Rem, activebackground="gray", activeforeground="white", bg=fg, height=5, width=10).place(x = 15,y = 101)
b4 = Button(win, text= "Koniec", border=border, command=Exit, activebackground="gray", activeforeground="white", bg=fg, height=5, width=10).place(x = 96,y = 101)


win.title('Rng')
win.geometry("500x200")
win.mainloop()
