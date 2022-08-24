from Model import *
from DataAccessLayer import *


class TeacherVD:
    def __init__(self, teacher: TeacherModel.Teacher):
        self.Teacher = teacher

    def validationForm(self):
        error = 0

        if len(self.Teacher.FirstName) > 20 or len(self.Teacher.LastName) > 20:
            msg.showerror('Validation Failed', 'The name must be less than 20 Letters!')
            error += 1
        if not self.Teacher.FirstName.isalpha() or not self.Teacher.LastName.isalpha():
            msg.showerror('Validation Failed', 'Name Entry is Mandatory:The name should be just letter !')
            error += 1
        if len(self.Teacher.NationalCode) == 0:
            msg.showerror('Validation Failed', 'Enter the NationalCode!')
            error += 1
        if self.Teacher.Mobile.isalpha():
            msg.showerror('Validation Failed', 'The mobile number should be just Number !')
            error += 1
        if len(self.Teacher.PostalCode) > 0:
            if len(self.Teacher.PostalCode) > 12 or not self.Teacher.PostalCode.isnumeric():
                msg.showerror('Validation Failed', 'The PostalCode should be just Number and less than 12 digit!')
                error += 1

        if error == 0:
            teacherdb = TeacherDB(self.Teacher)
            teacherdb.insertTeacher()


