from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as msg
from UserInterfaceLayer import *
from DataAccessLayer import *
from tkcalendar import DateEntry
from Model import *
from tkinter import messagebox as msg, filedialog


class TeacherUI:

    def __init__(self, user: User):
        self.User = user

    def teacherFormLoad(self):
        teacherfrm = Tk()
        teacherfrm.title('Register Teacher')
        teacherfrm.geometry('550x680')
        teacherfrm.resizable(False, False)
        positionRight = int(teacherfrm.winfo_screenwidth() / 2 - 500 / 2)
        positionDown = int(teacherfrm.winfo_screenheight() / 2 - 680 / 2) - 40
        teacherfrm.geometry("+{}+{}".format(positionRight, positionDown))

        def addToList():
            pass

        def backToMain():
            teacherfrm.destroy()
            from UserInterfaceLayer.MainForm import MainUI
            mainui = MainUI(self.User)
            mainui.mainFormLoad()

        def getTeacherCommand():
            FirstName = txtFirstName.get()
            LastName = txtLastName.get()
            TeacherPhoto = txtTeacherPhoto.get()
            NationalCode = txtNationalCode.get()
            Sex = txtSex.get()
            Birthdate = txtBirthdate.get()
            Email = txtEmail.get()
            Mobile = txtMobile.get()

            EducationDegree = txtEducationDegree.get()
            EducationField = txtEducationField.get()
            InsuranceNumber = txtInsuranceNumber.get()
            CardNumber = txtCardNumber.get()

            teacher = Model.Teacher(FirstName, LastName, TeacherPhoto, NationalCode, Sex, Birthdate, Email, Mobile,
                                    EducationDegree, EducationField, InsuranceNumber, CardNumber)
            from BusinessLogicLayer.TeacherBL import TeacherVD
            teachervd = TeacherVD(teacher)
            teachervd.validationForm()

        frameinfo = LabelFrame(teacherfrm, text=' Teacher Information ')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')

# region Widgets ...
        lblID = Label(frameinfo, text='Teacher ID : ')
        lblID.grid(row=0, column=0, padx=10, pady=5, sticky='w')

        lblFirstName = Label(frameinfo, text='FirstName: ')
        lblFirstName.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        txtFirstName = StringVar()
        entFirstName = Entry(frameinfo, textvariable=txtFirstName, width=40, highlightthickness=1)
        entFirstName.grid(row=1, column=1, padx=10, pady=5, sticky='w')

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
                txtTeacherPhoto.set(photoPath)

        lblTeacherPhoto = Label(frameinfo, text='Photo Pass:')
        lblTeacherPhoto.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        txtTeacherPhoto = StringVar()
        entTeacherPhoto = Entry(frameinfo, textvariable=txtTeacherPhoto, width=30, font='tahoma 11')
        entTeacherPhoto.grid(row=3, column=1, padx=10, pady=5, sticky='w')
        btnTeacherPhoto = Button(frameinfo, width=3, text='...', borderwidth=2, command=getFilePath)
        btnTeacherPhoto.grid(row=3, column=2, padx=10, pady=5)

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
                                 background='darkBlue', foreground='white', borderwidth=1, relief='solid',
                                 font='tahoma 10')
        entBirthdate.grid(row=6, column=1, padx=10, pady=5, sticky='w')
        lblBirthdateHint = Label(frameinfo, text='(Sample: YYYY/MM/DD)')
        lblBirthdateHint.grid(row=7, column=1, padx=10, pady=0, sticky='w')

        lblEmail = Label(frameinfo, text='Email: ')
        lblEmail.grid(row=8, column=0, padx=10, pady=5, sticky='w')
        txtEmail = StringVar()
        entEmail = Entry(frameinfo, textvariable=txtEmail, width=40, highlightthickness=1)
        entEmail.grid(row=8, column=1, padx=10, pady=5, sticky='w')

        lblMobile = Label(frameinfo, text='Mobile: ')
        lblMobile.grid(row=9, column=0, padx=10, pady=5, sticky='w')
        txtMobile = StringVar()
        entMobile = Entry(frameinfo, textvariable=txtMobile, width=40, highlightthickness=1)
        entMobile.grid(row=9, column=1, padx=10, pady=5, sticky='w')

        lblAddress = Label(frameinfo, text='Address: ')
        lblAddress.grid(row=10, column=0, padx=10, pady=5, sticky='w')

        txtCountry = StringVar(value='Country')
        entCountry = Entry(frameinfo, textvariable=txtCountry, width=15, highlightthickness=1)
        entCountry.grid(row=10, column=1, padx=10, pady=5, sticky='w')

        txtProvince = StringVar(value='Province')
        entProvince = Entry(frameinfo, textvariable=txtProvince, width=15, highlightthickness=1)
        entProvince.grid(row=10, column=1, padx=110, pady=5, sticky='w')

        txtCity = StringVar(value='City')
        entCity = Entry(frameinfo, textvariable=txtCity, width=15, highlightthickness=1)
        entCity.grid(row=10, column=1, padx=(210, 0), pady=5, sticky='w')

        txtStreet = StringVar(value='Street')
        entStreet = Entry(frameinfo, textvariable=txtStreet, width=15, highlightthickness=1)
        entStreet.grid(row=11, column=1, padx=10, pady=5, sticky='w')

        txtPostalCode = StringVar(value='PostalCode')
        entPostalCode = Entry(frameinfo, textvariable=txtPostalCode, width=15, highlightthickness=1)
        entPostalCode.grid(row=11, column=1, padx=(110, 0), pady=5, sticky='w')

        # TODO move to DAL, read from DB
        lblEducationDegree = Label(frameinfo, text='Education Degree: ')
        lblEducationDegree.grid(row=12, column=0, padx=10, pady=5, sticky='w')
        txtEducationDegree = StringVar()
        cmbEducationDegree = Combobox(frameinfo, width=20, textvariable=txtEducationDegree, state='readonly')
        arrayEducationDegree = []
        cmbEducationDegree['values'] = arrayEducationDegree  # educationDegreeList
        cmbEducationDegree.grid(row=12, column=1, padx=10, pady=5, sticky='w')
        cmbEducationDegree.current()

        # TODO move to DAL, read from DB
        lblEducationField = Label(frameinfo, text='Education Field: ')
        lblEducationField.grid(row=13, column=0, padx=10, pady=5, sticky='w')
        txtEducationField = StringVar()
        cmbEducationField = Combobox(frameinfo, width=20, textvariable=txtEducationField, state='readonly')
        arrayEducationField = []
        cmbEducationField['values'] = arrayEducationField
        cmbEducationField.grid(row=13, column=1, padx=10, pady=5, sticky='w')
        cmbEducationField.current()

        btnAdd = Button(frameinfo, text='Add', borderwidth=2, width=3, relief='groove',
                        command=addToList)
        btnAdd.grid(row=13, column=1, padx=(160, 0), pady=5, sticky='w')

        educations = ['a', 'b', 'c']
        educationsVar = StringVar(value=educations)
        listbox = Listbox(frameinfo, listvariable=educationsVar, height=5, borderwidth=2)
        listbox.grid(row=14, column=1, padx=10, pady=5, sticky='w')

        lblInsuranceNumber = Label(frameinfo, text='InsuranceNumber: ')
        lblInsuranceNumber.grid(row=15, column=0, padx=10, pady=5, sticky='w')
        txtInsuranceNumber = StringVar()
        entInsuranceNumber = Entry(frameinfo, textvariable=txtInsuranceNumber, width=40, highlightthickness=1)
        entInsuranceNumber.grid(row=15, column=1, padx=10, pady=5, sticky='w')

        lblCardNumber = Label(frameinfo, text='CardNumber: ')
        lblCardNumber.grid(row=16, column=0, padx=10, pady=5, sticky='w')
        txtCardNumber = StringVar()
        entCardNumber = Entry(frameinfo, textvariable=txtCardNumber, width=40, highlightthickness=1)
        entCardNumber.grid(row=16, column=1, padx=10, pady=5, sticky='w')

        btnRegisterStudent = Button(teacherfrm, text='Register Teacher', width=20, relief='groove',
                                    command=getTeacherCommand)
        btnRegisterStudent.grid(row=17, column=0, padx=30, pady=10, sticky='w')

        btnBack = Button(teacherfrm, text='Back to Main', width=20, relief='groove', command=backToMain)
        btnBack.grid(row=17, column=0, padx=30, pady=10, sticky='e')
# endregion
        teacherfrm.mainloop()
