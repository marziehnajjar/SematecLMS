from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as msg
from UserInterfaceLayer import *
from DataAccessLayer import *
from tkcalendar import DateEntry
from Model import *


class RegisterCourseUI:

    def __init__(self, user: User):
        self.User = user

    def courseFormLoad(self):
        coursefrm = Tk()
        coursefrm.title('Register a Course')
        coursefrm.geometry('350x230')
        coursefrm.resizable(0, 0)
        positionRight = int(coursefrm.winfo_screenwidth() / 2 - 350 / 2)
        positionDown = int(coursefrm.winfo_screenheight() / 2 - 230 / 2)
        coursefrm.geometry("+{}+{}".format(positionRight, positionDown))

        coursedb = CourseDB()
        courseCategoryList = coursedb.getCourseCategoryList()

        def backToMain():
            coursefrm.destroy()
            from UserInterfaceLayer.MainForm import MainUI
            mainui = MainUI(self.User)
            mainui.mainFormLoad()

        def insertCourseCommand():
            Description = txtDescription.get()
            Duration = txtDuration.get()
            CourseName = txtCourseName.get()
            CourseCategoryID = txtCourseCategoryName.get().split(' ')[0]

            course = Model.Course(CourseCategoryID, CourseName, Duration, Description)
            coursedbSave = CourseDB(course)
            coursedbSave.insertCourse()

        frameinfo = LabelFrame(coursefrm, text=' Course Information ')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')
# region Widgets ...
        lblCourseCategoryName = Label(frameinfo, text='Course Category Name: ')
        lblCourseCategoryName.grid(row=1, column=0, padx=10, pady=0, sticky='w')
        txtCourseCategoryName = StringVar()
        entCourseCategoryName = Combobox(frameinfo, width=20, textvariable=txtCourseCategoryName, state='readonly')
        entCourseCategoryName['values'] = courseCategoryList
        entCourseCategoryName.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        entCourseCategoryName.current()

        lblCourseName = Label(frameinfo, text='CourseName: ')
        lblCourseName.grid(row=2, column=0, padx=10, pady=0, sticky='w')
        txtCourseName = StringVar()
        entCourseName = Entry(frameinfo, textvariable=txtCourseName, width=20, highlightthickness=1)
        entCourseName.grid(row=2, column=1, padx=10, pady=0, sticky='w')

        lblDuration = Label(frameinfo, text='Duration: ')
        lblDuration.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        txtDuration = StringVar()
        entTDuration = Entry(frameinfo, textvariable=txtDuration, width=20, highlightthickness=1)
        entTDuration.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        lblDescription = Label(frameinfo, text='Description: ')
        lblDescription.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        txtDescription = StringVar()
        entDescription = Entry(frameinfo, textvariable=txtDescription, width=20, highlightthickness=1)
        entDescription.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        btnRegisterCourse = Button(coursefrm, text='Register Course', width=15, relief='groove',
                                   command=insertCourseCommand)
        btnRegisterCourse.grid(row=5, column=0, padx=30, pady=10, sticky='w')

        btnBack = Button(coursefrm, text='Back to Main', width=15, relief='groove', command=backToMain)
        btnBack.grid(row=5, column=0, padx=30, pady=10, sticky='e')
# endregion
        coursefrm.mainloop()

