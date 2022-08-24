import tkinter.messagebox
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
        selectfrm.geometry('340x340')
        selectfrm.resizable(False, False)
        positionRight = int(selectfrm.winfo_screenwidth() / 2 - 340 / 2)
        positionDown = int(selectfrm.winfo_screenheight() / 2 - 340 / 2)
        selectfrm.geometry("+{}+{}".format(positionRight, positionDown))

        def AddCommand():
            selectfrm.destroy()
            studentui = StudentUI(self.User)
            studentui.studentFormLoad()

        def backToMain():
            selectfrm.destroy()
            from UserInterfaceLayer.MainForm import MainUI
            mainui = MainUI(self.User)
            mainui.mainFormLoad()

        def viewCommand():
            selected = listbox.curselection()[0]
            selectedValue = listbox.get(selected)
            selectedID = selectedValue.split(':')[0]
            if self.Table == 'Student':
                studentui = StudentViewUI(self.User, selectedID)
                studentui.studentViewFormLoad()

            if self.Table == 'Teacher':
                teacheri = TeacherUI(self.User)
                teacheri.teacherFormLoad()

            if self.Table == 'Employee':
                employeeui = EmployeeUI(self.User)
                employeeui.employeeFormLoad()

        def deleteCommand():
            selected = listbox.curselection()[0]
            selectedValue = listbox.get(selected)
            selectedID = selectedValue.split(':')[0]
            msgbox = tkinter.messagebox.askquestion('Delete', 'Do you want to delete ' + selectedValue + ' ?',
                                                    icon='warning')
            if msgbox == 'No':
                return

            if self.Table == 'Student':
                studentdb = StudentDB()
                studentdb.deleteStudent(selectedID)

                self.List = studentdb.readStudentList()
                listVar.set(self.List)

            # if self.Table == 'Teacher':
            #     teacheri = TeacherUI(self.User)
            #     teacheri.deleteStudent()
            #
            # if self.Table == 'Employee':
            #     employeeui = EmployeeUI(self.User)
            #     employeeui.deleteStudent()

        def EditCommand():
            selected = listbox.curselection()[0]
            selectedValue = listbox.get(selected)
            selectedID = selectedValue.split(':')[0]
            if self.Table == 'Student':
                studentui = StudentUI(self.User, selectedID)
                studentui.studentFormLoad()


            if self.Table == 'Teacher':
                teacheri = TeacherUI(self.User)
                teacheri.teacherFormLoad()

            if self.Table == 'Employee':
                employeeui = EmployeeUI(self.User)
                employeeui.employeeFormLoad()

        frameinfo = LabelFrame(selectfrm, text=' Select Form ')
        frameinfo.grid(row=0, column=0, padx=(20, 5), pady=10, sticky='w')
# region Widgets ...
        lblFullname = Label(frameinfo, text='Fullname :')
        lblFullname.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        txtFullname = StringVar()
        entFullname = Entry(frameinfo, textvariable=txtFullname, width=20, highlightthickness=1)
        entFullname.grid(row=0, column=1, padx=10, pady=5, sticky='w')

        btnSearch = Button(frameinfo, text='Search', borderwidth=2, width=2, relief='groove')
        btnSearch.grid(row=0, column=1, padx=(150, 5), pady=5, sticky='w')

        listVar = StringVar(value=self.List)
        listbox = Listbox(frameinfo, listvariable=listVar, height=15, borderwidth=2)
        listbox.grid(row=1, column=1, padx=10, pady=5, sticky='n')

        btnAdd = Button(selectfrm, text='Add', height=2, width=4, relief='groove', command=AddCommand)
        btnAdd.grid(row=0, column=1, padx=0, pady=(20, 5), sticky='n')

        btnView = Button(selectfrm, text='View', height=2, width=4, relief='groove', command=viewCommand)
        btnView.grid(row=0, column=1, padx=0, pady=(70, 0), sticky='n')

        btnEdit = Button(selectfrm, text='Edit', height=2, width=4, relief='groove', command=EditCommand)
        btnEdit.grid(row=0, column=1, padx=0, pady=(120, 0), sticky='n')

        btnDelete = Button(selectfrm, text='Delete', height=2, width=4, relief='groove', command=deleteCommand)
        btnDelete.grid(row=0, column=1, padx=0, pady=(170, 0), sticky='n')

        btnBack = Button(selectfrm, text='Back', height=2, width=4, relief='groove', command=backToMain)
        btnBack.grid(row=0, column=1, padx=0, pady=(220, 10), sticky='s')
# endregion
        selectfrm.mainloop()
