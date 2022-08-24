from tkinter import messagebox as msg
from tkinter import *
import sqlite3
from Model import *


class LoginUI:
    def __init__(self):
        pass

    def loginFormLoad(self):
        loginfrm = Tk()
        loginfrm.attributes('-toolwindow', 'True')
        loginfrm.title('Login Form')
        loginfrm.iconbitmap('login.ico')
        loginfrm.geometry('290x340')
        loginfrm.resizable(False, False)
        positionRight = int(loginfrm.winfo_screenwidth() / 2 - 290 / 2)
        positionDown = int(loginfrm.winfo_screenheight() / 2 - 340 / 2)
        loginfrm.geometry("+{}+{}".format(positionRight, positionDown))

        def checkLogin():
            """
             input: Username , Password
             task: check Username , Password with User table in DB
             return: destroy the Login Form & Load the Main Form
            """
            # TODO: move to data access layer
            # TODO: SQL Server, SP
            # TODO: hashbytes password
            checkUserName = txtUserName.get()
            checkPassword = txtPassword.get()
            checkUserName = "vahidgh"
            checkPassword = "1360"

            # Connect to Database :
            dbName = 'DB/Sematec.db'
            # Select from table (in Database) :
            query = 'SELECT * FROM User WHERE UserName=? AND Password=?'
            params = (checkUserName, checkPassword)
            # Create a connection , input : database name = dbName :
            with sqlite3.Connection(dbName) as connection:
                # Create a cursor for select, insert, delete, update :
                cursor = connection.cursor()
                # execute = do, run, perform
                cursor.execute(query, params)
                # fetchall = fetches all , fetches = go and get Sth, bring :
                userList = cursor.fetchall()
                # output of fetchall -> list
                # committing the current transaction :
                connection.commit()
                # userList = [(,), (,), (,)] [(ID, firstName, lastName, userName, password, admin) , ()] -> User Table
            if len(userList) > 0:
                # userList[0] = userInfo = (ID, firstName, lastName, userName, password, admin)
                userInfo = userList[0]
                # print(userList[0])
                user = User(userName=checkUserName, password=checkPassword, firstName=userInfo[1], lastName=userInfo[2])
                # if int(userInfo[5]) == 1:
                #     print('Admin')
                loginfrm.destroy()
                from UserInterfaceLayer.MainForm import MainUI
                mainui = MainUI(user)
                mainui.mainFormLoad()

            else:
                msg.showerror('error', 'username or password is incorrect !!!')

        imglogin = PhotoImage(file='UserInterfaceLayer/icon/password.png')    # Relative Path

        lblLoginImage = Label(loginfrm, image=imglogin)
        lblLoginImage.grid(row=0, column=0, padx=20, pady=10)

        txtUserName = StringVar(loginfrm, value='UserName')
        entUserName = Entry(loginfrm, textvariable=txtUserName, width=40, highlightthickness=1, justify='center')
        entUserName.grid(row=1, column=0, padx=20, pady=10)

        txtPassword = StringVar(loginfrm, value='Password')
        entPassword = Entry(loginfrm, textvariable=txtPassword, width=40, highlightthickness=1, show='*',
                            justify='center')
        entPassword.grid(row=2, column=0, padx=20, pady=10)

        txtDatabase = IntVar()
        rdSQLite = Radiobutton(loginfrm, text='SQLite', variable=txtDatabase, value=1)
        rdSQLite.grid(row=3, column=0, padx=40, pady=10, sticky='w')
        rdSQLServer = Radiobutton(loginfrm, text='SQL Server', variable=txtDatabase, value=2)
        rdSQLServer.grid(row=3, column=0, padx=40, pady=10, sticky='e')

        btn = Button(loginfrm, text='Login', width=33, relief='groove', font='Tahoma 10', command=checkLogin)
        btn.grid(row=4, column=0, padx=20, pady=10)

        loginfrm.mainloop()
