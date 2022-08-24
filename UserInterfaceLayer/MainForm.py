from UserInterfaceLayer import *
from Model import *
from tkinter import *
from tkinter import messagebox as msg
from time import strftime


class MainUI:
    def __init__(self, user: User = None):
        self.User = user

    def mainFormLoad(self):
        mainfrm = Tk()
        mainfrm.title('Main Form')
        mainfrm.iconbitmap('UserInterfaceLayer/icon/Main.ico')
        mainfrm.geometry('500x530')
        mainfrm.resizable(False, False)
        positionRight = int(mainfrm.winfo_screenwidth() / 2 - 500 / 2)
        positionDown = int(mainfrm.winfo_screenheight() / 2 - 530 / 2)
        mainfrm.geometry("+{}+{}".format(positionRight, positionDown))
# TODO: User Profile ویرایش اطلاعات کاربری
# TODO: logout button

# region Functions ...
        def time():
            # strftime() -> raed time(str)
            string = strftime('%a | %I:%M:%S %p')
            # config() -> put time(str) in label
            clockLabel.config(text=string)
            # after() -> update label after 1000 ms with time function
            clockLabel.after(1000, time)

        def profileCommand():
            from UserInterfaceLayer.ProfileForm import ProfileUI
            profile = ProfileUI(self.User)
            profile.profileFormLoad()

        def LogoutCommand():
            mainfrm.destroy()
            login = LoginUI()
            login.loginFormLoad()

        def studentCommand():
            mainfrm.destroy()
            from UserInterfaceLayer.ListSelectForm import ListSelectUI
            listSelectUI = ListSelectUI(self.User, table='Student')
            listSelectUI.listSelectFormLoad()

        def teacherCommand():
            mainfrm.destroy()
            from UserInterfaceLayer.ListSelectForm import ListSelectUI
            listSelectUI = ListSelectUI(self.User, table='Teacher')
            listSelectUI.listSelectFormLoad()

        def employeeCommand():
            mainfrm.destroy()
            from UserInterfaceLayer.ListSelectForm import ListSelectUI
            listSelectUI = ListSelectUI(self.User, table='Employee')
            listSelectUI.listSelectFormLoad()

        def departmentCommand():
            mainfrm.destroy()
            from UserInterfaceLayer.DepartmentForm import DepartmentUI
            departmentui = DepartmentUI(self.User)
            departmentui.departmentFormLoad()

        def courseCategoryCommand():
            mainfrm.destroy()
            from UserInterfaceLayer.CourseCategoryForm import CourseCategoryUI
            courseCategoryui = CourseCategoryUI(self.User)
            courseCategoryui.courseCategoryFormLoad()

        def courseCommand():
            mainfrm.destroy()
            from UserInterfaceLayer.CourseForm import CourseUI
            courseui = CourseUI(self.User)
            courseui.courseFormLoad()

        def registerationCommand():
            mainfrm.destroy()
            from UserInterfaceLayer.RegisterationForm import RegisterationUI
            registerationui = RegisterationUI(self.User)
            registerationui.registerationFormLoad()

        # def registerationCommand():
        #     mainfrm.destroy()
        #     from UserInterfaceLayer.RegisterationForm import RegisterationUI
        #     registerationui = RegisterationUI(self.User)
        #     registerationui.registerationFormLoad()

        def trainingCalendarCommand():
            mainfrm.destroy()
            from UserInterfaceLayer.TrainingCalendarForm import TrainingCalendarUI
            trainingCalendarui = TrainingCalendarUI(self.User)
            trainingCalendarui.trainingCalendarFormLoad()

        def contractCommand():
            pass
            # mainfrm.destroy()
            # from UserInterfaceLayer.ContractForm import ContractUI
            # contractui = ContractUI(self.User)
            # contractui.contractFormLoad()

        def userCommand():
            mainfrm.destroy()
            from UserInterfaceLayer.UserForm import UserUI
            userui = UserUI(self.User)
            userui.userFormLoad()
# endregion

# region Images ...
        imgStudent = PhotoImage(file='UserInterfaceLayer/icon/student.png')
        imgTeacher = PhotoImage(file='UserInterfaceLayer/icon/presentation.png')
        imgEmployee = PhotoImage(file='UserInterfaceLayer/icon/Employee.png')
        imgDepartment = PhotoImage(file='UserInterfaceLayer/icon/university.png')
        imgCourse = PhotoImage(file='UserInterfaceLayer/icon/open-book.png')
        imgCourseCategory = PhotoImage(file='UserInterfaceLayer/icon/book.png')
        imgRegisteration = PhotoImage(file='UserInterfaceLayer/icon/Order.png')
        imgUser = PhotoImage(file='UserInterfaceLayer/icon/add-user.png')
        imgAboutUs = PhotoImage(file='UserInterfaceLayer/icon/info.png')
# endregion

        clockLabel = Label(mainfrm, font=('calibri', 10, 'bold'), foreground='black')
        clockLabel.grid(row=0, column=0, padx=20, pady=10, sticky='w')
        time()

        btnProfile = Button(mainfrm, text='Profile', height=1, width=8, relief='groove', command=profileCommand,
                            font='Tahoma 10 bold')
        btnProfile.grid(row=0, column=0, padx=100, pady=10, sticky='e')

        btnLogout = Button(mainfrm, text='Logout', fg='red', height=1, width=8, relief='groove', command=LogoutCommand,
                           font='Tahoma 10 bold')
        btnLogout.grid(row=0, column=0, padx=20, pady=10, sticky='e')

        frameinfo = LabelFrame(mainfrm, text=f'Welcome Dear {self.User.FirstName}')
        frameinfo.grid(row=1, column=0, padx=10, pady=10, sticky='w')

# region Buttons ...
        btnStudent = Button(frameinfo, text='Student', image=imgStudent, compound=TOP, height=100, width=100, pady=10,
                            relief='groove', command=studentCommand)
        btnStudent.grid(row=0, rowspan=2, column=0, columnspan=3, padx=5, pady=10)

        btnTeacher = Button(frameinfo, text='Teacher', image=imgTeacher, compound=TOP, height=100, width=100,
                            relief='groove', pady=10, command=teacherCommand)
        btnTeacher.grid(row=0, rowspan=2, column=3, columnspan=3, padx=5, pady=10)

        btnEmployee = Button(frameinfo, text='Employee', image=imgEmployee, compound=TOP, height=100, width=100,
                             relief='groove', pady=10, command=employeeCommand)
        btnEmployee.grid(row=0, rowspan=2, column=6, columnspan=3, padx=5, pady=10)

        btnDepartment = Button(frameinfo, text='Department', image=imgDepartment, compound=TOP, height=100, width=100,
                               relief='groove', pady=10, command=departmentCommand)
        btnDepartment.grid(row=0, rowspan=2, column=9, columnspan=3, padx=5, pady=10)

        btnCourseCategory = Button(frameinfo, text='CourseCategory', image=imgCourseCategory, compound=TOP, height=100,
                                   width=100, relief='groove', pady=10, command=courseCategoryCommand)
        btnCourseCategory.grid(row=3, rowspan=2, column=0, columnspan=3, padx=5, pady=10)

        btnCourse = Button(frameinfo, text='Course', image=imgCourse, compound=TOP, height=100, width=100,
                           relief='groove', pady=10, command=courseCommand)
        btnCourse.grid(row=3, rowspan=2, column=3, columnspan=3, padx=5, pady=10)

        btnRegisteration = Button(frameinfo, text='Registeration', image=imgRegisteration, compound=TOP, height=100,
                                  width=100, relief='groove', pady=10, command=registerationCommand)
        btnRegisteration.grid(row=3, rowspan=2, column=6, columnspan=3, padx=5, pady=10)

        btnPDF = Button(frameinfo, text='PDF', image=imgAboutUs, compound=TOP, height=100, width=100, relief='groove',
                        pady=10,)
        btnPDF.grid(row=3, rowspan=2, column=9, columnspan=3, padx=5, pady=10)

        btnTrainingCalendar = Button(frameinfo, text='TrainingCalendar', image=imgAboutUs, compound=TOP, height=100,
                                     width=100, relief='groove', pady=10, command=trainingCalendarCommand)
        btnTrainingCalendar.grid(row=6, rowspan=2, column=0, columnspan=3, padx=5, pady=10)

        btnContract = Button(frameinfo, text='Contract', image=imgAboutUs, compound=TOP, height=100, width=100,
                             relief='groove', pady=10, command=contractCommand)
        btnContract.grid(row=6, rowspan=2, column=3, columnspan=3, padx=5, pady=10)

        btn = Button(frameinfo, text='BTN', image=imgAboutUs, compound=TOP, height=100, width=100, relief='groove',
                     pady=10,)
        btn.grid(row=6, rowspan=2, column=6, columnspan=3, padx=5, pady=10)

        btnAddUser = Button(frameinfo, text='User', image=imgUser, compound=TOP, height=100, width=100, relief='groove',
                            pady=10,
                            command=userCommand)
        btnAddUser.grid(row=6, rowspan=2, column=9, columnspan=3, padx=5, pady=10)

# endregion
        mainfrm.mainloop()
