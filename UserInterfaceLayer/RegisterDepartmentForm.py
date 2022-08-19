from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as msg
from UserInterfaceLayer import *
from DataAccessLayer import *
from tkcalendar import DateEntry
from Model import *


class RegisterDepartmentUI:
    def __init__(self, user: User):
        self.User = user

    def departmentFormLoad(self):
        departmentfrm = Tk()
        departmentfrm.geometry('440x180')
        departmentfrm.title('Register a Department')
        departmentfrm.resizable(0, 0)
        positionRight = int(departmentfrm.winfo_screenwidth() / 2 - 440 / 2)
        positionDown = int(departmentfrm.winfo_screenheight() / 2 - 180 / 2)
        departmentfrm.geometry("+{}+{}".format(positionRight, positionDown))

        def backToMain():
            departmentfrm.destroy()
            from UserInterfaceLayer.MainForm import MainUI
            mainui = MainUI(self.User)
            mainui.mainFormLoad()

        def insertDepartmentCommand():
            DepartmentName = txtDepartmentName.get()
            department = Model.Department(DepartmentName)
            departmentdb = DepartmentDB(department)
            departmentdb.insertDepartment()

        frameinfo = LabelFrame(departmentfrm, text=' Department Information ')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        lblDepartmentName = Label(frameinfo, text='DepartmentName: ')
        lblDepartmentName.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        txtDepartmentName = StringVar()
        entDepartmentName = Entry(frameinfo, textvariable=txtDepartmentName, width=40, highlightthickness=1)
        entDepartmentName.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        lblDescription = Label(frameinfo, text='Description: ')
        lblDescription.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        txtDescription = StringVar()
        entDescription = Entry(frameinfo, textvariable=txtDescription, width=40, highlightthickness=1)
        entDescription.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        btnRegisterStudent = Button(departmentfrm, text='Register Department', width=20, relief='groove',
                                    command=insertDepartmentCommand)
        btnRegisterStudent.grid(row=3, column=0, padx=30, pady=10, sticky='w')

        btnBack = Button(departmentfrm, text='Back to Main', width=20, relief='groove', command=backToMain)
        btnBack.grid(row=3, column=0, padx=30, pady=10, sticky='e')

        departmentfrm.mainloop()
