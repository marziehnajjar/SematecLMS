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
        mainfrm.geometry('480x480')
        mainfrm.resizable(False, False)
        positionRight = int(mainfrm.winfo_screenwidth() / 2 - 480 / 2)
        positionDown = int(mainfrm.winfo_screenheight() / 2 - 480 / 2)
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

        # region Student
        def AddStudentCommand():
            mainfrm.destroy()
            from UserInterfaceLayer.StudentForm import StudentUI
            studentui = StudentUI(self.User)
            studentui.studentFormLoad()

        def ViewStudentCommand():
            mainfrm.destroy()
            from UserInterfaceLayer.ListSelectForm import ListSelectUI
            listSelectUI = ListSelectUI(self.User, table='Student')
            listSelectUI.listSelectFormLoad()

        # endregion

        # region Teacher
        def AddTeacherCommand():
            mainfrm.destroy()
            from UserInterfaceLayer.TeacherForm import TeacherUI
            teacherui = TeacherUI(self.User)
            teacherui.teacherFormLoad()

        def ViewTeacherCommand():
            mainfrm.destroy()
            from UserInterfaceLayer.ListSelectForm import ListSelectUI
            listSelectUI = ListSelectUI(self.User, table='Teacher')
            listSelectUI.listSelectFormLoad()

        # endregion

        # region Employee
        def AddEmployeeCommand():
            mainfrm.destroy()
            from UserInterfaceLayer.EmployeeForm import EmployeeUI
            employeeui = EmployeeUI(self.User)
            employeeui.employeeFormLoad()

        def ViewEmployeeCommand():
            mainfrm.destroy()
            from UserInterfaceLayer.ListSelectForm import ListSelectUI
            listSelectUI = ListSelectUI(self.User, table='Employee')
            listSelectUI.listSelectFormLoad()

        # endregion

        # region Department
        def AddDepartmentCommand():
            mainfrm.destroy()
            from UserInterfaceLayer.DepartmentForm import DepartmentUI
            departmentui = DepartmentUI(self.User)
            departmentui.departmentFormLoad()

        def EditDepartmentCommand():
            pass

        def ViewDepartmentCommand():
            pass

        # endregion

        # region CourseCategory
        def AddCourseCategoryCommand():
            mainfrm.destroy()
            from UserInterfaceLayer.CourseCategoryForm import CourseCategoryUI
            courseCategoryui = CourseCategoryUI(self.User)
            courseCategoryui.courseCategoryFormLoad()

        def EditCourseCategoryCommand():
            pass

        def ViewCourseCategoryCommand():
            pass

        # endregion

        # region Course
        def AddCourseCommand():
            mainfrm.destroy()
            from UserInterfaceLayer.CourseForm import CourseUI
            courseui = CourseUI(self.User)
            courseui.courseFormLoad()

        def EditCourseCommand():
            pass

        def ViewCourseCommand():
            pass

        # endregion

        # region Registeration
        def AddRegisterationCommand():
            mainfrm.destroy()
            from UserInterfaceLayer.RegisterationForm import RegisterationUI
            registerationui = RegisterationUI(self.User)
            registerationui.registerationFormLoad()

        def EditRegisterationCommand():
            pass

        def ViewRegisterationCommand():
            pass

        # endregion

        # region PDF
        # def AddRegisterationCommand():
        #     mainfrm.destroy()
        #     from UserInterfaceLayer.RegisterationForm import RegisterationUI
        #     registerationui = RegisterationUI(self.User)
        #     registerationui.registerationFormLoad()
        #
        # def EditRegisterationCommand():
        #     pass
        #
        # def ViewRegisterationCommand():
        #     pass

        # endregion

        # region TrainingCalendar
        def AddTrainingCalendarCommand():
            mainfrm.destroy()
            from UserInterfaceLayer.TrainingCalendarForm import TrainingCalendarUI
            trainingCalendarui = TrainingCalendarUI(self.User)
            trainingCalendarui.trainingCalendarFormLoad()

        def EditTrainingCalendarCommand():
            pass

        def ViewTrainingCalendarCommand():
            pass

        # endregion

        # region Contract
        def AddContractCommand():
            pass
            # mainfrm.destroy()
            # from UserInterfaceLayer.ContractForm import ContractUI
            # contractui = ContractUI(self.User)
            # contractui.contractFormLoad()

        def EditContractCommand():
            pass

        def ViewContractCommand():
            pass

        # endregion

        # region User
        def AddUserCommand():
            mainfrm.destroy()
            from UserInterfaceLayer.UserForm import UserUI
            userui = UserUI(self.User)
            userui.userFormLoad()

        def EditUserCommand():
            pass

        def ViewUserCommand():
            pass

        # endregion
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
        # region Student
        lblStudent = Label(frameinfo, image=imgStudent)
        lblStudent.grid(row=0, rowspan=2, column=0, columnspan=3, padx=15, pady=10)

        btnAddStudent = Button(frameinfo, text='A', height=1, width=2, relief='groove', command=AddStudentCommand)
        btnAddStudent.grid(row=2, column=0, padx=0, pady=0, sticky='e')

        btnViewStudent = Button(frameinfo, text='V', height=1, width=2, relief='groove', command=ViewStudentCommand)
        btnViewStudent.grid(row=2, column=2, padx=0, pady=0, sticky='w')
        # endregion
        # region Teacher
        lblTeacher = Label(frameinfo, image=imgTeacher)
        lblTeacher.grid(row=0, rowspan=2, column=3, columnspan=3, padx=15, pady=10)

        btnAddTeacher = Button(frameinfo, text='A', height=1, width=2, relief='groove', command=AddTeacherCommand)
        btnAddTeacher.grid(row=2, column=3, padx=0, pady=0, sticky='e')

        btnViewTeacher = Button(frameinfo, text='V', height=1, width=2, relief='groove', command=ViewTeacherCommand)
        btnViewTeacher.grid(row=2, column=5, padx=0, pady=0, sticky='w')
        # endregion
        # region Employee
        lblEmployee = Label(frameinfo, image=imgEmployee)
        lblEmployee.grid(row=0, rowspan=2, column=6, columnspan=3, padx=15, pady=10)

        btnAddEmployee = Button(frameinfo, text='A', height=1, width=2, relief='groove', command=AddEmployeeCommand)
        btnAddEmployee.grid(row=2, column=6, padx=0, pady=0, sticky='e')

        btnViewEmployee = Button(frameinfo, text='V', height=1, width=2, relief='groove', command=ViewEmployeeCommand)
        btnViewEmployee.grid(row=2, column=8, padx=0, pady=0, sticky='w')
        # endregion
        # region Department
        lblDepartment = Label(frameinfo, image=imgDepartment)
        lblDepartment.grid(row=0, rowspan=2, column=9, columnspan=3, padx=15, pady=10)

        btnAddDepartment = Button(frameinfo, text='A', height=1, width=2, relief='groove',
                                  command=AddDepartmentCommand)
        btnAddDepartment.grid(row=2, column=9, padx=0, pady=0, sticky='e')

        btnEditDepartment = Button(frameinfo, text='E', height=1, width=2, relief='groove',
                                   command=EditDepartmentCommand)
        btnEditDepartment.grid(row=2, column=10, padx=0, pady=0)

        btnViewDepartment = Button(frameinfo, text='V', height=1, width=2, relief='groove',
                                   command=ViewDepartmentCommand)
        btnViewDepartment.grid(row=2, column=11, padx=0, pady=0, sticky='w')
        # endregion
        # region CourseCategory
        lblCourseCategory = Label(frameinfo, image=imgCourseCategory)
        lblCourseCategory.grid(row=3, rowspan=2, column=0, columnspan=3, padx=20, pady=10)

        btnAddCourseCategory = Button(frameinfo, text='A', height=1, width=2, relief='groove',
                                      command=AddCourseCategoryCommand)
        btnAddCourseCategory.grid(row=5, column=0, padx=0, pady=0, sticky='e')

        btnEditCourseCategory = Button(frameinfo, text='E', height=1, width=2, relief='groove',
                                       command=EditCourseCategoryCommand)
        btnEditCourseCategory.grid(row=5, column=1, padx=0, pady=0)

        btnViewCourseCategory = Button(frameinfo, text='V', height=1, width=2, relief='groove',
                                       command=ViewCourseCategoryCommand)
        btnViewCourseCategory.grid(row=5, column=2, padx=0, pady=0, sticky='w')
        # endregion
        # region Course
        lblCourse = Label(frameinfo, image=imgCourse)
        lblCourse.grid(row=3, rowspan=2, column=3, columnspan=3, padx=20, pady=10)

        btnAddCourse = Button(frameinfo, text='A', height=1, width=2, relief='groove', command=AddCourseCommand)
        btnAddCourse.grid(row=5, column=3, padx=0, pady=0, sticky='e')

        btnEditCourse = Button(frameinfo, text='E', height=1, width=2, relief='groove', command=EditCourseCommand)
        btnEditCourse.grid(row=5, column=4, padx=0, pady=0)

        btnViewCourse = Button(frameinfo, text='V', height=1, width=2, relief='groove', command=ViewCourseCommand)
        btnViewCourse.grid(row=5, column=5, padx=0, pady=0, sticky='w')
        # endregion
        # region Registeration
        lblRegisteration = Label(frameinfo, image=imgRegisteration)
        lblRegisteration.grid(row=3, rowspan=2, column=6, columnspan=3, padx=20, pady=10)

        btnAddRegisteration = Button(frameinfo, text='A', height=1, width=2, relief='groove',
                                     command=AddRegisterationCommand)
        btnAddRegisteration.grid(row=5, column=6, padx=0, pady=0, sticky='e')

        btnEditRegisteration = Button(frameinfo, text='E', height=1, width=2, relief='groove',
                                      command=EditRegisterationCommand)
        btnEditRegisteration.grid(row=5, column=7, padx=0, pady=0)

        btnViewRegisteration = Button(frameinfo, text='V', height=1, width=2, relief='groove',
                                      command=ViewRegisterationCommand)
        btnViewRegisteration.grid(row=5, column=8, padx=0, pady=0, sticky='w')
        # endregion
        # region PDF
        lblPDF = Label(frameinfo, text='PDF')
        lblPDF.grid(row=3, rowspan=2, column=9, columnspan=3, padx=20, pady=10)

        btnAddUser = Button(frameinfo, text='A', height=1, width=2, relief='groove')
        btnAddUser.grid(row=5, column=9, padx=2, pady=0)

        btnEditUser = Button(frameinfo, text='E', height=1, width=2, relief='groove')
        btnEditUser.grid(row=5, column=10, padx=2, pady=0)

        btnViewUser = Button(frameinfo, text='V', height=1, width=2, relief='groove')
        btnViewUser.grid(row=5, column=11, padx=2, pady=0)
        # endregion
        # region TrainingCalendar
        lblTrainingCalendar = Label(frameinfo, text='TrainingCalendar')
        lblTrainingCalendar.grid(row=6, rowspan=2, column=0, columnspan=3, padx=20, pady=10)

        btnAddTrainingCalendar = Button(frameinfo, text='A', height=1, width=2, relief='groove',
                                        command=AddTrainingCalendarCommand)
        btnAddTrainingCalendar.grid(row=8, column=0, padx=0, pady=0, sticky='e')

        btnEditTrainingCalendar = Button(frameinfo, text='E', height=1, width=2, relief='groove',
                                         command=EditTrainingCalendarCommand)
        btnEditTrainingCalendar.grid(row=8, column=1, padx=0, pady=0)

        btnViewTrainingCalendar = Button(frameinfo, text='V', height=1, width=2, relief='groove',
                                         command=ViewTrainingCalendarCommand)
        btnViewTrainingCalendar.grid(row=8, column=2, padx=0, pady=0, sticky='w')
        # endregion
        # region Contract
        lblContract = Label(frameinfo, text='Contrct')
        lblContract.grid(row=6, rowspan=2, column=3, columnspan=3, padx=20, pady=10)

        btnAddContract = Button(frameinfo, text='A', height=1, width=2, relief='groove', command=AddContractCommand)
        btnAddContract.grid(row=8, column=3, padx=0, pady=0, sticky='e')

        btnEditContract = Button(frameinfo, text='E', height=1, width=2, relief='groove', command=EditContractCommand)
        btnEditContract.grid(row=8, column=4, padx=0, pady=0)

        btnViewContract = Button(frameinfo, text='V', height=1, width=2, relief='groove', command=ViewContractCommand)
        btnViewContract.grid(row=8, column=5, padx=0, pady=0, sticky='w')
        # endregion
        # region ?
        lblUser = Label(frameinfo, text='?')
        lblUser.grid(row=6, rowspan=2, column=6, columnspan=3, padx=20, pady=10)

        btnAddUser = Button(frameinfo, text='A', height=1, width=2, relief='groove')
        btnAddUser.grid(row=8, column=6, padx=2, pady=0)

        btnEditUser = Button(frameinfo, text='E', height=1, width=2, relief='groove')
        btnEditUser.grid(row=8, column=7, padx=2, pady=0)

        btnViewUser = Button(frameinfo, text='V', height=1, width=2, relief='groove')
        btnViewUser.grid(row=8, column=8, padx=2, pady=0)
        # endregion
        # region User
        lblUser = Label(frameinfo, image=imgUser)
        lblUser.grid(row=6, rowspan=2, column=9, columnspan=3, padx=20, pady=10)

        btnAddUser = Button(frameinfo, text='A', height=1, width=2, relief='groove', command=AddUserCommand)
        btnAddUser.grid(row=8, column=9, padx=0, pady=0, sticky='e')

        btnEditUser = Button(frameinfo, text='E', height=1, width=2, relief='groove', command=EditUserCommand)
        btnEditUser.grid(row=8, column=10, padx=0, pady=0)

        btnViewUser = Button(frameinfo, text='V', height=1, width=2, relief='groove', command=ViewUserCommand)
        btnViewUser.grid(row=8, column=11, padx=0, pady=0, sticky='w')
        # endregion
# endregion
        mainfrm.mainloop()
