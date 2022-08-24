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
        profilefrm.title('User Profile ')
        profilefrm.geometry('280x240')
        profilefrm.resizable(False, False)
        positionRight = int(profilefrm.winfo_screenwidth() / 2 - 280 / 2)
        positionDown = int(profilefrm.winfo_screenheight() / 2 - 240 / 2)
        profilefrm.geometry("+{}+{}".format(positionRight, positionDown))

        userdb = UserDB()
        rolesList = userdb.getRolesList()

        def CloseCommand():
            profilefrm.destroy()

        # def insertTeacherCommand():
        #     FirstName = txtFirstName.get()
        #     LastName = txtLastName.get()
        #     UserName = txtUserName.get()
        #     Password = txtPassword.get()
        #     LastLogin = txtLastLogin.get()
        #     Role = txtRole.get()

        frameinfo = LabelFrame(profilefrm, text=' information ')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')

# region Widgets ...
        lblFirstName = Label(frameinfo, text='FirstName: ')
        lblFirstName.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        txtFirstName = StringVar()
        entFirstName = Entry(frameinfo, textvariable=txtFirstName, width=20, highlightthickness=1)
        entFirstName.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        lblLastName = Label(frameinfo, text='LastName: ')
        lblLastName.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        txtLastName = StringVar()
        entLastName = Entry(frameinfo, textvariable=txtLastName, width=20, highlightthickness=1)
        entLastName.grid(row=2, column=1, padx=10, pady=5, sticky='w')

        lblUserName = Label(frameinfo, text='UserName: ')
        lblUserName.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        txtUserName = StringVar()
        entUserName = Entry(frameinfo, textvariable=txtUserName, width=20, highlightthickness=1)
        entUserName.grid(row=3, column=1, padx=10, pady=5, sticky='w')

        lblPassword = Label(frameinfo, text='Password: ')
        lblPassword.grid(row=4, column=0, padx=10, pady=5, sticky='w')
        txtPassword = StringVar()
        entPassword = Entry(frameinfo, textvariable=txtPassword, width=20, highlightthickness=1)
        entPassword.grid(row=4, column=1, padx=10, pady=5, sticky='w')

        lblLastLogin = Label(frameinfo, text='Last Login: ')
        lblLastLogin.grid(row=5, column=0, padx=10, pady=5, sticky='w')
        txtLastLogin = StringVar()
        entLastLogin = Entry(frameinfo, textvariable=txtLastLogin, width=20, highlightthickness=1)
        entLastLogin.grid(row=5, column=1, padx=10, pady=5, sticky='w')

        # lblRole = Label(frameinfo, text='Course Category Name: ')
        # lblRole.grid(row=6, column=0, padx=10, pady=0, sticky='w')
        # txtRole = StringVar()
        # entRole = Combobox(frameinfo, width=20, textvariable=txtRole, state='readonly')
        # entRole['values'] = rolesList
        # entRole.grid(row=6, column=1, padx=10, pady=10, sticky='w')
        # entRole.current()

        btnClose = Button(profilefrm, text='Close', width=10, relief='groove', command=CloseCommand)
        btnClose.grid(row=7, column=0, padx=30, pady=10, sticky='e')
# endregion
        profilefrm.mainloop()
