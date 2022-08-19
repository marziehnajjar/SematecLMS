from tkinter import *
from UserInterfaceLayer import *
from DataAccessLayer import *
from Model import *


class AddUserUI:

    def __init__(self, user: User):
        self.User = user

    def FormLoad(self):
        addUserfrm = Tk()
        addUserfrm.title('Add an User')
        addUserfrm.geometry('400x300')
        addUserfrm.resizable(0, 0)
        positionRight = int(addUserfrm.winfo_screenwidth() / 2 - 400 / 2)
        positionDown = int(addUserfrm.winfo_screenheight() / 2 - 300 / 2)
        addUserfrm.geometry("+{}+{}".format(positionRight, positionDown))

        userdb = UserDB()
        rolesList = userdb.getRolesList()

        def backToMain():
            addUserfrm.destroy()
            from UserInterfaceLayer.MainForm import MainUI
            mainui = MainUI(self.User)
            mainui.mainFormLoad()

        def insertUserCommand():
            FirstName = txtFirstName.get()
            LastName = txtLastName.get()
            UserName = txtUserName.get()
            Password = txtPassword.get()
            Role = txtRole.get()

            user = Model.User(UserName, Password, FirstName, LastName, Role)
            userdb = UserDB(user)
            userdb.insertRow()

        frameinfo = LabelFrame(addUserfrm, text=' User Information ')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')
# region Widgets ...
        lblFirstName = Label(frameinfo, text='FirstName: ')
        lblFirstName.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        txtFirstName = StringVar()
        entFirstName = Entry(frameinfo, textvariable=txtFirstName, width=40, highlightthickness=1)
        entFirstName.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        lblLastName = Label(frameinfo, text='LastName: ')
        lblLastName.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        txtLastName = StringVar()
        entLastName = Entry(frameinfo, textvariable=txtLastName, width=40, highlightthickness=1)
        entLastName.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        lblUserName = Label(frameinfo, text='UserName: ')
        lblUserName.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        txtUserName = StringVar()
        entUserName = Entry(frameinfo, textvariable=txtUserName, width=40, highlightthickness=1)
        entUserName.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        lblPassword = Label(frameinfo, text='Password: ')
        lblPassword.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        txtPassword = StringVar()
        entPassword = Entry(frameinfo, textvariable=txtPassword, width=40, highlightthickness=1)
        entPassword.grid(row=4, column=1, padx=10, pady=10, sticky='w')
        #
        # txtAdmin = IntVar()
        # chbAdmin = Checkbutton(frameinfo, text='Admin', variable=txtAdmin)
        # chbAdmin.grid(row=5, column=1, padx=5, pady=10, sticky='w')

        lblRole = Label(frameinfo, text='Course Category Name: ')
        lblRole.grid(row=5, column=0, padx=10, pady=0, sticky='w')
        txtRole = StringVar()
        entRole = Combobox(frameinfo, width=20, textvariable=txtRole, state='readonly')
        entRole['values'] = rolesList
        entRole.grid(row=5, column=1, padx=10, pady=10, sticky='w')
        entRole.current()

        btnAddUser = Button(addUserfrm, text='Add User', width=20, relief='groove', command=insertUserCommand)
        btnAddUser.grid(row=6, column=0, padx=30, pady=10, sticky='w')

        btnBack = Button(addUserfrm, text='Back to Main', width=20, relief='groove', command=backToMain)
        btnBack.grid(row=6, column=0, padx=30, pady=10, sticky='e')
# endregion
        addUserfrm.mainloop()
