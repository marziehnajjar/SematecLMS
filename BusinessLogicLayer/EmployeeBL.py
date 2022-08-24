from Model import *
from DataAccessLayer import *


class EmployeeVD:
    def __init__(self, employee: EmployeeModel.Employee):
        self.Employee = employee

    def validationForm(self):
        error = 0

        if error == 0:
            mployeedb = EmployeeDB(self.mployee)
            mployeedb.insertEmployee()
