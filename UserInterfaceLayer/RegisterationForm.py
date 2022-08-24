from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as msg
from UserInterfaceLayer import *
from DataAccessLayer import *
from tkcalendar import DateEntry
from Model import *


class RegisterationUI:

    def __init__(self, user: Model.User):
        self.User = user

    def registerationFormLoad(self):
        registerationfrm = Tk()
        registerationfrm.geometry('300x300')
        registerationfrm.title('Registeration')
        registerationfrm.resizable(False, False)
        positionRight = int(registerationfrm.winfo_screenwidth() / 2 - 300 / 2)
        positionDown = int(registerationfrm.winfo_screenheight() / 2 - 300 / 2)
        registerationfrm.geometry("+{}+{}".format(positionRight, positionDown))

        def backToMain():
            registerationfrm.destroy()
            from UserInterfaceLayer.MainForm import MainUI
            mainui = MainUI(self.User)
            mainui.mainFormLoad()

        def insertRowCommand():

            StudentID = txtStudentID.get().split(' ')[0]
            CourseID = txtCourseID.get().split(' ')[0]
            TeacherID = txtTeacherID.get().split(' ')[0]
            YearQuarter = txtYearQuarter.get()
            Score = txtScore.get()

            registerationSave = Model.Registeration(StudentID, CourseID, TeacherID, YearQuarter, Score)
            registerdbSave = RegisterationDB(registerationSave)
            registerdbSave.insertRow()

        registerationdb = RegisterationDB()
        courseList = registerationdb.getCourseList()
        teacherList = registerationdb.getTeacherList()
        studentList = registerationdb.getStudentList()

        frameinfo = LabelFrame(registerationfrm, text=' Registeration Information ')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')
# region Widgets ...
        lblStudentID = Label(frameinfo, text='Student: ')
        lblStudentID.grid(row=1, column=0, padx=10, pady=0, sticky='w')
        txtStudentID = StringVar()
        cmbStudentID = Combobox(frameinfo, width=20, textvariable=txtStudentID, state='readonly')
        cmbStudentID['values'] = studentList
        cmbStudentID.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        cmbStudentID.current()

        lblTeacherID = Label(frameinfo, text='Teacher: ')
        lblTeacherID.grid(row=2, column=0, padx=10, pady=0, sticky='w')
        txtTeacherID = StringVar()
        cmbTeacherID = Combobox(frameinfo, width=20, textvariable=txtTeacherID, state='readonly')
        cmbTeacherID['values'] = teacherList
        cmbTeacherID.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        cmbTeacherID.current()

        lblCourseID = Label(frameinfo, text='Course: ')
        lblCourseID.grid(row=3, column=0, padx=10, pady=0, sticky='w')
        txtCourseID = StringVar()
        cmbCourseID = Combobox(frameinfo, width=20, textvariable=txtCourseID, state='readonly')
        cmbCourseID['values'] = courseList
        cmbCourseID.grid(row=3, column=1, padx=10, pady=10, sticky='w')
        cmbCourseID.current()

        lblYearQuarter = Label(frameinfo, text='YearQuarter: ')
        lblYearQuarter.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        txtYearQuarter = StringVar()
        cmbYearQuarter = Combobox(frameinfo, width=20, textvariable=txtYearQuarter, state='readonly')
        arrayYearQuarter = []
        with open('DB/YearQuarter.csv', mode='r') as myfile:
            for line in myfile.readlines():
                temp = line.rstrip('\n')
                arrayYearQuarter.append(temp)
        cmbYearQuarter['values'] = arrayYearQuarter
        cmbYearQuarter.grid(row=4, column=1, padx=10, pady=10, sticky='w')
        cmbYearQuarter.current()

        lblScore = Label(frameinfo, text='Score: ')
        lblScore.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        txtScore = StringVar()
        entScore = Entry(frameinfo, textvariable=txtScore, width=10, highlightthickness=1)
        entScore.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        btnRegisteration = Button(registerationfrm, text='Register', width=15, relief='groove',
                                  command=insertRowCommand)
        btnRegisteration.grid(row=6, column=0, padx=30, pady=10, sticky='w')

        btnBack = Button(registerationfrm, text='Back to Main', width=15, relief='groove', command=backToMain)
        btnBack.grid(row=6, column=0, padx=30, pady=10, sticky='e')
# endregion
        registerationfrm.mainloop()
