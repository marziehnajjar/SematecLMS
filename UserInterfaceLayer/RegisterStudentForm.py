from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as msg
from tkcalendar import DateEntry
from UserInterfaceLayer import *
from DataAccessLayer import *
from Model import *


class RegisterStudentUI:
    def __init__(self, user: User):
        self.User = user

    def studentFormLoad(self):
        studentfrm = Tk()
        studentfrm.title('Register a Student')
        studentfrm.geometry('420x550')
        studentfrm.resizable(None, None)
        positionRight = int(studentfrm.winfo_screenwidth() / 2 - 420 / 2)
        positionDown = int(studentfrm.winfo_screenheight() / 2 - 550 / 2)
        studentfrm.geometry("+{}+{}".format(positionRight, positionDown))

        def backToMain():
            studentfrm.destroy()
            from UserInterfaceLayer.MainForm import MainUI
            mainui = MainUI(self.User)
            mainui.mainFormLoad()

        def insertStudentCommand():
            # get the parameters of classStudent from user:
            FirstName = txtFirstName.get()
            LastName = txtLastName.get()
            NationalCode = txtNationalCode.get()
            Sex = txtSex.get()
            Birthdate = txtBirthdate.get()
            Email = txtEmail.get()
            Mobile = txtMobile.get()
            Address = txtAddress.get()
            Education = txtEducation.get()
            Type = txtType.get()
            # give the parameters to attribute of object(instance of classStudent)
            student = Model.Student(FirstName, LastName, NationalCode, Sex, Birthdate, Email, Mobile, Address,
                                    Education, Type)
            studentdb = StudentDB(student)
            studentdb.insertStudent()

        frameinfo = LabelFrame(studentfrm, text=' Student Information ')
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

        lblNationalCode = Label(frameinfo, text='NationalCode: ')
        lblNationalCode.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        txtNationalCode = StringVar()
        entNationalCode = Entry(frameinfo, textvariable=txtNationalCode, width=40, highlightthickness=1)
        entNationalCode.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        lblSex = Label(frameinfo, text='Sex: ')
        lblSex.grid(row=4, column=0, padx=10, pady=20, sticky='w')
        txtSex = IntVar()
        rdMale = Radiobutton(frameinfo, text='Male', variable=txtSex, value=1)
        rdMale.grid(row=4, column=1, padx=5, pady=10, sticky='w')
        rdFemale = Radiobutton(frameinfo, text='Female', variable=txtSex, value=2)
        rdFemale.grid(row=4, column=1, padx=5, pady=10, sticky='e')

        lblBirthdate = Label(frameinfo, text='Birthdate: ')
        lblBirthdate.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        txtBirthdate = StringVar()
        entBirthdate = DateEntry(frameinfo, textvariable=txtBirthdate, width=14, year=2021, month=1, day=1,
                                 background='darkblue', foreground='white', borderwidth=1, relief='solid',
                                 font='tahoma 10')
        entBirthdate.grid(row=5, column=1, padx=10, pady=10, sticky='w')
        lblBirthdateHint = Label(frameinfo, text='(Sample: YYYY/MM/DD)')
        lblBirthdateHint.grid(row=6, column=1, padx=10, pady=0, sticky='w')

        lblEmail = Label(frameinfo, text='Email: ')
        lblEmail.grid(row=7, column=0, padx=10, pady=10, sticky='w')
        txtEmail = StringVar()
        entEmail = Entry(frameinfo, textvariable=txtEmail, width=40, highlightthickness=1)
        entEmail.grid(row=7, column=1, padx=10, pady=10, sticky='w')

        lblMobile = Label(frameinfo, text='Mobile: ')
        lblMobile.grid(row=8, column=0, padx=10, pady=10, sticky='w')
        txtMobile = StringVar()
        entMobile = Entry(frameinfo, textvariable=txtMobile, width=40, highlightthickness=1)
        entMobile.grid(row=8, column=1, padx=10, pady=10, sticky='w')

        lblAddress = Label(frameinfo, text='Address: ')
        lblAddress.grid(row=9, column=0, padx=10, pady=10, sticky='w')
        txtAddress = StringVar()
        entAddress = Entry(frameinfo, textvariable=txtAddress, width=40, highlightthickness=1)
        entAddress.grid(row=9, column=1, padx=10, pady=10, sticky='w')

        lblEducation = Label(frameinfo, text='Education: ')
        lblEducation.grid(row=10, column=0, padx=10, pady=10, sticky='w')
        txtEducation = StringVar()
        cmbEducation = Combobox(frameinfo, width=20, textvariable=txtEducation, state='readonly')
        arrayEducation = []
        with open('DB/Education.csv', mode='r') as myfile:
            for line in myfile.readlines()[1:]:
                temp = line.rstrip('\n').split(',')
                arrayEducation.append(temp[1])
        cmbEducation['values'] = arrayEducation
        cmbEducation.grid(row=10, column=1, padx=10, pady=10, sticky='w')
        cmbEducation.current()

        lblType = Label(frameinfo, text='Type: ')
        lblType.grid(row=11, column=0, padx=10, pady=10, sticky='w')
        txtType = StringVar()
        cmbType = Combobox(frameinfo, textvariable=txtType, width=20, state='readonly')
        arrayType = ['Organization', 'Individual']
        cmbType['values'] = arrayType
        cmbType.grid(row=11, column=1, padx=10, pady=10, sticky='w')
        cmbType.current()

        btnRegisterStudent = Button(studentfrm, text='Register Student', width=20, relief='groove',
                                    command=insertStudentCommand)
        btnRegisterStudent.grid(row=11, column=0, padx=30, pady=10, sticky='w')

        btnBack = Button(studentfrm, text='Back to Main', width=20, relief='groove', command=backToMain)
        btnBack.grid(row=11, column=0, padx=30, pady=10, sticky='e')
# endregion
        studentfrm.mainloop()
