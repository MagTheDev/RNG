import random, sys, time
import tkinter as tk
from tkinter import *

win = Tk()


Lf1 = LabelFrame(win, text = "", height=180, width=169).place(x = 10,y = 10)
#bottomlabel = Label(Lf1, text = "") 

Lf2 = LabelFrame(win, text = "", height=180, width=300).place(x = 190,y = 10) 
#bottomlabel = Label(Lf2, text = "")

label1 = Label(win, text="Label 1").place(x = 200, y = 15)
label2 = Label(win, text="Label 1").place(x = 200, y = 100)

border = 0
fg = "lightgrey"

b1 = Button(win, text= "Losovať", border=border,  activebackground="gray", activeforeground="white", bg=fg, height=5, width=10).place(x = 15,y = 15)
b2 = Button(win, text= "Pridať", border=border, activebackground="gray", activeforeground="white", bg=fg, height=5, width=10).place(x = 96,y = 15)
b3 = Button(win, text= "Odobrať", border=border, activebackground="gray", activeforeground="white", bg=fg, height=5, width=10).place(x = 15,y = 101)
b4 = Button(win, text= "Koniec", border=border, activebackground="gray", activeforeground="white", bg=fg, height=5, width=10).place(x = 96,y = 101)


win.title('Rng')
win.geometry("500x200")
win.mainloop()
