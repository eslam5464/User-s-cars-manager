import Database as db
from tkinter import *
from os import path
from Database import db_name


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.lbl_car_owner = Label(self, text="Owner: ")
        self.btn_removeUser = Button(self,
                                     text="Delete selected Owner/user", command=self.removeUser)
        self.lbl_addCar = Label(self, text="")
        self.btn_refreshUsers = Button(
            self, text="Refresh users", command=self.updateListBox)
        self.btn_addCar = Button(self, text="Add car", command=self.addCar)
        self.lb_userID = Listbox(Window, height=10,
                                 width=15,
                                 bg="grey",
                                 activestyle='dotbox',
                                 font="Helvetica",
                                 fg="yellow")
        self.entry_car_model = Entry(self, width=40)
        self.lbl_car_model = Label(self, text="Model: ")
        self.entry_car_brand = Entry(self, width=40)
        self.lbl_car_brand = Label(self, text="Brand: ")
        self.lbl_car = Label(self, text="Cars: ")
        self.lbl_addUser = Label(self, text="")
        self.btn_addUser = Button(self, text="Add user", command=self.addUser)
        self.entry_user_email = Entry(self, width=40)
        self.lbl_user_email = Label(self, text="Email: ")
        self.entry_user_name = Entry(self, width=40)
        self.lbl_user_name = Label(self, text="Name: ")
        self.lbl_user = Label(self, text="User: ")
        self.grid()

        if not path.exists(db_name):
            # db.removeDBfile()
            db.createDB()

        self.Create_widgets()

    def Create_widgets(self):
        line = 1
        self.lbl_user.grid(row=line, column=1, sticky=W)

        line += 1
        self.lbl_user_name.grid(row=line, column=1, sticky=W)

        self.entry_user_name.grid(row=line, column=2)

        line += 1
        self.lbl_user_email.grid(row=line, column=1, sticky=W)

        self.entry_user_email.grid(row=line, column=2)

        line += 1
        self.btn_addUser.grid(row=line, column=2)

        line += 1
        self.lbl_addUser.grid(row=line, column=2, sticky=N)

        # -------------------------

        line += 1
        self.lbl_car.grid(row=line, column=1, sticky=W)

        line += 1
        self.lbl_car_brand.grid(row=line, column=1, sticky=W)

        self.entry_car_brand.grid(row=line, column=2)

        line += 1
        self.lbl_car_model.grid(row=line, column=1, sticky=W)

        self.entry_car_model.grid(row=line, column=2)

        line += 1

        self.lb_userID.grid(row=line, column=0, sticky=W)

        # -----------

        line += 1
        self.btn_addCar.grid(row=line, column=2)

        self.btn_refreshUsers.grid(row=line, column=1)

        line += 1
        self.lbl_addCar.grid(row=line, column=2, sticky=N)

        self.lbl_car_owner.grid(row=line, column=1, sticky=W)

        line += 1
        self.btn_removeUser.grid(row=line, column=2)

    def updateListBox(self):
        self.lb_userID.delete(0, 'end')

        self.users_id = db.table_user.view("id")
        count = 1
        for id in self.users_id:
            self.lb_userID.insert(count, id)
            count += 1

    def addCar(self):
        db.table_cars.insert(self.entry_car_brand.get(),
                             self.entry_car_model.get(), str(self.lb_userID.get(self.lb_userID.curselection())[0]))
        self.lbl_addCar.config(
            text=f"Car '{self.entry_car_brand.get()} {self.entry_car_model.get()}' " +
                 f"added to user: '{self.lb_userID.get(self.lb_userID.curselection())[0]}' in database")

    def addUser(self):
        db.table_user.insert(self.entry_user_name.get(),
                             self.entry_user_email.get())
        self.lbl_addUser.config(
            text=f"User '{self.entry_user_name.get()}' added")

    def removeUser(self):
        if self.lb_userID.curselection():
            db.table_user.delete(self.lb_userID.get(
                self.lb_userID.curselection())[0])
            self.updateListBox()


Window = Tk()
Window.title("car system")
Window.geometry('350x450')
app = Application(Window)
app.mainloop()
