
import random, sys, time
import tkinter as tk
from tkinter import *

win = Tk()





Lf1 = LabelFrame(win, text = "", height=180, width=169).place(x = 10,y = 10)
bottomlabel = Label(Lf1, text = " ") 

Lf2 = LabelFrame(win, text = "", height=180, width=300).place(x = 190,y = 10) 
#bottomlabel = Label(Lf2, text = "test")

border = 0
fg = "lightgrey"

b1 = Button(win, text= "Losovať", border=border, activebackground="gray", activeforeground="white", bg=fg, height=5, width=10).place(x = 15,y = 15)
b2 = Button(win, text= "Pridať", border=border, activebackground="gray", activeforeground="white", bg=fg, height=5, width=10).place(x = 96,y = 15)
b3 = Button(win, text= "Odobrať", border=border, activebackground="gray", activeforeground="white", bg=fg, height=5, width=10).place(x = 15,y = 101)
b4 = Button(win, text= "Koniec", border=border, activebackground="gray", activeforeground="white", bg=fg, height=5, width=10).place(x = 96,y = 101)

win.title('Rng')
win.geometry("500x200")
win.mainloop()

"""
textOut=str("")
wwchd=0

#people:number

dct_name = {}
sfile = open("sfile.txt", "r")
sfile_name_number = sfile.readline()
sfile_name_number_fix = int(sfile_name_number).split("\n")
for i in range(sfile_name_number_fix[0]):
    name_get = sfile.readline().split("\n")
    name = name_get[0]
    number = random.randint(1, 10000)
    dct_name.update({name:number})
sfile.close()

people = ["Svitan Daniel", "Tulek Jakub"]

#lower score for some people

for guy in dct_name:
    if guy in people:
        dct_name[guy] = int(dct_name.get(guy) * 0.75)


#key return function

def search_by_val(dict, value):
    for key in dict:
        v = dict.get(key)
        if v == value:
            return key
    return None


#main definition

def Roll():
    wwchd = 0
    for name in dct_name:
        if int(dct_name[name]) > wwchd:
            wwchd = int(dct_name[name])
        elif int(dct_name[name]) <= wwchd:
            pass
    str(wwchd)
    winner = search_by_val(dict=dct_name, value=wwchd)
    textOut = "Dnes pôjde odpovedať " + winner + ", veľa štastia!"


#bottom definitions(add people, remove people)

def AddPeople():
    name = entry1.get()
    num = random.randint(1, 10000)
    dct_name.update({name:num})

def Exit():
    sys.Exit(0)

def RemPerson():
    name = entry1.get()
    dct_name.pop(name)



Roll()
"""

