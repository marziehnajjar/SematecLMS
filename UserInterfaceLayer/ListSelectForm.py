from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as msg
from tkcalendar import DateEntry
from UserInterfaceLayer import *
from DataAccessLayer import *
from Model import *
from BusinessLogicLayer import *


class ListSelectUI:
    def __init__(self, user: User, table):
        self.User = user
        self.List = []
        self.Table = table

        if table == 'Student':
            studentdb = StudentDB()
            self.List = studentdb.readStudentList()

        if table == 'Teacher':
            teacherdb = TeacherDB()
            self.List = teacherdb.readTeacherList()

        if table == 'Employee':
            employeedb = EmployeeDB()
            self.List = employeedb.readEmployeeList()

    def listSelectFormLoad(self):
        selectfrm = Tk()
        selectfrm.title('Select Form')
        selectfrm.geometry('330x370')
        selectfrm.resizable(False, False)
        positionRight = int(selectfrm.winfo_screenwidth() / 2 - 330 / 2)
        positionDown = int(selectfrm.winfo_screenheight() / 2 - 370 / 2)
        selectfrm.geometry("+{}+{}".format(positionRight, positionDown))

        def backToMain():
            selectfrm.destroy()
            from UserInterfaceLayer.MainForm import MainUI
            mainui = MainUI(self.User)
            mainui.mainFormLoad()

        def viewCommand():
            from UserInterfaceLayer.MainForm import MainUI

            selected = listbox.curselection()[0]
            selectedValue = listbox.get(selected)
            selectedID = selectedValue.split(':')[0]
            if self.Table == 'Student':
                studentui = StudentUI(self.User)
                studentui.studentFormLoad()

            if self.Table == 'Teacher':
                teacheri = TeacherUI(self.User)
                teacheri.teacherFormLoad()

            if self.Table == 'Employee':
                employeeui = EmployeeUI(self.User)
                employeeui.employeeFormLoad()

        frameinfo = LabelFrame(selectfrm, text=' Select Form ')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')
# region Widgets ...
        lblFullname = Label(frameinfo, text='Fullname :')
        lblFullname.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        txtFullname = StringVar()
        entFullname = Entry(frameinfo, textvariable=txtFullname, width=20, highlightthickness=1)
        entFullname.grid(row=0, column=1, padx=10, pady=5, sticky='w')

        btnSearch = Button(frameinfo, text='Search', borderwidth=2, width=6, relief='groove')
        btnSearch.grid(row=0, column=1, padx=(150, 5), pady=5, sticky='w')

        listVar = StringVar(value=self.List)
        listbox = Listbox(frameinfo, listvariable=listVar, height=15, borderwidth=2)
        listbox.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        btnView = Button(selectfrm, text='View', width=7, relief='groove', command=viewCommand)
        btnView.grid(row=2, column=0, padx=(20, 5), pady=5, sticky='w')

        btnEdit = Button(selectfrm, text='Edit', width=7, relief='groove', command=backToMain)
        btnEdit.grid(row=2, column=0, padx=(80, 0), pady=5, sticky='w')

        btnDelete = Button(selectfrm, text='Delete', width=7, relief='groove', command=backToMain)
        btnDelete.grid(row=2, column=0, padx=(140, 0), pady=5, sticky='w')

        btnBack = Button(selectfrm, text='Back', width=7, relief='groove', command=backToMain)
        btnBack.grid(row=2, column=0, padx=(220, 20), pady=5, sticky='e')
# endregion
        selectfrm.mainloop()
