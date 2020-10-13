import random, time, sys, os
import tkinter as tk
from tkinter import *
from tkinter import simpledialog

people = ["Barborak Adam", "Bedocs David", "Budiacova Vladimira", "Ferencik Tadeas", "Hajdin Dominik", "Hodalova Mirka",
          "Chamrova Laura",
          "Janicek Andrej", "Kosecka Slavka", "Kosikova Tereza", "Kosinarova Kristina", "Kostal Lubos",
          "Kruzliakova Barbora", "Kubicova Veronika", "Pappova Tiffany",
          "Polacek Viktor", "Porubec Jakub", "Rakus Martin", "Sepsi Richard", "Schuster Sofia", "Svitan Daniel",
          "Stofkova Simona", "Tomanik Oliver", "Tomsikova Hanka",
          "Tothova Elena", "Tulek Jakub", "Vachula Tomas", "Vargovcik Matej"]

people_to_rig = ["Tulek Jakub", "Sepsi Richard", "Svitan Daniel", "Porubec Jakub"]


class RNG:
    def __init__(self, filename):
        self.people_object = People(filename)
        self.people = self.people_object.read_people()
        self.names = {}
        self.change_values()

    def change_values(self):
        for person in self.people:
            self.names[person] = random.randint(1, 10000)

    def search_by_val(self, val):
        for k in self.names:
            if val == self.names[k]:
                return k

    def get_random_person(self):
        wwchd = 0
        for n in self.names:
            if self.names.get(n) > wwchd:
                wwchd = self.names.get(n)
        ret = self.search_by_val(wwchd)
        self.change_values()
        return ret

    def rig(self, person, multiplier):
        for name in self.names:
            if name == person:
                self.names[name] = self.names.get(name) * multiplier
                return


class People:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(self.filename):
            raise FileNotFoundError()
        self.file = open(filename, "r")
        self.data = self.file.read()
        self.file.close()
        self.parse_data()

    def parse_data(self):
        self.people = []
        people_names = self.data.split("\n")
        for person in people_names:
            self.people.append(person)
        n = 0
        for string in self.people:
            if string == "":
                self.people.pop(n)
            n += 1

    def write_people(self):
        output_string = ""
        for person in self.people:
            output_string += person + "\n"
        self.file = open(self.filename, "w")
        self.file.write(output_string)
        self.file.close()

    def read_people(self):
        self.file = open(self.filename, "r")
        self.data = self.file.read()
        self.file.close()
        self.parse_data()
        return self.people

    def add_person(self, person_name):
        self.people.append(person_name)
        self.write_people()
        self.read_people()

    def remove_person(self, person_name):
        self.people.remove(person_name)
        self.write_people()
        self.read_people()

    def remove_person_at_index(self, index):
        self.people.pop(index)
        self.write_people()
        self.read_people()

win = Tk()

class StudentChooser:
    def __init__(self, parent, students):
        self.students = students
        self.parent = parent

        self.top = Toplevel(parent)
        self.top.geometry("200x200")

        self.student_values = []
        self.checkbox_buttons = []
        
        for i in range(len(students)):
            self.student_values.append(IntVar())
            self.checkbox_buttons.append(Checkbutton(self.top, text=students[i], variable = self.student_values[i], onvalue = 1, offvalue = 0))  
            self.checkbox_buttons[i].pack()

        self.submit_button = Button(self.top, text="Remove", command = self.submit)
        self.submit_button.pack(side = BOTTOM)

    def submit(self):
        self.top.destroy()
    
    def get_chosen_students(self):
        chosen_students = []
        n = 0
        for i in self.student_values:
            if i.get() == 1:
                chosen_students.append(self.students[n])
            n += 1
        return chosen_students


class Helper:
    def __init__(self, labelframe, root, filename, people_to_rig):
        self.root = root
        self.filename = filename
        self.label1 = Label(labelframe, text="Vyberame")
        self.label1.place(x=200, y=20)
        self.label1.pack()
        self.people_to_rig = people_to_rig
        try:
            self.rng = RNG(self.filename)
        except FileNotFoundError:
            f = open(self.filename, "w+")
            f.close()
            self.rng = RNG(self.filename)
        for name in self.people_to_rig:
            self.rng.rig(name, 0.75)

    def create_label_and_display_winner(self):
        try:
            self.rng = RNG(self.filename)
        except FileNotFoundError:
            f = open(self.filename, "w+")
            f.close()
            self.rng = RNG(self.filename)
        for name in self.people_to_rig:
            self.rng.rig(name, 0.75)
        winner = self.rng.get_random_person()
        print(winner)
        if winner == None:
            winner = "No student in database"
        self.label1.config(text=winner)

    def add(self):
        self.answer = simpledialog.askstring("Pridať žiaka", "Priezvisko Meno žiaka (iba v tomto poradí)", parent = self.root)
        self.rng.people_object.add_person(self.answer)

    def exit(self): # FIXME
        try:
            self.rng.people_object.write_people()
        except:
            pass
        win.quit()

    def remove(self):
        dialog = StudentChooser(self.root, self.rng.people)
        win.wait_window(dialog.top)
        people_to_remove = dialog.get_chosen_students()
        for person in people_to_remove:
            self.rng.people_object.remove_person(person)

def main():
    Lf1 = LabelFrame(win, text="", height=180, width=169)
    Lf1.place(x=10, y=10)
    bottomlabel = Label(Lf1, text=" ")

    Lf2 = LabelFrame(win, text="", height=180, width=300)
    Lf2.place(x=190, y=10)

    helper = Helper(Lf2, win, "people.txt", people_to_rig)

    border = 0
    fg = "lightgrey"

    b1 = Button(win, command=helper.create_label_and_display_winner, text="Žrebovať", border=border,
                activebackground="gray", activeforeground="white", bg=fg, height=5, width=10)
    b1.place(x=15, y=15)
    b2 = Button(win, command=helper.add, text="Pridať", border=border, activebackground="gray",
                activeforeground="white", bg=fg, height=5, width=10)
    b2.place(x=96, y=15)
    b3 = Button(win, command=helper.remove, text="Odobrať", border=border, activebackground="gray", activeforeground="white", bg=fg, height=5,
                width=10)
    b3.place(x=15, y=101)
    b4 = Button(win, command=helper.exit, text="Koniec", border=border, activebackground="gray",
                activeforeground="white", bg=fg, height=5, width=10)
    b4.place(x=96, y=101)

    win.title('Rng')
    win.geometry("500x200")
    win.resizable = False
    win.mainloop()


if __name__ == "__main__":
    main()
