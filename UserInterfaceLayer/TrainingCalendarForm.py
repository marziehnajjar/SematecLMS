from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as msg
from UserInterfaceLayer import *
from DataAccessLayer import *
from tkcalendar import DateEntry
from Model import *


class TrainingCalendarUI:

    def __init__(self, user: Model.User):
        self.User = user

    def trainingCalendarFormLoad(self):
        registerationfrm = Tk()
        registerationfrm.geometry('280x210')
        registerationfrm.title('Training Calendar')
        registerationfrm.resizable(None, None)
        positionRight = int(registerationfrm.winfo_screenwidth() / 2 - 280 / 2)
        positionDown = int(registerationfrm.winfo_screenheight() / 2 - 210 / 2)
        registerationfrm.geometry("+{}+{}".format(positionRight, positionDown))

        def backToMain():
            registerationfrm.destroy()
            from UserInterfaceLayer.MainForm import MainUI
            mainui = MainUI(self.User)
            mainui.mainFormLoad()

        def getRowCommand():
            CourseID = txtCourseID.get().split(' ')[0]
            TeacherID = txtTeacherID.get().split(' ')[0]
            Status = txtStatus

            registerationSave = Model.Registeration(CourseID, TeacherID, Status)
            registerdbSave = RegisterationDB(registerationSave)
            registerdbSave.insertRow()

        registerationdb = RegisterationDB()
        courseList = registerationdb.getCourseList()
        teacherList = registerationdb.getTeacherList()
        studentList = registerationdb.getStudentList()

        frameinfo = LabelFrame(registerationfrm, text=' Training Calendar ')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')
# region Widgets ...

        lblTeacherID = Label(frameinfo, text='Teacher: ')
        lblTeacherID.grid(row=0, column=0, padx=10, pady=0, sticky='w')
        txtTeacherID = StringVar()
        cmbTeacherID = Combobox(frameinfo, width=20, textvariable=txtTeacherID, state='readonly')
        cmbTeacherID['values'] = teacherList
        cmbTeacherID.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        cmbTeacherID.current()

        lblCourseID = Label(frameinfo, text='Course: ')
        lblCourseID.grid(row=1, column=0, padx=10, pady=0, sticky='w')
        txtCourseID = StringVar()
        cmbCourseID = Combobox(frameinfo, width=20, textvariable=txtCourseID, state='readonly')
        cmbCourseID['values'] = courseList
        cmbCourseID.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        cmbCourseID.current()

        lblStatus = Label(frameinfo, text='Status: ')
        lblStatus.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        txtStatus = StringVar()
        entStatus = Combobox(frameinfo, textvariable=txtStatus, width=20, state='readonly')
        arrayStatus = ['ثبت نام', 'پایان یافته', 'درحال برگزاری']
        entStatus['values'] = arrayStatus
        entStatus.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        entStatus.current()


        btnRegisteration = Button(registerationfrm, text='Register', width=12, relief='groove',
                                  command=getRowCommand)
        btnRegisteration.grid(row=3, column=0, padx=30, pady=10, sticky='w')

        btnBack = Button(registerationfrm, text='Back to Main', width=12, relief='groove', command=backToMain)
        btnBack.grid(row=3, column=0, padx=30, pady=10, sticky='e')
# endregion
        registerationfrm.mainloop()
