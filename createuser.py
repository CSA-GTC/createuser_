'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

#Gregory Clarke
#Advanced Computer Programming
#9/20/2018

from tkinter import *
from tkinter import ttk

class App:

    def __init__(self):
        frame=Frame(root)
        frame.pack(anchor="w")
        #Username
        self.z = StringVar()
        self.username = Entry(frame, text="Username: ")
        self.username.pack(anchor="w")

        #Password
        self.x = StringVar()
        self.password = Entry(frame, show="*", text="Password: ")
        self.password.pack(anchor="w")

        #Radio Button
        frame1 = Frame(root)
        frame1.pack(anchor="w")
        self.y = StringVar()
        self.car = Radiobutton(frame1, text="Male", variable=self.y, value="male")
        self.car.pack(anchor="w")
        self.car.deselect()
        self.house = Radiobutton(frame1, text="Female", variable=self.y, value="female")
        self.house.pack(anchor="w")

        #Checkbox
        frame2 = Frame(root)
        frame2.pack(anchor="w")
        self.var = StringVar()
        self.var = set()
        self.one = Checkbutton(frame2, variable=self.var, text="User", onvalue="u")
        self.one.pack(anchor="w")
        self.two = Checkbutton(frame2, variable=self.var, text="Admin", onvalue="a")
        self.two.pack(anchor="w")
        self.three = Checkbutton(frame2, variable=self.var, text="Guest", onvalue="g")
        self.three.pack(anchor="w")

        #Combobox
        frame3=Frame(root)
        frame3.pack(anchor="w")
        self.y = StringVar()
        self.box = ttk.Combobox(frame3, state="readonly", textvariable=self.y)
        self.box["values"] = ["IT ", "HR", "Sales", "Maintenance", "Other"]
        self.box.pack()
        self.box.bind("<<ComboboxSelected>>")
        self.box.bind("<FocusIn>")

        frame4 = Frame(root)
        frame4.pack(anchor="w")
        self.clear = Button(frame4, text="Clear", command=self.clear)
        self.clear.pack(anchor="w")
        self.submit = Button(frame4, text="Submit", command=self.submit)
        self.submit.pack(anchor="w")

    def clear(self):
        self.username.delete(0, END)
        self.password.delete(0, END)
        self.y.set(0)
        self.var = 0
        self.box.set("")

    def submit(self):
        if self.z.get() != "" and self.x.get() != "" and self.y.get() != "" and self.var != "" and self.box.get() != "": #In order, username, password, radiobutton, checkbox, combobox
            with open("users.txt", "a") as file:
                file.write(self.z+"***"+self.x+"***"+self.y+"***"+self.var+"***"+self.box)
        else:
            print("Please enter all criteria")



root = Tk()
app = App()
root.title("Create User")
root.mainloop()
root.destroy()