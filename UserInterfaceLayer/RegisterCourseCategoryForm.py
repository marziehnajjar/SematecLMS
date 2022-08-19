from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as msg
from UserInterfaceLayer import *
from DataAccessLayer import *
from tkcalendar import DateEntry
from Model import *


class RegisterCourseCategoryUI:

    def __init__(self, user: User):
        self.User = user

    def courseCategoryFormLoad(self):
        courseCategoryfrm = Tk()
        courseCategoryfrm.title('Register a Course Categoryfrm')
        courseCategoryfrm.geometry('420x130')
        courseCategoryfrm.resizable(0, 0)
        positionRight = int(courseCategoryfrm.winfo_screenwidth() / 2 - 420 / 2)
        positionDown = int(courseCategoryfrm.winfo_screenheight() / 2 - 130 / 2)
        courseCategoryfrm.geometry("+{}+{}".format(positionRight, positionDown))

        def backToMain():
            courseCategoryfrm.destroy()
            from UserInterfaceLayer.MainForm import MainUI
            mainui = MainUI(self.User)
            mainui.mainFormLoad()

        def insertCourseCategoryCommand():
            CategoryName = txtCategoryName.get()
            courseCategory = Model.CourseCategory(CategoryName)
            courseCategorydb = CourseCategoryDB(courseCategory)
            courseCategorydb.insertCourseCategory()

        frameinfo = LabelFrame(courseCategoryfrm, text=' Course Category Information ')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        lblCategoryName = Label(frameinfo, text='CategoryName: ')
        lblCategoryName.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        txtCategoryName = StringVar()
        entCategoryName = Entry(frameinfo, textvariable=txtCategoryName, width=40, highlightthickness=1)
        entCategoryName.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        btnRegisterStudent = Button(courseCategoryfrm, text='Register Course Category', width=20, relief='groove',
                                    command=insertCourseCategoryCommand)
        btnRegisterStudent.grid(row=11, column=0, padx=30, pady=10, sticky='w')

        btnBack = Button(courseCategoryfrm, text='Back to Main', width=20, relief='groove', command=backToMain)
        btnBack.grid(row=11, column=0, padx=30, pady=10, sticky='e')

        courseCategoryfrm.mainloop()
