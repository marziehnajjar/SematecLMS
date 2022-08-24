from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as msg
from UserInterfaceLayer import *
from DataAccessLayer import *
from tkcalendar import DateEntry
from Model import *


class ProfileUI:
    def __init__(self, user: User):
        self.User = user

    def profileFormLoad(self):
        profilefrm = Tk()
        profilefrm.attributes('-toolwindow', 'True')
        profilefrm.title('User Profile ')
        profilefrm.geometry('200x230')
        profilefrm.resizable(False, False)
        positionRight = int(profilefrm.winfo_screenwidth() / 2 - 200 / 2)
        positionDown = int(profilefrm.winfo_screenheight() / 2 - 230 / 2)
        profilefrm.geometry("+{}+{}".format(positionRight, positionDown))

        userdb = UserDB()
        rolesList = userdb.getRolesList()

        frameinfo = LabelFrame(profilefrm, text=' information ')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')

# region Widgets ...
        lblFirstName = Label(frameinfo, text='FirstName: ')
        lblFirstName.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        entFirstName = Label(frameinfo, text=self.User.FirstName)
        entFirstName.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        lblLastName = Label(frameinfo, text='LastName: ')
        lblLastName.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        entLastName = Label(frameinfo, text=self.User.LastName)
        entLastName.grid(row=2, column=1, padx=10, pady=5, sticky='w')

        lblUserName = Label(frameinfo, text='UserName: ')
        lblUserName.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        entUserName = Label(frameinfo, text=self.User.UserName)
        entUserName.grid(row=3, column=1, padx=10, pady=5, sticky='w')

        lblPassword = Label(frameinfo, text='Password: ')
        lblPassword.grid(row=4, column=0, padx=10, pady=5, sticky='w')
        entPassword = Label(frameinfo, text=self.User.Password)
        entPassword.grid(row=4, column=1, padx=10, pady=5, sticky='w')

        lblRole = Label(frameinfo, text='Role: ')
        lblRole.grid(row=5, column=0, padx=10, pady=5, sticky='w')
        entRole = Label(frameinfo, text=self.User.Role)
        entRole.grid(row=5, column=1, padx=10, pady=5, sticky='w')

        lblLastLogin = Label(frameinfo, text='Last Login: ')
        lblLastLogin.grid(row=6, column=0, padx=10, pady=5, sticky='w')
        entLastLogin = Label(frameinfo, text=self.User.LastName)
        entLastLogin.grid(row=6, column=1, padx=10, pady=5, sticky='w')

# endregion
        profilefrm.mainloop()
