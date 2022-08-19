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
        mainfrm.geometry('600x600')
        mainfrm.resizable(None, None)
        positionRight = int(mainfrm.winfo_screenwidth() / 2 - 600 / 2)
        positionDown = int(mainfrm.winfo_screenheight() / 2 - 600 / 2)
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
            profile = ProfileUI(self.User)
            profile.profileFormLoad()

        def LogoutCommand():
            mainfrm.destroy()
            login = LoginUI()
            login.loginFormLoad()

        def registerStudentFormLoad():
            mainfrm.destroy()
            from UserInterfaceLayer.RegisterStudentForm import RegisterStudentUI
            registerStudentui = RegisterStudentUI(self.User)
            registerStudentui.studentFormLoad()

        def registerTeacherFormLoad():
            mainfrm.destroy()
            from UserInterfaceLayer.RegisterTeacherForm import RegisterTeacherUI
            registerTeacherui = RegisterTeacherUI(self.User)
            registerTeacherui.teacherFormLoad()

        def registerEmployeeFormLoad():
            mainfrm.destroy()
            from UserInterfaceLayer.RegisterEmployeeForm import RegisterEmployeeUI
            registerEmployeeui = RegisterEmployeeUI(self.User)
            registerEmployeeui.employeeFormLoad()

        def registerDepartmentFormLoad():
            mainfrm.destroy()
            from UserInterfaceLayer.RegisterDepartmentForm import RegisterDepartmentUI
            registerDepartmentui = RegisterDepartmentUI(self.User)
            registerDepartmentui.departmentFormLoad()

        def registerCourseCategoryFormLoad():
            mainfrm.destroy()
            from UserInterfaceLayer.RegisterCourseCategoryForm import RegisterCourseCategoryUI
            registerCourseCategoryui = RegisterCourseCategoryUI(self.User)
            registerCourseCategoryui.courseCategoryFormLoad()

        def registerCourseFormLoad():
            mainfrm.destroy()
            from UserInterfaceLayer.RegisterCourseForm import RegisterCourseUI
            registerCourseui = RegisterCourseUI(self.User)
            registerCourseui.courseFormLoad()

        def registerationFormLoad():
            mainfrm.destroy()
            from UserInterfaceLayer.RegisterationForm import RegisterationUI
            registerationui = RegisterationUI(self.User)
            registerationui.registerationFormLoad()

        def addUserFormLoad():
            mainfrm.destroy()
            from UserInterfaceLayer.AddUserForm import AddUserUI
            userui = AddUserUI(self.User)
            userui.FormLoad()

        def showAboutUs():
            msg.showinfo('About Us', 'Student : Marzieh Najjar\nTeacher : Vahid Ghorbani\nPython2021 / DataScience2022')
# endregion
# region Images ...
        imgRegisterStudent = PhotoImage(file='UserInterfaceLayer/icon/student.png')
        imgRegisterTeacher = PhotoImage(file='UserInterfaceLayer/icon/presentation.png')
        imgRegisterEmployee = PhotoImage(file='UserInterfaceLayer/icon/Employee.png')
        imgRegisterDepartment = PhotoImage(file='UserInterfaceLayer/icon/university.png')
        imgRegisterCourse = PhotoImage(file='UserInterfaceLayer/icon/open-book.png')
        imgRegisterCourseCategory = PhotoImage(file='UserInterfaceLayer/icon/book.png')
        imgRegisteration = PhotoImage(file='UserInterfaceLayer/icon/Order.png')
        imgAddUser = PhotoImage(file='UserInterfaceLayer/icon/add-user.png')
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

        frameinfo = LabelFrame(mainfrm, text='Welcome Dear ' + self.User.FirstName)
        frameinfo.grid(row=1, column=0, padx=20, pady=10, sticky='w')

# region Buttons ...
        btnRegisterStudent = Button(frameinfo, text='Register Student', image=imgRegisterStudent, compound=TOP, pady=10,
                                    height=120, width=140, relief='groove', font='tahoma 10 bold',
                                    command=registerStudentFormLoad)
        btnRegisterStudent.grid(row=2, column=0, padx=20, pady=10)

        btnRegisterTeacher = Button(frameinfo, text='Register Teacher', image=imgRegisterTeacher, compound=TOP, pady=10,
                                    height=120, width=140, relief='groove', font='tahoma 10 bold',
                                    command=registerTeacherFormLoad)
        btnRegisterTeacher.grid(row=2, column=1, padx=20, pady=10)

        btnRegisterEmployee = Button(frameinfo, text='Register Employee', image=imgRegisterEmployee, compound=TOP,
                                     pady=10, height=120, width=140, relief='groove', font='tahoma 10 bold',
                                     command=registerEmployeeFormLoad)
        btnRegisterEmployee.grid(row=2, column=2, padx=20, pady=10)

        btnRegisterDepartment = Button(frameinfo, text='Add Department', image=imgRegisterDepartment, compound=TOP,
                                       pady=10, height=120, width=140, relief='groove', font='tahoma 10 bold',
                                       command=registerDepartmentFormLoad)
        btnRegisterDepartment.grid(row=3, column=0, padx=20, pady=10)

        btnRegisterCourseCategory = Button(frameinfo, text='Add Course Category', image=imgRegisterCourseCategory,
                                           pady=10, compound=TOP, height=120, width=140, relief='groove',
                                           font='tahoma 10 bold', command=registerCourseCategoryFormLoad)
        btnRegisterCourseCategory.grid(row=3, column=1, padx=20, pady=10)

        btnRegisterCourse = Button(frameinfo, text='Add Course', image=imgRegisterCourse, compound=TOP, height=120,
                                   pady=10, width=140, relief='groove', font='tahoma 10 bold',
                                   command=registerCourseFormLoad)
        btnRegisterCourse.grid(row=3, column=2, padx=20, pady=10)

        btnRegisteration = Button(frameinfo, text='Registeration', image=imgRegisteration, compound=TOP, height=120,
                                  pady=10, width=140, relief='groove', font='tahoma 10 bold',
                                  command=registerationFormLoad)
        btnRegisteration.grid(row=4, column=0, padx=20, pady=10)

        # if int(self.User.Admin) == 1:
        btnAddUser = Button(frameinfo, text='Add User', image=imgAddUser, compound=TOP, height=120, pady=10,
                            width=140, relief='groove', font='tahoma 10 bold', command=addUserFormLoad)
        btnAddUser.grid(row=4, column=1, padx=20, pady=10)

        btnAbourUs = Button(frameinfo, text='About Us', image=imgAboutUs, compound=TOP, pady=10, height=120, width=140,
                            relief='groove', font='tahoma 10 bold', command=showAboutUs)
        btnAbourUs.grid(row=4, column=2, padx=20, pady=10)
# endregion
        mainfrm.mainloop()
