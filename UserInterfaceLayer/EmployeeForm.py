from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from UserInterfaceLayer import *
from DataAccessLayer import *


class EmployeeUI:

    def __init__(self, user: Model.User):
        self.User = user

    def employeeFormLoad(self):
        employeefrm = Tk()
        employeefrm.geometry('550x700')
        employeefrm.title('Register Employee')
        employeefrm.resizable(False, False)
        positionRight = int(employeefrm.winfo_screenwidth() / 2 - 550 / 2)
        positionDown = int(employeefrm.winfo_screenheight() / 2 - 700 / 2) - 40
        employeefrm.geometry("+{}+{}".format(positionRight, positionDown))

        employeedb = EmployeeDB()
        departmentList = employeedb.getDepartmentList()
        employeeList = employeedb.getEmployeeList()

        def addToList():
            pass

        def backToMain():
            employeefrm.destroy()
            from UserInterfaceLayer.MainForm import MainUI
            mainui = MainUI(self.User)
            mainui.mainFormLoad()

        def getEmployeeCommand():
            FirstName = txtFirstName.get()
            LastName = txtLastName.get()
            EmployeePhoto = txtEmployeePhoto.get()
            NationalCode = txtNationalCode.get()
            Sex = txtSex.get()
            Birthdate = txtBirthdate.get()
            Email = txtEmail.get()
            Mobile = txtMobile.get()

            EducationDegree = txtEducationDegree.get()
            EducationField = txtEducationField.get()
            Hiredate = txtHiredate.get()
            DepartmentID = txtDepartmentID.get().split(' ')[0]
            ManagerID = txtManagerID.get().split(' ')[0]
            JobLevelID = txtJobLevelID.get()

            employee = Model.Employee(ManagerID, DepartmentID, FirstName, LastName,EmployeePhoto, NationalCode, Sex,
                                      Birthdate, Email, Mobile, EducationDegree, EducationField, Hiredate,
                                      JobLevelID)

            employeevd = EmployeeVD(employee)
            employeevd.validationForm()

            # employeedb = EmployeeDB(employee)
            # employeedb.insertEmployee()

        frameinfo = LabelFrame(employeefrm, text=' Employee Information ')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')
# region Widgets ...
        lblID = Label(frameinfo, text='Employee ID : ')
        lblID.grid(row=0, column=0, padx=10, pady=5, sticky='w')

        lblFirstName = Label(frameinfo, text='FirstName: ')
        lblFirstName.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        txtFirstName = StringVar()
        entFirstName = Entry(frameinfo, textvariable=txtFirstName, width=40, highlightthickness=1)
        entFirstName.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        lblLastName = Label(frameinfo, text='LastName: ')
        lblLastName.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        txtLastName = StringVar()
        entLastName = Entry(frameinfo, textvariable=txtLastName, width=40, highlightthickness=1)
        entLastName.grid(row=2, column=1, padx=10, pady=5, sticky='w')

        def getFilePath():
            photoPath = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                                   filetype=(('jpeg files', '*.jpg'), ('PNG Files', '*.png'),
                                                             ('all files', '*.*')))
            if photoPath is not None:
                txtEmployeePhoto.set(photoPath)

        lblEmployeePhoto = Label(frameinfo, text='Photo Pass:')
        lblEmployeePhoto.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        txtEmployeePhoto = StringVar()
        entEmployeePhoto = Entry(frameinfo, textvariable=txtEmployeePhoto, width=30, font='tahoma 11')
        entEmployeePhoto.grid(row=3, column=1, padx=10, pady=5, sticky='w')
        btnEmployeePhoto = Button(frameinfo, width=3, text='...', borderwidth=2, command=getFilePath)
        btnEmployeePhoto.grid(row=3, column=2, padx=10, pady=5)

        lblNationalCode = Label(frameinfo, text='NationalCode: ')
        lblNationalCode.grid(row=4, column=0, padx=10, pady=5, sticky='w')
        txtNationalCode = StringVar()
        entNationalCode = Entry(frameinfo, textvariable=txtNationalCode, width=40, highlightthickness=1)
        entNationalCode.grid(row=4, column=1, padx=10, pady=5, sticky='w')

        lblSex = Label(frameinfo, text='Sex: ')
        lblSex.grid(row=5, column=0, padx=10, pady=5, sticky='w')
        txtSex = IntVar()
        rdMale = Radiobutton(frameinfo, text='Male', variable=txtSex, value=1)
        rdMale.grid(row=5, column=1, padx=5, pady=5, sticky='w')
        rdFemale = Radiobutton(frameinfo, text='Female', variable=txtSex, value=2)
        rdFemale.grid(row=5, column=1, padx=100, pady=5, sticky='e')

        lblBirthdate = Label(frameinfo, text='Birthdate: ')
        lblBirthdate.grid(row=6, column=0, padx=10, pady=5, sticky='w')
        txtBirthdate = StringVar()
        entBirthdate = DateEntry(frameinfo, textvariable=txtBirthdate, width=14, year=2021, month=1, day=1,
                                 background='darkblue', foreground='white', borderwidth=1, relief='solid',
                                 font='tahoma 10')
        entBirthdate.grid(row=6, column=1, padx=10, pady=5, sticky='w')
        # lblBirthdateHint = Label(frameinfo, text='(Sample: YYYY/MM/DD)')
        # lblBirthdateHint.grid(row=7, column=1, padx=10, pady=0, sticky='w')

        lblEmail = Label(frameinfo, text='Email: ')
        lblEmail.grid(row=7, column=0, padx=10, pady=5, sticky='w')
        txtEmail = StringVar()
        entEmail = Entry(frameinfo, textvariable=txtEmail, width=40, highlightthickness=1)
        entEmail.grid(row=7, column=1, padx=10, pady=5, sticky='w')

        lblMobile = Label(frameinfo, text='Mobile: ')
        lblMobile.grid(row=8, column=0, padx=10, pady=5, sticky='w')
        txtMobile = StringVar()
        entMobile = Entry(frameinfo, textvariable=txtMobile, width=40, highlightthickness=1)
        entMobile.grid(row=8, column=1, padx=10, pady=5, sticky='w')

        lblAddress = Label(frameinfo, text='Address: ')
        lblAddress.grid(row=9, column=0, padx=10, pady=5, sticky='w')

        txtCountry = StringVar(value='Country')
        entCountry = Entry(frameinfo, textvariable=txtCountry, width=15, highlightthickness=1)
        entCountry.grid(row=9, column=1, padx=10, pady=5, sticky='w')

        txtProvince = StringVar(value='Province')
        entProvince = Entry(frameinfo, textvariable=txtProvince, width=15, highlightthickness=1)
        entProvince.grid(row=9, column=1, padx=110, pady=5, sticky='w')

        txtCity = StringVar(value='City')
        entCity = Entry(frameinfo, textvariable=txtCity, width=15, highlightthickness=1)
        entCity.grid(row=9, column=1, padx=(210, 0), pady=5, sticky='w')

        txtStreet = StringVar(value='Street')
        entStreet = Entry(frameinfo, textvariable=txtStreet, width=15, highlightthickness=1)
        entStreet.grid(row=10, column=1, padx=10, pady=5, sticky='w')

        txtPostalCode = StringVar(value='PostalCode')
        entPostalCode = Entry(frameinfo, textvariable=txtPostalCode, width=15, highlightthickness=1)
        entPostalCode.grid(row=10, column=1, padx=(110, 0), pady=5, sticky='w')

        # TODO move to DAL, read from DB
        lblEducationDegree = Label(frameinfo, text='Education Degree: ')
        lblEducationDegree.grid(row=11, column=0, padx=10, pady=5, sticky='w')
        txtEducationDegree = StringVar()
        cmbEducationDegree = Combobox(frameinfo, width=20, textvariable=txtEducationDegree, state='readonly')
        arrayEducationDegree = []
        cmbEducationDegree['values'] = arrayEducationDegree  # educationDegreeList
        cmbEducationDegree.grid(row=11, column=1, padx=10, pady=5, sticky='w')
        cmbEducationDegree.current()

        # TODO move to DAL, read from DB
        lblEducationField = Label(frameinfo, text='Education Field: ')
        lblEducationField.grid(row=12, column=0, padx=10, pady=5, sticky='w')
        txtEducationField = StringVar()
        cmbEducationField = Combobox(frameinfo, width=20, textvariable=txtEducationField, state='readonly')
        arrayEducationField = []
        cmbEducationField['values'] = arrayEducationField
        cmbEducationField.grid(row=12, column=1, padx=10, pady=5, sticky='w')
        cmbEducationField.current()

        btnAdd = Button(frameinfo, text='Add', borderwidth=2, width=3, relief='groove',
                        command=addToList)
        btnAdd.grid(row=12, column=1, padx=(160, 0), pady=5, sticky='w')

        educations = ['a', 'b', 'c']
        educationsVar = StringVar(value=educations)
        listbox = Listbox(frameinfo, listvariable=educationsVar, height=3, borderwidth=2)
        listbox.grid(row=13, column=1, padx=10, pady=5, sticky='w')

        lblHiredate = Label(frameinfo, text='Hiredate : ')
        lblHiredate.grid(row=14, column=0, padx=10, pady=5, sticky='w')
        txtHiredate = StringVar()
        entHiredate = DateEntry(frameinfo, textvariable=txtHiredate, width=14, year=2021, month=1, day=1,
                                background='darkblue', foreground='white', borderwidth=1, relief='solid',
                                font='tahoma 10')
        entHiredate.grid(row=14, column=1, padx=10, pady=5, sticky='w')
        # lblHiredateHint = Label(frameinfo, text='(Sample: YYYY/MM/DD)')
        # lblHiredateHint.grid(row=16, column=1, padx=10, pady=0, sticky='w')

        lblDepartmentID = Label(frameinfo, text='DepartmentID: ')
        lblDepartmentID.grid(row=15, column=0, padx=10, pady=5, sticky='w')
        txtDepartmentID = StringVar()
        txtDepartmentID = StringVar()
        entDepartmentID = Combobox(frameinfo, width=30, textvariable=txtDepartmentID, state='readonly')
        entDepartmentID['values'] = departmentList
        entDepartmentID.grid(row=15, column=1, padx=10, pady=5, sticky='w')
        entDepartmentID.current()

        lblManagerID = Label(frameinfo, text='ManagerID: ')
        lblManagerID.grid(row=16, column=0, padx=10, pady=5, sticky='w')
        txtManagerID = StringVar()
        entManagerID = Combobox(frameinfo, width=20, textvariable=txtManagerID, state='readonly')
        entManagerID['values'] = employeeList
        entManagerID.grid(row=16, column=1, padx=10, pady=5, sticky='w')
        entManagerID.current()

        # TODO move to DAL, read from DB
        lblJobLevelID = Label(frameinfo, text='Job Level : ')
        lblJobLevelID.grid(row=17, column=0, padx=10, pady=5, sticky='w')
        txtJobLevelID = StringVar()
        cmbJobLevelID = Combobox(frameinfo, width=20, textvariable=txtJobLevelID, state='readonly')
        arrayJobLevelID = []
        cmbJobLevelID['values'] = arrayJobLevelID
        cmbJobLevelID.grid(row=17, column=1, padx=10, pady=5, sticky='w')
        cmbJobLevelID.current()

        btnRegisterEmployee = Button(employeefrm, text='Register Employee', width=20, relief='groove',
                                     command=getEmployeeCommand)
        btnRegisterEmployee.grid(row=18, column=0, padx=30, pady=10, sticky='w')

        btnBack = Button(employeefrm, text='Back to Main', width=20, relief='groove', command=backToMain)
        btnBack.grid(row=18, column=0, padx=30, pady=10, sticky='e')
# endregion
        employeefrm.mainloop()
