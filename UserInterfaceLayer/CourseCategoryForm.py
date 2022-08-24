from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as msg
from UserInterfaceLayer import *
from DataAccessLayer import *
from tkcalendar import DateEntry
from Model import *


class CourseCategoryUI:

    def __init__(self, user: User):
        self.User = user

    def courseCategoryFormLoad(self):
        courseCategoryfrm = Tk()
        courseCategoryfrm.title('Register a Course Categoryfrm')
        courseCategoryfrm.geometry('460x150')
        courseCategoryfrm.resizable(False, False)
        positionRight = int(courseCategoryfrm.winfo_screenwidth() / 2 - 460 / 2)
        positionDown = int(courseCategoryfrm.winfo_screenheight() / 2 - 150 / 2)
        courseCategoryfrm.geometry("+{}+{}".format(positionRight, positionDown))

        def backToMain():
            courseCategoryfrm.destroy()
            from UserInterfaceLayer.MainForm import MainUI
            mainui = MainUI(self.User)
            mainui.mainFormLoad()

        def getCourseCategoryCommand():
            CourseCategoryName = txtCourseCategoryName.get()

            courseCategory = Model.CourseCategory(CourseCategoryName)

            courseCategorydb = CourseCategoryDB(courseCategory)
            courseCategorydb.insertCourseCategory()

        frameinfo = LabelFrame(courseCategoryfrm, text=' Course Category Information ')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        lblID = Label(frameinfo, text='Course Category ID : ')
        lblID.grid(row=0, column=0, padx=10, pady=5, sticky='w')

        lblCourseCategoryName = Label(frameinfo, text='Course Category Name: ')
        lblCourseCategoryName.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        txtCourseCategoryName = StringVar()
        entCourseCategoryName = Entry(frameinfo, textvariable=txtCourseCategoryName, width=40, highlightthickness=1)
        entCourseCategoryName.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        btnRegisterCourseCategory = Button(courseCategoryfrm, text='Register Course Category', width=20, relief='groove'
                                           , command=getCourseCategoryCommand)
        btnRegisterCourseCategory.grid(row=11, column=0, padx=30, pady=5, sticky='w')

        btnBack = Button(courseCategoryfrm, text='Back to Main', width=20, relief='groove', command=backToMain)
        btnBack.grid(row=11, column=0, padx=30, pady=10, sticky='e')

        courseCategoryfrm.mainloop()
