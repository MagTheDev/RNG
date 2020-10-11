import tkinter as tk
from tkinter import *
import time

#win
win = Tk()
win.title("Pridať žiaka")
win.geometry("240x80")

text1= "Zadajte meno žiaka..."
list_of_new_people = []

#definitions
def Eget():
    new_name = entry1.get()
    text1 = "Pridávam žiaka " + new_name + "..."
    list_of_new_people.append(new_name)
    lbl.config(text=text1)

def Enter(var):
    Eget()

def Des():
    print(list_of_new_people)
    win.destroy()
    return list_of_new_people

#variables
entry1 = Entry(win, width=30)
entry1.place(x=30, y=10)

but = Button(win, text="Pridať", command=Eget)
but.place(x=100, y=50)

butD = Button(win, text="Odísť", command=Des)
butD.place(x=200, y=50)

lbl = Label(win, text=text1)
lbl.place(x=30, y=30)


#win config
win.bind_all('<Return>', Enter)
win.mainloop()
