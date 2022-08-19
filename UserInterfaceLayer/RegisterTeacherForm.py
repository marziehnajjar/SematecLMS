from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as msg
from UserInterfaceLayer import *
from DataAccessLayer import *
from tkcalendar import DateEntry
from Model import *
from tkinter import messagebox as msg, filedialog


class RegisterTeacherUI:

    def __init__(self, user: User):
        self.User = user

    def teacherFormLoad(self):
        teacherfrm = Tk()
        teacherfrm.title('Register a Teacher')
        teacherfrm.geometry('480x600')
        teacherfrm.resizable(None, None)
        positionRight = int(teacherfrm.winfo_screenwidth() / 2 - 480 / 2)
        positionDown = int(teacherfrm.winfo_screenheight() / 2 - 600 / 2)
        teacherfrm.geometry("+{}+{}".format(positionRight, positionDown))

        def backToMain():
            teacherfrm.destroy()
            from UserInterfaceLayer.MainForm import MainUI
            mainui = MainUI(self.User)
            mainui.mainFormLoad()

        def insertTeacherCommand():
            FirstName = txtFirstName.get()
            LastName = txtLastName.get()
            NationalCode = txtNationalCode.get()
            Sex = txtSex.get()
            Birthdate = txtBirthdate.get()
            Email = txtEmail.get()
            Mobile = txtMobile.get()
            Address = txtAddress.get()
            Education = txtEducation.get()
            CardNumber = txtCardNumber.get()

            teacher = Model.Teacher(FirstName, LastName, NationalCode, Sex, Birthdate, Email, Mobile, Address,
                                    Education, CardNumber)
            from BusinessLogicLayer.TeacherBL import TeacherVD
            teachervd = TeacherVD(teacher)
            teachervd.check_form()

        frameinfo = LabelFrame(teacherfrm, text=' Teacher Information ')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')

# region Widgets ...
        lblFirstName = Label(frameinfo, text='FirstName: ')
        lblFirstName.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        txtFirstName = StringVar()
        entFirstName = Entry(frameinfo, textvariable=txtFirstName, width=40, highlightthickness=1)
        entFirstName.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        lblLastName = Label(frameinfo, text='LastName: ')
        lblLastName.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        txtLastName = StringVar()
        entLastName = Entry(frameinfo, textvariable=txtLastName, width=40, highlightthickness=1)
        entLastName.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        def getFilePath():
            photoPath = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                                   filetype=(('jpeg files', '*.jpg'), ('PNG Files', '*.png'),
                                                             ('all files', '*.*')))
            if photoPath is not None:
                txtTeacherPhoto.set(photoPath)

        lblTeacherPhoto = Label(frameinfo, text='Teacher Photo Pass:')
        lblTeacherPhoto.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        txtTeacherPhoto = StringVar()
        entTeacherPhoto = Entry(frameinfo, textvariable=txtTeacherPhoto, width=30, font='tahoma 11')
        entTeacherPhoto.grid(row=3, column=1, padx=10, pady=10, sticky='w')
        btnTeacherPhoto = Button(frameinfo, width=3, text='...', borderwidth=2, command=getFilePath)
        btnTeacherPhoto.grid(row=3, column=2, padx=10, pady=10)

        lblNationalCode = Label(frameinfo, text='NationalCode: ')
        lblNationalCode.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        txtNationalCode = StringVar()
        entNationalCode = Entry(frameinfo, textvariable=txtNationalCode, width=40, highlightthickness=1)
        entNationalCode.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        lblSex = Label(frameinfo, text='Sex: ')
        lblSex.grid(row=5, column=0, padx=10, pady=20, sticky='w')
        txtSex = IntVar()
        rdMale = Radiobutton(frameinfo, text='Male', variable=txtSex, value=1)
        rdMale.grid(row=5, column=1, padx=5, pady=10, sticky='w')
        rdFemale = Radiobutton(frameinfo, text='Female', variable=txtSex, value=2)
        rdFemale.grid(row=5, column=1, padx=100, pady=10, sticky='e')

        lblBirthdate = Label(frameinfo, text='Birthdate: ')
        lblBirthdate.grid(row=6, column=0, padx=10, pady=10, sticky='w')
        txtBirthdate = StringVar()
        entBirthdate = DateEntry(frameinfo, textvariable=txtBirthdate, width=14, year=2021, month=1, day=1,
                                 background='darkBlue', foreground='white', borderwidth=1, relief='solid',
                                 font='tahoma 10')
        entBirthdate.grid(row=6, column=1, padx=10, pady=10, sticky='w')
        lblBirthdateHint = Label(frameinfo, text='(Sample: YYYY/MM/DD)')
        lblBirthdateHint.grid(row=7, column=1, padx=10, pady=0, sticky='w')

        lblEmail = Label(frameinfo, text='Email: ')
        lblEmail.grid(row=8, column=0, padx=10, pady=10, sticky='w')
        txtEmail = StringVar()
        entEmail = Entry(frameinfo, textvariable=txtEmail, width=40, highlightthickness=1)
        entEmail.grid(row=8, column=1, padx=10, pady=10, sticky='w')

        lblMobile = Label(frameinfo, text='Mobile: ')
        lblMobile.grid(row=9, column=0, padx=10, pady=10, sticky='w')
        txtMobile = StringVar()
        entMobile = Entry(frameinfo, textvariable=txtMobile, width=40, highlightthickness=1)
        entMobile.grid(row=9, column=1, padx=10, pady=10, sticky='w')

        lblAddress = Label(frameinfo, text='Address: ')
        lblAddress.grid(row=10, column=0, padx=10, pady=10, sticky='w')
        txtAddress = StringVar()
        entAddress = Entry(frameinfo, textvariable=txtAddress, width=40, highlightthickness=1)
        entAddress.grid(row=10, column=1, padx=10, pady=10, sticky='w')

        lblEducation = Label(frameinfo, text='Education: ')
        lblEducation.grid(row=11, column=0, padx=10, pady=10, sticky='w')
        txtEducation = StringVar()
        entEducation = Combobox(frameinfo, width=20, textvariable=txtEducation, state='readonly')
        arrayEducation = []
        with open('DB/Education.csv', mode='r') as myfile:
            for line in myfile.readlines()[1:]:
                temp = line.rstrip('\n').split(',')
                arrayEducation.append(temp[1])
        entEducation['values'] = arrayEducation
        entEducation.grid(row=11, column=1, padx=10, pady=10, sticky='w')
        entEducation.current()

        lblInsuranceNumber = Label(frameinfo, text='InsuranceNumber: ')
        lblInsuranceNumber.grid(row=12, column=0, padx=10, pady=10, sticky='w')
        txtInsuranceNumber = StringVar()
        entInsuranceNumber = Entry(frameinfo, textvariable=txtInsuranceNumber, width=40, highlightthickness=1)
        entInsuranceNumber.grid(row=12, column=1, padx=10, pady=10, sticky='w')

        lblCardNumber = Label(frameinfo, text='CardNumber: ')
        lblCardNumber.grid(row=13, column=0, padx=10, pady=10, sticky='w')
        txtCardNumber = StringVar()
        entCardNumber = Entry(frameinfo, textvariable=txtCardNumber, width=40, highlightthickness=1)
        entCardNumber.grid(row=13, column=1, padx=10, pady=10, sticky='w')

        btnRegisterStudent = Button(teacherfrm, text='Register Teacher', width=20, relief='groove',
                                    command=insertTeacherCommand)
        btnRegisterStudent.grid(row=14, column=0, padx=30, pady=10, sticky='w')

        btnBack = Button(teacherfrm, text='Back to Main', width=20, relief='groove', command=backToMain)
        btnBack.grid(row=14, column=0, padx=30, pady=10, sticky='e')
# endregion
        teacherfrm.mainloop()
