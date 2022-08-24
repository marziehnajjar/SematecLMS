from tkinter import *
from UserInterfaceLayer import *
from DataAccessLayer import *
from Model import *


class UserUI:

    def __init__(self, user: User):
        self.User = user

    def userFormLoad(self):
        addUserfrm = Tk()
        addUserfrm.title('Add an User')
        addUserfrm.geometry('400x480')
        addUserfrm.resizable(0, 0)
        positionRight = int(addUserfrm.winfo_screenwidth() / 2 - 400 / 2)
        positionDown = int(addUserfrm.winfo_screenheight() / 2 - 480 / 2)
        addUserfrm.geometry("+{}+{}".format(positionRight, positionDown))

        userdb = UserDB()
        rolesList = userdb.getRolesList()

        def addToList():
            pass

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

            uservd = UserVD(user)
            uservd.validationForm()

            # userdb = UserDB(user)
            # userdb.insertRow()

        frameinfo = LabelFrame(addUserfrm, text=' User Information ')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')
# region Widgets ...
        lblID = Label(frameinfo, text='User ID : ')
        lblID.grid(row=0, column=0, padx=10, pady=5, sticky='w')

        lblFirstName = Label(frameinfo, text='FirstName: ')
        lblFirstName.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        txtFirstName = StringVar()
        entFirstName = Entry(frameinfo, textvariable=txtFirstName, width=23, highlightthickness=1)
        entFirstName.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        lblLastName = Label(frameinfo, text='LastName: ')
        lblLastName.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        txtLastName = StringVar()
        entLastName = Entry(frameinfo, textvariable=txtLastName, width=23, highlightthickness=1)
        entLastName.grid(row=2, column=1, padx=10, pady=5, sticky='w')

        lblUserName = Label(frameinfo, text='UserName: ')
        lblUserName.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        txtUserName = StringVar()
        entUserName = Entry(frameinfo, textvariable=txtUserName, width=23, highlightthickness=1)
        entUserName.grid(row=3, column=1, padx=10, pady=5, sticky='w')

        lblPassword = Label(frameinfo, text='Password: ')
        lblPassword.grid(row=4, column=0, padx=10, pady=5, sticky='w')
        txtPassword = StringVar()
        entPassword = Entry(frameinfo, textvariable=txtPassword, width=23, highlightthickness=1)
        entPassword.grid(row=4, column=1, padx=10, pady=5, sticky='w')

        lblEmail = Label(frameinfo, text='Email: ')
        lblEmail.grid(row=5, column=0, padx=10, pady=5, sticky='w')
        txtEmail = StringVar()
        entEmail = Entry(frameinfo, textvariable=txtEmail, width=23, highlightthickness=1)
        entEmail.grid(row=5, column=1, padx=10, pady=5, sticky='w')

        lblPasswordHint = Label(frameinfo, text='Password Hint: ')
        lblPasswordHint.grid(row=6, column=0, padx=10, pady=5, sticky='w')
        txtPasswordHint = StringVar()
        entPasswordHint = Entry(frameinfo, textvariable=txtPasswordHint, width=23, highlightthickness=1)
        entPasswordHint.grid(row=6, column=1, padx=10, pady=5, sticky='w')

        lblLastLogin = Label(frameinfo, text='Last Login: ')
        lblLastLogin.grid(row=7, column=0, padx=10, pady=5, sticky='w')
        txtLastLogin = StringVar()
        entLastLogin = Entry(frameinfo, textvariable=txtLastLogin, width=23, highlightthickness=1)
        entLastLogin.grid(row=7, column=1, padx=10, pady=5, sticky='w')

        #
        # txtAdmin = IntVar()
        # chbAdmin = Checkbutton(frameinfo, text='Admin', variable=txtAdmin)
        # chbAdmin.grid(row=5, column=1, padx=5, pady=10, sticky='w')

        lblRole = Label(frameinfo, text='Role ID: ')
        lblRole.grid(row=8, column=0, padx=10, pady=0, sticky='w')
        txtRole = StringVar()
        entRole = Combobox(frameinfo, width=20, textvariable=txtRole, state='readonly')
        entRole['values'] = rolesList
        entRole.grid(row=8, column=1, padx=10, pady=5, sticky='w')
        entRole.current()

        btnAdd = Button(frameinfo, text=' + ', font='tahoma 10 bold', borderwidth=2 , width=3, relief='groove',
                        command=addToList)
        btnAdd.grid(row=8, column=2, padx=10, pady=5)

        roles = ('a', 'b', 'c')
        roleVar = StringVar(value=roles)
        listbox = Listbox(frameinfo, listvariable=roleVar, height=5)
        listbox.grid(row=9, column=1, padx=30, pady=5, sticky='e')

        btnAddUser = Button(addUserfrm, text='Add User', width=20, relief='groove', command=insertUserCommand)
        btnAddUser.grid(row=6, column=0, padx=30, pady=10, sticky='w')

        btnBack = Button(addUserfrm, text='Back to Main', width=20, relief='groove', command=backToMain)
        btnBack.grid(row=6, column=0, padx=30, pady=10, sticky='e')
# endregion
        addUserfrm.mainloop()
