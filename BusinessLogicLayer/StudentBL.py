from Model import *
from DataAccessLayer import *


class StudentVD:
    def __init__(self, student: StudentModel.Student):
        self.Student = student

    def validationForm(self):
        error = 0

        if error == 0:
            studentdb = StudentDB(self.Student)
            return studentdb.insertStudent()
