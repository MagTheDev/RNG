import tkinter as tk
from tkinter import *
import time

#win
win = Tk()
win.title("Odobrať žiaka")
win.geometry("240x80")

text1= "Zadajte meno žiaka..."
list_of_old_people = []

#definitions
def Eget():
    old_name = entry1.get()
    text1 = "Odoberám žiaka " + old_name + "..."
    list_of_old_people.append(old_name)
    lbl.config(text=text1)

def Enter(var):
    Eget()

def Des():
    print(list_of_old_people)
    win.destroy()
    return list_of_old_people

#variables
entry1 = Entry(win, width=30)
entry1.place(x=30, y=10)

but = Button(win, text="Odobrať", command=Eget)
but.place(x=100, y=50)

butD = Button(win, text="Odísť", command=Des)
butD.place(x=200, y=50)

lbl = Label(win, text=text1)
lbl.place(x=30, y=30)


#win config
win.bind_all('<Return>', Enter)
win.mainloop()
