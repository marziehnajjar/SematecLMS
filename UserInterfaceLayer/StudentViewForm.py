from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as msg
from tkcalendar import DateEntry
from UserInterfaceLayer import *
from DataAccessLayer import *
from Model import *
from BusinessLogicLayer import *


class StudentUI:
    def __init__(self, user: User, func):
        self.User = user
        self.FUNC = func
        self.State = 'normal'
        self.Educations = []

        studentdb = StudentDB(None)
        self.EducationFiels = studentdb.readEducationFiels()

        if func == 'view':
            self.State = 'disabled'

    def studentFormLoad(self):
        studentfrm = Tk()
        studentfrm.title('Register Student')
        studentfrm.geometry('490x610')
        studentfrm.resizable(False, False)
        positionRight = int(studentfrm.winfo_screenwidth() / 2 - 490 / 2)
        positionDown = int(studentfrm.winfo_screenheight() / 2 - 610 / 2)
        studentfrm.geometry("+{}+{}".format(positionRight, positionDown))

        def addToList():
            EducationDegree = txtEducationDegree.get()
            EducationField = txtEducationField.get()
            self.Educations.append(f'{EducationDegree}-{EducationField}')
            educationsVar.set(self.Educations)

        def backToMain():
            studentfrm.destroy()
            from UserInterfaceLayer.MainForm import MainUI
            mainui = MainUI(self.User)
            mainui.mainFormLoad()

        def getStudentCommand():
            # get the parameters of classStudent from user:
            FirstName = txtFirstName.get()
            LastName = txtLastName.get()
            NationalCode = txtNationalCode.get()
            Sex = txtSex.get()
            Birthdate = txtBirthdate.get()
            Email = txtEmail.get()
            Mobile = txtMobile.get()
            Country = txtCountry.get()
            Province = txtProvince.get()
            City = txtCity.get()
            Street = txtStreet.get()
            Postalcode = txtPostalCode.get()
            EducationDegree = txtEducationDegree.get()
            EducationField = txtEducationField.get()
            Type = int(txtType.get())
            # give the parameters to attribute of object(instance of classStudent)
            student = Model.Student(0, FirstName, LastName, NationalCode, Sex, Birthdate, Email, Mobile,
            Country, Province, City, Street, Postalcode, EducationDegree, EducationField, Type)

            studentvd = StudentVD(student)
            studentvd.validationForm()
            # for i in self.Educations:


        frameinfo = LabelFrame(studentfrm, text=' Student Information ')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')
# region Widgets ...
        lblID = Label(frameinfo, text='Student ID : ')
        lblID.grid(row=0, column=0, padx=10, pady=5, sticky='w')

        lblFirstName = Label(frameinfo, text='FirstName: ')
        lblFirstName.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        txtFirstName = StringVar()
        entFirstName = Entry(frameinfo, state=self.State, textvariable=txtFirstName, width=23, highlightthickness=1)
        entFirstName.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        lblLastName = Label(frameinfo, text='LastName: ')
        lblLastName.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        txtLastName = StringVar()
        entLastName = Entry(frameinfo, state=self.State, textvariable=txtLastName, width=23, highlightthickness=1)
        entLastName.grid(row=2, column=1, padx=10, pady=5, sticky='w')

        lblNationalCode = Label(frameinfo, text='NationalCode: ')
        lblNationalCode.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        txtNationalCode = StringVar()
        entNationalCode = Entry(frameinfo, state=self.State, textvariable=txtNationalCode, width=23, highlightthickness=1)
        entNationalCode.grid(row=3, column=1, padx=10, pady=5, sticky='w')

        lblSex = Label(frameinfo, text='Sex: ')
        lblSex.grid(row=4, column=0, padx=10, pady=5, sticky='w')
        txtSex = IntVar()
        rdMale = Radiobutton(frameinfo,state=self.State, text='Male', variable=txtSex, value=1)
        rdMale.grid(row=4, column=1, padx=5, pady=5, sticky='w')
        rdFemale = Radiobutton(frameinfo,state=self.State, text='Female', variable=txtSex, value=2)
        rdFemale.grid(row=4, column=1, padx=100, pady=5, sticky='e')

        lblBirthdate = Label(frameinfo, text='Birthdate: ')
        lblBirthdate.grid(row=5, column=0, padx=10, pady=5, sticky='w')
        txtBirthdate = StringVar()
        entBirthdate = DateEntry(frameinfo, state=self.State, textvariable=txtBirthdate, width=14, year=2021, month=1, day=1,
                                 background='darkblue', foreground='white', borderwidth=1, relief='solid',
                                 font='tahoma 10')
        entBirthdate.grid(row=5, column=1, padx=10, pady=5, sticky='w')
        lblBirthdateHint = Label(frameinfo, text='(Sample: YYYY/MM/DD)')
        lblBirthdateHint.grid(row=6, column=1, padx=10, pady=0, sticky='w')

        lblEmail = Label(frameinfo, text='Email: ')
        lblEmail.grid(row=7, column=0, padx=10, pady=5, sticky='w')
        txtEmail = StringVar()
        entEmail = Entry(frameinfo, state=self.State, textvariable=txtEmail, width=23, highlightthickness=1)
        entEmail.grid(row=7, column=1, padx=10, pady=5, sticky='w')

        lblMobile = Label(frameinfo, text='Mobile: ')
        lblMobile.grid(row=8, column=0, padx=10, pady=5, sticky='w')
        txtMobile = StringVar()
        entMobile = Entry(frameinfo, state=self.State, textvariable=txtMobile, width=23, highlightthickness=1)
        entMobile.grid(row=8, column=1, padx=10, pady=5, sticky='w')

        lblAddress = Label(frameinfo, text='Address: ')
        lblAddress.grid(row=9, column=0, padx=10, pady=5, sticky='w')

        txtCountry = StringVar(value='Country')
        entCountry = Entry(frameinfo, state=self.State, textvariable=txtCountry, width=15, highlightthickness=1)
        entCountry.grid(row=9, column=1, padx=10, pady=5, sticky='w')

        txtProvince = StringVar(value='Province')
        entProvince = Entry(frameinfo, state=self.State, textvariable=txtProvince, width=15, highlightthickness=1)
        entProvince.grid(row=9, column=1, padx=110, pady=5, sticky='w')

        txtCity = StringVar(value='City')
        entCity = Entry(frameinfo, state=self.State, textvariable=txtCity, width=15, highlightthickness=1)
        entCity.grid(row=9, column=1, padx=(210, 0), pady=5, sticky='w')

        txtStreet = StringVar(value='Street')
        entStreet = Entry(frameinfo, state=self.State, textvariable=txtStreet, width=15, highlightthickness=1)
        entStreet.grid(row=10, column=1, padx=10, pady=5, sticky='w')

        txtPostalCode = StringVar(value='PostalCode')
        entPostalCode = Entry(frameinfo, state=self.State, textvariable=txtPostalCode, width=15, highlightthickness=1)
        entPostalCode.grid(row=10, column=1, padx=(110, 0), pady=5, sticky='w')

        # TODO  read from DB
        lblEducationDegree = Label(frameinfo, text='Education Degree: ')
        lblEducationDegree.grid(row=11, column=0, padx=10, pady=5, sticky='w')
        txtEducationDegree = StringVar()
        cmbEducationDegree = Combobox(frameinfo, width=20, textvariable=txtEducationDegree, state=self.State)
        arrayEducationDegree = ['کارشناسی', 'کارشناسی ارشد', 'دکتری', 'دیپلم']
        cmbEducationDegree['values'] = arrayEducationDegree  #educationDegreeList
        cmbEducationDegree.grid(row=11, column=1, padx=10, pady=5, sticky='w')
        cmbEducationDegree.current()

        lblEducationField = Label(frameinfo, text='Education Field: ')
        lblEducationField.grid(row=12, column=0, padx=10, pady=5, sticky='w')
        txtEducationField = StringVar()
        cmbEducationField = Combobox(frameinfo, width=20, textvariable=txtEducationField, state=self.State)
        cmbEducationField['values'] = self.EducationFiels
        cmbEducationField.grid(row=12, column=1, padx=10, pady=5, sticky='w')
        cmbEducationField.current()

        btnAdd = Button(frameinfo, state=self.State, text='Add', borderwidth=2, width=3, relief='groove',
                        command=addToList)
        btnAdd.grid(row=12, column=1, padx=(160,0), pady=5, sticky='w')

        educationsVar = StringVar(value=self.Educations)
        listbox = Listbox(frameinfo, state=self.State, listvariable=educationsVar, height=5, borderwidth=2)
        listbox.grid(row=13, column=1, padx=10, pady=5, sticky='w')

        # TODO move to DAL, read from DB
        lblType = Label(frameinfo, text='Type: ')
        lblType.grid(row=14, column=0, padx=10, pady=5, sticky='w')
        txtType = StringVar()
        cmbType = Combobox(frameinfo, textvariable=txtType, width=20, state=self.State)
        arrayType = ['1', '2']
        cmbType['values'] = arrayType
        cmbType.grid(row=14, column=1, padx=10, pady=5, sticky='w')
        cmbType.current()

        btnRegisterStudent = Button(studentfrm, text='Register Student', width=20, relief='groove',
                                    command=getStudentCommand)
        btnRegisterStudent.grid(row=14, column=0, padx=30, pady=10, sticky='w')

        btnBack = Button(studentfrm, text='Back to Main', width=20, relief='groove', command=backToMain)
        btnBack.grid(row=14, column=0, padx=30, pady=10, sticky='e')
# endregion
        studentfrm.mainloop()
