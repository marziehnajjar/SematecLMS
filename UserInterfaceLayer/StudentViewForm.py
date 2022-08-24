from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as msg
from tkcalendar import DateEntry
from UserInterfaceLayer import *
from DataAccessLayer import *
from Model import *
from BusinessLogicLayer import *


class StudentViewUI:
    def __init__(self, user: User, studentid):
        studentdb = StudentDB(None)

        self.User = user
        self.Educations = studentdb.readStudentEducation(studentid)
        for i in range(5):
            self.Educations.append(' ')
        print(self.Educations)
        self.Student = Student()

        studentRow = studentdb.readStudent(studentid)
        print(studentRow)
        self.Student.StudentID = studentid
        self.Student.FirstName = studentRow[0]
        self.Student.LastName = studentRow[1]
        self.Student.NationalCode = studentRow[2]
        self.Student.Sex = studentRow[3]
        self.Student.Birthdate = studentRow[4]
        self.Student.Email = studentRow[5]
        self.Student.Mobile = studentRow[6]
        self.Student.Country = studentRow[7]
        self.Student.Province = studentRow[8]
        self.Student.Street = studentRow[9]
        self.Student.City = studentRow[10]
        self.Student.Postalcode = studentRow[11]
        self.Registerdate = studentRow[12]
        self.Student.Type = studentRow[13]

    def studentViewFormLoad(self):
        studentfrm = Tk()
        studentfrm.title('Register Student')
        studentfrm.geometry('440x620')
        studentfrm.resizable(False, False)
        positionRight = int(studentfrm.winfo_screenwidth() / 2 - 440 / 2)
        positionDown = int(studentfrm.winfo_screenheight() / 2 - 620 / 2)
        studentfrm.geometry("+{}+{}".format(positionRight, positionDown))

        def backToMain():
            studentfrm.destroy()


        frameinfo = LabelFrame(studentfrm, text=' Student Information ')
        frameinfo.grid(row=0, column=0, padx=20, pady=10, sticky='w')
# region Widgets ...
        lblID = Label(frameinfo, text='Student ID : ')
        lblID.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        lblID = Label(frameinfo, text=self.Student.StudentID, font='tahoma 10 bold')
        lblID.grid(row=0, column=1, padx=10, pady=5, sticky='w')

        lblFirstName = Label(frameinfo, text='FirstName: ')
        lblFirstName.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        entFirstName = Label(frameinfo, text=self.Student.FirstName, font='tahoma 10 bold')
        entFirstName.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        lblLastName = Label(frameinfo, text='LastName: ')
        lblLastName.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        entLastName = Label(frameinfo, text=self.Student.LastName, font='tahoma 10 bold')
        entLastName.grid(row=2, column=1, padx=10, pady=5, sticky='w')

        lblNationalCode = Label(frameinfo, text='NationalCode: ')
        lblNationalCode.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        entNationalCode = Label(frameinfo, text=self.Student.NationalCode, font='tahoma 10 bold')
        entNationalCode.grid(row=3, column=1, padx=10, pady=5, sticky='w')

        lblSex = Label(frameinfo, text='Sex: ')
        lblSex.grid(row=4, column=0, padx=10, pady=5, sticky='w')
        entSex = Label(frameinfo, text=self.Student.Sex, font='tahoma 10 bold')
        entSex.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        lblBirthdate = Label(frameinfo, text='Birthdate: ')
        lblBirthdate.grid(row=5, column=0, padx=10, pady=5, sticky='w')
        entBirthdate = Label(frameinfo, text=self.Student.Birthdate, font='tahoma 10 bold')
        entBirthdate.grid(row=5, column=1, padx=10, pady=5, sticky='w')

        lblEmail = Label(frameinfo, text='Email: ')
        lblEmail.grid(row=6, column=0, padx=10, pady=5, sticky='w')
        entEmail = Label(frameinfo, text=self.Student.Email, font='tahoma 10 bold')
        entEmail.grid(row=6, column=1, padx=10, pady=5, sticky='w')

        lblMobile = Label(frameinfo, text='Mobile: ')
        lblMobile.grid(row=7, column=0, padx=10, pady=5, sticky='w')
        entMobile = Label(frameinfo, text=self.Student.Mobile, font='tahoma 10 bold')
        entMobile.grid(row=7, column=1, padx=10, pady=5, sticky='w')

        lblAddress = Label(frameinfo, text='Address: ')
        lblAddress.grid(row=8, column=0, padx=10, pady=5, sticky='w')

        entCountry = Label(frameinfo, text=self.Student.Country, font='tahoma 10 bold')
        entCountry.grid(row=8, column=1, padx=10, pady=5, sticky='w')

        entProvince = Label(frameinfo, text=self.Student.Province, font='tahoma 10 bold')
        entProvince.grid(row=8, column=1, padx=110, pady=5, sticky='w')

        entCity = Label(frameinfo, text=self.Student.City, font='tahoma 10 bold')
        entCity.grid(row=8, column=1, padx=(210, 0), pady=5, sticky='w')

        entStreet = Label(frameinfo, text=self.Student.Street, font='tahoma 10 bold')
        entStreet.grid(row=9, column=1, padx=10, pady=5, sticky='w')

        entPostalCode = Label(frameinfo, text=self.Student.Postalcode, font='tahoma 10 bold')
        entPostalCode.grid(row=9, column=1, padx=(110, 0), pady=5, sticky='w')

        lblEducation = Label(frameinfo, text='Educations :')
        lblEducation.grid(row=10, column=0, padx=10, pady=5, sticky='nw')
        entEducation = Label(frameinfo, text=self.Educations[0], font='tahoma 10 bold')
        entEducation.grid(row=10, column=1, padx=10, pady=5, sticky='w')
        entEducation = Label(frameinfo, text=self.Educations[1], font='tahoma 10 bold')
        entEducation.grid(row=11, column=1, padx=10, pady=5, sticky='w')
        entEducation = Label(frameinfo, text=self.Educations[2], font='tahoma 10 bold')
        entEducation.grid(row=12, column=1, padx=10, pady=5, sticky='w')
        entEducation = Label(frameinfo, text=self.Educations[3], font='tahoma 10 bold')
        entEducation.grid(row=13, column=1, padx=10, pady=5, sticky='w')
        entEducation = Label(frameinfo, text=self.Educations[4], font='tahoma 10 bold')
        entEducation.grid(row=14, column=1, padx=10, pady=5, sticky='w')

        # educationsVar = StringVar(value=self.Educations)
        # listbox = Listbox(frameinfo, listvariable=educationsVar, height=5, borderwidth=2)
        # listbox.grid(row=10, column=1, padx=10, pady=5, sticky='w')

        lblType = Label(frameinfo, text='Type: ')
        lblType.grid(row=15, column=0, padx=10, pady=5, sticky='w')
        cmbType = Label(frameinfo, text=self.Student.Type, font='tahoma 10 bold')
        cmbType.grid(row=15, column=1, padx=10, pady=5, sticky='w')

        lblRegisterdate = Label(frameinfo, text='Registerdate: ')
        lblRegisterdate.grid(row=16, column=0, padx=10, pady=5, sticky='w')
        cmbRegisterdate = Label(frameinfo, text=self.Registerdate, font='tahoma 10 bold')
        cmbRegisterdate.grid(row=16, column=1, padx=10, pady=5, sticky='w')

        btnBack = Button(studentfrm, text='Back', width=20, relief='groove', command=backToMain)
        btnBack.grid(row=1, column=0, padx=30, pady=5, sticky='e')
# endregion
        studentfrm.mainloop()
